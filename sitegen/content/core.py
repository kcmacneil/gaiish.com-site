"""Cornerstone pages: home, what-is-gaiish, learn-gaiish, gaiish-method."""

from .. import config

DEF_SHORT = config.DEFINITION_SHORT
DEF_LONG = config.DEFINITION_LONG

WEBSITE_SCHEMA = {
    "@context": "https://schema.org",
    "@type": "WebSite",
    "name": "Gaiish",
    "url": config.SITE_URL,
    "description": config.SITE_DESCRIPTION,
    "publisher": {"@type": "Organization", "name": "Gaiish", "url": config.SITE_URL},
}

DEFINED_TERM_SET = {
    "@context": "https://schema.org",
    "@type": "DefinedTermSet",
    "name": "Gaiish",
    "url": config.SITE_URL + "/dictionary",
    "description": DEF_LONG,
}


HOME = {
    "route": "/",
    "title": "Gaiish",
    "title_full": "Gaiish — The Language of Human–AI Communication",
    "description": config.SITE_DESCRIPTION,
    "eyebrow": config.SITE_TAGLINE,
    "h1": "Learn to Speak Gaiish",
    "lede": DEF_SHORT,
    "cta": [
        ("Learn Gaiish", "/learn-gaiish", True),
        ("Build a Gaiish Prompt", "/tools/prompt-builder", True),
        ("What is Gaiish?", "/what-is-gaiish", False),
    ],
    "body_class": "home",
    "nav_key": "/learn-gaiish",
    "schema": [WEBSITE_SCHEMA, DEFINED_TERM_SET],
    "blocks": [
        ("lede",
         "Humans developed natural languages to communicate with each other. Humans developed "
         "programming languages to tell computers what to execute. <strong>Gaiish helps humans "
         "communicate intent effectively to generative AI.</strong>"),
        ("p",
         "Gaiish gives you a systematic way to express intent, context, instructions, "
         "constraints, desired results and validation — so the answer you get back is more "
         "accurate, more useful and more repeatable than the one a vague request produces."),
        ("h2", "Three Kinds of Language", "languages"),
        ("table",
         ["Language", "Used between", "What it carries"],
         [["Natural language", "Human ↔ human", "Meaning, negotiated as you go — ambiguity is repaired by conversation"],
          ["Programming language", "Human → computer", "Exact instructions a machine executes literally"],
          ["<strong>Gaiish</strong>", "Human ↔ generative AI", "Intent, context and constraints a model interprets probabilistically"]]),
        ("p",
         "Gaiish is not a programming language and it is not a new grammar you have to memorise. "
         "It is a structure for the things a model cannot infer, written in ordinary words."),
        ("h2", "The Gaiish Method", "method"),
        ("p",
         "Six components carry a request from your head to a result you can use. Every Gaiish "
         "framework on this site is a shape of these six."),
        ("framework", None),
        ("links", [("Learn the method", "/gaiish-method"),
                   ("Gaiish BASIC for beginners", "/gaiish-basic"),
                   ("Gaiish PRO for advanced work", "/gaiish-pro")]),
        ("h2", "Traditional Prompt vs Gaiish Prompt", "compare"),
        ("compare",
         "Write a marketing plan for my company.",
         "INTENT:\n"
         "Create a practical 90-day marketing strategy.\n\n"
         "CONTEXT:\n"
         "B2B SaaS, 12 people, $4k MRR, scheduling tool for dental practices.\n"
         "We sell direct; no channel partners today.\n\n"
         "AUDIENCE:\n"
         "Practice owners and office managers at 2–6 chair private dental practices.\n\n"
         "CONSTRAINTS:\n"
         "Budget $5,000 total. No paid search. One marketer, half time.\n"
         "Exclude anything that needs new engineering work.\n\n"
         "OUTPUT:\n"
         "Executive Summary\n"
         "90-Day Timeline (by fortnight)\n"
         "Budget table\n"
         "KPIs with target values\n\n"
         "VALIDATION:\n"
         "Check every activity against the budget and the half-time constraint, and list any "
         "assumption you had to make.",
         "The two prompts ask for the same artefact. The second one also communicates the "
         "business, the buyer, the money, the staffing, the exclusions, the document structure "
         "and how the model should check its own work. None of that was inferable from the "
         "first prompt, so the model had to guess it — and a guess you did not see is the most "
         "common reason an answer feels wrong. Providing this structure can improve instruction "
         "adherence and reduce ambiguity; it does not guarantee a better answer."),
        ("links", [("More examples", "/examples"), ("Prompt library by use case", "/prompt-library")]),
        ("h2", "How Gaiish Flows", "flow"),
        ("flow", ["Human", "Gaiish", "Generative AI", "Result"]),
        ("p",
         "Write once, communicate across AI models. Gaiish is model-independent: the same "
         "structure works with ChatGPT, Claude, Gemini, Copilot, Grok, Llama, Mistral, DeepSeek "
         "and Qwen. Models do not interpret prompts identically, so Gaiish makes your intent "
         "explicit rather than assuming any particular model's habits."),
        ("h2", "Start Here", "start"),
        ("cards", [
            ("What Is Gaiish?",
             "The definition, what Gaiish is not, and why a structured language for talking to "
             "generative AI is useful at all.",
             "/what-is-gaiish"),
            ("Learn Gaiish",
             "A short course: the method, the two frameworks, and your first prompt written in "
             "Gaiish.",
             "/learn-gaiish"),
            ("Gaiish BASIC",
             "Goal + Context + Action + Output. Four lines you can use in the next five minutes.",
             "/gaiish-basic"),
            ("Gaiish PRO",
             "Role, Intent, Context, Knowledge, Constraints, Process, Output, Validation — for "
             "work that has to be right.",
             "/gaiish-pro"),
            ("Prompt Builder",
             "Answer the fields, get a formatted Gaiish prompt you can copy. Runs entirely in "
             "your browser.",
             "/tools/prompt-builder"),
            ("Prompt Analyzer",
             "Paste a prompt and see which Gaiish components it is missing, with a heuristic "
             "Gaiish Score.",
             "/tools/prompt-analyzer"),
            ("Interactive Gaiish Map",
             "Explore the original visual map of Gaiish principles, outcomes and generative AI "
             "topics.",
             "/gaiish-map"),
        ]),
        ("h2", "Communicate. Collaborate. Optimize. Empower.", "outcomes"),
        ("p",
         "Clear communication with a model is not a party trick — it is what makes generative AI "
         "usable for work that matters. "
         '<a href="/outcomes/communicate">Communicate</a>, '
         '<a href="/outcomes/collaborate">collaborate</a>, '
         '<a href="/outcomes/optimize">optimize</a> and '
         '<a href="/outcomes/empower">empower</a> describe what changes when you do.'),
        ("callout", "A developing language",
         "Gaiish is a developing methodology and vocabulary for human–AI communication, "
         "documented here as it evolves. It is not an industry standard, and this site makes no "
         "claims about adoption or measured performance that have not been tested and published "
         'on the <a href="/research">research</a> page.'),
    ],
}


