"""Data-driven knowledge pages: dictionary terms, examples, and prompt library."""

from .. import config


TERMS = [
    {"slug": "ai-model", "term": "AI Model", "kind": "general",
     "short": "A trained computational system that produces predictions or generated outputs from input data.",
     "body": ["An AI model maps an input to an output using patterns learned during training and whatever context the current system provides. A model does not automatically know the facts, audience or purpose behind a request.", "The model matters to prompt engineering because context limits, tool access, instruction-following behaviour and output controls differ. Gaiish remains model-independent: use the structure with the model you actually intend to run, then validate the result."],
     "links": [("Generative AI", "/dictionary/generative-ai"), ("Model considerations", "/gaiish-language/specification#models")]},
    {"slug": "agent", "term": "Agent", "kind": "general",
     "short": "A system that uses a model to choose steps, tools or actions toward a task.",
     "body": ["An agent usually combines a model with instructions, state, tools and a loop that observes results and decides what to do next. The model may draft an answer, call a search or write to another system, depending on the permissions around it.", "A structured prompt is especially useful when an agent has consequential actions. State the intent, available knowledge, constraints, process and validation, and keep human approval where the workflow requires it."],
     "links": [("Agents and tool use", "/topics/agents"), ("Gaiish PRO", "/gaiish-pro")]},
    {"slug": "constraint", "term": "Constraint", "kind": "gaiish",
     "short": "A boundary that makes an answer acceptable: scope, limit, requirement, tone or exclusion.",
     "body": ["In Gaiish, CONSTRAINTS: states the rules the result must satisfy. Useful constraints quantify length or count, name the audience and tone, define scope, exclude unwanted material and say how to handle uncertainty.", "A constraint is not a wish for the model to be generally careful. “No more than 300 words” or “quote the supplied clause for every claim” gives a reviewer something concrete to check."],
     "links": [("The Constraints method section", "/gaiish-method#constraints"), ("Gaiish Syntax", "/gaiish-syntax#constraints")]},
    {"slug": "context", "term": "Context", "kind": "gaiish",
     "short": "The situation, audience and source material a model needs but cannot infer.",
     "body": ["In Gaiish, CONTEXT: supplies the facts that shape the task: documents, data, audience, timing, systems, decisions already made and what has been tried. Paste material rather than asking the model to guess what a document contains.", "Context is different from an instruction. Put the material under CONTEXT:, then say what to do with it under INSTRUCTION:. Large corpora may require retrieval so the relevant passage reaches the model."],
     "links": [("The Context method section", "/gaiish-method#context"), ("Embeddings and RAG", "/topics/embeddings-rag")]},
    {"slug": "context-window", "term": "Context Window", "kind": "general",
     "short": "The amount of input and output text a model can process in one interaction.",
     "body": ["A context window is measured in tokens and includes the instructions, supplied material, conversation history and sometimes the requested output. A larger window does not remove the need to choose relevant material or define its authority.", "When the source corpus is too large, retrieval or summarisation can select what belongs in CONTEXT:. Record what was supplied and what was omitted so the result is reviewable."],
     "links": [("Token", "/dictionary/token"), ("Embeddings and RAG", "/topics/embeddings-rag")]},
    {"slug": "generative-ai", "term": "Generative AI", "kind": "general",
     "short": "AI systems that generate new text, images, audio, video, code or other content.",
     "body": ["Generative AI systems produce an output rather than only assigning a label to existing data. Text models can continue, transform, summarise, classify and draft, but their fluency is not independent evidence that a claim is true.", "A Gaiish prompt makes the human request more explicit for a generative system by naming intent, context, instruction, constraints, result and validation."],
     "links": [("Generative AI overview", "/generative-ai"), ("The Gaiish Method", "/gaiish-method")]},
    {"slug": "grounding", "term": "Grounding", "kind": "general",
     "short": "Connecting a model's response to supplied, retrieved or otherwise identified evidence.",
     "body": ["Grounding narrows the material a response should rely on. A prompt may ground an answer in a pasted policy, a retrieved passage, a database result or a source list, while still requiring a person to check the evidence and the interpretation.", "In Gaiish, grounding belongs mainly in CONTEXT: or KNOWLEDGE:, with VALIDATION: asking the model to cite or flag claims the supplied material does not support."],
     "links": [("Context", "/dictionary/context"), ("Validation", "/dictionary/validation"), ("Embeddings and RAG", "/topics/embeddings-rag")]},
    {"slug": "instruction", "term": "Instruction", "kind": "gaiish",
     "short": "The action a model should take, expressed as a clear primary verb.",
     "body": ["In Gaiish, INSTRUCTION: tells the model what to do: draft, extract, compare, classify, analyse, rewrite or explain. Use one primary action where possible and number ordered actions when sequence matters.", "Instruction is different from intent. “Draft a decision brief” is an instruction; “help the finance lead choose whether to renew” is the intent behind it."],
     "links": [("The Instruction method section", "/gaiish-method#instruction"), ("Gaiish Syntax", "/gaiish-syntax#convention")]},
    {"slug": "intent", "term": "Intent", "kind": "gaiish",
     "short": "The outcome, decision or change that makes a request useful.",
     "body": ["In Gaiish, INTENT: states what the work is for, not merely the operation the model should perform. Include the audience or downstream use when that changes the trade-offs.", "Intent gives the model a reason to select relevant detail. It also gives a human reviewer a way to ask whether the output serves the actual decision rather than only matching the topic."],
     "links": [("The Intent method section", "/gaiish-method#intent"), ("Gaiish BASIC", "/gaiish-basic")]},
    {"slug": "iteration", "term": "Iteration", "kind": "general",
     "short": "A deliberate cycle of running, evaluating and refining a prompt or output.",
     "body": ["Iteration is not repeatedly asking the same vague question. Change a known variable — such as missing context, a constraint or the output shape — and compare the response against a stated criterion.", "Gaiish supports focused iteration because its components make the likely source of a failure visible. Keep what worked and revise the component that did not; validate again after the change."],
     "links": [("Optimize outcome", "/outcomes/optimize"), ("Validation", "/dictionary/validation"), ("Prompt Analyzer", "/tools/prompt-analyzer")]},
    {"slug": "large-language-model", "term": "Large Language Model", "kind": "general",
     "short": "A language model trained on large text datasets to predict and generate sequences of tokens.",
     "body": ["A large language model can generate fluent text because training gives it a broad statistical model of language and other patterns. It does not mean every generated statement is sourced, current or correct.", "Prompt structure helps a writer state what the model should use and produce. Different large language models still have different limits and behaviours, so test the actual model and review consequential outputs."],
     "links": [("Transformers and LLMs", "/topics/transformers"), ("AI Model", "/dictionary/ai-model")]},
    {"slug": "hallucination", "term": "Hallucination", "kind": "general",
     "short": "An unsupported or invented detail presented by a generative model as if it were reliable.",
     "body": ["A hallucination can be a fabricated citation, a wrong number, an invented event or a detail that was not in the supplied source. Fluency and confidence do not establish that a statement is supported.", "Gaiish does not claim to eliminate hallucinations. Supplying context, defining knowledge boundaries and asking for validation can reduce ambiguity; people must still verify facts, sources and actions that matter."],
     "links": [("Validation", "/dictionary/validation"), ("Grounding", "/dictionary/grounding"), ("Research plans", "/research")]},
    {"slug": "output-specification", "term": "Output Specification", "kind": "gaiish",
     "short": "A description of the result's artefact, fields, sections, format and useful limits.",
     "body": ["In Gaiish, RESULT: or OUTPUT: specifies what the finished answer should look like. Name headings, columns, schema, ordering, audience and format rather than only naming the topic.", "An output specification makes an answer easier to use and evaluate. It does not guarantee that the model will follow every field, so VALIDATION: should check the returned shape."],
     "links": [("The Result method section", "/gaiish-method#result"), ("Gaiish Syntax", "/gaiish-syntax#skeleton")]},
    {"slug": "prompt", "term": "Prompt", "kind": "general",
     "short": "The input a person or system sends to a generative AI model.",
     "body": ["A prompt may contain a question, instructions, source material, examples, constraints and an output request. In a conversation, previous messages and system instructions may also shape what the model receives.", "Gaiish is a way to structure the meaningful parts of a prompt. It does not require special software or a separate model language; the declarations are written in ordinary words."],
     "links": [("Gaiish Syntax", "/gaiish-syntax"), ("Prompt engineering", "/prompt-engineering")]},
    {"slug": "prompt-framework", "term": "Prompt Framework", "kind": "gaiish",
     "short": "A repeatable shape for organising the components of a prompt.",
     "body": ["A framework tells a writer which fields to consider and in what order. Gaiish BASIC uses Goal, Context, Action and Output; Gaiish PRO uses Role, Intent, Context, Knowledge, Constraints, Process, Output and Validation.", "Frameworks are choices, not rituals. Use the smallest shape that exposes the decisions the task requires, and move to a fuller framework when review, handoff or consequence makes additional structure useful."],
     "links": [("Gaiish BASIC", "/gaiish-basic"), ("Gaiish PRO", "/gaiish-pro")]},
    {"slug": "retrieval-augmented-generation", "term": "Retrieval-Augmented Generation", "kind": "general",
     "short": "A pattern that retrieves relevant source material and supplies it to a generative model before generation.",
     "body": ["Retrieval-augmented generation, or RAG, separates finding relevant material from generating a response. A retrieval system selects passages, then the model uses those passages as context for the answer.", "RAG does not make retrieval or generation automatically correct. Define source authority, require citations or evidence links where appropriate, and validate missing or conflicting material."],
     "links": [("Embeddings and RAG", "/topics/embeddings-rag"), ("Grounding", "/dictionary/grounding")]},
    {"slug": "token", "term": "Token", "kind": "general",
     "short": "A unit of text or other input that a language model processes.",
     "body": ["Tokens are not always whole words: a word, part of a word, punctuation mark or other text unit may be represented by one or more tokens. Token counts influence context-window limits, cost and sometimes latency.", "A Gaiish writer does not need to count every token to be clear. They do need to keep context relevant and know the model's limits when pasting long source material."],
     "links": [("Context Window", "/dictionary/context-window"), ("Transformers and LLMs", "/topics/transformers")]},
    {"slug": "validation", "term": "Validation", "kind": "gaiish",
     "short": "A check that the result satisfies the request, evidence boundary and declared constraints.",
     "body": ["In Gaiish, VALIDATION: asks the model to check its own response before returning it. Request checks against each constraint, support for factual claims, and an explicit list of gaps or assumptions.", "Validation is not independent proof. A model can perform a flawed self-check, so people remain responsible for verifying important facts, calculations, sources and decisions."],
     "links": [("The Validation method section", "/gaiish-method#validation"), ("Research plans", "/research")]},
]


