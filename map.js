(function () {
  var dialog = document.getElementById("popin");
  var body = dialog.querySelector(".popin-body");
  var panels = document.getElementById("panels");
  var lastFocus = null;

  function open(name) {
    var panel = panels.querySelector('[data-panel="' + name + '"]');
    if (!panel) return;
    body.innerHTML = panel.innerHTML;
    var heading = body.querySelector("h2");
    if (heading) heading.id = "popin-title";
    lastFocus = document.activeElement;
    if (typeof dialog.showModal === "function") {
      dialog.showModal();
    } else {
      dialog.setAttribute("open", "");
    }
  }

  function close() {
    if (typeof dialog.close === "function") {
      dialog.close();
    } else {
      dialog.removeAttribute("open");
    }
  }

  document.addEventListener("click", function (event) {
    var trigger = event.target.closest("[data-panel]");
    if (trigger && !panels.contains(trigger)) {
      open(trigger.getAttribute("data-panel"));
      return;
    }
    if (event.target.closest("[data-close]")) {
      close();
      return;
    }
    if (event.target === dialog) close();
  });

  dialog.addEventListener("close", function () {
    if (lastFocus && lastFocus.focus) lastFocus.focus();
  });
})();
