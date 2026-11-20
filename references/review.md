# Review: critique, audit and the AI-look tells

A review finds things and offers them. It never fixes anything by itself. Every finding ends as a decision card (see `choices.md`).

## Contents
1. How a review runs
2. The critique score (/40)
3. Severity
4. Personas and cognitive load
5. The technical audit (/20)
6. The AI-look tells
7. Quality-floor checklist
8. Worst-case data
9. Motion review
10. The report and the questions
11. Brand, pack, illustration and graphic pieces

---

## 1. How a review runs

1. **Capture first.** Take screenshots at 390 and 1440, in every language (and dark mode if it exists), with `scripts/shoot.mjs --full`. Judge the screenshots, not the code: you will read your own intentions into code.
2. **Scan.** Run `scripts/design_scan.py`, then `scripts/glyph_check.py --scan` if there are fonts, and `scripts/contrast.py` for any colour pair in doubt.
3. **Critique** (section 2) and **audit** (section 5), with the tells (section 6) and the checklist (section 7).
4. **Verify every finding before offering it.** Critiques have been wrong before: centred flex-wrap was fine, and `alt=""` on a decorative image is correct. A defect on one page is usually systemic, so when asked to check everything, check every page, not a sample.
5. **Report, then ask** (section 10). Be bounded: one batched inspection, one round of picked fixes, one confirming capture. Don't loop on your own.

## 2. The critique score (/40)

This is the score used in earlier reviews (26/40, then 28/40), so keep it comparable. Score Nielsen's ten heuristics from 0 to 4 each. 4 means genuinely excellent; most real interfaces land between 20 and 32.

| # | Heuristic | 0 | 4 | Look for |
|---|---|---|---|---|
| 1 | Visibility of system status | no feedback, guessing | every action confirms, progress visible | loaders, save/delete confirmation, where am I, inline validation |
| 2 | Match with the real world | jargon | the user's own words | trade words, logical order, recognisable icons, their language |
| 3 | User control and freedom | trapped | undo, cancel, back everywhere | undo, cancel on forms and dialogs, clear filters, a way home |
| 4 | Consistency and standards | stitched-together | predictable | same word and same result for the same thing, platform conventions |
| 5 | Error prevention | no guardrails | errors nearly impossible | constrained inputs, confirm or undo destructive actions, defaults |
| 6 | Recognition over recall | memorise everything | everything visible | visible options, labelled icons, recent items |
| 7 | Flexibility and efficiency | one rigid path | shortcuts for experts | shortcuts, bulk actions, favourites, fewer taps per item |
| 8 | Aesthetic and minimalist design | everything competes | every element earns its place | clear hierarchy, purposeful colour, only what's needed |
| 9 | Error recovery | cryptic codes | says what and how to fix, keeps work | plain language, near the field, form not wiped |
| 10 | Help and documentation | none | the right hint at the right moment | contextual help, empty states that teach |

**Bands:** 36 to 40 excellent · 28 to 35 good · 20 to 27 acceptable · 12 to 19 poor · 0 to 11 critical.
**Not applicable:** on a landing page or portfolio, heuristics 7 and 10 may be n/a (give a one-line reason). Then score out of 4 × the number scored (e.g. 24/32 = 75%), read the band by percentage (90/70/50/30%), and never print /40 over a partial set.

Alongside the number, give two plain verdicts:
- **Specific or interchangeable?** "Authored for this product, or could a competitor's logo sit on it?" Cover the logo and check.
- **What a stranger gets in 5 seconds:** what it is, who it's for, what to do next.

Things that cap the design quality, whatever the heuristic score (say them plainly): a 3+ line headline, unequal outer margins, two or more near-empty screens, small grey text, placeholder or invented content, a blank band from a failed reveal, no real first-screen action on a page whose job is an action.

## 3. Severity

| Level | Meaning | When |
|---|---|---|
| P0 blocking | stops the task | now |
| P1 major | real difficulty, or a WCAG AA failure | before release |
| P2 minor | a workaround exists | next pass |
| P3 polish | no real user impact | if wanted |

Tie-break: "would someone contact support about this?" If yes, it's at least P1. Not everything can be P0.

## 4. Personas and cognitive load

Walk 2 or 3 of these through the real screens. Report what broke for them, not the profile.

| Persona | Tests |
|---|---|
| Expert (a cashier at hour six) | core task in seconds, taps per item, shortcuts, bulk actions, no animation in the way |
| First-timer | first action obvious in 5 seconds, labelled icons, back/undo everywhere |
| Accessibility | keyboard only, visible focus, alt text, 4.5:1, state changes announced, 200% zoom |
| Stress tester | 0 and 1,000 items, long Kurdish names, emoji, paste, refresh mid-flow, offline |
| Phone user | thumb zone, 44/48px targets, interruptions, slow network, the keyboard open |