def _term_marker(term):
    if term["kind"] == "gaiish":
        return '<p class="term-marker gaiish-term">Gaiish term</p>'
    return '<p class="term-marker general-term">General AI term</p>'


def _term_schema(term, url):
    return {"@context": "https://schema.org", "@type": "DefinedTerm",
            "name": term["term"], "description": term["short"],
            "url": config.SITE_URL + url,
            "inDefinedTermSet": {"@type": "DefinedTermSet", "name": "Gaiish Dictionary",
                                 "url": config.SITE_URL + "/dictionary"}}


def _term_page(term):
    url = "/dictionary/" + term["slug"]
    blocks = [("html", _term_marker(term)), ("p", term["short"])]
    blocks.extend(("p", paragraph) for paragraph in term["body"])
    blocks += [("h2", "Related", "related"),
               ("links", list(term["links"]) + [("Back to the dictionary", "/dictionary#" + term["slug"])])]
    return {"route": url, "title": term["term"] + " — Gaiish Dictionary",
            "description": term["short"] + " Read the Gaiish Dictionary entry for " + term["term"] + ".",
            "eyebrow": "Dictionary", "h1": term["term"], "lede": term["short"],
            "breadcrumbs": [("Language", "/gaiish-language"), ("Dictionary", "/dictionary")],
            "nav_key": "/gaiish-language", "updated": config.LAST_UPDATED,
            "schema": [_term_schema(term, url)], "blocks": blocks}


