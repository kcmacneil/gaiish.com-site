"""Authority and site-background pages, written without invented provenance."""

from .. import config


ABOUT = {
    "route": "/about",
    "title": "About Gaiish",
    "description": (
        "About Gaiish: the purpose of the site, who maintains it, and the limits of what the "
        "current documentation claims."
    ),
    "eyebrow": "Background",
    "h1": "About Gaiish",
    "lede": config.DEFINITION_SHORT,
    "breadcrumbs": [("Use", "/gaiish-for-business")],
    "nav_key": "/gaiish-for-business",
    "updated": config.LAST_UPDATED,
    "blocks": [
        ("h2", "What this site is", "site"),
        ("p",
         "This is the working home of Gaiish: its definitions, method, frameworks, written "
         "syntax, examples and developing language specification. The site is intended to make "
         "human–AI communication easier to discuss as a practice, not to present a collection of "
         "unverifiable claims."),
        ("h2", "Who maintains it", "maintainer"),
        ("p",
         "Site owner: [Site owner name]. Maintainer contact: [Maintainer contact]. The owner and "
         "maintainer details will be replaced with factual information supplied by the site "
         "owner. No authors, credentials, partnerships, endorsements or audience numbers are "
         "being inferred here."),
        ("h2", "What we claim", "claims"),
        ("p",
         "Gaiish is documented here as a developing language and methodology. The site may say "
         "that explicit structure can improve instruction adherence and reduce ambiguity. It "
         "does not claim a fixed improvement percentage, industry-standard status, external "
         "adoption, endorsement or published research result."),
        ("h2", "How to read the material", "read"),
        ("p",
         "The cornerstone pages explain the idea; the frameworks show how much structure to use; "
         "the specification records the current language design; and the older principles, "
         "outcomes, topics and generative-AI pages remain supporting reference material. Model "
         "behaviour varies, so examples should be tested with the model and data used for the "
         "real task."),
        ("links", [
            ("Origin of Gaiish", "/origin-of-gaiish"),
            ("Research plans", "/research"),
            ("Changelog", "/changelog"),
            ("Source repository", "https://github.com/kcmacneil/gaiish.com-site"),
        ]),
    ],
}


ORIGIN = {
    "route": "/origin-of-gaiish",
    "title": "The Origin of Gaiish",
    "description": (
        "The developing origin story of Gaiish, a language and methodology for structured "
        "human–AI communication, without invented history or unsupported claims."
    ),
    "eyebrow": "Background",
    "h1": "The Origin of Gaiish",
    "lede": "Gaiish is a developing methodology, documented as it takes shape.",
    "breadcrumbs": [("Use", "/gaiish-for-business")],
    "nav_key": "/gaiish-for-business",
    "updated": config.LAST_UPDATED,
    "blocks": [
        ("h2", "A problem of communication", "problem"),
        ("p",
         "Generative AI makes it easy to produce a request and difficult to see everything that "
         "request leaves unstated. A short sentence can conceal the intended audience, source "
         "boundary, acceptable format, exclusions and test for success. When the answer misses "
         "one of those assumptions, the failure can look like a model failure even though the "
         "model was never given the information needed to choose well."),
        ("h2", "From idea to method", "method"),
        ("p",
         "Gaiish names the pieces of that communication and puts them into a reusable structure. "
         "The current method is Intent → Context → Instruction → Constraints → Result → "
         "Validation. BASIC and PRO offer practical shapes for different levels of task "
         "complexity. The language specification records the vocabulary and syntax so the "
         "method can be taught, reviewed and revised."),
        ("p",
         "This page intentionally does not assign a founder, date, discovery story or chain of "
         "influence that has not been supplied by the site owner. The factual maintainer details "
         "belong on the <a href=\"/about\">About</a> page when they are available."),
        ("h2", "Still developing", "developing"),
        ("p",
         "The architecture allows additional frameworks, dictionary entries, examples and "
         "research to be added later. Development is not evidence of adoption or effectiveness. "
         "It is an honest description of the work: define the structure, use it, test it in "
         "representative settings and publish what the evidence can support."),
        ("callout", "The current position",
         "Gaiish is a model-independent way to make human intent, context, instructions, "
         "constraints, results and validation explicit. It is not an industry standard and does "
         "not claim published performance results."),
        ("links", [
            ("Read the specification", "/gaiish-language/specification"),
            ("See the research plan", "/research"),
            ("View the changelog", "/changelog"),
        ]),
    ],
}


