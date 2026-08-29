"use strict";

const test = require("node:test");
const assert = require("node:assert/strict");
const fs = require("fs");
const identifyHandler = require("../api/identify");
const { isAllowedOrigin } = identifyHandler;
const {
  isValidEmail,
  isValidPhone,
  isValidIdentity,
  isValidInternalUserId,
  lookupRequest,
  mintInternalUserId,
  profileImportBody,
  subscribeBody,
  resolveIdentity,
} = require("../api/_identity");

test("client identity requests use normalized snake_case name fields", () => {
  const source = fs.readFileSync(require.resolve("../identity.js"), "utf8");
  assert.match(source, /if \(input\.first_name\) payload\.first_name = input\.first_name;/);
  assert.match(source, /if \(input\.last_name\) payload\.last_name = input\.last_name;/);
  assert.doesNotMatch(source, /payload\.first_name = input\.firstName/);
  assert.doesNotMatch(source, /payload\.last_name = input\.lastName/);
});

test("validates email and phone identities", () => {
  assert.equal(isValidEmail("person@example.com"), true);
  assert.equal(isValidEmail("not-an-email"), false);
  assert.equal(isValidEmail("a".repeat(250) + "@x.com"), false);
  assert.equal(isValidEmail('a"b@x.com'), false);
  assert.equal(isValidEmail("a\\\\b@x.com"), false);
  assert.equal(isValidEmail("a(b)@x.com"), false);
  assert.equal(isValidEmail("a\nb@x.com"), false);
  assert.equal(isValidPhone("+14155550123"), true);
  assert.equal(isValidPhone("4155550123"), false);
  assert.equal(isValidIdentity({ email: "person@example.com" }), true);
  assert.equal(isValidIdentity({ phone: "+14155550123" }), true);
  assert.equal(isValidIdentity({ email: "bad", phone: "+14155550123" }), false);
  assert.equal(isValidIdentity({}), false);
});

test("rejects unsafe email input at the HTTP boundary", async () => {
  const response = { headers: {}, statusCode: null, body: null };
  const res = {
    setHeader(name, value) {
      response.headers[name] = value;
    },
    status(statusCode) {
      response.statusCode = statusCode;
      return this;
    },
    json(body) {
      response.body = body;
      return this;
    },
  };
  await identifyHandler({
    method: "POST",
    headers: { origin: "http://localhost:8000" },
    body: { email: 'a"b@example.com' },
  }, res);
  assert.equal(response.statusCode, 400);
  assert.deepEqual(response.body, { error: "invalid_identity" });
  assert.equal(response.headers["Cache-Control"], "no-store");
});

test("mints the required Crockford internal user ID format", () => {
  const id = mintInternalUserId();
  assert.match(id, /^usr_[0-9A-HJKMNP-TV-Z]{26}$/);
  assert.equal(isValidInternalUserId(id), true);
  assert.equal(isValidInternalUserId("usr_TESTONLY0001"), false);
});

test("allows only the documented origins", () => {
  assert.equal(isAllowedOrigin("https://gaiish.com"), true);
  assert.equal(isAllowedOrigin("https://www.gaiish.com"), true);
  assert.equal(isAllowedOrigin("http://localhost:8000"), true);
  assert.equal(isAllowedOrigin("http://127.0.0.1:3000"), true);
  assert.equal(isAllowedOrigin("https://localhost:8000"), false);
  assert.equal(isAllowedOrigin("https://example.com"), false);
  assert.equal(isAllowedOrigin(undefined), false);
});

test("constructs lookup requests with the exact profile fields", () => {
  const request = lookupRequest({ email: "person@example.com" }, "secret");
  assert.match(request.url, /filter=equals%28email%2C%22person%40example\.com%22%29/);
  assert.match(request.url, /fields%5Bprofile%5D=email%2Cphone_number%2Cproperties/);
  assert.equal(request.options.headers.Authorization, "Klaviyo-API-Key secret");
  assert.equal(request.options.headers.revision, "2024-10-15");
});

test("reuses an existing valid internal user ID", async () => {
  const calls = [];
  const fetchImpl = async (url, options) => {
    calls.push({ url, options });
    if (calls.length === 1) {
      return {
        ok: true,
        status: 200,
        json: async () => ({
          data: [{
            id: "profile_existing",
            attributes: { properties: { internal_user_id: "usr_0123456789ABCDEFGHJKMNPQRS" } },
          }],
        }),
      };
    }
    return {
      ok: true,
      status: 200,
      json: async () => ({ data: { id: "profile_existing" } }),
    };
  };
  const result = await resolveIdentity(
    { email: "person@example.com", first_name: "Person" },
    { apiKey: "secret", fetchImpl, now: "2026-08-29T00:00:00.000Z" }
  );
  assert.equal(result.internalUserId, "usr_0123456789ABCDEFGHJKMNPQRS");
  assert.equal(result.klaviyoProfileId, "profile_existing");
  const body = JSON.parse(calls[1].options.body);
  assert.equal(body.data.attributes.properties.internal_user_id, result.internalUserId);
  assert.equal("signup_date" in body.data.attributes.properties, false);
  assert.equal("signup_source" in body.data.attributes.properties, false);
});

