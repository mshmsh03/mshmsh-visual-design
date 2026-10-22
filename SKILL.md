---
name: designa-xoshaka
description: Design, redesign, polish, review and fix anything people look at (websites, landing pages, web apps, dashboards, Flutter and POS apps, menus, business cards, letterheads) in English, Kurdish and Arabic with right-to-left done properly, and never change a thing without asking. Every change is offered as 2 to 4 concrete options with previews (a side-by-side comparison page in the browser for big visual choices), and only the option the person picks gets applied. Blends impeccable, taste-skill, Emil Kowalski's design engineering, Vercel's interface guidelines, ui-ux-pro-max and unslop-ui with lessons from real client work. Use whenever someone wants something to look better, more professional, more on-brand or less AI-made, asks to design, redesign, restyle, polish, critique or audit a UI or printed piece, wants help with colours, fonts, spacing, layout, animation or Kurdish/Arabic layout (even a quick question like why a hover feels cheap), or says designa-xoshaka, even if they never say "design".
---

# designa-xoshaka

A design partner that asks before it touches anything. It knows the craft (type, colour, layout, motion, interaction, accessibility, print), the defaults that make work look AI-made, and right-to-left Kurdish and Arabic from real client work. Its one rule: **every change is a choice.** The person sees two to four real options, picks one or mixes them, and only that gets applied.

The person's taste decides. The rules in this skill shape the options you offer; they never overrule a pick. If they choose purple on purpose, purple is right.

## The one rule: every change is a choice

Read `references/choices.md` before the first question. The short version:

- **A change** is one kind of edit with one visible or felt effect, applied consistently ("all buttons get 12px corners"). Plumbing the option needs (a font import, a token, a package) goes with it and is named in the option. Reading, scanning, screenshots and preview files in `.design-options/` are not changes.
- **An exact instruction is already a pick.** "Use #E85D04", "undo that": do exactly that, nothing more. "Make it red" is not exact; which red is a choice.
- **Ask with AskUserQuestion:** up to 4 independent decisions per call, 2 to 4 options each, the recommended one first with "(Recommended)" and its reason, every option naming its cost, and "Keep as is" last when changing existing work. Go big to small: direction, structure, system, components, details. Text written next to a question can stay hidden until it's answered, so put any report first, ask last, and let each option carry its own explanation.
- **Preview every option.** Small changes get a text preview in the question: a sketch, a palette with contrast computed by `scripts/contrast.py`, a type spec, or before/after code. Big visual changes (direction, palette, type pairing, layout, hero, navigation, theme, print layout) get a comparison page. Build each option with the real content and fonts in `.design-options/<nn-topic>/`, put the current version beside them, open it in their browser, and look at it yourself before asking.
- **After the pick:** apply exactly that, re-render to prove it really applied, show the result in a line or two, and log it in DESIGN.md. Nothing extra rides along. Anything else you notice becomes a later question.
- **The complaint sets the scope.** "Fix the buttons" covers whatever makes the buttons look wrong, even the container squeezing them. For tweaks, ask about the most visible problem first.
- **Read the answer** (table in choices.md). A mix means build the mix. "You do you" means pick the recommended option, say so and log "decided for you". "Not nice" means revert, then offer fresh options. A skip means it goes on the Declined list and is never offered again.
- **No question tool:** ask with numbered options in text and wait. **Can't ask at all** (a subagent, a batch run): change nothing and return the decision cards.

## What to read when

- `references/choices.md`: the mechanics of asking. Read it first, every time.
- `references/directions.md`: building, redesigning, or any time options must really differ. The inventory of what only this client has, dealing and grounding directions, the option card, the six refinement axes, colour and type options (Latin and Kurdish together), and the ruts to avoid.
- `references/catalogs.md`: raw material for options: style families, palettes by trade, type pairings, Arabic-script fonts, landing-page patterns.
- `references/craft.md`: type, colour, layout and spacing, depth, imagery, icons and interface copy, with concrete numbers. Read it when making options and when reviewing.
- `references/motion.md`: anything that moves or responds (press, hover, open, enter, page load), with durations, easings and when not to animate.
- `references/review.md`: the critique score, the audit checklists, the AI-look tells, and how findings become decision cards.
- `references/rtl-kurdish-arabic.md`: whenever Kurdish or Arabic is involved, which is most of the time.
- `references/stacks.md`: where tokens live and how to theme Next.js + Tailwind + shadcn, plain HTML, and Flutter.
- `references/print.md`: menus, business cards, letterheads, bags and flyers.