Landing pages: first-timer, stress tester, phone. Tills and dashboards: expert, accessibility. Checkout and forms: phone, stress tester, first-timer.

**Cognitive load:** one focus per screen, chunks of 4 or fewer, clear grouping and hierarchy, one decision at a time, 4 or fewer visible options per decision, nothing to remember across screens, advanced things one level deeper. 0 to 1 failures is low load, 2 to 3 moderate, 4+ high.

## 5. The technical audit (/20)

Five dimensions, 0 to 4 each (18 to 20 excellent, 14 to 17 good, 10 to 13 acceptable, 6 to 9 poor, below 6 critical):
1. **Accessibility:** contrast, focus visibility and order, semantic HTML (headings, landmarks, buttons not divs), labels and errors on forms, alt text, reduced motion.
2. **Performance:** LCP under 2.5s, INP under 200ms, CLS under 0.1; images sized and lazy; fonts subset and preloaded wisely; no animated layout properties; long lists virtualised.
3. **Theming:** tokens instead of hard-coded colours, dark mode designed (not inverted), values that update on theme switch.
4. **Responsive:** no sideways scroll at 320 to 390, targets 44px (web) / 48dp (apps), no hover-only functions, real layouts per size (not squeezed), Kurdish strings fit.
5. **Integrity:** the work is what it claims (no fake proof, no decorative "UI"), consistent with DESIGN.md, and not a stitched kit.

Native apps (Flutter): replace 4 with **platform fit**: real platform navigation and back behaviour, insets, platform controls, text scaling.

## 6. The AI-look tells

A tell is a default nobody chose, not a banned look. If the brand owns it (the client's purple, the client's Montserrat), it's a decision: mark the line `dx-ignore` and move on.

