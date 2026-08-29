(function () {
  "use strict";

  var STORAGE_KEY = "gaiish_identity";
  var GUIDE_URL = "/pdfguides/gaiish-key-concepts-and-definitions.pdf";

  function debugEnabled() {
    return location.hostname === "localhost" ||
      location.hostname === "127.0.0.1" ||
      new URLSearchParams(location.search).get("gaiishDebug") === "1";
  }

  function debug(message, details) {
    if (debugEnabled()) console.debug("[gaiish identity] " + message, details || {});
  }

  function value(value) {
    return typeof value === "string" ? value.trim() : "";
  }

  function readStoredIdentity() {
    try {
      var stored = JSON.parse(localStorage.getItem(STORAGE_KEY) || "null");
      if (!stored || typeof stored !== "object") return null;
      return {
        internal_user_id: value(stored.internal_user_id),
        klaviyo_profile_id: value(stored.klaviyo_profile_id)
      };
    } catch (error) {
      return null;
    }
  }

  function saveIdentity(identity) {
    try {
      localStorage.setItem(STORAGE_KEY, JSON.stringify({
        internal_user_id: value(identity.internal_user_id),
        klaviyo_profile_id: value(identity.klaviyo_profile_id)
      }));
    } catch (error) {
      debug("identity storage unavailable", {});
    }
  }

  function amplitudeReady(callback) {
    if (typeof window.gaiishAnalyticsReady === "function") {
      window.gaiishAnalyticsReady(callback);
    } else if (window.amplitude) {
      try {
        callback();
      } catch (error) {
        debug("Amplitude callback failed", {});
      }
    }
  }

  function applyAmplitudeIdentity(identity, properties) {
    if (!window.amplitude) return;
    var amplitude = window.amplitude;
    if (typeof amplitude.setUserId === "function" && identity.internal_user_id) {
      amplitude.setUserId(identity.internal_user_id);
    }
    var keys = Object.keys(properties);
    if (!keys.length || typeof amplitude.identify !== "function") return;

    if (typeof amplitude.Identify === "function") {
      try {
        var identify = new amplitude.Identify();
        keys.forEach(function (key) {
          if (typeof identify.set !== "function") {
            throw new Error("Identify.set unavailable");
          }
          identify.set(key, properties[key]);
        });
        amplitude.identify(identify);
        return;
      } catch (error) {
        debug("Amplitude Identify API unavailable", {});
      }
    }
    amplitude.identify(properties);
  }

  function applyStoredIdentity() {
    var stored = readStoredIdentity();
    if (!stored || !stored.internal_user_id) return;
    amplitudeReady(function () {
      applyAmplitudeIdentity(stored, {});
      debug("restored identity", { internal_user_id: stored.internal_user_id });
    });
  }

  function klaviyoIdentify(input, internalUserId) {
    if (!window.klaviyo || typeof window.klaviyo.push !== "function") return;
    var profile = {};
    if (input.email) profile.email = input.email;
    if (input.phone) profile.phone_number = input.phone;
    if (input.first_name) profile.first_name = input.first_name;
    if (input.last_name) profile.last_name = input.last_name;
    if (internalUserId) profile.internal_user_id = internalUserId;
    if (Object.keys(profile).length) window.klaviyo.push(["identify", profile]);
  }

  function requestIdentity(input) {
    var payload = {};
    if (input.email) payload.email = input.email;
    if (input.phone) payload.phone = input.phone;
    if (input.firstName) payload.first_name = input.firstName;
    if (input.lastName) payload.last_name = input.lastName;
    if (input.source) payload.source = input.source;
    return fetch("/api/identify", {
      method: "POST",
      headers: { "content-type": "application/json", accept: "application/json" },
      body: JSON.stringify(payload)
    }).then(function (response) {
      if (!response.ok) return { ok: false, internal_user_id: null, klaviyo_profile_id: null };
      return response.json().then(function (body) {
        return {
          ok: typeof body.internal_user_id === "string",
          internal_user_id: body.internal_user_id || null,
          klaviyo_profile_id: body.klaviyo_profile_id || null
        };
      });
    }).catch(function () {
      return { ok: false, internal_user_id: null, klaviyo_profile_id: null };
    });
  }

  window.gaiishIdentify = async function (details) {
    details = details || {};
    var input = {
      email: value(details.email),
      phone: value(details.phone),
      first_name: value(details.firstName),
      last_name: value(details.lastName),
      source: value(details.source)
    };
    var result = { ok: false, internalUserId: null };
    var serverIdentity = null;

    try {
      serverIdentity = await requestIdentity(input);
      if (serverIdentity.ok && serverIdentity.internal_user_id) {
        result.ok = true;
        result.internalUserId = serverIdentity.internal_user_id;
        saveIdentity(serverIdentity);
        amplitudeReady(function () {
          var properties = {};
          if (input.email) properties.email = input.email;
          if (input.phone) properties.phone = input.phone;
          if (input.first_name) properties.first_name = input.first_name;
          if (input.last_name) properties.last_name = input.last_name;
          if (input.source) properties.signup_source = input.source;
          if (serverIdentity.klaviyo_profile_id) {
            properties.klaviyo_profile_id = serverIdentity.klaviyo_profile_id;
          }
          applyAmplitudeIdentity(serverIdentity, properties);
          debug("Amplitude identity applied", {
            internal_user_id: serverIdentity.internal_user_id,
            has_email: Boolean(input.email),
            has_phone: Boolean(input.phone)
          });
        });
      }
    } catch (error) {
      debug("identity resolution failed", {
        has_email: Boolean(input.email),
        has_phone: Boolean(input.phone)
      });
    }

    try {
      klaviyoIdentify(input, serverIdentity && serverIdentity.ok
        ? serverIdentity.internal_user_id
        : null);
    } catch (error) {
      debug("Klaviyo identity failed", {});
    }
    debug("identify complete", {
      ok: result.ok,
      internal_user_id: result.internalUserId,
      has_email: Boolean(input.email),
      has_phone: Boolean(input.phone)
    });
    return result;
  };

  window.gaiishLogout = function () {
    try {
      localStorage.removeItem(STORAGE_KEY);
    } catch (error) {
      debug("identity storage unavailable", {});
    }
    amplitudeReady(function () {
      try {
        if (window.amplitude && typeof window.amplitude.reset === "function") {
          window.amplitude.reset();
        }
      } catch (error) {
        debug("Amplitude reset failed", {});
      }
    });
  };

  function setupCaptureForms() {
    document.querySelectorAll("[data-capture-form]").forEach(function (form) {
      form.addEventListener("submit", async function (event) {
        event.preventDefault();
        var submit = form.querySelector('button[type="submit"]');
        var status = form.querySelector("[data-capture-status]");
        var email = value(form.querySelector('[name="email"]').value);
        var firstName = value(form.querySelector('[name="first_name"]').value);
        submit.disabled = true;
        status.textContent = "Saving your details…";
        var result = await window.gaiishIdentify({
          email: email,
          firstName: firstName,
          source: location.pathname
        });
        window.gaiishTrack("lead_captured", {
          source: location.pathname,
          form_name: "gaiish_guide_download",
          content_type: "pdf"
        });
        if (result.ok) {
          form.outerHTML = '<p class="capture-success" role="status">Thanks — your guide is ready. '
            + '<a href="' + GUIDE_URL + '">Download the Gaiish reference guide (PDF)</a>.</p>';
        } else {
          submit.disabled = false;
          status.innerHTML = "We couldn't save your details right now, but you can still "
            + '<a href="' + GUIDE_URL + '">download the Gaiish reference guide (PDF)</a>.';
        }
      });
    });
  }

  applyStoredIdentity();
  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", setupCaptureForms);
  } else {
    setupCaptureForms();
  }
})();
