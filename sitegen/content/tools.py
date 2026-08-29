"""Browser-only interactive tools."""

from .. import config


TOOLS_HUB = {
    "route": "/tools", "title": "Gaiish Tools",
    "description": "Free browser-based Gaiish tools: build a structured prompt or inspect one with a heuristic score.",
    "eyebrow": "Interactive tools", "h1": "Gaiish Tools",
    "lede": "Shape a prompt, inspect its structure, and keep your work on your own device.",
    "breadcrumbs": [("Tools", "/tools")], "nav_key": "/tools",
    "updated": config.LAST_UPDATED,
    "schema": [{
        "@context": "https://schema.org", "@type": "CollectionPage",
        "name": "Gaiish Tools", "url": config.SITE_URL + "/tools",
        "hasPart": [{"@type": "WebApplication", "name": "Gaiish Prompt Builder",
                    "url": config.SITE_URL + "/tools/prompt-builder",
                    "applicationCategory": "BusinessApplication", "operatingSystem": "Web",
                    "isAccessibleForFree": True, "description": "A browser-based prompt builder with no account."},
                   {"@type": "WebApplication", "name": "Gaiish Prompt Analyzer",
                    "url": config.SITE_URL + "/tools/prompt-analyzer",
                    "applicationCategory": "BusinessApplication", "operatingSystem": "Web",
                    "isAccessibleForFree": True, "description": "A browser-based heuristic prompt analyzer with no account."}],
    }],
    "blocks": [
        ("callout", "Private by design", "Everything runs in your browser. Nothing you type is sent to a server or to analytics. Do not paste material into any tool unless you are allowed to use it in your browser."),
        ("cards", [
            ("Prompt Builder", "Answer ten guided fields and get a formatted Gaiish prompt. Copy it or save it locally on this device.", "/tools/prompt-builder"),
            ("Prompt Analyzer", "Inspect how explicitly a prompt expresses the six Gaiish components. The score is a heuristic, not a validated measurement.", "/tools/prompt-analyzer"),
        ]),
        ("h2", "Use the tools with judgment", "judgment"),
        ("p", "A structured prompt can improve instruction adherence and reduce ambiguity, but no form or score guarantees a correct response. Models do not interpret prompts identically. Validate important facts, calculations, sources and actions."),
    ],
}


BUILDER = {
    "route": "/tools/prompt-builder", "title": "Gaiish Prompt Builder",
    "description": "Build a structured Gaiish prompt in your browser with guided fields, local saving and clipboard support.",
    "eyebrow": "Tool", "h1": "Gaiish Prompt Builder",
    "lede": "Fill in only what matters, then copy a clear prompt structure. Your entries stay in this browser.",
    "breadcrumbs": [("Tools", "/tools")], "nav_key": "/tools",
    "updated": config.LAST_UPDATED, "scripts": ["/tools/prompt-builder.js"],
    "schema": [{
        "@context": "https://schema.org", "@type": "WebApplication",
        "name": "Gaiish Prompt Builder", "url": config.SITE_URL + "/tools/prompt-builder",
        "applicationCategory": "BusinessApplication", "operatingSystem": "Web",
        "isAccessibleForFree": True, "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"},
        "description": "A free browser-based form for building a Gaiish prompt. No account is required; entries are not sent to a server or analytics.",
        "featureList": ["Guided Gaiish fields", "Local browser saving", "Clipboard copy"],
    }],
    "blocks": [("html", """
<div class="tool-layout">
  <form id="prompt-builder-form" class="tool-form">
    <p class="privacy-note"><strong>Private by design:</strong> this tool runs in your browser. Nothing you type is sent to a server or analytics.</p>
    <p class="form-intro">Fields marked recommended help most tasks. You can leave a field blank and add it later.</p>
    <div class="field"><label for="builder-intent">Goal / Intent <span>(recommended)</span></label><p id="hint-builder-intent" class="field-hint">What outcome should this work support, and who will use it?</p><textarea id="builder-intent" name="intent" aria-describedby="hint-builder-intent" rows="3"></textarea></div>
    <div class="field"><label for="builder-context">Context <span>(recommended)</span></label><p id="hint-builder-context" class="field-hint">Add the situation, audience and source material the model cannot infer.</p><textarea id="builder-context" name="context" aria-describedby="hint-builder-context" rows="4"></textarea></div>
    <div class="field"><label for="builder-audience">Audience</label><p id="hint-builder-audience" class="field-hint">Who will read or use the result?</p><input id="builder-audience" name="audience" aria-describedby="hint-builder-audience" /></div>
    <div class="field"><label for="builder-role">Role</label><p id="hint-builder-role" class="field-hint">What useful perspective or role should the model take?</p><input id="builder-role" name="role" aria-describedby="hint-builder-role" /></div>
    <div class="field"><label for="builder-knowledge">Knowledge</label><p id="hint-builder-knowledge" class="field-hint">What sources, definitions or evidence should be authoritative?</p><textarea id="builder-knowledge" name="knowledge" aria-describedby="hint-builder-knowledge" rows="3"></textarea></div>
    <div class="field"><label for="builder-instructions">Instructions <span>(recommended)</span></label><p id="hint-builder-instructions" class="field-hint">Name the action with a clear primary verb; number steps when order matters.</p><textarea id="builder-instructions" name="instructions" aria-describedby="hint-builder-instructions" rows="4"></textarea></div>
    <div class="field"><label for="builder-constraints">Constraints</label><p id="hint-builder-constraints" class="field-hint">State scope, limits, tone, requirements and exclusions.</p><textarea id="builder-constraints" name="constraints" aria-describedby="hint-builder-constraints" rows="3"></textarea></div>
    <div class="field"><label for="builder-output">Output</label><p id="hint-builder-output" class="field-hint">Describe the artefact: sections, fields, format and useful length.</p><textarea id="builder-output" name="output" aria-describedby="hint-builder-output" rows="3"></textarea></div>
    <div class="field"><label for="builder-tone">Tone</label><p id="hint-builder-tone" class="field-hint">For example: concise, warm, formal or plain language.</p><input id="builder-tone" name="tone" aria-describedby="hint-builder-tone" /></div>
    <div class="field"><label for="builder-validation">Validation</label><p id="hint-builder-validation" class="field-hint">How should the result be checked, and what should be flagged?</p><textarea id="builder-validation" name="validation" aria-describedby="hint-builder-validation" rows="3"></textarea></div>
    <div class="tool-actions"><button type="submit" class="cta cta-primary">Generate Prompt</button><button type="button" id="builder-copy" class="cta">Copy Prompt</button><button type="button" id="builder-save" class="cta">Save locally</button><button type="button" id="builder-clear" class="cta">Clear</button></div>
    <p id="builder-status" class="tool-status" role="status" aria-live="polite"></p>
  </form>
  <section class="prompt-result" aria-labelledby="builder-result-heading">
    <h2 id="builder-result-heading">Your Gaiish Prompt</h2>
    <p class="field-hint">Edit the fields above to update this preview.</p>
    <pre id="builder-output-preview" tabindex="0"></pre>
    <button type="button" id="builder-edit" class="cta">Edit fields</button>
  </section>
</div>
""")],
}


