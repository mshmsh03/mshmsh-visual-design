# mshmsh-visual-design

A Claude skill for visual design that never changes anything without asking (formerly **designa-xoshaka**). Every change (a colour, a font, a layout, a logo shape, a pack front, an accessibility fix) is offered as 2 to 4 concrete options with a preview, and only the one you pick gets applied.

It covers websites, landing pages, web apps, dashboards, Flutter and POS apps, logos and brand identities with their guidelines, packaging and labels, illustration, posters, flyers and social media posts, and printed pieces like menus, business cards and letterheads. It is built for work in English, Kurdish and Arabic, with right-to-left done properly: real Kurdish fonts, optical size matching, logical properties, mirrored layouts, digits and mixed-direction text.

It blends the best parts of design skills (impeccable, taste-skill, Emil Kowalski's design engineering, Vercel's interface guidelines, ui-ux-pro-max, unslop-ui, and for brand, packaging and illustration work, RampStack's logo and identity skills plus open packaging, poster and SVG skills) with lessons from real client projects. See the credits below.

## Install

**Claude app:** download [mshmsh-visual-design.zip](https://github.com/mshmsh03/mshmsh-visual-design/releases/download/latest/mshmsh-visual-design.zip) and upload it in your skill settings. To update, upload the new zip in place of the old one. Comparison pages, the logo sheet, the pack mockup and the scripts need Claude Code (or any computer with Node.js and Python).

**Claude Code (full version with scripts):**

```bash
npx skills add mshmsh03/mshmsh-visual-design
```

Or by hand: download this repo and put the folder at

- Windows: `C:\Users\<you>\.claude\skills\mshmsh-visual-design`
- macOS / Linux: `~/.claude/skills/mshmsh-visual-design`

Restart Claude Code, then type `/mshmsh-visual-design`, or just ask for design help ("make this landing page look less AI-made", "design a logo for my bakery", "a label for a 500 g honey jar", "an Instagram post for Friday's event", "design a bilingual menu").

**Renamed:** this skill was called `designa-xoshaka` until 2026-11-20. If you have the old one, remove it after installing this one so the two don't both load. In the Claude app, delete designa-xoshaka. In Claude Code, run `npx skills remove designa-xoshaka -g`.

## What you need

- Node.js 22 or newer and Chrome or Edge, for screenshots, comparison pages, logo sheets and pack mockups (`scripts/shoot.mjs`).
- Python 3.8 or newer for the scanners, the direction dealer and the barcode tool. `python -m pip install fonttools brotli` adds the font glyph checker.

## How it works

1. **It looks first.** It reads the project, the brand files and any `DESIGN.md`, runs the scanners and takes screenshots at phone and desktop size in each language. For brand and print work it looks for the old logo, product photos, the printer's dieline and the legal text.
2. **A short brief.** It asks only what it couldn't find: who it's for, the first thing they should do, the brand, the languages, the devices or print sizes, and where the work gets made (code, Canva or Figma). The answers are saved in `DESIGN.md`.
3. **Directions** (for new work and redesigns). It deals three directions that differ in structure, not just colour, and grounds each in what only this client has. Logos first differ in architecture (wordmark, letter symbol, seal...), packs in the structure of the front shown as a range, illustration in style family, posters in layout. They are built as real mockups and shown side by side in your browser, next to the current version.
4. **One decision at a time.** Every change becomes a question with 2 to 4 options. Each option has a preview, its cost, and a recommendation.
5. **Only what you pick.** The picked option is applied, re-rendered to prove it worked, and logged in `DESIGN.md`. Things you decline are remembered and never offered again.
6. **Review.** A usability score out of 40 and a technical audit out of 20 for interfaces, and domain checklists for logos, packs, illustration and graphic pieces, with every finding offered as a choice, never fixed silently.

Say "you decide" to hand a decision back, mix options ("A's colours with C's type"), or answer "not nice" to go back and get fresh options.

## Brand, packaging, illustration and graphic design

- **Logos and identities:** the brief ("this, not that", the competitor wall), mark architectures with a primary, compact and favicon-grade mark, Kurdish and Latin lockups designed together, drawing marks as clean SVG, a test sheet for every candidate (16 px, app icon masks, one colour, reversed, blur, print size, competitor wall), colour values in HEX, RGB, CMYK and Pantone, a guidelines document and a complete hand-off package.
- **Packaging and labels:** the converter's dieline and its layers, the front's hierarchy with shelf, arm's-length and thumbnail tests, ranges and variants, the legal information (including Iraq's Arabic labelling rules), barcodes at exact GS1 sizes, inks, white ink and finishes, Kurdish on packs, a 3D box and jar mockup, and a preflight list.
- **Illustration:** a written style sheet, ten style families, production routes (SVG in code, drawn, generated then rebuilt), characters, local motifs and patterns, and rules for generated images.
- **Graphic pieces:** one message and three reading levels, grids and mirrored reading paths, type sizes for distance and phones, current social sizes and safe zones (including Instagram's 3:4 grid), templates and series, and making it in code, Canva or Figma.
- **Free resources:** a vetted list of free tools, fonts, icons, illustration and photo sources with their licences, packaging tools, references and learning resources (`references/resources.md`).

## Kurdish fonts that really work

Google's "Arabic" label doesn't mean a font can write Kurdish. Thirty-five Arabic-script Google Fonts were checked against every Sorani letter. Many popular ones fail: Cairo, Almarai, Alexandria, Changa, El Messiri, Lalezar, Lemonada, Markazi Text, Rakkas and Rubik lack ڕ ڵ ە ۆ ێ, and Readex Pro and Tajawal lack even پ چ ژ ک گ ی. The skill only offers fonts that pass, and its scanner flags the others. The full list is in `references/catalogs.md`.

## Tested

The interface workflow was tested against plain Claude with skill-creator's method (October 2026): four tasks, a simulated user who always takes the recommended option, and an independent grader reading every diff.

- **Tasks:** a redesign of an AI-looking English/Kurdish cafe site, a Flutter POS checkout polish, a "fix the buttons" request, and a bilingual business card for print.
- **Asking first:** with the skill, every change was asked first, and the grader found no unasked changes in any task. When changing existing work, plain Claude made 8 to 13 changes per task that nobody had asked for.
- **Checks passed:** 95% with the skill, 67% without.
- **Cost:** about twice the time and tokens, because every option is built as a real preview.
- **Triggering:** across 120 trigger checks, design requests went to this skill 59 times out of 60, and none of the 60 unrelated requests did.

The brand, packaging, illustration and graphic additions (November 2026) were checked tool by tool: 28 barcodes from `ean13.py` (random numbers at 80, 100 and 150%) all decoded back to the right number with a barcode reader; the dealer deals from all seven kinds with no duplicate ids; the logo sheet and pack mockup were rendered and inspected. Four new test tasks are in `evals/evals.json`, and `python tests/run.py` (run by GitHub on every push) checks the references, the dealer, the barcode tool and the preview pages.

## What is in this folder

| Path | What it is |
| --- | --- |
| `SKILL.md` | The workflow and the one rule |
| `references/choices.md` | How every change is asked: options, previews, comparison pages, reading answers |
| `references/directions.md` | Making options that really differ: inventory, dealing, option cards, ruts to avoid |
| `references/craft.md` | Type, colour, layout, surfaces, imagery, words, states, app screens, persuasive pages |
| `references/motion.md` | When to animate, easing and durations, recipes, Flutter, option sets |
| `references/review.md` | The /40 critique, the /20 audit, AI-look tells (including logos, packs, illustration and posters), the quality checklist |
| `references/rtl-kurdish-arabic.md` | Fonts, sizing, mirroring, numbers, Word and PDF traps, Flutter locales |
| `references/stacks.md` | Where decisions live in Next.js + Tailwind + shadcn, plain HTML and Flutter |
| `references/print.md` | Bleed, sizes, type on paper, building and checking print files, Canva exports |
| `references/identity.md` | Logos and brand identities: brief, architectures, bilingual lockups, tests, colour values, guidelines, hand-off |
| `references/packaging.md` | Boxes, labels and pouches: dielines, the front, ranges, legal information, barcodes, inks, finishes, preflight |
| `references/illustration.md` | Style sheets, style families, SVG craft, characters, patterns, generated images |
| `references/graphic.md` | Posters, flyers, social posts and ads: hierarchy, type for distance, sizes, safe zones, templates |
| `references/resources.md` | Free tools, fonts, icons, assets with licences, packaging tools, references, learning |
| `references/catalogs.md` | Style families, palettes by trade, type pairings, Arabic-script fonts, page patterns |
| `scripts/design_scan.py` | Finds right-to-left mistakes, quality-floor misses and AI-look tells |
| `scripts/glyph_check.py` | Finds characters a font can't draw (boxes) |
| `scripts/contrast.py` | WCAG contrast ratios |
| `scripts/shoot.mjs` | Screenshots at any size (phone, desktop, social posts), full page, dark mode, right-to-left, CSS previews, element close-ups, and PDFs for print |
| `scripts/deal.py` | Deals design directions at random (pages, apps, print, identities, packs, illustration, graphic pieces) so options aren't the usual default |
| `scripts/ean13.py` | Checks a GTIN's check digit and draws its EAN-13 barcode at exact GS1 size |
| `assets/compare.html` | The side-by-side comparison page |
| `assets/logo-sheet.html` | Every logo test on one sheet |
| `assets/pack-mockup.html` | A 3D box and jar mockup from flat panel artwork |
| `assets/DESIGN-template.md` | The design contract every project gets |
| `evals/` | Test tasks for the skill |
| `tests/` | `run.py` and its fixtures: the checks GitHub runs on every push |
| `CHANGELOG.md` | What changed in each version |

## Credits

See [THIRD-PARTY-NOTICES.md](THIRD-PARTY-NOTICES.md) for the projects this skill learned from and their licences.

## Licence

MIT. See [LICENSE](LICENSE).