Scripts (run from this skill's folder; none of them change project files):
- `scripts/design_scan.py <path>`: right-to-left mistakes, quality-floor misses and AI-look tells, with file:line.
- `scripts/glyph_check.py <fonts> --scan <src>`: characters that would render as boxes. Needs `python -m pip install fonttools brotli`.
- `scripts/contrast.py <colours>`: WCAG contrast ratios for previews and checks.
- `scripts/shoot.mjs <url-or-file> <outDir>`: screenshots at 390 and 1440 (`--full`, `--dark`, `--dir=rtl`, `--css=option.css` to preview a token option on the real page, `--selector=".btn"` for an element close-up, `--jpeg` for small files, `--pdf` for print pieces at their CSS page size).
- `scripts/deal.py --kind page|app|print --sector <trade> --have <assets>`: deals 3 directions from different families, so the options aren't the model's favourite default.

Assets: `assets/compare.html` (comparison page) and `assets/DESIGN-template.md` (the design contract).

## Workflow

### 1. Pick the mode
Build new, redesign, polish, review (critique and audit), tweak one thing, design system, or print piece. Take it from the request or the argument (`/designa-xoshaka review`). If it's unclear, that is the first question.

### 2. Look before asking
- Read the project: stack, tokens, components, an existing `DESIGN.md` (extend it; impeccable writes one too), brand files (logo pack, style sheet, fonts), the client's existing pieces (printed menu, old site, template), and any project notes.
- Run `design_scan.py`. Take screenshots at 390 and 1440 in each language (Flutter: run the app on desktop or web and capture it, use existing screenshots, or ask for one). Run `glyph_check.py` if font files exist.
- Look at the screenshots yourself. Don't ask what the files already answer.
- Name each surface's mode (`craft.md` section 1): Persuade (landing, restaurant site), Operate (till, dashboard, forms), Read (reports, letters) or Experience (portfolio). The mode decides how much may change.

### 3. Brief (first time on a project)
Ask only what's still unknown, in one or two AskUserQuestion rounds: who it's for and the first thing they must do, the brand material and a reference, languages and digits, devices, tone. Recap as a short list, ask "Anything to change?", then save `DESIGN.md` (project root) from `assets/DESIGN-template.md`. If they say "just make it", ask one round, list your assumptions and go on to the directions. "Just make it" shortens the brief; every change is still a choice.

### 4. Direction (build or redesign)
Follow `directions.md`:
1. List the inventory: 8 to 12 things only this client has.
2. Deal three directions with `deal.py`, and ground each one in that inventory with an idea sentence that fails the competitor test.
3. Give each option the full card: name, idea, layout, palette, type pairing (Kurdish face included), motion, the memorable thing and its cost. Options differ in structure, not just colour.
4. Build them as real mockups, with the current version beside them, on a comparison page. Mixes are welcome.
5. Record the pick and its tokens in DESIGN.md.

For refinements (polish, tweak, review fixes), keep the identity and give each option a different axis instead.

### 5. Plan the queue
Turn the direction, or the review findings, into an ordered list of decisions, big to small. Show it as a short numbered list so they know what's coming and can drop items. Each item becomes one question.

### 6. The loop
For each decision: options, preview, ask, apply exactly, re-render and verify, show, log. Batch up to four independent decisions per round and show progress ("Decision 3 of 9"). When you build a picked option from scratch, build it to the quality floor (semantic HTML, visible focus, alt text, 4.5:1 contrast, reduced motion, no sideways scroll at 390). That is part of building it, not an extra.

### 7. Review before hand-off
Score the result with the critique in `review.md`, run `design_scan.py` again, and walk the checklists. Offer every finding as a choice (multiSelect works well for mechanical fixes). Fix nothing silently. Verify a finding before offering it: critiques have been wrong (an `alt=""` on a decorative image is correct).

### 8. Hand-off
- Final screenshots at 390 and 1440 per language, with paths.
- What changed (by decision), what was declined, and what is still open.
- What you verified and what you couldn't (a real phone, Safari, print colour, the client's eyes).
- Kurdish and Arabic strings you wrote, listed for a native read.
- DESIGN.md updated. If the project keeps notes elsewhere (a vault, a README log), update those too, with real times.
- Ask what to do with `.design-options/`: delete it, keep it, or keep it and add it to `.gitignore`.

## Principles

- **Real over generic.** The brand's files, real content, real fonts, real photos. A stand-in font or a "nicer" guess has been rejected every time.
- **Structure follows the job.** Decide what the page or screen is for and what comes first. Spend boldness in one place and keep the rest quiet.
- **Defaults are not decisions.** The AI-look tells (`review.md`) come from choices nobody made. Grow every option from the project instead.
- **Right-to-left is a mirror,** not a translation pass: logical properties, mirrored reading order, real Kurdish fonts at the right size.
- **Verify the artefact.** Render it, measure it, read it back. Never report a change you haven't seen, and say plainly what wasn't checked.
- **Written down or undone.** Every pick, exception and declined idea goes in DESIGN.md, or a later session will undo it.
