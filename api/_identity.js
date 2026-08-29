"use strict";

const crypto = require("crypto");

const EMAIL_RE = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
const PHONE_RE = /^\+[1-9]\d{7,14}$/;
const INTERNAL_USER_ID_RE = /^usr_[0-9A-HJKMNP-TV-Z]{26}$/;
const CROCKFORD = "0123456789ABCDEFGHJKMNPQRSTVWXYZ";

function hasValue(value) {
  return typeof value === "string" && value.trim() !== "";
}

function isValidEmail(email) {
  return typeof email === "string" &&
    email.length <= 254 &&
    !/[\\\"()\u0000-\u001f\u007f]/.test(email) &&
    EMAIL_RE.test(email);
}

function isValidPhone(phone) {
  return typeof phone === "string" && PHONE_RE.test(phone);
}

function isValidIdentity(identity) {
  if (!identity) return false;
  const hasEmail = hasValue(identity.email);
  const hasPhone = hasValue(identity.phone);
  return (hasEmail || hasPhone) &&
    (!hasEmail || isValidEmail(identity.email)) &&
    (!hasPhone || isValidPhone(identity.phone));
}

function isValidInternalUserId(value) {
  return typeof value === "string" && INTERNAL_USER_ID_RE.test(value);
}

function mintInternalUserId() {
  const bytes = crypto.randomBytes(26);
  let suffix = "";
  for (let index = 0; index < 26; index += 1) {
    suffix += CROCKFORD[bytes[index] & 31];
  }
  return "usr_" + suffix;
}

function lookupRequest(identity, apiKey) {
  const field = hasValue(identity.email) ? "email" : "phone_number";
  const value = hasValue(identity.email) ? identity.email : identity.phone;
  const params = new URLSearchParams();
  params.set("filter", `equals(${field},"${value}")`);
  params.set("fields[profile]", "email,phone_number,properties");
  return {
    url: "https://a.klaviyo.com/api/profiles?" + params.toString(),
    options: {
      method: "GET",
      headers: {
        Authorization: "Klaviyo-API-Key " + apiKey,
        revision: "2024-10-15",
        accept: "application/json",
      },
    },
  };
}

function profileImportBody(identity, internalUserId, options = {}) {
  const attributes = {};
  if (hasValue(identity.email)) attributes.email = identity.email;
  if (hasValue(identity.phone)) attributes.phone_number = identity.phone;
  if (hasValue(identity.first_name)) attributes.first_name = identity.first_name;
  if (hasValue(identity.last_name)) attributes.last_name = identity.last_name;

  const properties = { internal_user_id: internalUserId };
  if (options.minted) {
    properties.signup_date = options.now || new Date().toISOString();
    if (hasValue(identity.source)) properties.signup_source = identity.source;
  }
  if (options.consent === true) {
    properties.gaiish_updates_consent = true;
    properties.gaiish_updates_consent_date = options.now || new Date().toISOString();
  }
  attributes.properties = properties;
  return { data: { type: "profile", attributes } };
}

function subscribeBody(identity, options = {}) {
  const attributes = {
    email: identity.email,
    subscriptions: { email: { marketing: { consent: "SUBSCRIBED" } } },
  };
  const jobAttributes = { profiles: { data: [{ type: "profile", attributes }] } };
  if (hasValue(options.customSource)) jobAttributes.custom_source = options.customSource;
  const body = {
    data: {
      type: "profile-subscription-bulk-create-job",
      attributes: jobAttributes,
    },
  };
  if (hasValue(options.listId)) {
    body.data.relationships = {
      list: { data: { type: "list", id: options.listId } },
    };
  }
  return body;
}

function klaviyoError(status) {
  const error = new Error("Klaviyo request failed");
  error.klaviyoStatus = status;
  return error;
}

async function resolveIdentity(identity, options = {}) {
  const fetchImpl = options.fetchImpl || global.fetch;
  if (typeof fetchImpl !== "function") throw new Error("fetch_unavailable");
  if (!isValidIdentity(identity)) throw new Error("invalid_identity");

  const lookup = lookupRequest(identity, options.apiKey);
  const lookupResponse = await fetchImpl(lookup.url, lookup.options);
  if (!lookupResponse.ok) throw klaviyoError(lookupResponse.status);
  const lookupPayload = await lookupResponse.json();
  const profile = Array.isArray(lookupPayload.data) ? lookupPayload.data[0] : null;
  const existingId = profile && profile.attributes && profile.attributes.properties
    ? profile.attributes.properties.internal_user_id
    : null;
  const minted = !isValidInternalUserId(existingId);
  const internalUserId = minted ? mintInternalUserId() : existingId;

  const importBody = profileImportBody(identity, internalUserId, {
    minted,
    now: options.now,
    consent: identity.consent,
  });
  const importResponse = await fetchImpl(
    "https://a.klaviyo.com/api/profile-import",
    {
      method: "POST",
      headers: {
        Authorization: "Klaviyo-API-Key " + options.apiKey,
        revision: "2024-10-15",
        "content-type": "application/json",
        accept: "application/json",
      },
      body: JSON.stringify(importBody),
    }
  );
  if (![200, 201].includes(importResponse.status)) {
    throw klaviyoError(importResponse.status);
  }
  const importPayload = await importResponse.json();
  const klaviyoProfileId = importPayload.data && importPayload.data.id;
  if (typeof klaviyoProfileId !== "string" || klaviyoProfileId === "") {
    throw klaviyoError(importResponse.status);
  }
  let emailSubscribeStatus = null;
  if (identity.consent === true && hasValue(identity.email)) {
    const subscribeResponse = await fetchImpl(
      "https://a.klaviyo.com/api/profile-subscription-bulk-create-jobs",
      {
        method: "POST",
        headers: {
          Authorization: "Klaviyo-API-Key " + options.apiKey,
          revision: "2024-10-15",
          "content-type": "application/json",
          accept: "application/json",
        },
        body: JSON.stringify(subscribeBody(identity, {
          listId: options.listId,
          customSource: options.customSource || "Gaiish reference guide",
        })),
      }
    );
    emailSubscribeStatus = subscribeResponse.status;
  }

  return {
    internalUserId,
    klaviyoProfileId,
    emailSubscribed: emailSubscribeStatus === 202,
    emailSubscribeStatus,
  };
}

module.exports = {
  CROCKFORD,
  EMAIL_RE,
  PHONE_RE,
  INTERNAL_USER_ID_RE,
  isValidEmail,
  isValidPhone,
  isValidIdentity,
  isValidInternalUserId,
  mintInternalUserId,
  lookupRequest,
  profileImportBody,
  subscribeBody,
  resolveIdentity,
};
