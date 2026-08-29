# Analytics and identity

Gaiish has an anonymous-to-identified identity layer shared by Amplitude and Klaviyo. It does
not add authentication: the capture form is an exposed, optional lead-collection helper and
there is no login or logout UI.

## Architecture

`site.js` owns the one Amplitude Browser SDK load and initialization. Visitors begin with an
Amplitude device ID. When a visitor supplies an email or phone through the reference-guide
capture form, the browser posts the contact details to `/api/identify`. The Vercel function
resolves the contact against Klaviyo and returns a stable internal ID. The browser then applies
that ID to Amplitude and identifies the same profile in Klaviyo.

```text
Anonymous Visitor
       |
       v
Amplitude Device ID
       |
       v
User provides email / phone / login
       |
       v
Resolve or create internal_user_id
       |
       +----------------------+
       |                      |
       v                      v
Amplitude                 Klaviyo
user_id                   email / phone
internal_user_id          internal_user_id
       |                      |
       +----------+-----------+
                  |
                  v
          Unified User Identity
```

## The stable internal ID

`internal_user_id` has the exact format `usr_` followed by 26 uppercase Crockford base32
characters (`0-9`, excluding `I`, `L`, `O` and `U` where Crockford requires). It is minted
server-side in `api/_identity.js` from cryptographic random bytes. Klaviyo is the system of
record: the ID is stored on the Klaviyo profile as the `internal_user_id` custom property.

The identity function first looks up the profile by email, or by E.164 phone when no email was
provided. A valid existing ID is reused. A missing or malformed ID causes one new ID to be
minted. The function always runs the Klaviyo profile import with the resolved ID and supplied
contact/name fields, so a later phone submission can update the same profile.

Email and phone are never used as the Amplitude `user_id`, event properties, URLs or response
logs. The API response contains only `internal_user_id` and `klaviyo_profile_id`.

## Provider identity

### Amplitude

Before identification, Amplitude remains device-only and anonymous. After the server resolves
the lead, `identity.js` calls `amplitude.setUserId(internal_user_id)` and sends user properties
through the Browser SDK `Identify` API when available. The PII user properties are explicitly:

- `email`
- `phone`
- `first_name`
- `last_name`

It also sets the non-contact properties `klaviyo_profile_id` and `signup_source` when values are
available. No prompt text, source material or form contents are sent as event properties.

The Amplitude SDK loads asynchronously. `site.js` exposes `window.gaiishAnalyticsReady(callback)`
and flushes callbacks immediately after its single `amplitude.init` call. `identity.js` uses
this registry to restore a returning visitor's user ID without creating a second SDK load or
initialization path. If an ad blocker prevents the SDK from loading, identity resolution and
Klaviyo's browser queue still degrade independently.

### Klaviyo

Klaviyo identifies profiles primarily by email or phone. The browser sends its identify queue
entry with the supplied `email`, `phone_number`, `first_name`, `last_name`, and the resolved
`internal_user_id` when the server returned one. If the server is unavailable, the Klaviyo
identify call still contains the contact and name fields but omits `internal_user_id`.

The private API key exists only as the `KLAVIYO_PRIVATE_API_KEY` Vercel environment variable.
It is never sent to the browser or written to logs.

## Anonymous to identified transition

1. A visitor uses the site anonymously with an Amplitude device ID.
2. The visitor completes the required-consent reference-guide form on the homepage,
   `/learn-gaiish` or `/dictionary`.
3. `/api/identify` validates the origin and email/phone, resolves or creates the Klaviyo
   profile ID and stable internal ID, and returns those IDs.
4. Amplitude receives `internal_user_id` as `user_id` and the listed user properties.
5. Klaviyo receives its email/phone identity and the same internal ID custom property.
6. The browser stores only `{ internal_user_id, klaviyo_profile_id }` in localStorage under
   `gaiish_identity`. It never stores email, phone or names there.

## Logout and reset

`window.gaiishLogout()` is an unused-but-ready helper because the site has no authentication or
logout UI today. It removes `gaiish_identity` and calls `amplitude.reset()` when available,
which clears the current Amplitude user ID and regenerates the device ID. It does not delete a
Klaviyo profile.

## Consent and known gap

The capture form requires the checkbox: “Email me Gaiish updates. Unsubscribe any time.” There
is currently no cookie-consent banner. Amplitude and Klaviyo load on page load, including for
visitors in the EU, so consent management for those page-load technologies is a known GDPR/EU
gap. Do not describe the checkbox as solving that broader gap; a future consent decision must
govern provider loading as well as lead capture.

## Troubleshooting

- **Amplitude is absent:** ad blockers can block the CDN loader. Check the browser network panel
  for `cdn.amplitude.com`; the tools and Klaviyo path should still fail gracefully.
- **503 `identity_unavailable`:** `KLAVIYO_PRIVATE_API_KEY` is missing or empty in the Vercel
  environment.
- **502 `identity_lookup_failed`:** Klaviyo lookup or profile import failed or timed out. The
  server logs only the error code and Klaviyo status code, never contact values.
- **Check a profile:** search Klaviyo by the submitted email or phone, then inspect the profile's
  custom properties for `internal_user_id`. The value should match the `usr_` format.
- **No ID in localStorage:** inspect only `localStorage.gaiish_identity`; it should contain IDs
  and no contact details. On localhost, append `?gaiishDebug=1` for boolean/ID debug messages.

## Testing scenarios

The unit suite is `node --test tests/identity.test.js`; it stubs fetch and does not contact
Klaviyo. A live probe uses `/home/ubuntu/.klaviyo_private_key` only in process memory and a
fresh test email.

1. Anonymous page load: Amplitude has a device ID and no identified user ID.
2. Valid email capture: the API returns an internal ID and Klaviyo profile ID; the browser
   applies the Amplitude ID and queues Klaviyo identity.
3. Returning page load: only the two stored IDs are read and the Amplitude ID is restored
   without another API call.
4. Valid phone-only capture: lookup uses `phone_number` and the same resolution path.
5. Repeat email capture: a valid existing Klaviyo internal ID is reused.
6. Missing Klaviyo key: API returns 503; the browser reports failure without throwing, and
   provider calls remain independently guarded.
7. Klaviyo error/timeout or blocked Amplitude: API failure returns 502 or the SDK is absent;
   the capture UI exposes the PDF link and the rest of the page continues working.