**Wave 1 (2023 to 2024):** violet/indigo primary, purple-to-blue gradients, gradient text, a glowing "Get started", a grey shadow under every card, three icon-in-a-rounded-square feature cards, emoji as icons, glassmorphism as decoration.
**Wave 2 (2025):** a tracked-caps eyebrow label above every heading, a pill badge over the hero ("New"), one headline word in italic serif or another colour, bento tiles everywhere, near-black with neon glow, a floating blurred pill nav, a fake grey-bar dashboard, pulsing status dots, fade-and-rise on every section.
**Wave 3 (2025 to 2026), the fix that became the look:** cream or beige ground with a high-contrast serif display and a terracotta/clay accent (Anthropic's own palette: #F4F1EA, #D97757); a serif display as the shortcut to "premium"; oversized italic serif headlines; "broadsheet cosplay" (hairlines, zero radius, dense newspaper columns); fake-editorial labels ("Field notes"); meta strings joined with middle dots; a "→" on every link.
**Structural tells:** the centred hero, then three icon cards, then testimonials, then a CTA band; one 12 to 16px radius on everything; nine near-equal type sizes; more than 70% of text centred; 01/02/03 numbering on things that aren't a sequence; untouched shadcn/Tailwind defaults (slate cards, `--radius: 0.5rem`, Inter/Geist); Flutter's template `Colors.deepPurple`; the hero-metric template (big number, small label, three stats); stock illustrations; device mockups instead of the real product.
**Copy tells:** elevate, unleash, unlock, supercharge, seamless, empower, effortless, reimagine, cutting-edge, world-class, "take your X to the next level", "not just X, it's Y", "Fast. Simple. Secure.", "Welcome to", "Learn more" / "Get started" as the only CTAs, invented testimonials, user counts or ratings, and an em dash in every other sentence.

**Removal is not enough.** A page stripped of tells with nothing added is "an empty page with good manners". Each removal needs a replacement option grown from the subject: the idea, scale, real content, real photos, a colour field.

## 7. Quality-floor checklist

**Accessibility:** icon-only buttons have `aria-label`; form controls have labels; `<button>` for actions and `<a>` for navigation; images have `alt` (or `alt=""` if decorative); headings in order; a skip link on nav-heavy pages; async updates use `aria-live="polite"`; colour is never the only signal.
**Focus:** visible `:focus-visible` on everything interactive; never `outline: none` without a replacement; sticky bars never cover the focused element (`scroll-padding`).
**Forms:** `autocomplete`, the right `type` and `inputmode`; paste allowed; 16px inputs on phones; errors inline beside the field, first error focused on submit; the submit button stays enabled until the request starts, then shows progress; warn before leaving with unsaved changes.
**Touch:** targets 44px web / 48dp apps (POS: bigger); `touch-action: manipulation`; `overscroll-behavior: contain` in sheets and modals; `:hover` rules inside `@media (hover: hover) and (pointer: fine)`; no hover-only actions.
**Content:** text containers handle long content (`min-width: 0`, `overflow-wrap: anywhere` for emails and URLs, `line-clamp` for previews); empty states; never truncate numbers, amounts or dates.
**Images:** explicit width and height (or aspect-ratio); `loading="lazy"` below the fold; priority on the hero image only.
**Typography:** `…` not `...`, curly quotes, a non-breaking space between number and unit, `tabular-nums` for prices and totals, `text-wrap: balance` on headings.
**Theme:** `color-scheme` on `<html>`, `<meta name="theme-color">` matching the header, styled native `<select>` in dark mode, and themed browser surfaces (selection colour, caret, focus ring, underline offset).
**Navigation and state:** the URL reflects filters, tabs and pages; destructive actions get undo or a confirmation that names the object; links are real links (Ctrl+click works).
**i18n:** `Intl` for dates, numbers and currency (with `numberingSystem` set on purpose); plurals through a library; whole translatable sentences, never glued fragments (Kurdish word order differs); `translate="no"` on brand names.
**Never:** `user-scalable=no` or `maximum-scale=1`, `transition: all`, click handlers on divs, animated GIFs where a video would do.

## 8. Worst-case data

Test with plausible worst cases, not "aaaa". For example: `نور الهدى عبد الرحمن`, a Kurdish name of 40 characters, `bartholomew.fitzgerald@northwind-holdings.example.com`, a one-letter name, no avatar, 0 / 1 / 1,284 / 1,000,000 items, a price of 12,345,000 IQD, "1 members", an empty list, a translated badge twice as long, 200% zoom, 320px width, dark mode, and the right-to-left version. Fix with `min-width: 0`, `flex-shrink: 0` on icons and actions, `Intl.PluralRules`, `Intl.NumberFormat`, and wrap/truncate/clamp chosen per field (never truncate numbers).

## 9. Motion review

Flag: `transition: all`; entering from `scale(0)` or a pure fade with no other change; ease-in on UI; animation on keyboard actions or anything used 100+ times a day; UI motion over 300ms without a reason; popovers growing from the centre instead of their trigger; keyframes on toasts or toggles; animated width/height/top/left/margin; no reduced-motion handling; ungated `:hover`; everything entering at once where a stagger belongs, or a stagger where nothing should move. Prefer fixes in this order: delete it, reduce it, fix the easing, fix the origin, make it interruptible, move it to transform/opacity. See `motion.md`.

## 10. The report and the questions

Write the report first, then ask. A structured question can hide text written alongside it, so the question comes last and every option carries its own explanation.

```
Review: <surface>, <date>
Score: 28/40 (good). Audit: 15/20.
Specific or interchangeable: <one line>
5-second test: <what a stranger gets>
What's working: <2-3 items, with why>
Top issues:
  [P1] <what> / <why it matters> / <the screenshot>
  [P2] ...
Not checked: <a real phone, Safari, print colour, ...>
```

Then the decision cards:
- **Priority first:** "Which should we tackle first?" with the top 2 to 4 issue groups as options.
- **One question per real design choice,** with 2 to 4 ways to fix it (sketch or before/after in the preview), plus "Keep as is".
- **Mechanical fixes** (alt text, focus rings, `…`) as a multiSelect checklist, one fix per option.
- Record unticked or skipped findings under Declined in DESIGN.md, and never raise them again unless asked.
- After the picked fixes, capture again and give the new score next to the old ones: "26 → 28 → 31 /40".

## 11. Brand, pack, illustration and graphic pieces

The /40 critique is for interfaces. For these pieces, walk the checklist at the end of the matching file (`identity.md` section 11, `packaging.md` section 13, `illustration.md` section 11, `graphic.md` section 10), look for these tells, and use the same severity levels (section 3) and report format (section 10):

- **Logos:** a generic object for the category (coffee bean, tooth, house roof, leaf, chef's hat, globe), a letter in a circle presented as a symbol, gradients or gloss in the master mark, three metaphors in one symbol, a mark that only works in colour, an invented "since" year, a Kurdish name set in a fallback font next to a crafted Latin wordmark.
- **Packs:** designed on a mockup and never checked on the dieline, the category default (every honey jar gets a bee and a hexagon on cream; every organic pack gets kraft and a green leaf), fake craft textures, claims without the plain product name, legal text in light grey or over a picture, a barcode squeezed into a corner, over a pattern or across a fold.
- **Illustration:** the corporate flat look (tiny heads, noodle limbs, purple people), untouched stock or library scenes, generated images with broken lettering or hands, two styles in one project.
- **Graphic pieces:** everything centred, five focal points, a stock photo under a gradient, text hidden behind the platform's own buttons, the same layout for every post in a series.