DICTIONARY = {
    "route": "/dictionary", "title": "Gaiish Dictionary",
    "description": "The Gaiish Dictionary: concise, substantive definitions for Gaiish components and general AI terminology, with related method and topic links.",
    "eyebrow": "Reference", "h1": "Gaiish Dictionary",
    "lede": "A working vocabulary for structured human–AI communication, with Gaiish terms marked separately from general AI terminology.",
    "breadcrumbs": [("Language", "/gaiish-language")], "nav_key": "/gaiish-language",
    "updated": config.LAST_UPDATED, "blocks": [],
}
DICTIONARY["schema"] = [{
    "@context": "https://schema.org", "@type": "DefinedTermSet", "name": "Gaiish Dictionary",
    "url": config.SITE_URL + "/dictionary",
    "description": "Gaiish terms and general AI terminology used throughout the site.",
    "hasDefinedTerm": [{"@type": "DefinedTerm", "name": term["term"],
                        "description": term["short"],
                        "url": config.SITE_URL + "/dictionary/" + term["slug"]}
                       for term in sorted(TERMS, key=lambda item: item["term"].lower())],
}]
_sorted_terms = sorted(TERMS, key=lambda item: item["term"].lower())
_letters = [letter for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            if any(term["term"].upper().startswith(letter) for term in TERMS)]
DICTIONARY["blocks"].append(("html", '<nav class="az-jump" aria-label="Dictionary alphabet">%s</nav>' %
                             "".join('<a href="#letter-%s">%s</a>' % (letter.lower(), letter)
                                     for letter in _letters)))
for letter in _letters:
    DICTIONARY["blocks"].append(("h2", letter, "letter-" + letter.lower()))
    for term in [item for item in _sorted_terms if item["term"].upper().startswith(letter)]:
        DICTIONARY["blocks"] += [
            ("html", _term_marker(term)),
            ("html", '<h3 id="%s"><a href="/dictionary/%s" class="term-heading">%s</a></h3>' %
             (term["slug"], term["slug"], term["term"])),
            ("p", term["short"]),
            ("links", [("Read full entry", "/dictionary/" + term["slug"])])
        ]


