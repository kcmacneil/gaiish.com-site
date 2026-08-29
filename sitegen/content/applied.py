"""Applied-practice pages: prompt engineering, teams, business and education."""

from .. import config


PROMPT_ENGINEERING = {
    "route": "/prompt-engineering",
    "title": "Prompt Engineering",
    "description": (
        "A practical, honest introduction to prompt engineering and how Gaiish structures "
        "intent, context, instructions, constraints, results and validation."
    ),
    "eyebrow": "Practice",
    "h1": "Prompt Engineering",
    "lede": (
        "Prompt engineering is the practice of designing, testing and refining instructions for "
        "a generative AI system."
    ),
    "breadcrumbs": [("Context", "/prompt-engineering")],
    "nav_key": "/prompt-engineering",
    "updated": config.LAST_UPDATED,
    "blocks": [
        ("p",
         "A prompt is an interface between a person's goal and a model's probabilistic "
         "interpretation. Prompt engineering makes that interface more deliberate: choose the "
         "right context, write an unambiguous task, specify the result, test the response and "
         "refine the part that failed. It applies to a one-off question and to prompts embedded "
         "in a product or workflow."),
        ("h2", "What the practice includes", "includes"),
        ("ul", [
            "Understanding the task, audience, source material and model you are working with.",
            "Writing instructions that say what to do, with useful constraints and an explicit "
            "output shape.",
            "Testing representative inputs and checking results rather than judging one lucky "
            "answer.",
            "Iterating from evidence: preserve what works, then change one unclear or missing "
            "part at a time.",
            "Designing human review for factual, sensitive or consequential outputs.",
        ]),
        ("h2", "A structure for the work", "structure"),
        ("p",
         "Gaiish is one way to organise prompt-engineering practice. Its vocabulary puts the "
         "questions in view: what is the intent, what context is missing, what instruction "
         "should run, which constraints matter, what result is usable and how will it be "
         "validated? It does not replace testing, model knowledge or domain expertise."),
        ("framework", None),
        ("compare",
         "Make this report better and shorter.",
         "INTENT:\n"
         "Give a board member the evidence needed to decide whether to continue the pilot.\n\n"
         "CONTEXT:\n"
         "[paste report]\n"
         "The reader has five minutes and has not seen the underlying data.\n\n"
         "INSTRUCTION:\n"
         "Extract the decision-relevant findings and rewrite the report around them.\n\n"
         "CONSTRAINTS:\n"
         "Do not remove caveats or change numbers. Use plain language and no more than 700 words.\n\n"
         "RESULT:\n"
         "Executive summary, evidence table, risks and decision question.\n\n"
         "VALIDATION:\n"
         "Check every number against the source and list any finding the report does not support.",
         "The structured prompt makes the engineering choices inspectable. It names the reader "
         "and decision, supplies the report, limits the rewrite, defines a usable shape and "
         "requires source checks. It can improve instruction adherence and reduce ambiguity, "
         "while the output still needs review."),
        ("h2", "Go deeper", "next"),
        ("links", [
            ("The Gaiish Method", "/gaiish-method"),
            ("Gaiish vs prompt engineering", "/gaiish-vs-prompt-engineering"),
            ("Generative AI foundations", "/generative-ai"),
            ("Topics: embeddings and RAG", "/topics/embeddings-rag"),
            ("Topics: agents", "/topics/agents"),
        ]),
    ],
}


