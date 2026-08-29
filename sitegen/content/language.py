"""Language pages: the Gaiish language hub and versioned specification."""

from .. import config


LANGUAGE = {
    "route": "/gaiish-language",
    "title": "The Gaiish Language",
    "description": (
        "Explore Gaiish as a language: its vocabulary, grammar, declarations and written "
        "syntax, with links to the specification, dictionary and changelog."
    ),
    "eyebrow": "Language",
    "h1": "The Gaiish Language",
    "lede": (
        "Gaiish is more than a collection of prompt tips. It is a shared vocabulary and grammar "
        "for making human intent legible to generative AI."
    ),
    "breadcrumbs": [],
    "nav_key": "/gaiish-language",
    "updated": config.LAST_UPDATED,
    "blocks": [
        ("p",
         "A tip helps once. A language gives people a way to name what they are doing, recognise "
         "what is missing and read one another's work. Gaiish supplies the names — Intent, "
         "Context, Instruction, Constraints, Result and Validation — and a stable order for "
         "using them. The words remain ordinary language; the structure makes their job in a "
         "prompt visible."),
        ("h2", "Vocabulary, grammar and declarations", "parts"),
        ("dl", [
            ("Vocabulary",
             "The components and their meanings: the words a Gaiish writer can use to describe "
             "purpose, evidence, action, limits, output and checks."),
            ("Grammar",
             "The written convention that puts an uppercase label and colon before each block, "
             "separates blocks with blank lines and keeps source material under the declaration "
             "where it belongs."),
            ("Declarations",
             "A declaration tells the model what a particular component means for this task. "
             "INTENT: declares the outcome; CONTEXT: declares the situation and material; "
             "VALIDATION: declares how the result will be checked."),
        ]),
        ("h2", "A language for model-independent communication", "model-independent"),
        ("p",
         "The same Gaiish structure can be used with ChatGPT, Claude, Gemini, Copilot, Grok, "
         "Llama, Mistral, DeepSeek and Qwen. Models do not interpret prompts identically, and "
         "Gaiish does not pretend otherwise. It keeps the human's intent, evidence and "
         "boundaries explicit so the prompt can travel between systems without depending on a "
         "provider-specific trick."),
        ("h2", "The current shape", "shape"),
        ("framework", None),
        ("p",
         "The six components are the canonical method. Gaiish BASIC and Gaiish PRO are practical "
         "frameworks: BASIC compresses the method into four everyday fields, while PRO expands "
         "it into eight fields for complex work. The architecture allows sibling frameworks to "
         "be added later without changing the core vocabulary."),
        ("h2", "Read the language", "read"),
        ("cards", [
            ("Language Specification",
             "The versioned description of purpose, vocabulary, grammar, declarations, examples "
             "and anti-patterns.",
             "/gaiish-language/specification"),
            ("Dictionary",
             "The terms of Gaiish, defined for reference. The dictionary is part of the next "
             "knowledge-system handoff.",
             "/dictionary"),
            ("Gaiish Syntax",
             "The practical writing rules: labels, blocks, pasted material and modifiers.",
             "/gaiish-syntax"),
            ("Changelog",
             "A record of changes to the site and the versioned language documentation.",
             "/changelog"),
        ]),
        ("callout", "A developing language",
         "This specification documents Gaiish as it exists here. It does not claim external "
         "standards recognition, industry adoption or research validation. Those questions "
         "belong in the <a href=\"/research\">research infrastructure</a>, where no results "
         "have been published yet."),
    ],
}


