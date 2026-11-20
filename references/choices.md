# Choices: how every change gets asked

The skill's one rule is that nothing changes until the person picks. This file is the mechanics: what counts as one change, how to make options worth choosing between, how to preview them, how to ask, and how to read the answer.

## Contents
1. What counts as one change
2. Options worth choosing between
3. Asking with AskUserQuestion
4. Text previews (small changes)
5. Comparison pages (big visual changes)
6. After the pick
7. Reading the answer
8. Without the question tool

---

## 1. What counts as one change

A change is one kind of edit with one visible or felt effect, applied consistently wherever it belongs. "All buttons get 12px corners" is one change. "Corners and colour" is two.

- **Plumbing goes with its change.** The font import for a picked font, the token variable for a picked colour, the icon package for a picked icon set: these are part of the option and named in its description ("adds the lucide-react package"). They are not separate questions and never surprises.
- **Quality-floor basics are part of building, not extras.** When you build a picked option from scratch, build it properly: semantic HTML, visible focus, alt text, 4.5:1 text contrast, reduced-motion support, no sideways scroll at 390px. When existing work is missing these, fixing them is a change and gets asked.
- **Not changes:** reading files, running the scanners, taking screenshots, and writing preview files inside `.design-options/`.
- **An exact instruction is already a pick.** "Make the button #E85D04", "undo that", "use Montserrat" — do exactly that and nothing beyond it. "Make the button red" is not exact: which red is a choice.
- **The complaint sets the scope, not the element.** Asked to fix the buttons, everything that makes the buttons look wrong is in scope, including a cramped container that squeezes them into two lines (say in the option that it touches the nav). Leaving the most visible part of their complaint unfixed because it sits one element over is a failure, not discipline. Unrelated problems you notice go on the queue ("I also noticed the menu photos have different heights; want to look at that after?"), never into the current edit.

## 2. Options worth choosing between

- **Two to four options**, each a real answer that differs on the axis being decided. Three shades of the same idea is one option asked three times.
- **Structure, not just colour.** For directions, layouts and print pieces, options differ in structure (arrangement, hierarchy, what leads), not only in palette. Colour-only variants of a layout have been rejected before with "change the design too, not just the colours".
- **Recommended first**, label ending in "(Recommended)", and the reason in its description: tied to the brief, the brand or the job of the page, not to taste in general.
- **Every description names the cost.** What it changes, what it gives up, how big the change is ("fully round is a two-value change; softer and more playful").
- **"Keep as is" last** when changing existing work and a slot is free. When all four slots carry real alternatives, they can still type "keep" in Other.
- **Grow options from the project.** The brand guide, the client's fonts, their printed menu, the logo's colours, the radius the main buttons already use, the subject's world (materials, place, vernacular). The model's favourite default is not an option. See `directions.md` for the defaults to avoid.
- **Questions of fact get no recommendation; decisions always do.** A fact is something only they know about their world: "Is the purple your brand colour?", "Do you have a logo file?", "How do customers order today?". Order those options by likelihood, mark none as recommended, and say what you'll assume if they skip. Everything else is a decision you can advise on from the brief (which language opens first, which digits, which layout), so it gets a recommended option with its reason. The recap ("Anything to change?") recommends "Looks right".
- **No straw men.** Never add a weak option to make the recommended one look good. If only one answer is sensible (an image needs alt text), the options are about *how* (describe the dish / mark it decorative / skip), plus skip.
- **Never re-offer what was declined.** Check the Declined list in DESIGN.md before offering anything.

## 3. Asking with AskUserQuestion

