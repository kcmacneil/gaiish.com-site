"""Framework guides: Gaiish BASIC, PRO, and the written syntax."""

from .. import config


BASIC = {
    "route": "/gaiish-basic",
    "title": "Gaiish BASIC",
    "description": (
        "Learn Gaiish BASIC: Goal, Context, Action and Output, a four-part structure for "
        "clearer everyday requests to generative AI."
    ),
    "eyebrow": "Beginner framework",
    "h1": "Gaiish BASIC",
    "lede": (
        "Goal + Context + Action + Output. Four parts are enough to turn an everyday request "
        "into a prompt another person could understand."
    ),
    "breadcrumbs": [("Learn", "/learn-gaiish")],
    "nav_key": "/learn-gaiish",
    "updated": config.LAST_UPDATED,
    "blocks": [
        ("p",
         "BASIC is the shortest practical shape of the Gaiish method. It asks four questions: "
         "what are you trying to achieve, what does the model need to know, what should it do, "
         "and what should come back? You can write the answers in four labelled blocks or use "
         "the questions as a quick check before you press send."),
        ("h2", "The four parts", "parts"),
        ("dl", [
            ("Goal",
             "The outcome behind the request. Name the decision, change or deliverable, and "
             "say who will use it when that changes the answer."),
            ("Context",
             "The situation and source material the model cannot infer. Paste the document, "
             "describe the audience, and include the relevant facts already known."),
            ("Action",
             "The primary verb: draft, compare, extract, explain, plan or rewrite. If the "
             "work has an order, number the actions."),
            ("Output",
             "The artefact you expect back. Name its format, sections, length or fields so "
             "the result can be used without another round of guessing."),
        ]),
        ("h2", "When BASIC is enough", "when"),
        ("p",
         "Use BASIC for a self-contained task with a clear audience and a result you can inspect "
         "yourself: turning notes into an email, summarising a meeting, planning a weekend, or "
         "asking for first-pass ideas. It is deliberately light. It gives the model the purpose, "
         "the missing background, the verb and the shape of the answer without making a small "
         "request feel like a specification."),
        ("p",
         "BASIC is not a lower standard of thinking. It is a decision about how much structure "
         "the task needs. Move to the full method when you need explicit constraints and "
         "validation; move to PRO when role, knowledge boundaries, process or handoff matter."),
        ("h2", "Example 1 — a meeting summary", "example-1"),
        ("compare",
         "Summarise these meeting notes.",
         "GOAL:\n"
         "Give the project sponsor a concise record of decisions and next actions.\n\n"
         "CONTEXT:\n"
         "[paste the meeting notes]\n"
         "The sponsor did not attend. The team has a launch review on Friday.\n\n"
         "ACTION:\n"
         "Extract decisions, open questions and actions from the notes.\n\n"
         "OUTPUT:\n"
         "Use three headings: Decisions, Open questions, Actions. For each action include an "
         "owner and due date only when the notes name one.",
         "The conversational version names a topic but not a use. BASIC supplies the absent "
         "audience, the reason the summary matters, the categories to extract and a rule for "
         "missing ownership. That gives the model a useful stopping point and makes omissions "
         "visible to the reader. It can improve instruction adherence and reduce ambiguity; it "
         "does not guarantee a correct summary."),
        ("h2", "Example 2 — a customer email", "example-2"),
        ("compare",
         "Write a nice email telling customers about the delay.",
         "GOAL:\n"
         "Help customers understand the delayed shipment and choose whether to wait or cancel.\n\n"
         "CONTEXT:\n"
         "Orders placed 3–10 June are delayed by a warehouse issue. The new estimate is 18 "
         "June. Customers can cancel for a full refund. Audience: people who have already "
         "received an order confirmation.\n\n"
         "ACTION:\n"
         "Draft a customer email that explains the delay and presents both options plainly.\n\n"
         "OUTPUT:\n"
         "Subject line plus a 120-word email. Put the new date and cancellation option in the "
         "first two paragraphs. Use a calm, accountable tone.",
         "“Nice” leaves the model to invent the situation, remedy, tone and length. The BASIC "
         "version supplies the facts a customer needs, tells the model what decision the email "
         "must support and puts the important information where it belongs. The instruction is "
         "still small enough to write in a minute, but the result is reviewable against the "
         "brief."),
        ("h2", "A BASIC prompt in four lines", "skeleton"),
        ("code",
         "GOAL:\n"
         "State the outcome and who will use it.\n\n"
         "CONTEXT:\n"
         "Paste the material and name the situation.\n\n"
         "ACTION:\n"
         "Use one clear primary verb.\n\n"
         "OUTPUT:\n"
         "Name the artefact, format and useful limits."),
        ("callout", "Know when to upgrade",
         "Add explicit constraints and validation when the cost of a wrong or unusable answer "
         "is high. The <a href=\"/gaiish-method\">Gaiish Method</a> shows the six-component "
         "structure; <a href=\"/gaiish-pro\">Gaiish PRO</a> separates the additional decisions "
         "that complex work requires."),
        ("links", [
            ("Write it down with Gaiish Syntax", "/gaiish-syntax"),
            ("Try the Prompt Builder", "/tools/prompt-builder"),
            ("Browse more examples", "/examples"),
            ("Use the Prompt Library", "/prompt-library"),
        ]),
    ],
}