WHAT_IS = {
    "route": "/what-is-gaiish",
    "title": "What Is Gaiish?",
    "description": (
        "Gaiish is a language humans use to optimize communication with Generative AI models. "
        "What it is, what it is not, and why structured human–AI communication produces more "
        "predictable results."
    ),
    "eyebrow": "Definition",
    "h1": "What Is Gaiish?",
    "lede": DEF_SHORT,
    "breadcrumbs": [("Learn", "/learn-gaiish")],
    "nav_key": "/learn-gaiish",
    "updated": config.LAST_UPDATED,
    "schema": [
        {
            "@context": "https://schema.org",
            "@type": "DefinedTerm",
            "name": "Gaiish",
            "description": DEF_LONG,
            "url": config.SITE_URL + "/what-is-gaiish",
            "inDefinedTermSet": {
                "@type": "DefinedTermSet",
                "name": "Gaiish",
                "url": config.SITE_URL + "/dictionary",
            },
        }
    ],
    "blocks": [
        ("h2", "The definition", "definition"),
        ("callout", "Gaiish", DEF_LONG),
        ("p",
         "A generative model does not answer what you meant. It answers the text you actually "
         "sent. Everything the answer depends on — the situation, the audience, the limits, the "
         "shape of the output — is either in that text or is invented by the model. Gaiish is "
         "the discipline of putting it in the text, in a consistent order, so you and anyone "
         "reading your prompt can see what was communicated and what was left out."),
        ("h2", "Why a language rather than a set of tips", "why"),
        ("ul", [
            "<strong>It is repeatable.</strong> A named structure can be reused, reviewed and "
            "handed to a colleague. A clever one-off prompt cannot.",
            "<strong>It makes omissions visible.</strong> When the components are named, an "
            "empty one is obvious — you can see that you never said who the output is for.",
            "<strong>It is model-independent.</strong> Structure survives model upgrades and "
            "provider changes in a way that provider-specific tricks do not.",
            "<strong>It is teachable.</strong> Six components and two frameworks can be taught "
            "in an afternoon and used by a whole team.",
        ]),
        ("h2", "What Gaiish is not", "not"),
        ("ul", [
            "<strong>Not a programming language.</strong> There is no compiler and no execution "
            "guarantee. A model interprets Gaiish probabilistically, like any other text.",
            "<strong>Not a magic phrase.</strong> No wording forces a correct answer. Gaiish "
            "reduces ambiguity; it does not remove the need to check the result.",
            "<strong>Not tied to one AI provider.</strong> Examples use several models, and the "
            "methodology assumes none of them.",
            "<strong>Not a claim about accuracy.</strong> Where this site says structure helps, "
            "it means it can improve instruction adherence and reduce ambiguity — not a measured "
            'percentage. Any measurements will be published under <a href="/research">research'
            "</a>.",
        ]),
        ("h2", "The six components", "components"),
        ("p",
         "Every Gaiish framework is a shape of the same six components. This is the vocabulary "
         "the rest of the site uses."),
        ("framework", None),
        ("links", [("The Gaiish Method in full", "/gaiish-method"),
                   ("Gaiish Syntax", "/gaiish-syntax"),
                   ("Dictionary", "/dictionary")]),
        ("h2", "A first example", "example"),
        ("compare",
         "Summarise this contract.",
         "INTENT:\n"
         "Decide whether we can terminate this vendor contract before renewal.\n\n"
         "CONTEXT:\n"
         "[paste the contract]\n"
         "We are the customer. Renewal date is 1 May. Legal will review your answer.\n\n"
         "INSTRUCTION:\n"
         "Identify the termination, notice and auto-renewal clauses and explain what they "
         "require of us.\n\n"
         "CONSTRAINTS:\n"
         "Quote the clause number and text for every claim. Do not give legal advice or "
         "opinions on enforceability. Ignore pricing terms.\n\n"
         "OUTPUT:\n"
         "A table of clause / requirement / deadline, then a short plain-English summary.\n\n"
         "VALIDATION:\n"
         "If a required clause is absent from the document, say so explicitly rather than "
         "inferring standard terms.",
         "The first prompt leaves the model to decide what matters in a contract. The second "
         "names the decision being made, who will read it, which clauses matter, what to quote, "
         "what to ignore and what to do when the document is silent — the exact points where a "
         "summary would otherwise go quietly wrong."),
        ("h2", "Where to go next", "next"),
        ("cards", [
            ("Learn Gaiish", "The short course, in order.", "/learn-gaiish"),
            ("Gaiish BASIC", "Four lines for everyday requests.", "/gaiish-basic"),
            ("Gaiish vs prompt engineering",
             "How Gaiish relates to the wider practice of prompt engineering.",
             "/gaiish-vs-prompt-engineering"),
        ]),
    ],
}