ANALYZER = {
    "route": "/tools/prompt-analyzer", "title": "Gaiish Prompt Analyzer",
    "description": "Analyze a prompt in your browser against the six-part Gaiish framework with a transparent heuristic score.",
    "eyebrow": "Tool", "h1": "Gaiish Prompt Analyzer",
    "lede": "See which parts of your request are explicit, then decide what to improve. The result is a heuristic, not a validated measurement.",
    "breadcrumbs": [("Tools", "/tools")], "nav_key": "/tools",
    "updated": config.LAST_UPDATED, "scripts": ["/tools/analyzer-score.js", "/tools/prompt-analyzer.js"],
    "schema": [{
        "@context": "https://schema.org", "@type": "WebApplication",
        "name": "Gaiish Prompt Analyzer", "url": config.SITE_URL + "/tools/prompt-analyzer",
        "applicationCategory": "BusinessApplication", "operatingSystem": "Web",
        "isAccessibleForFree": True, "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"},
        "description": "A free browser-based heuristic analyzer for prompt structure. No account is required; prompt text is not sent to a server or analytics.",
        "featureList": ["Gaiish component breakdown", "Heuristic score", "Convert to Gaiish"],
    }],
    "blocks": [("html", """
<div class="analyzer-layout">
  <form id="prompt-analyzer-form" class="tool-form">
    <p class="privacy-note"><strong>Private by design:</strong> this tool runs in your browser. Nothing you type is sent to a server or analytics.</p>
    <label for="analyzer-input">Prompt to analyze</label>
    <p id="hint-analyzer-input" class="field-hint">Paste a prompt. It will be inspected locally and never submitted.</p>
    <textarea id="analyzer-input" aria-describedby="hint-analyzer-input" rows="12" placeholder="Write a marketing plan for my company."></textarea>
    <div class="tool-actions"><button type="submit" class="cta cta-primary">Analyze Prompt</button><button type="button" id="analyzer-convert" class="cta">Convert to Gaiish</button><button type="button" id="analyzer-clear" class="cta">Clear</button></div>
    <p id="analyzer-status" class="tool-status" role="status" aria-live="polite"></p>
  </form>
  <section id="analyzer-results" class="analyzer-results" aria-live="polite" aria-labelledby="analyzer-score-heading" hidden>
    <p class="heuristic-warning"><strong>Heuristic only:</strong> this score reflects explicit Gaiish structure. It is not a validated measurement and does not judge truth, quality or model behaviour.</p>
    <h2 id="analyzer-score-heading">Gaiish Score: <span id="analyzer-total">0</span><span class="score-out-of"> / 100</span></h2>
    <p id="analyzer-band"></p>
    <div id="analyzer-breakdown"></div>
    <div class="analyzer-columns"><section><h2>What's Good</h2><ul id="analyzer-good"></ul></section><section><h2>What's Missing</h2><ul id="analyzer-missing"></ul></section></div>
    <section><h2>Suggested Improvements</h2><ul id="analyzer-improvements"></ul></section>
  </section>
</div>
""")],
}


PAGES = [TOOLS_HUB, BUILDER, ANALYZER]
