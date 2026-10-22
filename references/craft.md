# Craft: the numbers behind good options

Use this file in two ways: to build options that are good on their own terms, and to review existing work. Every rule here shapes options. None of them overrules a pick: if the person picks something outside these numbers, it's theirs.

## Contents
1. Know the surface first
2. Typography
3. Colour
4. Layout and spacing
5. Surfaces, depth and corners
6. Imagery and icons
7. Interface words
8. States and interaction
9. App screens, dashboards and tills
10. Pages that persuade (landing, restaurant, company)

---

## 1. Know the surface first

The same project has surfaces with different jobs. Decide the mode per screen, because it changes the rules:

| Mode | The visitor... | Examples | What may vary |
|---|---|---|---|
| **Persuade** | decides and acts | landing, restaurant site, company profile, pricing | everything: the design is the argument |
| **Operate** | completes a task, again and again | POS till, dashboard, admin, settings, forms | type, palette, density and ONE signature element; layout and controls follow convention |
| **Read** | understands something | docs, reports, articles, letters | the reading structure; never the reading column itself |
| **Experience** | is inside the work | portfolio, gallery, a showpiece | presentation and pacing |

A till is Operate even when its brand is loud: the brand lives in precise details (colour on the frame, the receipt, the typeface), not in decoration.

## 2. Typography

**Pick faces for a reason.** A face from the subject's world (a sign painter's grotesk for a street-food brand, a sturdy slab for a contractor), and one family or two clearly different ones. A third face only for a job nothing else can do. Never two faces in one headline. The client's brand faces always win, including fonts lists call "overused" (Montserrat on a brand that owns it is right).

**Overexposed defaults to avoid unless chosen on purpose:** Inter, Roboto, Open Sans, Poppins, Lato, Geist, Space Grotesk, Plus Jakarta Sans, Outfit, DM Sans as the only face; Instrument Serif, Fraunces, Playfair Display, Cormorant, DM Serif as the "premium" shortcut. Monospace only for real code or for money columns in an app.

**Scale:**
- Pages: 2 to 3 sizes do the visible work, 5 at most. Display at least 4x body on desktop. Phone hero around 40px (32 to 59). If two sizes look almost the same, make them the same.
  ```css
  --step-small:   clamp(0.8125rem, 0.79rem + 0.1vw, 0.875rem);  /* 13-14px */
  --step-body:    clamp(1.0625rem, 1rem + 0.25vw, 1.1875rem);   /* 17-19px */
  --step-lead:    clamp(1.25rem, 1.1rem + 0.7vw, 1.625rem);     /* 20-26px */
  --step-head:    clamp(2rem, 1.3rem + 3.2vw, 4rem);            /* 32-64px */
  --step-display: clamp(3rem, 1rem + 9vw, 9rem);
  ```
