# GamblingLawyers.com

Global directory and editorial intelligence portal for specialist gambling and iGaming counsel.

## What this is

A single-page application delivering:

- A curated, verified directory of specialist gambling law firms (115 firms across 17 jurisdictions at launch)
- Jurisdiction landing pages for the regulated gambling markets we cover
- Practice area landing pages for the work specialist counsel handle
- Editorial analysis of licensing, regulatory and enforcement developments
- Confidential introduction workflow for clients seeking counsel
- Listing workflow for firms seeking inclusion

The entire public site is a single self-contained `index.html` — no build step, no backend, no external runtime dependencies. Data is embedded as JSON inside the file.

## Structure

```
index.html                  # the site (single-file SPA, hash-based router)
vercel.json                 # Vercel deployment config (headers, URL rules)
seed_csvs/                  # source data used to regenerate index.html
  README.md
  jurisdictions.csv
  practice_areas.csv
  law_firms.csv             # 115 verified firms with provenance
  lawyers.csv
  articles.csv              # 5 editorial pieces at launch
0*.md                       # editorial planning notes (not deployed)
```

`.vercelignore` keeps the planning docs, seed data and internal tooling out of the deployed bundle.

## Local preview

No build required. Serve the folder with any static server:

```sh
# Python
python3 -m http.server 8000

# Node
npx serve .
```

Then open <http://localhost:8000>.

## Deployment

Deploys to Vercel as a static site. `main` is the production branch. Any push to `main` triggers a production deployment; pull-request branches get preview URLs automatically.

## Editorial policy

- Every firm on the directory has been assessed against verification criteria before listing (Chambers, Legal 500, IMGL, firm websites).
- A firm appears under a jurisdiction only where it has a physical office in that country.
- Editorial content is analytical commentary on public regulatory developments; it is not legal advice.

## Contact

Editorial and partnerships: <info@gamblinglawyers.com>
