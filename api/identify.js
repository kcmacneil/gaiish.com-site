"use strict";

const {
  isValidIdentity,
  resolveIdentity,
} = require("./_identity");

const ALLOWED_ORIGINS = new Set([
  "https://gaiish.com",
  "https://www.gaiish.com",
]);

function isAllowedOrigin(origin) {
  if (typeof origin !== "string" || origin === "") return false;
  if (ALLOWED_ORIGINS.has(origin)) return true;
  try {
    const parsed = new URL(origin);
    return parsed.protocol === "http:" &&
      (parsed.hostname === "localhost" || parsed.hostname === "127.0.0.1");
  } catch (error) {
    return false;
  }
}

function send(res, status, body) {
  res.setHeader("Cache-Control", "no-store");
  res.status(status).json(body);
}

function logFailure(code, status) {
  const details = { code };
  if (typeof status === "number") details.status = status;
  console.error("identity_request_failed", details);
}

function parseBody(body) {
  if (body && typeof body === "object") return body;
  if (typeof body !== "string" || body === "") return {};
  try {
    return JSON.parse(body);
  } catch (error) {
    return {};
  }
}

module.exports = async (req, res) => {
  if (req.method !== "POST") {
    send(res, 405, { error: "method_not_allowed" });
    return;
  }
  if (!isAllowedOrigin(req.headers && req.headers.origin)) {
    send(res, 403, { error: "origin_forbidden" });
    return;
  }

  const body = parseBody(req.body);
  if (!isValidIdentity(body)) {
    send(res, 400, { error: "invalid_identity" });
    return;
  }

  const apiKey = typeof process.env.KLAVIYO_PRIVATE_API_KEY === "string"
    ? process.env.KLAVIYO_PRIVATE_API_KEY.trim()
    : "";
  if (!apiKey) {
    send(res, 503, { error: "identity_unavailable" });
    return;
  }

  const controller = new AbortController();
  const timeout = setTimeout(() => controller.abort(), 10000);
  const fetchImpl = (url, options) => global.fetch(url, { ...options, signal: controller.signal });
  try {
    const listId = typeof process.env.KLAVIYO_LIST_ID === "string"
      ? process.env.KLAVIYO_LIST_ID.trim()
      : "";
    const result = await resolveIdentity(body, { apiKey, fetchImpl, listId });
    if (result.emailSubscribeStatus !== null && !result.emailSubscribed) {
      logFailure("email_subscribe_failed", result.emailSubscribeStatus);
    }
    send(res, 200, {
      internal_user_id: result.internalUserId,
      klaviyo_profile_id: result.klaviyoProfileId,
      email_subscribed: result.emailSubscribed,
    });
  } catch (error) {
    const status = typeof error.klaviyoStatus === "number" ? error.klaviyoStatus : undefined;
    logFailure("identity_lookup_failed", status);
    send(res, 502, { error: "identity_lookup_failed" });
  } finally {
    clearTimeout(timeout);
  }
};

module.exports.isAllowedOrigin = isAllowedOrigin;
module.exports.parseBody = parseBody;