VS_PROMPT_ENGINEERING = {
    "route": "/gaiish-vs-prompt-engineering",
    "title": "Gaiish vs Prompt Engineering",
    "description": (
        "How Gaiish relates to prompt engineering: a structured methodology and vocabulary "
        "within the broader practice of designing and refining AI prompts."
    ),
    "eyebrow": "Context",
    "h1": "Gaiish vs Prompt Engineering",
    "lede": (
        "They are not competing ideas. Prompt engineering is the broad practice; Gaiish is a "
        "structured vocabulary and method that can be used within it."
    ),
    "breadcrumbs": [("Context", "/prompt-engineering")],
    "nav_key": "/prompt-engineering",
    "updated": config.LAST_UPDATED,
    "blocks": [
        ("h2", "The relationship", "relationship"),
        ("p",
         "Prompt engineering includes understanding a model, selecting and supplying context, "
         "designing prompts, evaluating outputs and improving a workflow. Gaiish focuses on the "
         "communication structure inside that practice. It gives a writer named places for "
         "intent, context, instruction, constraints, result and validation, plus practical "
         "frameworks for choosing how much detail a task needs."),
        ("table", ["Question", "Prompt engineering", "Gaiish"], [
            ["Scope", "A broad practice of designing, testing and refining prompts and workflows.",
             "A language and method for expressing the structure of a request."],
            ["Focus", "The whole interaction: model, prompt, context, evaluation and iteration.",
             "The human-readable declarations inside the prompt."],
            ["Use together", "Test whether a design works for its task and model.",
             "Make the design's purpose, evidence, boundaries and checks explicit."],
        ]),
        ("h2", "What Gaiish adds", "adds"),
        ("p",
         "A shared structure helps people review a prompt before they run it. A colleague can "
         "ask “where is the audience?” or “what validates this number?” instead of offering a "
         "general opinion that the wording feels unclear. Teams can teach the same components, "
         "hand prompts to one another and compare revisions without relying on a private set of "
         "phrases."),
        ("p",
         "That is a communication benefit, not a superiority claim. Gaiish does not replace "
         "model evaluation, retrieval design, tool permissions, fine-tuning or domain review. "
         "It is one structure among the techniques a prompt engineer may choose."),
        ("h2", "A useful way to combine them", "combine"),
        ("steps", [
            ("Frame", "Use Gaiish to state the intent, context, instruction, constraints, result and validation."),
            ("Design", "Choose the model, tools, context window and workflow that fit the task."),
            ("Test", "Run representative cases and inspect facts, format and instruction adherence."),
            ("Refine", "Change the missing or ambiguous component, then test again."),
        ]),
        ("callout", "Keep the distinction clear",
         "Gaiish is not an industry standard or a guarantee of performance. It is a developing "
         "methodology and vocabulary documented here. Models do not interpret prompts "
         "identically, so the model-specific part of prompt engineering still matters."),
        ("links", [
            ("Learn the six components", "/gaiish-method"),
            ("Use BASIC", "/gaiish-basic"),
            ("Use PRO", "/gaiish-pro"),
            ("Read generative AI background", "/generative-ai"),
        ]),
    ],
}


BUSINESS = {
    "route": "/gaiish-for-business",
    "title": "Gaiish for Business",
    "description": (
        "How managers and teams can use Gaiish for shared prompt structure, review, handoff and "
        "more explicit AI-assisted business work."
    ),
    "eyebrow": "Applied use",
    "h1": "Gaiish for Business",
    "lede": (
        "A shared prompt structure turns an individual trick into a brief a team can review, "
        "reuse and hand to the next person."
    ),
    "breadcrumbs": [("Use", "/gaiish-for-business")],
    "nav_key": "/gaiish-for-business",
    "updated": config.LAST_UPDATED,
    "blocks": [
        ("h2", "The team problem", "problem"),
        ("p",
         "A useful prompt often lives in one person's memory: which document to paste, what "
         "“good” means, which claims need a source and which format a manager expects. When the "
         "work changes hands, those decisions disappear. Gaiish makes them part of the brief. "
         "The result is not automatic quality; it is a prompt another teammate can read and "
         "challenge before using."),
        ("h2", "A shared review habit", "review"),
        ("steps", [
            ("Name the outcome", "Write INTENT: or GOAL: so the team knows what decision or deliverable the work serves."),
            ("Supply the evidence", "Put source material and relevant operating context under CONTEXT: or KNOWLEDGE:."),
            ("Set the boundary", "Record audience, scope, tone, limits, exclusions and uncertainty under CONSTRAINTS:."),
            ("Make it checkable", "Describe the artefact under OUTPUT: and ask VALIDATION: to check the source and rules."),
        ]),
        ("h2", "Worked example — a weekly customer brief", "example"),
        ("code",
         "INTENT:\n"
         "Give the customer-success lead a weekly brief that helps her choose which accounts "
         "need a human follow-up.\n\n"
         "CONTEXT:\n"
         "[paste the week's account notes]\n"
         "Accounts are mid-market software customers. The lead has 20 minutes to review the "
         "brief. A follow-up means a named owner and a next action.\n\n"
         "INSTRUCTION:\n"
         "Identify accounts with a specific risk signal and summarise the evidence for each.\n\n"
         "CONSTRAINTS:\n"
         "Do not infer risk from silence. Do not include accounts without evidence in the notes. "
         "Use plain language and preserve customer names exactly as supplied.\n\n"
         "OUTPUT:\n"
         "A table with Account, Evidence, Risk signal, Suggested next action and Evidence gap, "
         "followed by a three-sentence overview.\n\n"
         "VALIDATION:\n"
         "Check each row against the notes, flag unsupported inferences and count the rows in "
         "the overview."),
        ("p",
         "A manager can review this before it runs: is the source current, is “risk signal” "
         "defined, are the exclusions appropriate, and can the lead act on the output? The same "
         "brief can be adapted for another week without rediscovering its shape."),
        ("h2", "Where it fits", "fits"),
        ("p",
         "Use Gaiish alongside the team's existing security, privacy, legal and approval "
         "processes. Do not paste confidential material into a model unless the organisation "
         "has approved that workflow and its handling. A well-structured prompt cannot authorise "
         "access the model does not have."),
        ("links", [
            ("Gaiish PRO for repeatable work", "/gaiish-pro"),
            ("The Gaiish Method", "/gaiish-method"),
            ("Research plans", "/research"),
        ]),
    ],
}


