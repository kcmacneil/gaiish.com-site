# gaiish.com-site

The gaiish.com site. gaiish is a language humans use to optimise communication with generative AI models. The front page is the brand map itself: every element on the image is a hotspot that pops a summary panel in place, linking on to the full page behind it. Static site hosted on Vercel (project `gaiish-com-site`, domains gaiish.com and www.gaiish.com).

## Files

- `index.html` — front page: the brand map with pop-in panels
- `map.js` — opens the pop-in panels (the only script on the site)
- `generative-ai.html` — generative AI intro, technology cards and the language model table
- `principles/*.html` — the five gaiish principles (clarity, context, intent, precision, result) with prompt examples
- `outcomes/*.html` — the four gaiish outcomes (communicate, collaborate, optimize, empower) with worked examples
- `topics/*.html` — detail pages (transformers, diffusion, multimodal, embeddings & RAG, fine-tuning, agents)
- `assets/hero.jpg` — hero image
- `assets/brand/` — brand reference image and alternate renders used as templates for new imagery
- `styles.css` — styling
- `vercel.json` — Vercel config (clean URLs)

## Local preview

```bash
python3 -m http.server 8000
# open http://localhost:8000
```

## Deploy

Connect this repository to Vercel (Add New → Project → import `gaiish.com-site`), or from the CLI:

```bash
npx vercel        # preview deployment
npx vercel --prod # production deployment
```


