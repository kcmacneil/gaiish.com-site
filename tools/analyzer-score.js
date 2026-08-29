/**
 * Gaiish Score — a heuristic, not a validated measurement.
 *
 * The score describes how much of the Gaiish framework a prompt makes explicit. It cannot
 * judge whether a prompt is good, whether the facts in it are true, or how a given model will
 * respond to it. Weights follow the framework's emphasis:
 *
 *   Intent 20 · Context 20 · Instruction 20 · Constraints 15 · Output 15 · Validation 10
 *
 * Each component scores in three parts:
 *   - labelled:  an explicit Gaiish label (INTENT:, CONTEXT:, …) is present
 *   - signalled: wording that carries the component even without a label
 *   - substance: enough material to actually communicate it (length / specificity)
 *
 * Everything runs in the browser; prompt text never leaves the page.
 */
(function (root) {
  "use strict";

  var COMPONENTS = [
    {
      key: "intent",
      name: "Intent",
      weight: 20,
      labels: [/\bintent\b\s*:/i, /\bgoal\b\s*:/i, /\bobjective\b\s*:/i, /\bpurpose\b\s*:/i],
      signals: [
        /\b(so that|in order to|so we can|the goal is|i(?:'m| am) trying to|i need to|we need to|so i can)\b/i,
        /\b(decide|decision|choose between|evaluate whether|determine whether)\b/i
      ],
      missing:
        "Say what the output is for — the decision, deliverable or change behind the request.",
      improve:
        "Add an INTENT line naming the outcome you are working toward and who will use the result."
    },
    {
      key: "context",
      name: "Context",
      weight: 20,
      labels: [/\bcontext\b\s*:/i, /\bbackground\b\s*:/i, /\baudience\b\s*:/i, /\bknowledge\b\s*:/i],
      signals: [
        /\b(our|we are|we have|my team|the company|currently|today we|attached|below|following|pasted)\b/i,
        /\b(audience|readers?|customers?|stakeholders?|users?) (are|is|will be)\b/i
      ],
      missing:
        "Supply what the model cannot infer: the material, the situation, the audience, what has already been tried.",
      improve:
        "Paste the source material and add a CONTEXT line with the situation and the audience."
    },
    {
      key: "instruction",
      name: "Instruction",
      weight: 20,
      labels: [/\binstruction[s]?\b\s*:/i, /\btask\b\s*:/i, /\baction\b\s*:/i, /\bprocess\b\s*:/i],
      signals: [
        /\b(write|draft|rewrite|summari[sz]e|analy[sz]e|compare|extract|classify|list|explain|translate|review|plan|generate|refactor|debug|design|calculate)\b/i
      ],
      missing: "Name the action explicitly with a single primary verb.",
      improve:
        "State one primary action (draft, analyse, extract …) and number the steps when order matters."
    },
    {
      key: "constraints",
      name: "Constraints",
      weight: 15,
      labels: [/\bconstraint[s]?\b\s*:/i, /\brules?\b\s*:/i, /\brequirements?\b\s*:/i, /\blimits?\b\s*:/i, /\btone\b\s*:/i],
      signals: [
        /\b(no more than|at most|at least|under|maximum|minimum|max|min|exactly)\b/i,
        /\b\d+\s*(words?|sentences?|bullets?|paragraphs?|rows?|items?|characters?|pages?|slides?|days?|weeks?)\b/i,
        /\b(do not|don't|avoid|exclude|without|never|only)\b/i,
        /\b(tone|register|reading level|plain language|formal|informal)\b/i,
        /\b(budget|deadline|currency|\$\d)/i
      ],
      missing:
        "Bound the answer: quantities, scope, tone, and what to leave out.",
      improve:
        "Add a CONSTRAINTS line with numbers (length, counts, budget) and explicit exclusions."
    },
    {
      key: "output",
      name: "Output",
      weight: 15,
      labels: [/\boutput\b\s*:/i, /\bresult\b\s*:/i, /\bformat\b\s*:/i, /\bdeliverable\b\s*:/i],
      signals: [
        /\b(as (a|an) (table|list|email|json|csv|markdown|bullet|summary|report|memo|outline)|in (json|csv|markdown|yaml|xml))\b/i,
        /\b(sections?|columns?|headings?|schema|template|structure)\b/i,
        /\b(table|bullet points|numbered list|json|csv|markdown)\b/i
      ],
      missing:
        "Describe the artefact you expect: the sections, columns or schema, in order.",
      improve:
        "Add an OUTPUT line listing the exact sections or fields the finished result should contain."
    },
    {
      key: "validation",
      name: "Validation",
      weight: 10,
      labels: [/\bvalidation\b\s*:/i, /\bverify\b\s*:/i, /\bcheck\b\s*:/i, /\bquality\b\s*:/i],
      signals: [
        /\b(check|verify|confirm|double[- ]check|make sure|ensure) (that |the |your |each |every )?(output|result|answer|response|it|this|every|each)\b/i,
        /\b(cite|quote|reference) (the |your |every |each )?(source|clause|line|passage|document)\b/i,
        /\b(list|state|flag|mark) (any |every |all )?(assumption|assumptions|gaps?|uncertaint\w+|unknowns?)\b/i,
        /\b(if .* (is )?(missing|absent|not (present|available|found)))\b/i,
        /\bsay so\b/i
      ],
      missing:
        "Ask the model to check its own output against the request and report what it could not do.",
      improve:
        "Add a VALIDATION line: check the result against each constraint, and list assumptions or missing facts instead of inventing them."
    }
  ];

  // Substance thresholds, in words of prompt material attributable to the component.
  var SUBSTANCE_WORDS = 12;

  function words(text) {
    var trimmed = text.trim();
    return trimmed ? trimmed.split(/\s+/).length : 0;
  }

  function labelledSections(text) {
    // Splits "LABEL: body" sections so substance can be attributed per component.
    var sections = {};
    var pattern = /^[ \t]*([A-Za-z][A-Za-z /_-]{1,30}?)[ \t]*:[ \t]*$|^[ \t]*([A-Za-z][A-Za-z /_-]{1,30}?)[ \t]*:[ \t]+(.*)$/gm;
    var match;
    var order = [];
    while ((match = pattern.exec(text)) !== null) {
      var label = (match[1] || match[2] || "").trim().toLowerCase();
      order.push({ label: label, start: match.index, bodyStart: pattern.lastIndex });
    }
    for (var i = 0; i < order.length; i += 1) {
      var end = i + 1 < order.length ? order[i + 1].start : text.length;
      var body = text.slice(order[i].bodyStart, end);
      sections[order[i].label] = (sections[order[i].label] || "") + " " + body;
    }
    return sections;
  }

  function matchesAny(patterns, text) {
    for (var i = 0; i < patterns.length; i += 1) {
      if (patterns[i].test(text)) return true;
    }
    return false;
  }

  function sectionBodyFor(component, sections) {
    for (var label in sections) {
      if (!Object.prototype.hasOwnProperty.call(sections, label)) continue;
      for (var i = 0; i < component.labels.length; i += 1) {
        if (component.labels[i].test(label + ":")) return sections[label];
      }
    }
    return null;
  }

  /**
   * Score one component out of its weight:
   *   40% for being present at all (label or signal)
   *   30% for an explicit Gaiish label
   *   30% for substance (a labelled body of >= SUBSTANCE_WORDS words, or, when unlabelled,
   *        a prompt long enough that the signal is carrying real material)
   */
  function scoreComponent(component, text, sections, totalWords) {
    var labelled = matchesAny(component.labels, text);
    var signalled = matchesAny(component.signals, text);
    var body = sectionBodyFor(component, sections);
    var bodyWords = body === null ? 0 : words(body);

    var fraction = 0;
    if (labelled || signalled) fraction += 0.4;
    if (labelled) fraction += 0.3;
    if (labelled && bodyWords >= SUBSTANCE_WORDS) {
      fraction += 0.3;
    } else if (labelled && bodyWords >= SUBSTANCE_WORDS / 2) {
      fraction += 0.15;
    } else if (!labelled && signalled && totalWords >= 40) {
      fraction += 0.15;
    }

    var points = Math.round(component.weight * Math.min(fraction, 1));
    return {
      key: component.key,
      name: component.name,
      weight: component.weight,
      points: points,
      labelled: labelled,
      signalled: signalled,
      bodyWords: bodyWords,
      state: points >= component.weight * 0.8 ? "strong" : points > 0 ? "partial" : "absent",
      missing: component.missing,
      improve: component.improve
    };
  }

  function analyze(text) {
    var input = String(text || "");
    var totalWords = words(input);
    var sections = labelledSections(input);
    var results = COMPONENTS.map(function (component) {
      return scoreComponent(component, input, sections, totalWords);
    });
    var total = results.reduce(function (sum, result) {
      return sum + result.points;
    }, 0);

    var good = results.filter(function (r) {
      return r.state === "strong";
    });
    var partial = results.filter(function (r) {
      return r.state === "partial";
    });
    var absent = results.filter(function (r) {
      return r.state === "absent";
    });

    return {
      total: total,
      words: totalWords,
      components: results,
      good: good,
      partial: partial,
      absent: absent,
      band:
        total >= 85
          ? "Fully structured Gaiish"
          : total >= 65
          ? "Mostly structured — some components thin"
          : total >= 40
          ? "Partially structured — several components missing"
          : "Unstructured prompt"
    };
  }

  /** Rewrites a prompt into labelled Gaiish sections, preserving the author's own words. */
  function toGaiish(text) {
    var input = String(text || "").trim();
    var sections = labelledSections(input);
    var hasLabels = Object.keys(sections).length > 0;
    var lines = [
      "INTENT:",
      "[what you are trying to accomplish, and who the result is for]",
      "",
      "CONTEXT:",
      hasLabels ? "[the material and situation the model cannot infer]" : input || "[the material and situation the model cannot infer]",
      "",
      "INSTRUCTION:",
      "[the single action you want performed]",
      "",
      "CONSTRAINTS:",
      "[length, scope, tone, and what to leave out]",
      "",
      "OUTPUT:",
      "[the sections, columns or schema the finished result should contain]",
      "",
      "VALIDATION:",
      "[check the result against the constraints above and list any assumption you had to make]"
    ];
    return lines.join("\n");
  }

  root.GaiishScore = {
    COMPONENTS: COMPONENTS,
    analyze: analyze,
    toGaiish: toGaiish
  };
})(typeof window !== "undefined" ? window : globalThis);
