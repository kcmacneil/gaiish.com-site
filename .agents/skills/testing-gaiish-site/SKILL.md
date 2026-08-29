---
name: testing-gaiish-site
description: How to runtime-test the gaiish.com static site (nav, Prompt Builder, Prompt Analyzer, mobile layout, metadata) in a browser and via shell.
---

# Testing the gaiish.com static site

## Where to test
- Production is `https://gaiish.com` (Vercel). Prefer it when the change is already deployed.
- Local: `python3 build.py` then `python3 -m http.server 8000` from the repo root; serve URLs as
  `http://localhost:8000/<route>/` (local server needs the directory form; production uses no trailing slash).
- No auth, no secrets, no dependency installs are needed for either mode.

## Devin Secrets Needed
- None.

## Prompt Analyzer (`/tools/prompt-analyzer`)
- Scoring lives in `tools/analyzer-score.js`. Weights: Intent 20, Context 20, Instruction 20,
  Constraints 15, Output 15, Validation 10.
- The section parser credits "substance" (>= 12 words) for both supported label forms:
  ```
  INTENT:
  <body text on the next line>

  INTENT: body text on the same line
  ```
  Standalone labels and inline-labelled sections score equivalently when their bodies have the same
  substance. If a "fully labelled prompt should score ~100" test fails, inspect body length and
  component wording before filing a scoring bug.
- Useful baselines: `Write a marketing plan for my company.` → 8/100 "Unstructured prompt";
  six standalone labels with >=12-word bodies → 100/100 "Fully structured Gaiish";
  "Convert to Gaiish" skeleton → 90/100.

## Prompt Builder (`/tools/prompt-builder`)
- Field ids are `builder-intent`, `builder-context`, `builder-audience`, `builder-role`,
  `builder-knowledge`, `builder-instructions`, `builder-constraints`, `builder-output`,
  `builder-tone`, `builder-validation`. localStorage key: `gaiish-prompt-builder`.
- "Save locally" persists across reloads; the status paragraph is `role="status" aria-live="polite"`.
- Prove clipboard for real by clicking Copy Prompt then pasting (ctrl+v) into the Analyzer textarea —
  do not assert on the status text alone.

## Mobile / responsive
- Resize the Chrome window rather than relying on devtools emulation; verify actual width with
  `innerWidth` in the console. A ~373px CSS width is close enough to the 390px target.
- Overflow check per page:
  `document.documentElement.scrollWidth > document.documentElement.clientWidth + 2`.
  The home "Three Kinds of Language" table lives in a scrollable wrapper, so the *table* being wider
  than its wrapper is by design — only the document-level measure matters.
- Known risk areas to re-check after CSS changes:
  - Mobile nav submenus (`.nav-sub`) may be `display:none` at mobile widths, making all sub-links
    unreachable; tapping a top-level item just navigates. Check
    `[...document.querySelectorAll('.nav-sub')].map(e => getComputedStyle(e).display)`.
  - The six framework cards (`ol[aria-label^="The Gaiish framework"]`, on `/`, `/learn-gaiish`,
    `/gaiish-method`) can clip long titles. Compare `scrollWidth` vs `clientWidth` of the title element
    per card — Instruction/Constraints/Validation are the ones that overflow.

## Accessibility quick checks (console one-liners)
- Label association: `[...document.querySelectorAll('form input,form textarea')].map(f => [f.id, f.labels[0]?.getAttribute('for')])`.
- Status regions: `[...document.querySelectorAll('[role=status],[aria-live]')]`.
- Headings: `[...document.querySelectorAll('h1,h2,h3')].map(e => e.tagName + e.textContent)` (expect exactly one h1).
- Contrast scripts that walk up for `backgroundColor` produce a bogus 1.0 ratio on the hero, because the
  hero background is a gradient (`background-image`). Verify the hero visually instead.

## Metadata / infra (shell, no browser needed)
- `curl -s https://gaiish.com/<route> | grep -E '<title>|description|canonical|og:'`.
- `robots.txt` should reference `https://gaiish.com/sitemap.xml`; sitemap has ~58 URLs, no trailing slashes.
- Documented redirects return 308: `/prompt-builder`, `/prompt-analyzer`, `/specification`, `/method`,
  `/basic`, `/pro`, `/learn`, `/glossary`.
