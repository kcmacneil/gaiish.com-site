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

  /*
   * Analytics integrations may listen to this event shim. It never receives prompt text;
   * callers should pass only an event name and non-sensitive metadata.
   */
  window.gaiishTrack = function (event, detail) {
    if (Array.isArray(window.dataLayer)) {
      window.dataLayer.push({ event: event, detail: detail });
    }
  };
})();