RESEARCH = {
    "route": "/research",
    "title": "Gaiish Research",
    "description": (
        "The Gaiish research plan: future comparisons of traditional and structured prompts "
        "across models, with defined measures and no results published yet."
    ),
    "eyebrow": "Evidence",
    "h1": "Gaiish Research",
    "lede": "Infrastructure for future evaluation, not a report of results.",
    "breadcrumbs": [("Use", "/gaiish-for-business")],
    "nav_key": "/gaiish-for-business",
    "updated": config.LAST_UPDATED,
    "blocks": [
        ("callout", "Current status",
         "No results have been published yet. This page describes what future studies could "
         "compare; it is not evidence that Gaiish improves any measure."),
        ("h2", "A future comparison", "comparison"),
        ("p",
         "A useful study could compare traditional prompts with prompts that use a documented "
         "Gaiish structure across representative tasks and models. The comparison would need "
         "the same task brief, source material, model conditions and evaluation process, with "
         "enough varied examples to avoid treating one prompt or one model as representative of "
         "all use. The design, sampling, exclusions and analysis would need to be documented "
         "before results were interpreted."),
        ("h2", "Measures to define", "measures"),
        ("table", ["Measure", "What a study could examine"], [
            ["Accuracy", "Whether factual or calculated claims match the supplied evidence or reference answer."],
            ["Completeness", "Whether the response covers the required information without material omissions."],
            ["Instruction adherence", "Whether the response follows the task and stated requirements."],
            ["Formatting compliance", "Whether the response matches the requested structure, schema or limits."],
            ["Hallucination frequency", "How often the response introduces unsupported facts, sources or details."],
            ["Human preference", "Which response reviewers prefer under a defined rubric and task context."],
            ["Iterations required", "How many prompt–response revisions are needed to reach a predeclared criterion."],
        ]),
        ("h2", "What would need controlling", "controls"),
        ("p",
         "Models differ in training, context limits, system instructions, tools and response "
         "style. A study would need to record the model and version, prompt text, supplied "
         "material, temperature or equivalent settings where available, evaluator rubric and "
         "human-review procedure. It would also need to separate the effect of explicit "
         "structure from extra words or extra context."),
        ("h2", "What this page does not say", "limits"),
        ("p",
         "There is no published result here, no claimed percentage improvement and no claim that "
         "one framework is best for every task. Structure can improve instruction adherence and "
         "reduce ambiguity as a practical hypothesis; whether it does so under a particular "
         "condition is an empirical question."),
        ("links", [
            ("Read the method", "/gaiish-method"),
            ("See the language specification", "/gaiish-language/specification"),
            ("About the project", "/about"),
        ]),
    ],
}


CHANGELOG = {
    "route": "/changelog",
    "title": "Gaiish Changelog",
    "description": (
        "The Gaiish site and language changelog, including the initial Version "
        + config.SPEC_VERSION + " documentation build."
    ),
    "eyebrow": "Reference",
    "h1": "Changelog",
    "lede": "A compact record of changes to the site and the versioned Gaiish language.",
    "breadcrumbs": [("Language", "/gaiish-language")],
    "nav_key": "/gaiish-language",
    "updated": config.LAST_UPDATED,
    "blocks": [
        ("h2", "Version " + config.SPEC_VERSION, "v1"),
        ("p",
         "Initial site and specification build. Added the Gaiish language hub, specification, "
         "BASIC and PRO frameworks, syntax guide, applied pages, authority pages, generated "
         "navigation and accessible documentation chrome. Preserved the existing principles, "
         "outcomes, topics and generative-AI reference pages."),
        ("ul", [
            "Published the canonical definition and six-component Gaiish method across the new IA.",
            "Added a model-independent explanation covering ChatGPT, Claude, Gemini, Copilot, "
            "Grok, Llama, Mistral, DeepSeek and Qwen.",
            "Added a research page that records planned measures and explicitly reports no results "
            "published yet.",
            "Moved the interactive brand map to /gaiish-map while the generated home page becomes "
            "the site's editorial entry point.",
        ]),
        ("h2", "How versions work", "versions"),
        ("p",
         "The language specification is versioned independently from individual site pages. "
         "config.SPEC_VERSION supplies the current version string. Future specifications such "
         "as 1.1 or 2.0 can be added as sibling routes so earlier documents remain readable and "
         "linkable."),
        ("links", [
            ("Current specification", "/gaiish-language/specification"),
            ("About Gaiish", "/about"),
            ("Interactive Gaiish map", "/gaiish-map"),
        ]),
    ],
}


NOT_FOUND = {
    "route": "/404",
    "title": "Page not found",
    "title_full": "Page not found — Gaiish",
    "description": "The Gaiish page you requested was not found. Return to the home page or explore the main sections.",
    "eyebrow": "404",
    "h1": "Page not found",
    "lede": "That route does not point to a page in the current Gaiish site.",
    "nav_key": None,
    "blocks": [
        ("p",
         "Try one of the main sections below, or return to the home page and start again."),
        ("cards", [
            ("Learn Gaiish", "The method, frameworks and written syntax.", "/learn-gaiish"),
            ("The Gaiish Language", "Vocabulary, grammar and the current specification.", "/gaiish-language"),
            ("Examples", "Examples and prompt resources.", "/examples"),
            ("Generative AI", "The technology and reference articles.", "/generative-ai"),
            ("About", "Project background and scope.", "/about"),
        ]),
        ("links", [("Return home", "/"), ("Open the Gaiish map", "/gaiish-map")]),
    ],
}


PAGES = [ABOUT, ORIGIN, RESEARCH, CHANGELOG, NOT_FOUND]
