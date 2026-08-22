# devFirstVercel

A basic static website hosted on Vercel.

## Files

- `index.html` — the page
- `styles.css` — styling
- `vercel.json` — Vercel config (static build, clean URLs)

## Local preview

```bash
python3 -m http.server 8000
# open http://localhost:8000
```

## Deploy

Connect this repository to Vercel (Add New → Project → import `devFirstVercel`), or from the CLI:

```bash
npx vercel        # preview deployment
npx vercel --prod # production deployment
```