EXAMPLES = [
    {"title": "Business — a decision brief",
     "traditional": "Review this sales report and tell me what to do next.",
     "gaiish": "INTENT:\nChoose the one sales action the commercial lead should take this week.\n\nCONTEXT:\n[paste the report]\nThe lead has 20 minutes. The report covers the last quarter and uses closed-won revenue.\n\nINSTRUCTION:\nExtract the strongest trend, compare it with the stated target, and recommend one action.\n\nCONSTRAINTS:\nDo not invent causes. Quote the report for every number. Separate evidence from interpretation.\n\nOUTPUT:\nA five-sentence recommendation followed by an Evidence table with metric, value and source.\n\nVALIDATION:\nCheck every number against the report and list any question the report cannot answer.",
     "why": "The Gaiish version adds Intent, Context, Instruction, Constraints, Output and Validation. It turns an open-ended opinion request into a decision brief with an evidence boundary and a checkable shape.",
     "links": [("Intent", "/dictionary/intent"), ("Context", "/dictionary/context"), ("Validation", "/dictionary/validation")]},
    {"title": "Writing — an audience-aware rewrite",
     "traditional": "Rewrite this announcement to sound more professional.",
     "gaiish": "INTENT:\nHelp existing customers understand the product change and what they need to do.\n\nCONTEXT:\n[paste announcement]\nAudience: non-technical customers who already use the product. The change takes effect on 1 October.\n\nINSTRUCTION:\nRewrite the announcement in plain language and preserve every factual detail.\n\nCONSTRAINTS:\nCalm, direct tone. No jargon, hype or exclamation marks. No more than 180 words.\n\nRESULT:\nSubject line plus email body, with the customer action in a separate final paragraph.\n\nVALIDATION:\nCompare dates, product names and customer actions with the source and list any ambiguous sentence.",
     "why": "The rewrite adds Intent and Audience through Context, then makes tone and length concrete under Constraints. Result and Validation prevent a fluent rewrite from quietly changing a date or omitting the action.",
     "links": [("Context", "/dictionary/context"), ("Constraint", "/dictionary/constraint"), ("Output Specification", "/dictionary/output-specification")]},
    {"title": "Information technology — incident summary",
     "traditional": "Summarise this incident for leadership.",
     "gaiish": "INTENT:\nGive the technology director enough evidence to decide whether the incident requires a customer communication.\n\nCONTEXT:\n[paste incident timeline and logs]\nThe director is not an incident responder. Times are UTC; the service affected is the billing API.\n\nINSTRUCTION:\nSeparate confirmed events, likely contributing factors and unresolved questions.\n\nCONSTRAINTS:\nDo not infer root cause from a log absence. Preserve timestamps. Avoid security-sensitive values and secrets.\n\nOUTPUT:\nA 150-word executive summary, then a timeline table and a Risks / Decisions needed section.\n\nVALIDATION:\nCheck each event against the timeline, flag missing intervals and mark every inference as inference.",
     "why": "Intent names the leadership decision, Context supplies the reader and source, and Constraints state an important evidence and security boundary. Output and Validation turn a summary into something leadership can review.",
     "links": [("Grounding", "/dictionary/grounding"), ("Constraint", "/dictionary/constraint"), ("Validation", "/dictionary/validation")]},
    {"title": "Education — a source-based explanation",
     "traditional": "Explain this chapter to my students.",
     "gaiish": "GOAL:\nHelp students distinguish the chapter's central claim from its supporting examples.\n\nCONTEXT:\n[paste source passage]\nStudents are 14 and have 25 minutes. They know the vocabulary in the lesson glossary.\n\nACTION:\nCreate a short worked example and a paired classification activity.\n\nOUTPUT:\nTeacher instructions, student handout and answer key.\n\nCONSTRAINTS:\nUse only the passage and glossary. Keep reading level accessible.\n\nVALIDATION:\nQuote the passage for every answer-key decision and mark ambiguous items.",
     "why": "BASIC adds a Goal, source Context, an Action and an assessable Output. The source-only constraint and validation make it easier for the educator to catch invented context.",
     "links": [("Gaiish BASIC", "/gaiish-basic"), ("Context", "/dictionary/context"), ("Validation", "/dictionary/validation")]},
    {"title": "Analysis — comparing alternatives",
     "traditional": "Compare these vendors and recommend one.",
     "gaiish": "INTENT:\nSelect the vendor that best fits a small team needing a reliable support platform this year.\n\nCONTEXT:\n[paste the three proposals]\nTeam size: 6. Current system has no export automation. Decision owner: operations manager.\n\nINSTRUCTION:\nExtract comparable facts, score each proposal against the criteria, and state the trade-off behind the recommendation.\n\nCONSTRAINTS:\nUse only supplied proposal facts. Do not treat marketing adjectives as evidence. Weight reliability and export capability above optional features.\n\nOUTPUT:\nA criteria table, a weighted score with calculation notes, recommendation and two questions for the preferred vendor.\n\nVALIDATION:\nCheck each score against the criteria and mark missing prices, terms or capabilities as unknown.",
     "why": "The structured version adds a decision Intent, operating Context, an explicit comparison Instruction, weighting Constraints, a reviewable Output and Validation for missing evidence.",
     "links": [("Intent", "/dictionary/intent"), ("Constraint", "/dictionary/constraint"), ("Iteration", "/dictionary/iteration")]},
    {"title": "Customer service — an accountable reply",
     "traditional": "Reply to this angry customer.",
     "gaiish": "INTENT:\nResolve the customer's documented issue and make the next step clear without promising an unapproved remedy.\n\nCONTEXT:\n[paste the customer message and case history]\nThe agent may offer a refund only when the policy below allows it. Audience: the customer, who is frustrated.\n\nINSTRUCTION:\nDraft a reply that acknowledges the issue, states what is known, and gives the next action.\n\nCONSTRAINTS:\nWarm but direct. Do not blame the customer or claim an investigation is complete. Do not promise a refund unless the policy supports it. Under 160 words.\n\nOUTPUT:\nEmail body with no subject line, followed by an internal note listing any approval needed.\n\nVALIDATION:\nCheck every promise against the case history and policy, and flag missing facts before the reply is sent.",
     "why": "The Gaiish version supplies the case Context, the service Intent, a precise Instruction and safety Constraints. The Output separates the customer-facing reply from internal follow-up, while Validation catches unsupported promises.",
     "links": [("Context", "/dictionary/context"), ("Constraint", "/dictionary/constraint"), ("Validation", "/dictionary/validation")]},
]