- Up to **4 questions per call**, 2 to 4 options each. Batch only questions that don't depend on each other. Palette waits for the direction; the hover style waits for the button shape.
- **Order: big to small** for builds and redesigns: direction, then structure, then the system (colour, type, spacing, radius, motion), then sections and components, then details and polish. Big picks make small questions simpler.
- **Order: worst first** for tweaks and polish: start with the most visible part of what they complained about (the label breaking on their phone), so even an interrupted session fixes what bothered them.
- **Fewer rounds, not fewer questions.** The person's time is the number of rounds. Whenever decisions don't depend on each other (hover, focus ring and labels for the same buttons), ask them in one call.
- **header** is 12 characters or fewer ("Colours", "Hero", "Btn corners"); **label** is 1 to 5 words; **description** is one or two sentences with the trade-off.
- **preview** (single-select only) holds the text preview from section 4. Keep it short enough to read at a glance.
- **multiSelect** suits lists of mechanical fixes that each have one sensible form: "Which of these should I fix?" with one fix per option, up to 4 per question and 4 questions per call. Unticked means declined: record it.
- **Number the journey** in the question text when there is a queue: "Decision 3 of 9: button corners".
- "Other" is always available. People type mixes, values or "you decide" there; read them with section 7.

## 4. Text previews (small changes)

Use the `preview` field. Pick the form that shows the difference fastest.

Layout sketch:
```
┌─────────────────────────────────────┐
│ [logo]          Menu  Visit  [Order]│
├──────────────────┬──────────────────┤
│                  │ Coffee roasted   │
│   bar photo      │ in Sulaymaniyah  │
│   (real one)     │ [See the menu]   │
└──────────────────┴──────────────────┘
```

Palette with contrast (compute the ratios with `scripts/contrast.py`; never guess them):
```
page     #16120F
surface  #221B16
text     #F3EDE4   on page 16.0:1  ok
muted    #B8AC9C   on page  8.4:1  ok
accent   #E0A040   buttons only, text on it #16120F 8.2:1
```

Type spec:
```
Heading   Montserrat 800   40/44
Kurdish   UniSIRWAN Adelle 800   46 (1.14x) / 1.55
Body      Montserrat 400   17/1.6, 65ch max
Prices    tabular figures, inline end
```

Before and after:
```
- rounded-full px-8 py-3 hover:scale-105
+ rounded-xl px-6 py-3.5 active:scale-[0.97]
```

Motion spec:
```
press   scale 0.97, 120ms ease-out
open    200ms cubic-bezier(0.23, 1, 0.32, 1), from scale 0.96 + fade
reduced: fade only
```

## 5. Comparison pages (big visual changes)

**Big** means the person has to *see* it to judge it: the direction, palette, type pairing, page or section layout, hero, navigation pattern, imagery style, light/dark theme, logo placement, menu or card structure, a logo candidate, a pack front or range, an illustration style, a poster or post layout. For these, build a comparison page, open it, look at it yourself, then ask.