PRO = {
    "route": "/gaiish-pro",
    "title": "Gaiish PRO",
    "description": (
        "Learn Gaiish PRO: Role, Intent, Context, Knowledge, Constraints, Process, Output and "
        "Validation for complex, consequential or repeatable AI work."
    ),
    "eyebrow": "Advanced framework",
    "h1": "Gaiish PRO",
    "lede": (
        "Role, Intent, Context, Knowledge, Constraints, Process, Output, Validation. PRO makes "
        "the decisions behind a complex prompt explicit."
    ),
    "breadcrumbs": [("Learn", "/learn-gaiish")],
    "nav_key": "/learn-gaiish",
    "updated": config.LAST_UPDATED,
    "blocks": [
        ("p",
         "PRO is for work that has a reviewer, a downstream system, a meaningful consequence or "
         "a need to be repeated by someone else. It expands the compact BASIC shape into eight "
         "components. Role establishes the stance and expertise to adopt; Knowledge separates "
         "provided facts from general background; Process makes reasoning steps inspectable; "
         "Constraints and Validation bound and check the result."),
        ("h2", "The eight components", "components"),
        ("dl", [
            ("Role",
             "The perspective, responsibility or expertise the model should use. A role sets "
             "the lens; it does not grant real-world credentials or access."),
            ("Intent",
             "The outcome the work serves and the decision or deliverable behind the request."),
            ("Context",
             "The situation, audience, source material and prior decisions that shape the task."),
            ("Knowledge",
             "Facts, definitions, policies or domain rules the model must treat as the working "
             "knowledge for this task. Mark assumptions and unknowns."),
            ("Constraints",
             "Hard boundaries: scope, exclusions, tone, safety, budget, time, length and "
             "requirements that make an answer acceptable."),
            ("Process",
             "The sequence or method to follow. Ask for intermediate checks or a decision "
             "procedure when the order affects the outcome."),
            ("Output",
             "The finished artefact and its exact structure: sections, fields, schema, format "
             "and audience."),
            ("Validation",
             "The checks the model should perform before returning the result, including "
             "source support, constraints, gaps and assumptions."),
        ]),
        ("h2", "When to choose PRO over BASIC", "choose"),
        ("p",
         "Choose PRO when the prompt will be handed to a colleague, used repeatedly, evaluated "
         "against a rubric or fed into a workflow. PRO is also useful when the model must keep "
         "provided policy separate from its general knowledge, follow a multi-stage process or "
         "show where the source material does not answer a question. BASIC remains the better "
         "choice for a quick, low-risk request where those distinctions would add more writing "
         "than value."),
        ("flow", ["Role", "Intent", "Context + Knowledge", "Constraints", "Process", "Output", "Validation"]),
        ("h2", "A full PRO prompt", "worked-example"),
        ("code",
         "ROLE:\n"
         "You are an internal operations analyst preparing a decision brief for a COO. Be "
         "precise about evidence and do not present assumptions as facts.\n\n"
         "INTENT:\n"
         "Decide whether our support team should move from four shifts to three without reducing "
         "coverage for urgent tickets.\n\n"
         "CONTEXT:\n"
         "[paste the last 12 weeks of ticket volumes by hour and priority]\n"
         "The team has 8 people. Current coverage is 08:00–20:00 Monday–Friday. The COO will "
         "review the brief on Monday.\n\n"
         "KNOWLEDGE:\n"
         "Urgent means priority P1 or P2. A shift is 8 paid hours. The source table is the "
         "authority for volumes; do not fill missing hours with estimates.\n\n"
         "CONSTRAINTS:\n"
         "Do not recommend overtime or hiring. Preserve current weekday coverage. Show all "
         "calculations, use plain language, and distinguish observed values from assumptions.\n\n"
         "PROCESS:\n"
         "1. Check the source for missing or inconsistent rows.\n"
         "2. Calculate urgent-ticket volume by hour and compare it with each shift pattern.\n"
         "3. Identify the coverage gap, if any, under three shifts.\n"
         "4. State the decision the evidence supports and the evidence it cannot support.\n\n"
         "OUTPUT:\n"
         "A decision brief with Recommendation, Evidence table, Calculation notes, Risks, and "
         "Questions for the COO. Include a one-sentence executive summary.\n\n"
         "VALIDATION:\n"
         "Recheck every calculation against the pasted rows, flag missing hours, and list each "
         "assumption. If the data cannot support a decision, say so instead of inventing a "
         "coverage estimate."),
        ("h2", "A shorter request, made PRO", "compare"),
        ("compare",
         "Look at our support data and tell me if we can reduce shifts.",
         "ROLE: Internal operations analyst writing for the COO.\n\n"
         "INTENT: Decide whether three shifts preserve urgent-ticket coverage.\n\n"
         "CONTEXT: 8-person team; current weekday coverage 08:00–20:00; [paste 12 weeks of "
         "ticket volumes by hour and priority].\n\n"
         "KNOWLEDGE: P1/P2 are urgent; pasted rows are authoritative; missing hours are unknown.\n\n"
         "CONSTRAINTS: No overtime or hiring; show calculations; separate facts from assumptions.\n\n"
         "PROCESS: Check data, calculate hourly urgent volume, compare shift patterns, identify "
         "gaps, then state the limit of the evidence.\n\n"
         "OUTPUT: Decision brief with recommendation, evidence table, calculations, risks and "
         "questions.\n\n"
         "VALIDATION: Recheck calculations and flag every missing value or assumption.",
         "The PRO version does not ask the model to be more confident. It gives the model and "
         "the reviewer a shared record of the role, decision, evidence boundary, rules, process, "
         "deliverable and checks. That makes the prompt easier to hand off and the answer easier "
         "to challenge. Models still interpret prompts probabilistically and should not replace "
         "human review."),
        ("h2", "A framework, not a ceiling", "extensible"),
        ("p",
         "PRO is the current eight-component framework, not a claim that every future task must "
         "look exactly like this. The architecture allows further frameworks to be added later "
         "as the vocabulary develops. New shapes can be documented alongside BASIC and PRO "
         "without changing the six canonical components of the Gaiish method."),
        ("links", [
            ("How to write the labels", "/gaiish-syntax"),
            ("Read the language specification", "/gaiish-language/specification"),
            ("Compare with BASIC", "/gaiish-basic"),
            ("Check component definitions", "/dictionary"),
        ]),
    ],
}