LEARN = {
    "route": "/learn-gaiish",
    "title": "Learn Gaiish",
    "description": (
        "A short course in Gaiish: the six components of the method, Gaiish BASIC for everyday "
        "requests, Gaiish PRO for work that has to be right, and how to write your first "
        "structured AI prompt."
    ),
    "eyebrow": "Course",
    "h1": "Learn Gaiish",
    "lede": (
        "Four steps, in order. Read the method, write a BASIC prompt, upgrade it to PRO, then "
        "check it with the analyzer."
    ),
    "breadcrumbs": [],
    "nav_key": "/learn-gaiish",
    "updated": config.LAST_UPDATED,
    "blocks": [
        ("h2", "Step 1 — Learn the six components", "step-1"),
        ("p",
         "Intent, context, instruction, constraints, result and validation. Each one answers a "
         "question the model cannot answer for itself."),
        ("framework", None),
        ("links", [("The Gaiish Method", "/gaiish-method")]),
        ("h2", "Step 2 — Write a Gaiish BASIC prompt", "step-2"),
        ("p",
         "Goal + Context + Action + Output. Four lines, no ceremony. Use it for everyday "
         "requests where you would otherwise type a single sentence."),
        ("code",
         "GOAL: what you are trying to accomplish\n"
         "CONTEXT: what the model cannot infer\n"
         "ACTION: what you want it to do\n"
         "OUTPUT: the artefact you expect back"),
        ("links", [("Gaiish BASIC", "/gaiish-basic")]),
        ("h2", "Step 3 — Upgrade to Gaiish PRO when it matters", "step-3"),
        ("p",
         "Role, Intent, Context, Knowledge, Constraints, Process, Output, Validation. Use it "
         "when the work is going to someone else, when the output feeds a system, or when being "
         "wrong is expensive."),
        ("links", [("Gaiish PRO", "/gaiish-pro"), ("Gaiish Syntax", "/gaiish-syntax")]),
        ("h2", "Step 4 — Check and refine", "step-4"),
        ("p",
         "Paste your prompt into the analyzer to see which components are thin, then keep what "
         "worked and correct the specific part that did not. Refine rather than restart."),
        ("links", [("Prompt Analyzer", "/tools/prompt-analyzer"),
                   ("Prompt Builder", "/tools/prompt-builder")]),
        ("h2", "Keep going", "keep-going"),
        ("cards", [
            ("Examples", "Traditional and Gaiish prompts side by side.", "/examples"),
            ("Prompt Library", "Prompts organised by role and use case.", "/prompt-library"),
            ("Dictionary", "The vocabulary, defined.", "/dictionary"),
            ("Specification", "The formal write-up of the language, versioned.",
             "/gaiish-language/specification"),
        ]),
    ],
}