1. **Folder.** `.design-options/<nn-topic>/` in the project root (for example `.design-options/02-palette/`). It is scratch space, kept until hand-off.
2. **Build each option with the real thing.** Use the real content, logo and photos, and the real fonts. Copy or link the project's font files. Never judge a Kurdish preview rendered in a substitute font. If the work is bilingual, show the Kurdish version too.
   - *Structure* (direction, layout, hero, print layout): one self-contained page per option, `a.html`, `b.html`, ...
   - *Tokens on an existing page* (colours, fonts, radius, spacing): one CSS override per option (`a.css` redefining the project's variables or classes), shot over the real page without editing the project:
     `node <skill>/scripts/shoot.mjs http://localhost:3000 .design-options/02-palette --css=.design-options/02-palette/a.css --name=a`
     Then give the compare page `shots` instead of `src`.
   - *Flutter screens:* an HTML mock per option at the device size (1366x768 for a till, 390x844 for a phone), built from the app's real strings and colours. Changing app code just to preview is a change, so ask first.
   - *Print:* render each option at true size (HTML to PDF/PNG with WeasyPrint or Chrome), plus one page showing all of them side by side.
   - *Logos:* each candidate in black and white on a plain ground, plus its `assets/logo-sheet.html` tests, plus 3 to 5 applications from the client's world (`identity.md` section 7).
   - *Packs:* the flat panels at true size and the whole range in `assets/pack-mockup.html`, side by side with competitors' packs at the same scale when you have them (`packaging.md` section 10).
   - *Social posts and posters:* each option exported at its real pixel size, and shown at phone size next to the full size (`graphic.md` section 3).
   - When changing existing work, add the **current version** as the first card, named "Current". Never blend the options into one.
   - **Keep previews light.** Show what the decision is about, not the whole site every time:
     - for a component, shoot the element only (`shoot.mjs --selector=".hero .btn" --jpeg`, about 10 KB);
     - full-page shots only when the decision is the whole page (direction, layout);
     - `--jpeg` for every preview, and delete shots that a newer round replaced.
     A button decision should cost kilobytes, not the 65 MB one test run produced.
3. **Page.** Copy `assets/compare.html` to `.design-options/<nn-topic>/index.html` and fill in its CONFIG block (question, context, options with `src` or `shots`, recommended flag).
4. **Look before showing.** Shoot it (`node <skill>/scripts/shoot.mjs .design-options/<nn-topic>/index.html .design-options/<nn-topic> --name=check`) and read the PNGs. Fix anything broken, such as an empty frame, missing font or overflow. A broken preview wastes their pick.
5. **Open it for them.** Windows: `start "" ".design-options\<nn-topic>\index.html"`. macOS: `open`. Linux: `xdg-open`. Or use the browser tool if they work in Chrome.
6. **Ask.** The option labels match the page letters ("A: Roast brown (Recommended)"). The preview field carries the three or four lines of spec, and the description carries the trade-off. Say in the question text that the comparison page is open in their browser.
7. **Keep the folder** until hand-off. They may combine options or go back to one, so never delete alternates mid-session.

## 6. After the pick

1. **Apply exactly the picked option.** Re-read the live file first: they sometimes edit files themselves, and those edits are decisions. Never revert them.
2. **Check that it really applied.** Render 390 and 1440 (and the Kurdish version) and compare with the preview. Changes can silently do nothing: a cascade that cancels a rule, a size the renderer ignores, a font that never loaded. Never report a change you haven't seen.
3. **Show it.** Write one or two lines on what changed, plus the screenshot path or the image, then move on to the next decision.
4. **Log it** in DESIGN.md under Decisions: date, decision, picked, over what, and why, in their words when they gave any. A rule that isn't written down gets undone in a later session.

## 7. Reading the answer

| They say | Do this |
|---|---|
| A letter or label | Apply it (section 6). |
| A mix: "A with C's type", "D and J" | Build the mix as a new option and show it next to the originals, then confirm with a short question. |
| "X, but change it" / "I like the idea, not that look" | Keep X's structure and offer variations on what they pointed at. |
| "you do you", "you decide", "do what's needed" | Pick the recommended option for this decision (or the rest of the queue if they said so). Say what you picked and why, keep the alternates, and log it as "decided for you" so they can reverse it. |
| "not nice", "I don't like that design" | Revert to the version before, then offer fresh options. Don't restyle the rejected one. |
| "too simple", "still missing something" | Add the brand's real material (artwork, photography, a bolder type moment, the logo's shapes). More boxes and lines won't fix it. |
| "undo", "revert to the first design" | An exact instruction: do it, and log it. |
| "show both", "decide later" | Keep both, log it as Open, and carry on with independent decisions. |
| No, skip, or unticked | Keep as is and add it to Declined. Never offer it again unless they bring it up. |
| Skipped a brief question | Infer from their own material (the printed menu, the old site, the brand guide) and state the assumption in the recap. |

## 8. Without the question tool

If AskUserQuestion isn't available (Claude app, another agent), ask in text and wait for the reply before editing:

```
**Decision 3 of 9: Button corners**
A. 12px corners (Recommended): matches the cards; calm.
B. Fully round: softer, more playful; changes two values.
C. 4px corners: sharper, more formal.
D. Keep as is.
Reply with a letter, a mix ("B but 8px"), or "you decide".
```

If you are running somewhere you can't ask at all (a subagent, a batch job), don't apply design changes. Return the decision cards to whoever called you.