SYNTAX = {
    "route": "/gaiish-syntax",
    "title": "Gaiish Syntax",
    "description": (
        "Gaiish syntax: write uppercase component labels followed by a colon, keep one "
        "component per block, paste material under CONTEXT, and use modifiers deliberately."
    ),
    "eyebrow": "Written form",
    "h1": "Gaiish Syntax",
    "lede": (
        "A small written convention makes a prompt legible to humans and models: uppercase "
        "labels, one component per block, and a blank line between blocks."
    ),
    "breadcrumbs": [("Learn", "/learn-gaiish")],
    "nav_key": "/learn-gaiish",
    "updated": config.LAST_UPDATED,
    "blocks": [
        ("h2", "The basic convention", "convention"),
        ("p",
         "Write a component name in uppercase, followed by a colon. Put the component's "
         "contents below it. Separate blocks with a blank line. Labels are signposts, not "
         "commands: the material below CONTEXT remains context even when it contains sentences "
         "that look like instructions."),
        ("ul", [
            "<strong>Labels:</strong> use uppercase names such as INTENT:, CONTEXT:, "
            "INSTRUCTION:, CONSTRAINTS:, RESULT: and VALIDATION:.",
            "<strong>One block:</strong> keep one component's material together so a reader can "
            "see its scope.",
            "<strong>Blank lines:</strong> leave a blank line between blocks for scanning and "
            "for reliable section boundaries.",
            "<strong>Material:</strong> paste documents, data and examples under CONTEXT or "
            "KNOWLEDGE rather than hiding them in a vague instruction.",
        ]),
        ("h2", "Canonical skeleton", "skeleton"),
        ("code",
         "INTENT:\n"
         "[what you are trying to accomplish and who will use the result]\n\n"
         "CONTEXT:\n"
         "[paste source material and describe the situation]\n\n"
         "INSTRUCTION:\n"
         "[the primary action the model should take]\n\n"
         "CONSTRAINTS:\n"
         "[limits, requirements, tone, exclusions and treatment of uncertainty]\n\n"
         "RESULT:\n"
         "[the artefact, sections, fields or format you expect]\n\n"
         "VALIDATION:\n"
         "[checks, citations, assumptions and missing information to report]"),
        ("h2", "Framework labels", "frameworks"),
        ("p",
         "The six canonical labels above map directly to the Gaiish method. BASIC uses GOAL:, "
         "CONTEXT:, ACTION: and OUTPUT:. PRO uses ROLE:, INTENT:, CONTEXT:, KNOWLEDGE:, "
         "CONSTRAINTS:, PROCESS:, OUTPUT: and VALIDATION:. Use the labels belonging to the "
         "framework you chose; do not add empty ceremony to a small request."),
        ("p",
         "Labels are case-insensitive in meaning, but uppercase is the written convention because "
         "it makes the structure immediately visible. A model may interpret equivalent wording "
         "differently, so keep names consistent within a team or document."),
        ("h2", "Optional modifiers", "modifiers"),
        ("p",
         "Modifiers add a useful instruction without pretending to be new components. Put them "
         "inside the block they qualify, and explain an unfamiliar modifier the first time it "
         "appears. Examples include a tone or audience modifier under CONSTRAINTS, a source "
         "priority under KNOWLEDGE, or a numbered process under PROCESS."),
        ("code",
         "CONSTRAINTS:\n"
         "TONE: direct and calm.\n"
         "AUDIENCE: a non-specialist manager.\n"
         "LENGTH: no more than 500 words.\n"
         "EXCLUDE: unsupported claims and unexplained jargon."),
        ("h2", "What not to do", "anti-patterns"),
        ("ul", [
            "<strong>Do not hide the goal in a vague verb.</strong> “Do something with this” "
            "does not tell the model what success means.",
            "<strong>Do not paste instructions into CONTEXT without marking them.</strong> "
            "Separate source material from what you want the model to do.",
            "<strong>Do not make every sentence a new label.</strong> Components are blocks, "
            "not a decorative line-by-line format.",
            "<strong>Do not use contradictory constraints.</strong> Resolve “be exhaustive” "
            "and “use 50 words” before sending the prompt.",
            "<strong>Do not treat validation as a guarantee.</strong> A model's self-check is "
            "a useful pass, not independent proof.",
            "<strong>Do not assume labels erase ambiguity.</strong> Supply the facts, audience "
            "and boundaries the answer depends on.",
        ]),
        ("h2", "Syntax in practice", "practice"),
        ("p",
         "Start with the smallest framework that fits. Write the blocks in a stable order, then "
         "read only the labels: can another person reconstruct the task from them? Read the "
         "contents next: is each claim in the right block, and does validation check the actual "
         "constraints? This two-pass habit catches missing structure before a model does."),
        ("links", [
            ("Read Gaiish BASIC", "/gaiish-basic"),
            ("Read Gaiish PRO", "/gaiish-pro"),
            ("Specification", "/gaiish-language/specification"),
        ]),
    ],
}


PAGES = [BASIC, PRO, SYNTAX]