EXAMPLES_PAGE = {
    "route": "/examples", "title": "Gaiish Examples",
    "description": "Traditional and Gaiish prompt examples across business, writing, IT, education, analysis and customer service.",
    "eyebrow": "Reference", "h1": "Gaiish Examples",
    "lede": "See the same kind of request before and after its purpose, context, boundaries and checks are made explicit.",
    "breadcrumbs": [("Examples", "/examples")], "nav_key": "/gaiish-language",
    "updated": config.LAST_UPDATED, "blocks": [],
}
for example in EXAMPLES:
    anchor = example["title"].lower().replace(" ", "-").replace("—", "").replace("--", "-")
    EXAMPLES_PAGE["blocks"] += [("h2", example["title"], anchor),
                                ("compare", example["traditional"], example["gaiish"], example["why"]),
                                ("links", example["links"])]


LIBRARY = [
    {"category": "Business", "entries": [
        ("Quarterly decision brief", "INTENT:\nHelp the leadership team decide whether to continue the pilot.\n\nCONTEXT:\n[paste pilot metrics and customer notes]\nThe pilot has run for one quarter; separate observed results from customer opinions.\n\nINSTRUCTION:\nSummarise evidence for continuation, change or stop.\n\nCONSTRAINTS:\nDo not infer causation. Preserve metric definitions and flag missing baselines.\n\nOUTPUT:\nRecommendation, evidence table, risks and decision questions.\n\nVALIDATION:\nCheck every number against the supplied metrics and list unsupported conclusions.",
         "The decision, evidence boundary and review shape are explicit, so the brief supports a real choice rather than a generic summary.", [("Intent", "/dictionary/intent"), ("Validation", "/dictionary/validation")]),
        ("Process handoff", "INTENT:\nGive the next operator a reliable handoff for today's unresolved work.\n\nCONTEXT:\n[paste ticket list and notes]\nThe next operator has 30 minutes and can change status but cannot approve refunds.\n\nINSTRUCTION:\nGroup the work by urgency and write the next action for each item.\n\nCONSTRAINTS:\nDo not close a ticket without evidence. Keep customer identifiers exactly as supplied.\n\nOUTPUT:\nPriority table with ticket, evidence, owner and next action.\n\nVALIDATION:\nFlag missing owners, missing evidence and any item needing approval.",
         "Context, authority limits and validation make the handoff useful to another person and safer to act on.", [("Context", "/dictionary/context"), ("Constraint", "/dictionary/constraint")]),
    ]},
    {"category": "Management", "entries": [
        ("One-to-one preparation", "GOAL:\nHelp a manager prepare a constructive 30-minute one-to-one.\n\nCONTEXT:\n[paste role description and recent notes]\nThe employee has asked to discuss priorities and support.\n\nACTION:\nDraft five open questions and a two-item agenda.\n\nOUTPUT:\nAgenda first, then questions with the purpose of each.\n\nCONSTRAINTS:\nDo not diagnose performance or infer feelings from silence.\n\nVALIDATION:\nMark questions that rely on an assumption not present in the notes.",
         "The goal and boundaries keep the model from turning sparse notes into a performance judgement.", [("Gaiish BASIC", "/gaiish-basic"), ("Validation", "/dictionary/validation")]),
        ("Team planning", "INTENT:\nTurn the team's committed work into a realistic fortnight plan.\n\nCONTEXT:\n[paste backlog and capacity notes]\nFour people are available for 10 working days; production incidents take priority.\n\nINSTRUCTION:\nGroup work by dependency, identify a critical path and propose a plan.\n\nCONSTRAINTS:\nDo not schedule more capacity than stated. Mark estimates as estimates.\n\nOUTPUT:\nPlan by day, dependency list and risks requiring a manager decision.\n\nVALIDATION:\nRecheck capacity totals and list every assumption.",
         "Capacity is context and a hard constraint; validation checks arithmetic instead of rewarding a confident schedule.", [("Context", "/dictionary/context"), ("Constraint", "/dictionary/constraint")]),
    ]},
    {"category": "Information Technology", "entries": [
        ("Architecture review", "INTENT:\nIdentify the two largest operational risks in this proposed service architecture.\n\nCONTEXT:\n[paste architecture diagram and requirements]\nThe service must support the stated traffic range and a weekday on-call team.\n\nINSTRUCTION:\nTrace request flow, identify failure points and compare each with the requirements.\n\nCONSTRAINTS:\nUse only the supplied design. Distinguish a design gap from a missing diagram detail.\n\nOUTPUT:\nRisk table with component, failure mode, evidence, impact and open question.\n\nVALIDATION:\nCite the diagram or requirement for each risk and mark unsupported assumptions.",
         "The source boundary and failure-oriented output make the review specific without pretending to know an undocumented deployment.", [("Grounding", "/dictionary/grounding"), ("Output Specification", "/dictionary/output-specification")]),
        ("Runbook draft", "INTENT:\nHelp an on-call engineer recover the documented service failure safely.\n\nCONTEXT:\n[paste incident notes and approved runbook fragments]\nThe engineer may restart the worker but may not change database schema.\n\nINSTRUCTION:\nOrder the diagnostic and recovery steps, with a stop condition after each risky action.\n\nCONSTRAINTS:\nDo not invent commands. Preserve rollback steps and escalation contacts.\n\nOUTPUT:\nNumbered runbook with prerequisites, steps, stop conditions and escalation.\n\nVALIDATION:\nCheck every command against the supplied fragments and flag any missing prerequisite.",
         "Role and permission context plus stop conditions turn prose into a safer operational artefact.", [("Instruction", "/dictionary/instruction"), ("Constraint", "/dictionary/constraint")]),
    ]},
    {"category": "Marketing", "entries": [
        ("Campaign brief", "INTENT:\nPlan a 30-day campaign that increases qualified demo requests from practice owners.\n\nCONTEXT:\n[paste product notes and existing campaign results]\nTeam: one marketer half-time. Audience: private dental practices with 2–6 chairs.\n\nINSTRUCTION:\nPropose channels, messages, weekly activities and a measurement plan.\n\nCONSTRAINTS:\nBudget is $5,000. No paid search or new engineering. Do not claim results not in the source.\n\nOUTPUT:\nStrategy, weekly plan, budget table, message examples and measures.\n\nVALIDATION:\nCheck activities against budget and staffing and list assumptions.",
         "The campaign has a buyer, resource boundary, exclusions and measurement shape rather than a request for generic ideas.", [("Intent", "/dictionary/intent"), ("Constraint", "/dictionary/constraint")]),
        ("Customer story interview", "INTENT:\nPrepare an interview guide that reveals why a customer adopted the product.\n\nCONTEXT:\n[paste account notes]\nInterview length: 30 minutes. The customer has agreed to discuss workflow, not confidential finances.\n\nINSTRUCTION:\nWrite eight open questions in a logical sequence.\n\nCONSTRAINTS:\nDo not lead the customer toward a preferred answer. Avoid questions about restricted information.\n\nOUTPUT:\nQuestion, purpose and optional follow-up for each item.\n\nVALIDATION:\nFlag any question that assumes a benefit or asks for restricted information.",
         "The goal, interview context and ethical constraints produce questions that can generate evidence instead of praise.", [("Context", "/dictionary/context"), ("Validation", "/dictionary/validation")]),
    ]},
    {"category": "Education", "entries": [
        ("Lesson activity", "GOAL:\nHelp students practise distinguishing evidence from interpretation.\n\nCONTEXT:\n[paste source passage]\nStudents are 14 and have 25 minutes. They know the vocabulary in the lesson glossary.\n\nACTION:\nCreate a short worked example and a paired classification activity.\n\nOUTPUT:\nTeacher instructions, student handout and answer key.\n\nCONSTRAINTS:\nUse only the passage and glossary. Keep reading level accessible.\n\nVALIDATION:\nQuote the passage for every answer-key decision and mark ambiguous items.",
         "The output serves both teacher and student, while the source-only constraint makes the activity auditable.", [("Gaiish BASIC", "/gaiish-basic"), ("Context", "/dictionary/context")]),
        ("Feedback rubric", "INTENT:\nGive a student actionable feedback on an argument draft without rewriting it for them.\n\nCONTEXT:\n[paste draft and assignment rubric]\nThe student is revising a first draft.\n\nINSTRUCTION:\nIdentify one strength and the three highest-impact revisions, each tied to a rubric criterion.\n\nCONSTRAINTS:\nDo not invent citations or supply a replacement essay. Use encouraging, specific language.\n\nOUTPUT:\nCriterion, evidence in draft, revision suggestion and question for the student.\n\nVALIDATION:\nCheck each comment against the draft and rubric and flag criteria not evidenced.",
         "The rubric and evidence columns keep feedback tied to the student's work and preserve student agency.", [("Constraint", "/dictionary/constraint"), ("Output Specification", "/dictionary/output-specification")]),
    ]},
    {"category": "Research", "entries": [
        ("Literature extraction", "INTENT:\nCreate a traceable extraction table for studies relevant to the stated review question.\n\nCONTEXT:\n[paste papers or abstracts]\nReview question: [question]. The supplied text is the only source authority.\n\nINSTRUCTION:\nExtract population, intervention, comparison, outcome and limitation for each study.\n\nCONSTRAINTS:\nDo not infer absent methods or results. Quote page or section references when present.\n\nOUTPUT:\nOne row per study plus a Missing information column.\n\nVALIDATION:\nCompare every row with the source and list studies where the supplied text is incomplete.",
         "The evidence boundary, extraction schema and missing-information rule reduce the temptation to fill gaps.", [("Grounding", "/dictionary/grounding"), ("Validation", "/dictionary/validation")]),
        ("Research question refinement", "INTENT:\nTurn the project idea into one answerable research question and a list of definitions to resolve.\n\nCONTEXT:\n[paste project notes]\nAudience: supervisor reviewing feasibility. No data has been collected yet.\n\nINSTRUCTION:\nIdentify the proposed phenomenon, population, comparison and outcome, then draft two candidate questions.\n\nCONSTRAINTS:\nDo not claim the question is novel or feasible without evidence. Preserve uncertainty.\n\nOUTPUT:\nAssumptions, candidate questions, what each would measure and feasibility questions.\n\nVALIDATION:\nMark every claim that requires a source or a decision from the supervisor.",
         "The prompt separates a framing exercise from unsupported claims about novelty or feasibility.", [("Intent", "/dictionary/intent"), ("Constraint", "/dictionary/constraint")]),
    ]},
    {"category": "Writing", "entries": [
        ("Editorial outline", "INTENT:\nGive an editor a usable outline for an article that explains the decision behind the topic.\n\nCONTEXT:\n[paste source notes]\nAudience: informed general readers. The article must distinguish sourced facts from interpretation.\n\nINSTRUCTION:\nPropose a thesis, section sequence and evidence needed for each section.\n\nCONSTRAINTS:\nDo not invent sources or settle disputed claims. Keep the outline under 500 words.\n\nOUTPUT:\nHeadline options, thesis, numbered outline and open research questions.\n\nVALIDATION:\nFlag each section that lacks supplied evidence.",
         "The outline asks for the structure of an article while keeping research gaps visible.", [("Intent", "/dictionary/intent"), ("Output Specification", "/dictionary/output-specification")]),
        ("Plain-language edit", "INTENT:\nHelp a resident understand what action the policy requires of them.\n\nCONTEXT:\n[paste policy]\nAudience: residents with no specialist knowledge. Legal review will use the edited draft.\n\nINSTRUCTION:\nRewrite the policy explanation in plain language without changing obligations.\n\nCONSTRAINTS:\nPreserve dates, exceptions and defined terms. No more than 400 words. Do not add legal advice.\n\nOUTPUT:\nHeading, short explanation, required action and questions the resident may need to ask.\n\nVALIDATION:\nCompare every obligation and date with the source and list any ambiguous term.",
         "Audience, source authority and preservation constraints make “plain language” a controlled rewrite rather than a paraphrase.", [("Context", "/dictionary/context"), ("Constraint", "/dictionary/constraint")]),
    ]},
    {"category": "Analysis", "entries": [
        ("Spreadsheet interpretation", "INTENT:\nExplain the three material changes in this monthly operating report for a finance review.\n\nCONTEXT:\n[paste table]\nDefinitions: revenue excludes tax; variance is actual minus plan. The reader has not seen prior months.\n\nINSTRUCTION:\nCalculate stated variances, identify trends and separate observation from possible explanation.\n\nCONSTRAINTS:\nDo not invent causes. Preserve units and rounding. Show calculations.\n\nOUTPUT:\nExecutive summary, variance table, observations and questions for the data owner.\n\nVALIDATION:\nRecalculate each variance against the supplied values and flag missing periods.",
         "Definitions in Context and calculation checks prevent familiar business language from hiding a changed metric meaning.", [("Context", "/dictionary/context"), ("Validation", "/dictionary/validation")]),
        ("Options analysis", "INTENT:\nHelp a project owner choose between the three options using the stated criteria.\n\nCONTEXT:\n[paste options and criteria]\nThe owner values reversibility and delivery time above optional scope.\n\nINSTRUCTION:\nCompare options criterion by criterion and identify the trade-off of the leading option.\n\nCONSTRAINTS:\nUse only the supplied criteria and facts. Do not convert qualitative claims into false precision.\n\nOUTPUT:\nComparison matrix, leading option, trade-off and two questions before commitment.\n\nVALIDATION:\nCheck each comparison cell against the source and mark unknowns.",
         "The prompt makes decision priorities explicit without pretending qualitative evidence is more precise than it is.", [("Intent", "/dictionary/intent"), ("Constraint", "/dictionary/constraint")]),
    ]},
    {"category": "Productivity", "entries": [
        ("Inbox triage", "GOAL:\nTurn today's inbox into a short list of actions for the owner.\n\nCONTEXT:\n[paste messages]\nThe owner has 45 minutes. Messages containing personal or confidential details must not be reproduced.\n\nACTION:\nGroup messages by action, urgency and waiting-on-person.\n\nOUTPUT:\nA table with message subject, action, due date if stated and suggested reply; omit message bodies.\n\nCONSTRAINTS:\nDo not infer urgency from tone alone. Preserve stated dates.\n\nVALIDATION:\nCheck each due date against the source and flag ambiguous ownership.",
         "BASIC supplies a time limit, privacy boundary and usable table without turning triage into a new workflow.", [("Gaiish BASIC", "/gaiish-basic"), ("Constraint", "/dictionary/constraint")]),
        ("Weekly planning", "INTENT:\nCreate a realistic weekly plan that protects the two stated priorities.\n\nCONTEXT:\n[paste tasks and calendar constraints]\nAvailable focus time is 12 hours. Meetings and fixed deadlines are listed below.\n\nINSTRUCTION:\nSequence tasks by dependency and deadline and identify what must be deferred.\n\nCONSTRAINTS:\nDo not schedule more than 12 focus hours. Leave 20% unallocated for interruptions.\n\nOUTPUT:\nDay-by-day plan, deferred list and risks.\n\nVALIDATION:\nCheck hours, dependencies and deadlines and list assumptions.",
         "The plan is constrained by real capacity and includes a deliberate deferral decision instead of fitting every task into an impossible week.", [("Intent", "/dictionary/intent"), ("Validation", "/dictionary/validation")]),
    ]},
    {"category": "Software Development", "entries": [
        ("Code review", "INTENT:\nFind correctness, security and maintainability risks before this change is merged.\n\nCONTEXT:\n[paste diff and relevant tests]\nThe code handles user-provided filenames. Existing conventions are in the adjacent module.\n\nINSTRUCTION:\nReview the diff, trace error paths and compare behaviour with the tests.\n\nCONSTRAINTS:\nReport only issues supported by the diff or supplied files. Do not rewrite the patch.\n\nOUTPUT:\nFindings ordered by severity with file/line, evidence, impact and suggested test.\n\nVALIDATION:\nCheck each finding against the exact diff and distinguish a confirmed issue from a question.",
         "The review has a severity-aware output and evidence rule, helping a developer act on findings without accepting speculation.", [("Context", "/dictionary/context"), ("Validation", "/dictionary/validation")]),
        ("Test design", "INTENT:\nAdd tests that expose the boundary cases in the date parser.\n\nCONTEXT:\n[paste parser, current tests and accepted date formats]\nThe parser must reject ambiguous dates rather than guessing.\n\nINSTRUCTION:\nList partitions and write test cases for valid, invalid and ambiguous inputs.\n\nCONSTRAINTS:\nUse the accepted formats only. Do not change production code or invent a locale rule.\n\nOUTPUT:\nTest table with input, expected result, reason and missing coverage.\n\nVALIDATION:\nCheck every expected result against the supplied format rules.",
         "The format rules and reject-on-ambiguity constraint turn a broad testing request into inspectable coverage.", [("Constraint", "/dictionary/constraint"), ("Output Specification", "/dictionary/output-specification")]),
    ]},
    {"category": "Customer Service", "entries": [
        ("Ticket categorisation", "INTENT:\nRoute incoming tickets to the correct team without losing evidence of uncertainty.\n\nCONTEXT:\n[paste ticket text and routing rules]\nCategories and escalation triggers are listed in the rules.\n\nINSTRUCTION:\nAssign one category, identify any escalation trigger and quote the supporting phrase.\n\nCONSTRAINTS:\nDo not infer a trigger absent from the rules. If no category fits, mark Unclear.\n\nOUTPUT:\nTicket ID, category, evidence, escalation and confidence note.\n\nVALIDATION:\nCompare each assignment with the routing rules and list unclear cases.",
         "The routing rules become explicit knowledge and the Unclear outcome prevents forced classifications.", [("Knowledge", "/gaiish-pro"), ("Validation", "/dictionary/validation")]),
        ("Support macro", "INTENT:\nDraft a reusable reply for customers who cannot complete the documented setup step.\n\nCONTEXT:\n[paste help article and approved policy]\nAudience: new customers. The agent can link the article but cannot change account settings.\n\nINSTRUCTION:\nDraft a reply that diagnoses the documented step, links the relevant section and asks for one missing detail.\n\nCONSTRAINTS:\nDo not promise a fix or ask for passwords. Under 140 words.\n\nOUTPUT:\nCustomer-facing reply and one internal escalation note.\n\nVALIDATION:\nCheck links, permissions and promises against the supplied material.",
         "The prompt protects account boundaries, gives the customer a next step and separates the reusable response from escalation.", [("Context", "/dictionary/context"), ("Constraint", "/dictionary/constraint")]),
    ]},
    {"category": "Human Resources", "entries": [
        ("Interview guide", "INTENT:\nCreate a structured interview guide that tests the stated competencies fairly.\n\nCONTEXT:\n[paste role description and competency rubric]\nInterview length: 45 minutes. All candidates receive the same core questions.\n\nINSTRUCTION:\nWrite one primary question and one follow-up for each competency.\n\nCONSTRAINTS:\nDo not ask about protected characteristics or infer them from a response. Keep questions job-related.\n\nOUTPUT:\nQuestion sequence, competency tested, evidence to listen for and permitted follow-up.\n\nVALIDATION:\nCheck every question against the rubric and flag any question that is not job-related.",
         "The rubric, consistent core questions and explicit boundaries support a reviewable process without pretending a prompt makes hiring objective.", [("Constraints", "/gaiish-method#constraints"), ("Validation", "/dictionary/validation")]),
        ("Policy explanation", "INTENT:\nHelp employees understand the steps and contact point in the leave policy.\n\nCONTEXT:\n[paste approved policy]\nAudience: employees; HR will approve the final explanation.\n\nINSTRUCTION:\nRewrite the procedure in plain language while preserving eligibility and deadlines.\n\nCONSTRAINTS:\nDo not interpret an employee's individual eligibility. Preserve defined terms and escalation contacts.\n\nOUTPUT:\nShort explanation, numbered steps, deadline table and questions for HR.\n\nVALIDATION:\nCompare every deadline and eligibility statement with the policy and list ambiguous wording.",
         "The source and approval boundary make the rewrite useful while keeping individual decisions with HR.", [("Context", "/dictionary/context"), ("Output Specification", "/dictionary/output-specification")]),
    ]},
]


LIBRARY_PAGE = {
    "route": "/prompt-library", "title": "Gaiish Prompt Library",
    "description": "A practical Gaiish prompt library organised by Business, Management, IT, Marketing, Education, Research and eight other use cases.",
    "eyebrow": "Reference", "h1": "Gaiish Prompt Library",
    "lede": "Reusable starting points for real work. Adapt the context and constraints; do not paste sensitive material into an unapproved system.",
    "breadcrumbs": [("Examples", "/examples")], "nav_key": "/gaiish-language",
    "updated": config.LAST_UPDATED, "blocks": [],
}
for category in LIBRARY:
    LIBRARY_PAGE["blocks"].append(("h2", category["category"], category["category"].lower().replace(" ", "-")))
    for title, prompt, why, links in category["entries"]:
        LIBRARY_PAGE["blocks"] += [("h3", title), ("code", prompt),
                                   ("p", "<strong>Why this works:</strong> " + why),
                                   ("links", links)]


PAGES = [DICTIONARY] + [_term_page(term) for term in TERMS] + [EXAMPLES_PAGE, LIBRARY_PAGE]