EDUCATION = {
    "route": "/gaiish-for-education",
    "title": "Gaiish for Education",
    "description": (
        "How educators and students can teach structured AI communication with Gaiish, including "
        "a classroom example and an academic-integrity note."
    ),
    "eyebrow": "Applied use",
    "h1": "Gaiish for Education",
    "lede": (
        "Teach the structure of a request, not a bag of magic phrases. Students can show what "
        "they know by making goals, evidence, constraints and checks explicit."
    ),
    "breadcrumbs": [("Use", "/gaiish-for-education")],
    "nav_key": "/gaiish-for-education",
    "updated": config.LAST_UPDATED,
    "blocks": [
        ("h2", "A teachable structure", "structure"),
        ("p",
         "Gaiish gives a class a way to discuss why an AI response went wrong. Was the goal "
         "unclear? Was the source material missing? Did the output ignore a format requirement? "
         "Was there no validation step? Those questions move the conversation from “the AI is "
         "bad” or “the student found the right phrase” to the design of the communication."),
        ("p",
         "An educator can introduce BASIC for low-stakes practice, then use the full method or "
         "PRO to make evidence boundaries and evaluation criteria explicit. Students should "
         "still learn the subject matter; a structure helps them direct and inspect a model, "
         "but it does not substitute for reading, reasoning or source evaluation."),
        ("h2", "Worked example — comparing two explanations", "example"),
        ("compare",
         "Explain photosynthesis for my class.",
         "GOAL:\n"
         "Help Year 9 students explain the inputs, process and output of photosynthesis in their "
         "own words after reading the supplied passage.\n\n"
         "CONTEXT:\n"
         "[paste the class passage]\n"
         "Students know that plants need light but have not learned the chemical equation. "
         "Audience: mixed reading confidence, 13–14 years old.\n\n"
         "ACTION:\n"
         "Draft an explanation, then write three questions that reveal whether a student can "
         "distinguish an input from an output.\n\n"
         "OUTPUT:\n"
         "A 180-word explanation, a simple text equation, and three questions with answer keys. "
         "Use no jargon that the passage does not define.",
         "The second version gives the model a source, a learning goal, an age range, a boundary "
         "around new vocabulary and a way to make the result assessable. The teacher can compare "
         "the answer with the passage and edit the questions. Structure can improve instruction "
         "adherence and reduce ambiguity, but the educator remains responsible for accuracy and "
         "suitability."),
        ("h2", "Academic integrity", "integrity"),
        ("callout", "Use must follow the course rules",
         "Whether and how students may use generative AI is an institutional and instructor "
         "decision. Follow the assignment policy, disclose permitted assistance and do not "
         "present generated work as your own where that is prohibited. A Gaiish prompt can make "
         "the interaction more transparent by recording the goal, source material and requested "
         "output; it does not make unauthorised work acceptable."),
        ("h2", "A classroom activity", "activity"),
        ("ol", [
            "Give pairs the same vague request and ask them to predict what the model would have "
            "to guess.",
            "Have each pair rewrite it with GOAL, CONTEXT, ACTION and OUTPUT.",
            "Compare the two outputs against the source passage and the stated learning goal.",
            "Add a validation instruction and discuss which errors it catches and which still "
            "need a human check.",
        ]),
        ("links", [
            ("Learn Gaiish", "/learn-gaiish"),
            ("Gaiish Syntax", "/gaiish-syntax"),
            ("The language specification", "/gaiish-language/specification"),
            ("Generative AI background", "/generative-ai"),
        ]),
    ],
}


PAGES = [PROMPT_ENGINEERING, VS_PROMPT_ENGINEERING, BUSINESS, EDUCATION]
