"use strict";

const test = require("node:test");
const assert = require("node:assert/strict");
const { isAllowedOrigin } = require("../api/identify");
const {
  isValidEmail,
  isValidPhone,
  isValidIdentity,
  isValidInternalUserId,
  lookupRequest,
  mintInternalUserId,
  profileImportBody,
  resolveIdentity,
} = require("../api/_identity");

test("validates email and phone identities", () => {
  assert.equal(isValidEmail("person@example.com"), true);
  assert.equal(isValidEmail("not-an-email"), false);
  assert.equal(isValidEmail("a".repeat(250) + "@x.com"), false);
  assert.equal(isValidPhone("+14155550123"), true);
  assert.equal(isValidPhone("4155550123"), false);
  assert.equal(isValidIdentity({ email: "person@example.com" }), true);
  assert.equal(isValidIdentity({ phone: "+14155550123" }), true);
  assert.equal(isValidIdentity({ email: "bad", phone: "+14155550123" }), false);
  assert.equal(isValidIdentity({}), false);
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
