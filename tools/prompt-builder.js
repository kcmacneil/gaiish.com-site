(function () {
  "use strict";

  var form = document.getElementById("prompt-builder-form");
  if (!form) return;

  var fields = ["intent", "context", "audience", "role", "knowledge", "instructions", "constraints", "output", "tone", "validation"];
  var storageKey = "gaiish-prompt-builder";
  var preview = document.getElementById("builder-output-preview");
  var status = document.getElementById("builder-status");
  var labels = {
    intent: "INTENT",
    context: "CONTEXT",
    audience: "AUDIENCE",
    role: "ROLE",
    knowledge: "KNOWLEDGE",
    instructions: "INSTRUCTION",
    constraints: "CONSTRAINTS",
    output: "OUTPUT",
    tone: "TONE",
    validation: "VALIDATION"
  };

  function value(name) {
    return form.elements[name].value.trim();
  }

  function promptText() {
    return fields.filter(function (name) {
      return value(name);
    }).map(function (name) {
      return labels[name] + ":\n" + value(name);
    }).join("\n\n");
  }

  function setStatus(message) {
    status.textContent = message;
  }

  function generate(announce) {
    preview.textContent = promptText() || "Your prompt will appear here as you fill in the fields.";
    if (announce) {
      setStatus("Prompt generated locally.");
      window.gaiishTrack("prompt_generated", { source: "builder" });
    }
  }

  function save() {
    var data = {};
    fields.forEach(function (name) { data[name] = value(name); });
    try {
      window.localStorage.setItem(storageKey, JSON.stringify(data));
      setStatus("Prompt fields saved on this device.");
      window.gaiishTrack("prompt_saved", { source: "builder" });
    } catch (error) {
      setStatus("Could not save locally in this browser.");
    }
  }

  function load() {
    try {
      var saved = JSON.parse(window.localStorage.getItem(storageKey) || "null");
      if (!saved) return false;
      fields.forEach(function (name) {
        if (typeof saved[name] === "string") form.elements[name].value = saved[name];
      });
      return true;
    } catch (error) {
      return false;
    }
  }

  function copyFallback(text) {
    var area = document.createElement("textarea");
    area.value = text;
    area.setAttribute("readonly", "");
    area.style.position = "fixed";
    area.style.opacity = "0";
    document.body.appendChild(area);
    area.select();
    var copied = false;
    try { copied = document.execCommand("copy"); } catch (error) { copied = false; }
    document.body.removeChild(area);
    return copied;
  }

  function copy() {
    var text = promptText();
    if (!text) {
      setStatus("Add at least one field before copying.");
      return;
    }
    var result = window.navigator.clipboard && window.navigator.clipboard.writeText
      ? window.navigator.clipboard.writeText(text)
      : Promise.resolve(copyFallback(text));
    result.then(function (success) {
      if (success === false) throw new Error("fallback failed");
      setStatus("Prompt copied to your clipboard.");
      window.gaiishTrack("prompt_copied", { source: "builder" });
    }).catch(function () {
      setStatus("Copy was unavailable. Select the prompt and copy it manually.");
    });
  }

  form.addEventListener("submit", function (event) {
    event.preventDefault();
    generate(true);
  });
  fields.forEach(function (name) {
    form.elements[name].addEventListener("input", function () { generate(false); });
  });
  document.getElementById("builder-copy").addEventListener("click", copy);
  document.getElementById("builder-save").addEventListener("click", save);
  document.getElementById("builder-clear").addEventListener("click", function () {
    fields.forEach(function (name) { form.elements[name].value = ""; });
    generate(false);
    setStatus("Fields cleared.");
    window.gaiishTrack("prompt_cleared", { source: "builder" });
  });
  document.getElementById("builder-edit").addEventListener("click", function () {
    form.elements.intent.focus();
    window.scrollTo({ top: form.getBoundingClientRect().top + window.scrollY - 20, behavior: "smooth" });
  });

  var restored = load();
  generate(false);
  if (restored) setStatus("Saved fields restored from this device.");
  window.gaiishTrack("tool_viewed", { tool: "prompt_builder" });
})();