SPEC = {
    "route": "/gaiish-language/specification",
    "title": "Gaiish Language Specification v" + config.SPEC_VERSION,
    "description": (
        "Gaiish Language Specification — Version " + config.SPEC_VERSION +
        ": purpose, design philosophy, vocabulary, grammar, declarations, modifiers, examples "
        "and anti-patterns."
    ),
    "eyebrow": "Specification v" + config.SPEC_VERSION,
    "h1": "Gaiish Language Specification — Version " + config.SPEC_VERSION,
    "lede": (
        "A working specification for the language humans use to optimize communication with "
        "Generative AI models."
    ),
    "breadcrumbs": [("Language", "/gaiish-language")],
    "nav_key": "/gaiish-language",
    "updated": config.LAST_UPDATED,
    "blocks": [
        ("callout", "Status",
         "Version " + config.SPEC_VERSION + " documents the current language design. It is a "
         "developing methodology, not an externally recognised standard. Future versions such "
         "as 1.1 or 2.0 can be added as sibling routes and linked from this page without "
         "rewriting this version."),
        ("h2", "1. Purpose", "purpose"),
        ("p",
         "Gaiish provides a common way to express a human request to a generative AI model. Its "
         "purpose is to make the parts of a request that affect interpretation — intent, context, "
         "instructions, constraints, result and validation — explicit and reviewable. It does "
         "not define a model API, a programming language or a guarantee about an output."),
        ("h2", "2. Design philosophy", "design-philosophy"),
        ("p",
         "Gaiish favours explicit meaning over clever phrasing, reusable structure over one-off "
         "tricks and human review over declarations of certainty. A writer should be able to "
         "show a colleague what the model was told, what evidence it received and how the answer "
         "will be checked. The method is model-independent, while acknowledging that models "
         "interpret the same text differently."),
        ("p",
         "The language is deliberately additive. A writer can start with a small BASIC prompt "
         "and add PRO fields or the full six-component method as the task demands. Structure can "
         "improve instruction adherence and reduce ambiguity, but it cannot supply facts that "
         "were never provided or make a model's answer independently true."),
        ("h2", "3. Vocabulary", "vocabulary"),
        ("table", ["Term", "Meaning"], [
            ["Gaiish", "A language and methodology for structured human–AI communication."],
            ["Component", "A named kind of information carried by a Gaiish prompt."],
            ["Declaration", "A labelled block that states one component for a task."],
            ["Material", "Source text, data or examples supplied to the model."],
            ["Modifier", "An optional instruction inside a block that narrows how it is used."],
            ["Framework", "A selected shape of the vocabulary, such as BASIC or PRO."],
        ]),
        ("h2", "4. Grammar", "grammar"),
        ("p",
         "A Gaiish document consists of one or more declarations. A declaration begins with an "
         "uppercase label followed by a colon. Its content continues until the next declaration. "
         "A blank line between blocks is recommended for human scanning and clear boundaries. "
         "The canonical six-component order is Intent, Context, Instruction, Constraints, Result "
         "and Validation; BASIC and PRO define their own documented subsets or expansions."),
        ("code",
         "LABEL:\n"
         "The material belonging to LABEL.\n"
         "It may contain multiple sentences or pasted source text.\n\n"
         "NEXT LABEL:\n"
         "The next declaration."),
        ("h2", "5. Intent declarations", "intent"),
        ("p",
         "INTENT: states the outcome behind the request: the decision, change or deliverable "
         "that makes the work useful. It is different from the verb in INSTRUCTION:. Include the "
         "audience or downstream use when those details affect trade-offs. Keep one primary "
         "outcome per prompt; name a second prompt when the work truly has two independent goals."),
        ("code",
         "INTENT:\n"
         "Prepare a decision brief for the finance lead so she can choose whether to renew the "
         "vendor contract."),
        ("h2", "6. Context declarations", "context"),
        ("p",
         "CONTEXT: states the situation and supplies what the model cannot infer. Paste the "
         "source material under this label, then identify the audience, relevant history, "
         "systems, timing and decisions already made. Context is not a place to hide the task; "
         "use INSTRUCTION: for the task."),
        ("code",
         "CONTEXT:\n"
         "The reader is a non-technical customer. The current help article is below.\n"
         "[paste article]"),
        ("h2", "7. Instruction declarations", "instruction"),
        ("p",
         "INSTRUCTION: names the action with a clear primary verb: analyse, draft, extract, "
         "compare, classify, translate or rewrite. Number ordered actions. Say what to do, not "
         "only what to avoid, and keep the action separate from pasted material."),
        ("h2", "8. Constraint declarations", "constraints"),
        ("p",
         "CONSTRAINTS: defines the boundaries of an acceptable answer. It may include scope, "
         "length, count, tone, audience, budget, deadline, exclusions, safety requirements and "
         "what to do with uncertainty. Quantified constraints are easier to inspect than vague "
         "adjectives. Contradictory constraints should be resolved before the prompt is sent."),
        ("h2", "9. Output declarations", "output"),
        ("p",
         "RESULT: or OUTPUT: names the finished artefact and its shape. State headings, columns, "
         "fields, schema, order and format. A result declaration describes something a person "
         "can use, not merely the topic the model should discuss."),
        ("h2", "10. Validation instructions", "validation"),
        ("p",
         "VALIDATION: asks the model to check its response against the declared request. Require "
         "it to recheck constraints, support claims with supplied sources, flag missing material "
         "and list assumptions. This is a self-check, not proof: a human must verify facts and "
         "anything consequential before relying on it."),
        ("h2", "11. Modifiers", "modifiers"),
        ("p",
         "Modifiers are optional, local instructions within a declaration. They are useful when "
         "a task needs a tone, audience, source priority or explicit treatment of uncertainty. "
         "A modifier does not become a new canonical component. Define a team-specific modifier "
         "the first time it is used and do not let a dense collection of modifiers obscure the "
         "main declarations."),
        ("code",
         "CONSTRAINTS:\n"
         "TONE: direct, calm and non-technical.\n"
         "LENGTH: no more than 300 words.\n"
         "EXCLUDE: claims not supported by the supplied source."),
        ("h2", "12. Examples", "examples"),
        ("p",
         "A small request can use BASIC. A request that needs explicit evidence boundaries and "
         "review can use the six-component method or PRO. The framework choice is part of good "
         "communication: use enough structure to expose the decisions that matter, not so much "
         "that labels become ceremony."),
        ("code",
         "GOAL:\n"
         "Help a new manager prepare for her first one-to-one.\n\n"
         "CONTEXT:\n"
         "The meeting is 30 minutes. The manager has the employee's role description below.\n"
         "[paste role description]\n\n"
         "ACTION:\n"
         "Draft five open questions that invite discussion of priorities and support.\n\n"
         "OUTPUT:\n"
         "A numbered list, with one sentence explaining the purpose of each question."),
        ("links", [
            ("See a full PRO example", "/gaiish-pro#worked-example"),
            ("Compare BASIC prompts", "/gaiish-basic#example-1"),
            ("Read practical syntax", "/gaiish-syntax"),
            ("Browse all Gaiish examples", "/examples"),
            ("Adapt a prompt from the library", "/prompt-library"),
        ]),
        ("h2", "13. Anti-patterns", "anti-patterns"),
        ("ul", [
            "A label with no useful content: INTENT: alone does not communicate an outcome.",
            "A single paragraph that mixes source material, instructions and constraints so no "
            "reader can tell which is which.",
            "Conflicting limits, such as exhaustive coverage in ten words, left for the model to "
            "resolve silently.",
            "Provider-specific hidden assumptions presented as if they were part of the language.",
            "A request for confidence or certainty instead of a validation rule and an explicit "
            "way to report gaps.",
        ]),
        ("h2", "14. Model-specific considerations", "models"),
        ("p",
         "Gaiish is designed to be usable across ChatGPT, Claude, Gemini, Copilot, Grok, Llama, "
         "Mistral, DeepSeek and Qwen, but no two models interpret text identically. Context "
         "limits, instruction following, tool access, system messages and output controls vary "
         "by model and product. Keep declarations explicit, test the actual model you will use, "
         "and validate the returned result. Do not describe a provider's private behaviour as a "
         "Gaiish rule."),
        ("h2", "15. Version history", "version-history"),
        ("p",
         "Version " + config.SPEC_VERSION + " is the initial published specification in this "
         "repository. The version is supplied by config.SPEC_VERSION so a future version can be "
         "rendered as a sibling route, for example /gaiish-language/specification/1.1 or "
         "/gaiish-language/specification/2.0, while this document remains addressable."),
        ("h2", "16. Changelog", "changelog"),
        ("table", ["Version", "Change"], [
            [config.SPEC_VERSION, "Initial language specification and site documentation for this build."],
        ]),
        ("callout", "Scope of this document",
         "This specification makes no claim of external standards recognition, adoption, "
         "endorsement or research findings. See the <a href=\"/changelog\">site changelog</a> "
         "for implementation changes and <a href=\"/research\">research</a> for the planned "
         "study infrastructure."),
    ],
}


PAGES = [LANGUAGE, SPEC]