test("mints for a malformed ID and includes signup properties only on mint", async () => {
  const calls = [];
  const fetchImpl = async (url, options) => {
    calls.push({ url, options });
    if (calls.length === 1) {
      return {
        ok: true,
        status: 200,
        json: async () => ({
          data: [{
            id: "profile_malformed",
            attributes: { properties: { internal_user_id: "usr_TESTONLY0001" } },
          }],
        }),
      };
    }
    return {
      ok: true,
      status: 201,
      json: async () => ({ data: { id: "profile_malformed" } }),
    };
  };
  const result = await resolveIdentity(
    {
      email: "new@example.com",
      phone: "+14155550123",
      source: "/dictionary",
      first_name: "New",
      last_name: "Lead",
    },
    { apiKey: "secret", fetchImpl, now: "2026-08-29T00:00:00.000Z" }
  );
  assert.match(result.internalUserId, /^usr_[0-9A-HJKMNP-TV-Z]{26}$/);
  const body = JSON.parse(calls[1].options.body);
  assert.deepEqual(body.data.attributes.properties, {
    internal_user_id: result.internalUserId,
    signup_date: "2026-08-29T00:00:00.000Z",
    signup_source: "/dictionary",
  });
  assert.equal(body.data.attributes.email, "new@example.com");
  assert.equal(body.data.attributes.phone_number, "+14155550123");
  assert.equal(body.data.attributes.first_name, "New");
  assert.equal(body.data.attributes.last_name, "Lead");
});

test("omits absent profile attributes", () => {
  const body = profileImportBody(
    { email: "person@example.com", source: "/learn-gaiish" },
    "usr_0123456789ABCDEFGHJKMNPQRS",
    { minted: true, now: "2026-08-29T00:00:00.000Z" }
  );
  assert.deepEqual(body.data.attributes, {
    email: "person@example.com",
    properties: {
      internal_user_id: "usr_0123456789ABCDEFGHJKMNPQRS",
      signup_date: "2026-08-29T00:00:00.000Z",
      signup_source: "/learn-gaiish",
    },
  });
});

test("records affirmative consent without writing false", () => {
  const consentBody = profileImportBody(
    { email: "person@example.com" },
    "usr_0123456789ABCDEFGHJKMNPQRS",
    { minted: false, consent: true, now: "2026-08-29T00:00:00.000Z" }
  );
  assert.equal(consentBody.data.attributes.properties.gaiish_updates_consent, true);
  assert.equal(
    consentBody.data.attributes.properties.gaiish_updates_consent_date,
    "2026-08-29T00:00:00.000Z"
  );
  const noConsentBody = profileImportBody(
    { email: "person@example.com" },
    "usr_0123456789ABCDEFGHJKMNPQRS",
    { minted: false, consent: false, now: "2026-08-29T00:00:00.000Z" }
  );
  assert.equal("gaiish_updates_consent" in noConsentBody.data.attributes.properties, false);
  assert.equal(
    "gaiish_updates_consent_date" in noConsentBody.data.attributes.properties,
    false
  );
  const absentConsentBody = profileImportBody(
    { email: "person@example.com" },
    "usr_0123456789ABCDEFGHJKMNPQRS",
    { minted: false, now: "2026-08-29T00:00:00.000Z" }
  );
  assert.equal(
    "gaiish_updates_consent" in absentConsentBody.data.attributes.properties,
    false
  );
});

test("constructs the exact email subscription body", () => {
  const withList = subscribeBody(
    { email: "person@example.com" },
    { listId: "XcbCUG", customSource: "Gaiish reference guide" }
  );
  assert.equal(withList.data.type, "profile-subscription-bulk-create-job");
  assert.equal(
    withList.data.attributes.profiles.data[0].attributes.email,
    "person@example.com"
  );
  assert.equal(
    withList.data.attributes.profiles.data[0].attributes.subscriptions.email.marketing.consent,
    "SUBSCRIBED"
  );
  assert.equal(withList.data.attributes.custom_source, "Gaiish reference guide");
  assert.deepEqual(withList.data.relationships.list.data, {
    type: "list",
    id: "XcbCUG",
  });

  const withoutList = subscribeBody(
    { email: "person@example.com" },
    { customSource: "Gaiish reference guide" }
  );
  assert.equal("relationships" in withoutList.data, false);
});