METHOD = {
    "route": "/gaiish-method",
    "title": "The Gaiish Method",
    "description": (
        "The Gaiish method in full: intent, context, instruction, constraints, result and "
        "validation — what each component communicates to a generative AI model, and how to "
        "write it."
    ),
    "eyebrow": "Framework",
    "h1": "The Gaiish Method",
    "lede": (
        "Intent → Context → Instruction → Constraints → Result → Validation. Six components, "
        "each answering a question the model cannot answer for itself."
    ),
    "breadcrumbs": [("Learn", "/learn-gaiish")],
    "nav_key": "/learn-gaiish",
    "updated": config.LAST_UPDATED,
    "blocks": [
        ("framework", None),
        ("h2", "Intent", "intent"),
        ("p", "<strong>What are you trying to accomplish?</strong>"),
        ("p",
         "Intent is the outcome behind the request, not the request itself. \"Summarise this "
         "report\" is an instruction; \"decide whether to renew this contract\" is an intent. "
         "State it and the model can judge which details matter — omit it and every detail "
         "looks equally important."),
        ("ul", [
            "Name the decision, deliverable or change you are working toward.",
            "Say who the output is for and what they will do with it.",
            "One intent per prompt. Two intents produce a shallow attempt at both.",
        ]),
        ("h2", "Context", "context"),
        ("p", "<strong>What does the AI need to know?</strong>"),
        ("p",
         "Context is everything the model cannot infer: the documents, the situation, the "
         "audience, the decisions already made. A model with your context outperforms a larger "
         "model without it."),
        ("ul", [
            "Paste the material rather than describing it.",
            "Include the constraints of the situation, not just the task — team size, deadline, "
            "systems in use.",
            "Say what has already been tried and rejected, so the model does not propose it.",
            "When the corpus is too large to paste, retrieval puts the right passage in the "
            'prompt for you — see <a href="/topics/embeddings-rag">embeddings and RAG</a>.',
        ]),
        ("h2", "Instruction", "instruction"),
        ("p", "<strong>What should the AI do?</strong>"),
        ("p",
         "The instruction is the verb: analyse, draft, rewrite, extract, classify, compare. Keep "
         "it single and explicit, and number the steps when the work has an order."),
        ("ul", [
            "Use one primary verb; if you need several, number them.",
            "Say what to do, not only what to avoid — \"be concise\" is not an instruction, "
            "\"three sentences\" is.",
            "Separate the instruction from the material so the model cannot confuse the two.",
        ]),
        ("h2", "Constraints", "constraints"),
        ("p",
         "<strong>What rules, limits, tone, format, requirements or exclusions apply?</strong>"),
        ("p",
         "Constraints are the boundary of an acceptable answer. They are also where most "
         "disappointment originates, because an unstated constraint is invisible until it is "
         "violated."),
        ("ul", [
            "Quantify: word counts, row counts, time periods, currency, reading level.",
            "State exclusions explicitly — what to leave out is an instruction too.",
            "Name the tone and register rather than adjectives like \"professional\".",
            "Say what to do with uncertainty: report gaps rather than fill them.",
        ]),
        ("h2", "Result", "result"),
        ("p", "<strong>What should the finished output look like?</strong>"),
        ("p",
         "Describe the artefact, not the topic. A named shape — sections, columns, a schema — is "
         "the difference between an essay and something you can use directly."),
        ("ul", [
            "List the sections or columns you expect, in order.",
            "For machine-read output, give the exact schema and forbid commentary.",
            "Paste an exemplar when you have one: one good example beats a paragraph of "
            "description.",
        ]),
        ("h2", "Validation", "validation"),
        ("p", "<strong>How should the AI verify the result satisfies the request?</strong>"),
        ("p",
         "Validation asks the model to check its own output against the request before "
         "presenting it, and to be explicit about what it could not do. It is the component "
         "most often left out entirely."),
        ("ul", [
            "Ask it to check the output against each constraint and report violations.",
            "Ask it to list the assumptions it made and the facts it could not find.",
            "Require citations to the supplied material for factual claims.",
            "Remember that self-checking is not proof — verify anything irreversible yourself.",
        ]),
        ("h2", "The method in one prompt", "example"),
        ("compare",
         "Help me improve our onboarding emails.",
         "INTENT:\n"
         "Reduce first-week churn by improving the onboarding email sequence.\n\n"
         "CONTEXT:\n"
         "[paste the current 3 emails]\n"
         "Product: team scheduling tool. Free trial is 14 days.\n"
         "Activation = inviting one teammate. 38% of trials never activate.\n"
         "Audience: office managers, not technical.\n\n"
         "INSTRUCTION:\n"
         "Rewrite the three emails so each one drives the single next action toward "
         "activation.\n\n"
         "CONSTRAINTS:\n"
         "Max 120 words per email. One call to action each. No feature tours, no discounts. "
         "Plain language, no exclamation marks.\n\n"
         "OUTPUT:\n"
         "For each email: subject line, body, and one sentence on the action it drives.\n\n"
         "VALIDATION:\n"
         "Confirm every email is under 120 words with exactly one call to action, and list any "
         "claim about the product you could not verify from the material above.",
         "Each component is doing distinct work: the intent explains why the emails exist, the "
         "context supplies the activation metric the model could never guess, the constraints "
         "rule out the two things it would otherwise reach for (feature tours and discounts), "
         "and validation catches invented product claims before you read them."),
        ("h2", "Related", "related"),
        ("cards", [
            ("Gaiish BASIC", "The four-line beginner shape of the same six components.",
             "/gaiish-basic"),
            ("Gaiish PRO", "The eight-component shape for advanced work.", "/gaiish-pro"),
            ("Gaiish Syntax", "How to write the components down consistently.", "/gaiish-syntax"),
            ("Specification", "The formal, versioned definition.",
             "/gaiish-language/specification"),
            ("Dictionary", "Definitions for Gaiish components and general AI terms.",
             "/dictionary"),
            ("Examples", "Traditional and structured prompts across real domains.",
             "/examples"),
            ("Prompt Library", "Adaptable prompts organised by use case.",
             "/prompt-library"),
        ]),
    ],
}


PAGES = [HOME, WHAT_IS, LEARN, METHOD]