- Apps and tills: fixed sizes, not clamp. About 6 sizes (12/14/16/18/24/32), 3 weights, bold for one job (money or the title). No heading over 32px, no figure at 48px+ unless it is *the* number (a till's total).
- Body text: 16px minimum (17 to 19 on reading pages), never below 13px for anything, 11px floor for tiny labels in apps.

**Lines:**
- Measure 45 to 75 characters (about 65ch). Body leading 1.5 (1.45 to 1.6). Display leading 0.95 to 1.1.
- Latin display tracking -0.02 to -0.04em, tighter as size grows. Body tracking 0. Small caps labels at most +0.03em.
- Headlines: at most 2 lines and about 32 characters at every width (do the arithmetic: characters per line ≈ line width ÷ (font size × 0.5)). `text-wrap: balance` on headings, `pretty` on paragraphs. More space above a heading than below it.
- **Kurdish and Arabic follow their own rules** (no tracking, 1.55 to 1.85 leading, 1.09 to 1.15x size): see `rtl-kurdish-arabic.md`.

**Details:** `tabular-nums` for prices, totals and tables; curly quotes; the `…` character; a non-breaking space between number and unit; no weight change on hover; secondary text is the same face in a muted colour, not a lighter weight; never justify text on screen; no centred paragraphs over 3 lines; load only the weights you use.

## 3. Colour

**Start from something real:** the brand guide, the logo, the client's printed menu, the shopfront, the product photo. Sample exact values, and record any deliberate deviation from the guide.

**Pick a strategy before colours** (a good axis for options):
- **Restrained:** tinted neutrals + one accent. The floor for apps and tills.
- **Committed:** one strong colour owns 30 to 60% of the surface.
- **Fields:** sections are flat full-bleed colours, each with its own ink, told apart by lightness, not just hue.
- **Drenched:** the surface is the colour.

**Light or dark?** Write one sentence about the physical scene: who uses it, where, under what light ("a cashier under fluorescent light at 11pm", "a family choosing dinner on a phone in the car"). Let that decide, never the category.

**Roles, as tokens only** (a raw hex in a component is a second palette starting): page, surface (2 to 6 lightness points from the page), text, muted text, one accent + its ink, border, and success/warning/danger/info. On colour, tint secondary text from that hue; never grey on colour.

**Proportions:** ground 70 to 90%. **One accent**, on the action and at most one other recurring thing, small (around 5 to 10% of a screen). Never small accent-coloured text (yellow on white fails), never an accent that looks like a warning. Neutral buttons are a valid choice.

**Contrast** (compute with `scripts/contrast.py`): body text 4.5:1, large text 3:1, icons, borders and focus rings 3:1, in every state and both themes. Measure on the real background, including images and scrims.

**Dark mode is designed, not inverted:** a tinted deep ground (e.g. a warm black made from the brand colour with its saturation nearly off, like #16120F), cards a step lighter than the page and inputs a step lighter again, softer light text, brand colour on the frame only, no glow. A brand brown as the page with darker brown cards looked "muddy".

**Palettes for the web:** build ramps in OKLCH, and reduce chroma near white and black. Shift default framework hues (Tailwind's #2563EB, #DC2626, #059669, slate #0F172A) per brand. Raw, they read as "default Tailwind".

## 4. Layout and spacing

- **Structure follows the job.** Decide what the screen is for and what comes first, then let that decide the sections. Show the real product (the real menu, the real numbers) rather than abstract cards.
- **The frame:** equal outer margins at every width (16 to 32px; never under 16), nav on the same margins. Asymmetry lives inside the grid, never in the frame. One grid per page. Constrain text measure, not the whole page (no reflex `max-width: 1200px` box).
- **Spacing scale on a 4px base** (4, 8, 12, 16, 24, 32, 48, 64, 96...). Proximity before containers: tight inside groups, generous between them. One value everywhere is monotonous; random values everywhere read as machine-made.
- **Sections** (persuade pages): 120 to 240px apart on desktop, 72 to 112px on phones. Neighbours never share a layout. Alternate dense and calm, picture and type, light and dark. One deliberate rest per page; a section that looks empty needs its main element bigger, or cutting, not "something added".
- **Rest vs hole:** empty space is placed only where something closes it. Half a screen of nothing, text in one half and nothing in the other, or top-aligned pictures of unequal height (the classic broken card grid) are holes.
- **Cards are the lazy container.** Never nested cards, never a grid of identical icon + heading + text cards as page structure. Use rows, fields of colour, alignment and type instead.
- **Symmetry is a real option.** Formal clients (contractors, official letters) have asked for "formal / symmetric" and rejected diagonals on a symmetric brand. Asymmetry isn't automatically better.
- **Phone is its own composition:** re-author line breaks, re-crop pictures, keep some unevenness, margins 16 to 20, body 16 to 18, targets 44px+. Check that 390px never scrolls sideways.
- **Squint test:** blurred, can you still find the primary element, the secondary one and the groups, in order?

## 5. Surfaces, depth and corners

- **Flat by default.** Surfaces differ by one tone step, not lines and shadows. A border or a shadow, never both. One shadow role or none (for example, only things that float over the page cast a shadow).
- A shadow needs an offset and a soft blur. A zero-offset coloured halo is glow, and glow is decoration.
- **Radius by role, in tokens:** for example panels 24 to 28, everything tappable 12 to 16, an inner highlight smaller so it follows the outer curve, fully round only for chips and marks. Every button shares one radius. Square (0 to 2px) and full pill are both strong choices; 9 to 16px "soft" on everything is the weak default.
- Theme the browser's own surfaces: selection colour, caret, focus ring, scrollbar where appropriate, underline offset (0.18em) and thickness. It's the cheapest sign a page was built rather than assembled.

## 6. Imagery and icons

**Images, in order of preference:**
1. The client's own photos (the real shop, dish, product, team), with the brand's real artwork and logo files (never redrawn or retyped).
2. Generated images written as a photographer's brief (subject, angle, light, background, ratio, "no text"), labelled as generated.
3. Real pictures of the subject's world from open collections (Wikimedia Commons, Openverse, museum archives: old postcards and maps of the city, materials, the trade), licence checked (CC0/PD/CC BY/BY-SA), credited, and never passed off as the client's own.
4. Drawn from the subject (its own objects, one graphic language, three levels of detail).
5. Type and colour alone, which is legitimate.

**Rules:**
- One treatment for every photo on a page (untouched, or all greyscale, or all multiplied on a field), and two aspect ratios for most pictures.
- No device mockups, stock 3D blobs, people-at-laptops, gradient blobs, colour washes, duotone or tilted polaroids by default.
- Bright and natural beat dark and moody unless the brand is night-time. A picture leads its screen or stays small.
- Every image has dimensions or `aspect-ratio` reserved, and alt text.

**Icons:**
- One set (Lucide, Phosphor or Tabler, or icons drawn from the client's own material), one stroke weight, sized by token. Match visual weight: two bold icons beside thin ones looked wrong.
- No emoji or dingbats as icons (and ➜ ✎ ® may not exist in the font).
- Mirror directional icons in right-to-left.
- An icon-only control needs a label. An icon that needs a label to be understood should just be a labelled button.

## 7. Interface words

- **Headlines** say what this is, in the client's own terms: the name, what it is ("Coffee roasted in Slemani"), the claim, the instruction, or the place and moment. About 32 characters, 2 lines at most. Avoid "Welcome to", "X, reimagined", "Elevate your Y", tricolons ("Fast. Simple. Secure."), "not just X, it's Y", and one word styled differently.
- **Buttons** name the action (verb + object: "See the menu", "Save changes", "Print receipt"). One name for one action through the whole flow: the button "Publish" gives the toast "Published". One primary action per screen, and a second action as a text link.
- **Errors** say what happened, then how to fix it, in the interface's voice. Never blame, never apologise vaguely, never show raw codes as the message.
- **Empty states** say what will be here and how to start. **Loading** names the operation ("Loading today's orders…").
- **Never invent proof:** no fake testimonials, customer counts, ratings, prices or logos. Sample content (dish names, prices) is expected so the design is judged at real density, but list every invented sample for the client to replace.
- Specific nouns and real numbers ("38 seats", "open 4pm to 11pm") beat adjectives ("cosy", "premium").
- Translatable sentences are whole, with variables, never glued fragments (Kurdish word order differs). Kurdish written by Claude goes on the "Text to check" list.

## 8. States and interaction

- Every control has: default, hover (only for fine pointers), `:focus-visible`, active/pressed, disabled (still legible, says why when it matters), loading, and error/success where relevant.
- Feedback within 100ms. Disable the submit button only once the request starts, and show progress.
- **Forms:** labels above inputs (placeholders are examples, not labels), the right `type`/`inputmode`/`autocomplete`, 16px inputs on phones, validation on blur, errors beside the field plus a focused summary on submit. Requirements are shown before submitting, not discovered after.
- **Destructive actions:** undo is better than a confirmation dialog. A confirmation names the object and the result ("Delete order #1042"), never Yes/No/OK.
- **Touch:** targets 44px (web) / 48dp (apps), 8px apart; bigger for things tapped all day; no hover-only actions; swipe actions also have a visible button.
- **Overlays** escape overflow containers (`<dialog>`, popover API, portals). A modal is rarely the first answer; a page, a sheet or inline editing often is.

## 9. App screens, dashboards and tills

- **Name the screen's one question** ("Did today's sales come in?") and put the answer at the top, with its action beside it. Blocks below answer the next questions.
- **Give the product a face:** a ground or frame tinted from its world, the brand colour on the main data element or the frame, and one element only this product has (a sell-out strip for a bakery, the live order drawn as a thermal receipt for a till). Stock kit look (white 12px cards on #f8f8f8 with Inter) is the main complaint about generated dashboards.
- **Colour on data, not chrome.** No dark or saturated sidebar on a light canvas. Nav rows around 32px, icons 16px, labels 14px.
- **KPIs are type, not tiles:** values 16 to 40px (the answer figure biggest), grey sentence-case labels above, units as a smaller suffix, no icon circles, no sparklines. Delta colour means good/bad, not up/down (rising costs are bad), and zero change is grey. Use "+4 (new)" when the previous value was zero.
- **Data truth:** totals and deltas computed from the values shown, every relative number names its baseline, fixed decimals per kind (IQD 0, percentages 1).
- **Charts:** one series (max 3), 2px lines, no markers, 3 to 5 faint gridlines, round ticks, no legend for one series, annotate real events.
- **Tables:** rows around 45px, headers 12px grey sentence case, no zebra stripes, numbers right-aligned (inline end) and tabular, one status mark per row, row actions in one trailing column.
- **States:** real zeros printed, missing values as a dash, loading as the final layout with flat grey bars at real size (no shimmer, no layout shift), errors inside the failed block with Retry.
- **Tills (POS):**
  - Count the taps per item and remove any that aren't needed (one shop went from 3 taps to 2: a size tap adds the item).
  - One filled accent button per view: the next step.
  - Targets 48px+ on everything used while selling.
  - Money in a tabular face.
  - Count badges are neutral, never red. Red is only for the truly bad state.
  - A failed print stays on screen with "Print again".
  - Kiosk wording never mentions hardware the shop doesn't have.
  - Tools built for hundreds of products (search, tile-size controls) look generic on a seven-item menu.
- **Phone/tablet:** sidebar becomes a top bar + full-screen menu or a 4 to 5 item bottom bar, tables become two-line rows below about 640px (fields move to line 2, never dropped), and actions move up.

## 10. Pages that persuade (landing, restaurant, company)

- **The first screen says what this is** (name + what it does, or what/when/where for an event), with a real action on it.
- **The primary action works in place:** a restaurant's real menu and order/call/directions, not a "View menu" link to elsewhere.
- **One idea, grown from the client:** list 8 to 12 things only this client has (the name and its meaning, the street and how it looks, its materials and colours, its rituals and hours, its numbers, its printed things). Then fill in "On this page, [one of those] becomes [the device]". Swap in the nearest competitor: if the sentence still works, it's a category idea, not theirs. See `directions.md`.
- **One live thing:** one real interaction from the idea (pick a size and the whole price board changes; set the loan and read the real monthly figure). It needs real content, works by thumb, has a no-JS fallback, and never blocks reading.
- **Endings are designed:** the name at full width, a closing scene, or one quiet line, not a link-column footer dump.
- **Show, don't claim:** the product doing its job, the real menu, the real numbers.