test("subscribes only affirmative email consent", async () => {
  async function run(identity) {
    const calls = [];
    const fetchImpl = async (url, options) => {
      calls.push({ url, options });
      if (calls.length === 1) {
        return {
          ok: true,
          status: 200,
          json: async () => ({ data: [] }),
        };
      }
      if (calls.length === 2) {
        return {
          ok: true,
          status: 201,
          json: async () => ({ data: { id: "profile_subscription" } }),
        };
      }
      return {
        ok: true,
        status: 202,
        json: async () => ({}),
      };
    };
    const result = await resolveIdentity(identity, {
      apiKey: "secret",
      fetchImpl,
      listId: "XcbCUG",
    });
    return { calls, result };
  }

  const optedIn = await run({ email: "person@example.com", consent: true });
  assert.equal(optedIn.calls.length, 3);
  assert.equal(
    optedIn.calls[2].url,
    "https://a.klaviyo.com/api/profile-subscription-bulk-create-jobs"
  );
  assert.equal(optedIn.calls[2].options.method, "POST");
  assert.equal(optedIn.calls[2].options.headers.revision, "2024-10-15");
  assert.equal(optedIn.result.emailSubscribed, true);

  const declined = await run({ email: "person@example.com", consent: false });
  assert.equal(declined.calls.length, 2);
  const unspecified = await run({ email: "person@example.com" });
  assert.equal(unspecified.calls.length, 2);
  const phoneOnly = await run({ phone: "+14155550123", consent: true });
  assert.equal(phoneOnly.calls.length, 2);
});

test("preserves identity when email subscription fails", async () => {
  const calls = [];
  const fetchImpl = async (url, options) => {
    calls.push({ url, options });
    if (calls.length === 1) {
      return {
        ok: true,
        status: 200,
        json: async () => ({ data: [] }),
      };
    }
    if (calls.length === 2) {
      return {
        ok: true,
        status: 201,
        json: async () => ({ data: { id: "profile_failed_subscription" } }),
      };
    }
    return {
      ok: false,
      status: 403,
      json: async () => ({}),
    };
  };
  const result = await resolveIdentity(
    { email: "person@example.com", consent: true },
    { apiKey: "secret", fetchImpl, listId: "XcbCUG" }
  );
  assert.equal(calls.length, 3);
  assert.match(result.internalUserId, /^usr_[0-9A-HJKMNP-TV-Z]{26}$/);
  assert.equal(result.klaviyoProfileId, "profile_failed_subscription");
  assert.equal(result.emailSubscribed, false);
  assert.equal(result.emailSubscribeStatus, 403);
});

test("serializes the HTTP response with the documented snake_case keys", async () => {
  const previousFetch = global.fetch;
  const previousKey = process.env.KLAVIYO_PRIVATE_API_KEY;
  const previousListId = process.env.KLAVIYO_LIST_ID;
  const calls = [];
  global.fetch = async (url, options) => {
    calls.push({ url, options });
    if (calls.length === 1) {
      return {
        ok: true,
        status: 200,
        json: async () => ({ data: [] }),
      };
    }
    if (calls.length === 2) {
      return {
        ok: true,
        status: 201,
        json: async () => ({ data: { id: "profile_http" } }),
      };
    }
    return {
      ok: true,
      status: 202,
      json: async () => ({}),
    };
  };
  process.env.KLAVIYO_PRIVATE_API_KEY = "secret";
  process.env.KLAVIYO_LIST_ID = "XcbCUG";
  const response = { headers: {}, statusCode: null, body: null };
  const res = {
    setHeader(name, value) {
      response.headers[name] = value;
    },
    status(statusCode) {
      response.statusCode = statusCode;
      return this;
    },
    json(body) {
      response.body = body;
      return this;
    },
  };
  try {
    await identifyHandler({
      method: "POST",
      headers: { origin: "http://localhost:8000" },
      body: { email: "person@example.com", consent: true },
    }, res);
  } finally {
    global.fetch = previousFetch;
    if (previousKey === undefined) delete process.env.KLAVIYO_PRIVATE_API_KEY;
    else process.env.KLAVIYO_PRIVATE_API_KEY = previousKey;
    if (previousListId === undefined) delete process.env.KLAVIYO_LIST_ID;
    else process.env.KLAVIYO_LIST_ID = previousListId;
  }
  assert.equal(response.statusCode, 200);
  assert.equal(response.headers["Cache-Control"], "no-store");
  assert.deepEqual(Object.keys(response.body).sort(), [
    "email_subscribed",
    "internal_user_id",
    "klaviyo_profile_id",
  ]);
  assert.match(response.body.internal_user_id, /^usr_[0-9A-HJKMNP-TV-Z]{26}$/);
  assert.equal(response.body.klaviyo_profile_id, "profile_http");
  assert.equal(response.body.email_subscribed, true);
  const importBody = JSON.parse(calls[1].options.body);
  assert.equal(importBody.data.attributes.properties.gaiish_updates_consent, true);
});
