# GamblingLawyers.com — Seed CMS CSVs

Five import-ready CSV files for the launch build. Reference data (jurisdictions, practice areas) plus real verified firm data sourced from Chambers and Partners, Legal 500, IMGL and firm websites.

## Files

1. `jurisdictions.csv` — 35 jurisdictions from the master brief
2. `practice_areas.csv` — 20 practice areas from the master brief
3. `law_firms.csv` — 115 verified specialist gambling law firms across the top 10 markets
4. `lawyers.csv` — empty; individual lawyer profiles to be populated
5. `articles.csv` — empty; editorial content to be populated

## Conventions

- **Encoding:** UTF-8. All files use a header row.
- **Separator:** Comma. Fields containing commas, quotes or newlines are wrapped in double quotes with internal double quotes doubled (`""`).
- **Multi-value fields:** Semicolon-separated inside a single quoted field. Example: `"malta;united-kingdom;germany"`.
- **Foreign keys:** CSVs reference one another by `slug` (not by numeric ID). This lets the import stay stable across rebuilds.
  - `law_firms.jurisdictions` → `jurisdictions.slug`
  - `law_firms.practice_areas` → `practice_areas.slug`
  - `law_firms.key_lawyer_slugs` → `lawyers.slug`
  - `lawyers.firm_slug` → `law_firms.slug`
  - `lawyers.jurisdictions` → `jurisdictions.slug`
  - `lawyers.practice_areas` → `practice_areas.slug`
  - `articles.related_jurisdictions` → `jurisdictions.slug`
  - `articles.related_firms` → `law_firms.slug`
  - `articles.related_lawyers` → `lawyers.slug`
- **Booleans:** `true` or `false` (lowercase).
- **Dates:** ISO 8601 (`YYYY-MM-DD`).
- **Status:** `draft`, `published` or `archived`.

## Suggested import order

1. `jurisdictions.csv`
2. `practice_areas.csv`
3. `law_firms.csv`
4. `lawyers.csv` (depends on firms)
5. `articles.csv` (depends on all of the above)

## Firm data provenance

Every row in `law_firms.csv` has a `sources` field containing two or more public URLs — typically a Chambers and Partners or Legal 500 gaming ranking plus the firm's own gambling practice page. Firms were included only where they are ranked, listed as IMGL members, or maintain a dedicated gambling/gaming/betting practice page on their website.

The `jurisdictions` column is tight: a firm is listed under a country only if it has an office in that country. Cross-border advisory reach is not encoded in the jurisdiction slugs.
