# designa-xoshaka

A Claude skill for design that never changes anything without asking. Every change (a colour, a font, a layout, a button corner, an accessibility fix) is offered as 2 to 4 concrete options with a preview, and only the one you pick gets applied.

It covers websites, landing pages, web apps, dashboards, Flutter and POS apps, and printed pieces like menus, business cards and letterheads. It is built for work in English, Kurdish and Arabic, with right-to-left done properly: real Kurdish fonts, optical size matching, logical properties, mirrored layouts, digits and mixed-direction text.

It blends the best parts of six design skills (impeccable, taste-skill, Emil Kowalski's design engineering, Vercel's interface guidelines, ui-ux-pro-max and unslop-ui) with lessons from real client projects.

## Install

**Claude Code (recommended, full version with scripts)**

```bash
npx skills add mshmsh03/designa-xoshaka
```

Or by hand: download this repo and put the folder at

- Windows: `C:\Users\<you>\.claude\skills\designa-xoshaka`
- macOS / Linux: `~/.claude/skills/designa-xoshaka`

Restart Claude Code, then type `/designa-xoshaka`, or just ask for design help ("make this landing page look less AI-made", "polish the checkout screen", "design a bilingual menu").

**Claude app:** zip the folder and upload it in the app's skills settings. Comparison pages and the scripts need Claude Code (or any computer with Node.js and Python).

## What you need

- Node.js 22 or newer and Chrome or Edge, for screenshots and comparison pages (`scripts/shoot.mjs`).
- Python 3.8 or newer for the scanners. `python -m pip install fonttools brotli` adds the font glyph checker.

## How it works

1. **It looks first.** It reads the project, the brand files and any `DESIGN.md`, runs the scanners and takes screenshots at phone and desktop size in each language.
2. **A short brief.** It asks only what it couldn't find: who it's for, the first thing they should do, the brand, the languages, the devices. The answers are saved in `DESIGN.md`.
3. **Directions** (for new work and redesigns). It deals three directions that differ in structure, not just colour, and grounds each in what only this client has. They are built as real mockups and shown side by side in your browser, next to the current version.
4. **One decision at a time.** Every change becomes a question with 2 to 4 options. Each option has a preview, its cost, and a recommendation. Small changes get a sketch or code preview inside the question; big visual ones get a comparison page.
5. **Only what you pick.** The picked option is applied, re-rendered to prove it worked, and logged in `DESIGN.md`. Things you decline are remembered and never offered again.
6. **Review.** A usability score out of 40 (the same scale as earlier critiques) and a technical audit out of 20, with every finding offered as a choice, never fixed silently.

Say "you decide" to hand a decision back, mix options ("A's colours with C's type"), or answer "not nice" to go back and get fresh options.

## Kurdish fonts that really work

Google's "Arabic" label doesn't mean a font can write Kurdish. Thirty-five Arabic-script Google Fonts were checked against every Sorani letter. Many popular ones fail: Cairo, Almarai, Alexandria, Changa, El Messiri, Lalezar, Lemonada, Markazi Text, Rakkas and Rubik lack ڕ ڵ ە ۆ ێ, and Readex Pro and Tajawal lack even پ چ ژ ک گ ی. The skill only offers fonts that pass, and its scanner flags the others. The full list is in `references/catalogs.md`.

## Tested

The skill was tested against plain Claude with skill-creator's method: four tasks, a simulated user who always takes the recommended option, and an independent grader reading every diff.

- **Tasks:** a redesign of an AI-looking English/Kurdish cafe site, a Flutter POS checkout polish, a "fix the buttons" request, and a bilingual business card for print.
- **Asking first:** with the skill, every change was asked first, and the grader found no unasked changes in any task. When changing existing work, plain Claude made 8 to 13 changes per task that nobody had asked for.
- **Checks passed:** 95% with the skill, 67% without.
- **Cost:** about twice the time and tokens, because every option is built as a real preview.
- **Triggering:** across 120 trigger checks, design requests went to this skill 59 times out of 60, and none of the 60 unrelated requests (bugs, video, wallpapers, charts, security, letters) did.

## What is in this folder

| Path | What it is |
| --- | --- |
| `SKILL.md` | The workflow and the one rule |
| `references/choices.md` | How every change is asked: options, previews, comparison pages, reading answers |
| `references/directions.md` | Making options that really differ: inventory, dealing, option cards, ruts to avoid |
| `references/craft.md` | Type, colour, layout, surfaces, imagery, words, states, app screens, persuasive pages |
| `references/motion.md` | When to animate, easing and durations, recipes, Flutter, option sets |
| `references/review.md` | The /40 critique, the /20 audit, AI-look tells, the quality checklist |
| `references/rtl-kurdish-arabic.md` | Fonts, sizing, mirroring, numbers, Word and PDF traps, Flutter locales |
| `references/stacks.md` | Where decisions live in Next.js + Tailwind + shadcn, plain HTML and Flutter |
| `references/print.md` | Bleed, sizes, type on paper, building and checking print files |
| `references/catalogs.md` | Style families, palettes by trade, type pairings, Arabic-script fonts, page patterns |
| `scripts/design_scan.py` | Finds right-to-left mistakes, quality-floor misses and AI-look tells |
| `scripts/glyph_check.py` | Finds characters a font can't draw (boxes) |
| `scripts/contrast.py` | WCAG contrast ratios |
| `scripts/shoot.mjs` | Phone and desktop screenshots, full page, dark mode, right-to-left, CSS previews, element close-ups, and PDFs for print at their CSS page size |
| `scripts/deal.py` | Deals design directions at random so options aren't the usual default |
| `assets/compare.html` | The side-by-side comparison page |
| `assets/DESIGN-template.md` | The design contract every project gets |

## Credits

See [THIRD-PARTY-NOTICES.md](THIRD-PARTY-NOTICES.md) for the projects this skill learned from and their licences.

## Licence

MIT. See [LICENSE](LICENSE).
