(function () {
  "use strict";

  var form = document.getElementById("prompt-analyzer-form");
  if (!form || !window.GaiishScore) return;
  var input = document.getElementById("analyzer-input");
  var results = document.getElementById("analyzer-results");
  var status = document.getElementById("analyzer-status");
  var total = document.getElementById("analyzer-total");
  var band = document.getElementById("analyzer-band");
  var breakdown = document.getElementById("analyzer-breakdown");

  function list(id, items, empty) {
    var target = document.getElementById(id);
    target.innerHTML = "";
    if (!items.length) {
      target.innerHTML = "<li>" + empty + "</li>";
      return;
    }
    items.forEach(function (item) {
      var li = document.createElement("li");
      li.textContent = item;
      target.appendChild(li);
    });
  }

  function analyze() {
    var report = window.GaiishScore.analyze(input.value);
    total.textContent = report.total;
    band.textContent = report.band + " · " + report.words + " words";
    breakdown.innerHTML = "";
    var table = document.createElement("div");
    table.className = "score-list";
    report.components.forEach(function (component) {
      var item = document.createElement("div");
      item.className = "score-item score-" + component.state;
      item.innerHTML = "<div><strong>" + component.name + "</strong><span>" + component.points + " / " + component.weight + "</span></div>" +
        "<p><span class=\"score-state\">" + component.state + "</span> " +
        (component.labelled ? "Explicitly labelled." : component.signalled ? "Signalled by wording." : "Not explicit.") + "</p>";
      table.appendChild(item);
    });
    breakdown.appendChild(table);
    list("analyzer-good", report.good.map(function (item) { return item.name + " — " + item.points + " / " + item.weight; }), "No components are strong yet.");
    list("analyzer-missing", report.absent.map(function (item) { return item.name + ": " + item.missing; }).concat(report.partial.map(function (item) { return item.name + " is partial: " + item.missing; })), "No major components are absent.");
    list("analyzer-improvements", report.components.filter(function (item) { return item.state !== "strong"; }).map(function (item) { return item.name + ": " + item.improve; }), "The six components are all strongly represented.");
    results.hidden = false;
    status.textContent = "Prompt analyzed locally.";
    window.gaiishTrack("prompt_analyzed", { source: "analyzer", score_band: report.band });
  }

  form.addEventListener("submit", function (event) {
    event.preventDefault();
    analyze();
  });
  document.getElementById("analyzer-convert").addEventListener("click", function () {
    input.value = window.GaiishScore.toGaiish(input.value);
    analyze();
    status.textContent = "Prompt converted to a Gaiish skeleton locally.";
    window.gaiishTrack("prompt_converted", { source: "analyzer" });
  });
  document.getElementById("analyzer-clear").addEventListener("click", function () {
    input.value = "";
    results.hidden = true;
    status.textContent = "Prompt cleared.";
  });
  window.gaiishTrack("tool_viewed", { tool: "prompt_analyzer" });
})();
