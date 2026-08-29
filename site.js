(function () {
  "use strict";

  var nav = document.querySelector(".sitenav");
  var toggle = nav && nav.querySelector(".nav-toggle");

  function closeNav() {
    if (!nav || !toggle) return;
    nav.classList.remove("nav-open");
    toggle.setAttribute("aria-expanded", "false");
  }

  if (nav && toggle) {
    toggle.addEventListener("click", function () {
      var expanded = toggle.getAttribute("aria-expanded") === "true";
      toggle.setAttribute("aria-expanded", String(!expanded));
      nav.classList.toggle("nav-open", !expanded);
    });

    document.addEventListener("click", function (event) {
      if (!nav.contains(event.target)) closeNav();
    });

    document.addEventListener("keydown", function (event) {
      if (event.key === "Escape") closeNav();
    });
  }

  var AMPLITUDE_API_KEY = "4a2afc52a58978951b1f9581137bc7a1";

  var queue = [];

  function loadAmplitude() {
    if (!AMPLITUDE_API_KEY) return;
    var script = document.createElement("script");
    script.src = "https://cdn.amplitude.com/script/" + AMPLITUDE_API_KEY + ".js";
    script.async = true;
    script.onload = function () {
      if (!window.amplitude) return;
      if (window.sessionReplay && typeof window.sessionReplay.plugin === "function") {
        window.amplitude.add(
          window.sessionReplay.plugin({
            sampleRate: 1,
            privacyConfig: { defaultMaskLevel: "conservative" }
          })
        );
      }
      window.amplitude.init(AMPLITUDE_API_KEY, {
        fetchRemoteConfig: true,
        autocapture: { attribution: true, pageViews: true, sessions: true, elementInteractions: false }
      });
      while (queue.length) {
        var queued = queue.shift();
        window.amplitude.track(queued[0], queued[1]);
      }
    };
    document.head.appendChild(script);
  }

  loadAmplitude();

  /*
   * Analytics event shim. It never receives prompt text; callers pass only an event name and
   * non-sensitive metadata. Events raised before the SDK is ready are queued and flushed.
   * Amplitude session replay is enabled site-wide with conservative masking for all text and
   * inputs.
   */
  window.gaiishTrack = function (event, detail) {
    if (Array.isArray(window.dataLayer)) {
      window.dataLayer.push({ event: event, detail: detail });
    }
    if (window.amplitude && typeof window.amplitude.track === "function") {
      window.amplitude.track(event, detail);
    } else {
      queue.push([event, detail]);
    }
  };
})();
