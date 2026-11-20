# Directions: options that differ for real

A model asked for three directions returns the category default three times: the cafe gets cream and serif, the startup gets purple, the dashboard gets white cards. This file is how to avoid that, so the person chooses between real alternatives grown from their own project.

## Contents
1. Refine or depart?
2. The inventory: what only this client has
3. Dealing directions and grounding them
4. The option card
5. Checks before showing
6. Refining: six axes and what words mean
7. Colour options
8. Type options (Latin and Kurdish together)
9. The rut: defaults to steer away from
10. Catalogues

---

## 1. Refine or depart?

- **Refine** (the default, about 90% of the time): keep the identity, vary its expression. Use it for polish, tweak, review fixes, and "make it better" on something that already has a look.
- **Depart:** a new look. Only when the person says "redesign", "from scratch", "completely different", or when there is nothing yet.
- **Unsure means refine.** A wrong refine costs three similar on-brand options (recoverable). A wrong departure costs three off-brand ones (trust lost).

Before refining, write the **identity lock**: one sentence of what is actually on screen, in real values. For example: "Dark #0B0F19 ground, one purple-to-blue gradient accent, Inter 400/800, centred stacks, 16px radius everywhere, three emoji feature cards." Take it from DESIGN.md, then CSS variables, then computed styles. Every refinement option must still read as the same brand beside the others.

## 2. The inventory: what only this client has

Before any direction, list 8 to 12 things only this client has. Read them from their material, notes and site; ask only for what you can't find.
- the name and what it means, and where it comes from
- the street or neighbourhood and how it looks (signs, tiles, paint, light, the mountain behind it)
- numbers: seats, years open, items, prices, hours, branches, square metres
- the constraint it lives with ("one batch a day", "open only evenings")
- materials and colours (packaging, uniforms, the counter, the product itself)
- rituals and times ("the grill is lit at four")
- printed things of its world: the menu, the receipt, the ticket, the business card, the price board
- its own artwork, logo shapes and photographs
- its languages, and which one leads

Then write the **idea sentence**: "On this page, [one item from the inventory] becomes [the device]." For example: "On this page, the counter's price board becomes the whole menu: one size switch reprices everything."

**Competitor test:** swap in the nearest competitor. If the sentence still works ("a cup of coffee becomes the hero"), it's a category idea, not theirs. Dig again.

## 3. Dealing directions and grounding them

1. **Name the rut first:** the page this category always ships, and its predictable opposite. Neither is an option, unless the person asks for it.
2. **Deal:** `python scripts/deal.py --kind page|app|print|identity|packaging|illustration|graphic --sector <their trade> --have <what really exists> [--tone <tone>]`. It deals 3 directions from different families, filtered by the assets they have, and skips the ones dealt recently. Don't redeal because a card feels unfamiliar; redeal only when a card can't work (`--exclude <id>`) and say why.
3. **Ground each card** in the inventory: the idea sentence, the client's real colours and fonts (or chosen ones with a reason), the real content. A dealt card is a structure; the client's world fills it.
4. **Lock what's fixed.** Brand colours, brand fonts and the logo stay in every option unless the person opens them up. Then the options differ in structure, density, hierarchy and motion, not in brand.
5. **Add the person's own idea** if they gave one: it takes a slot.
6. **The classic option.** One option may be "the category standard, done really well" when the client is conservative (contractors, official letters, formal companies have asked for exactly this). Label it honestly as the safe choice, and don't recommend it by default.

## 4. The option card

Every option gets the same anatomy, at the same fidelity, so none wins by being more finished:

```
A. <Name>  (Recommended)
   Idea:      On this page, <inventory item> becomes <device>.
   Layout:    <first screen in one sentence + an ASCII sketch>
   Colour:    <strategy> · 4-6 hex with roles (contrast computed)
   Type:      <Latin face/weight> + <Kurdish face/weight, size factor>
   Motion:    <the one moment, or "still">
   Memorable: <the one thing someone would describe an hour later>
   Cost:      <honest risk: what it needs, what it gives up, how familiar it is>
```

In AskUserQuestion, the label is the name. The description carries the idea and the cost. The preview carries the layout sketch plus the colour and type lines. For big choices, the comparison page shows each card built for real (`choices.md` section 5).

## 5. Checks before showing

- **Distinct at thumbnail size.** If two options can only be told apart by their descriptions, cut one. Two real directions beat three padded ones.
- **Structure, not just colour.** Colour-only variants of one layout count as one option ("change the design too, not just the colours").
- **Three colour worlds, not three shades** when colour is the axis: no shared dominant hue.
- **Family pass:** give each option a one-word family (poster, report, board, gallery...). If two share it, rework one.
- **Sentence pass:** put the three idea sentences side by side. If two rhyme, rework one.
- **Feasibility:** each option is buildable with assets that exist. Missing photos means a photo-led option is a lie.
- **Every option is a good default.** No straw men.

## 6. Refining: six axes and what words mean

For refinements, each option takes a **different primary axis**:

| Axis | Varies |
|---|---|
| Hierarchy | what commands the eye first |
| Layout topology | stacked / side by side / grid / asymmetric / overlay |
| Type system | pairing logic, scale ratio, weight and case (within the brand's faces) |
| Colour strategy | which existing colour carries the surface: restrained / committed / fields / drenched |
| Density | spacious / comfortable / dense |
| Structure | merge, split, or move things one level deeper |

When the person uses a word, map it to axes rather than guessing a look:

| They say | Offer options that... |
|---|---|
| bolder, stronger, punchier | push scale, commit the colour, or make one structural move (one option each) |
| quieter, calmer, cleaner | reduce colour, remove ornament, or open the spacing |
| simpler | cut visual noise, cut redundant content, or flatten nesting |
| more professional, more formal | tighten alignment and symmetry, reduce type sizes to fewer steps, or move to a classic structure |
| more modern | usually means "less template": change the type, cut decoration, or show the real product |
| warmer | warm the neutrals, add real photography, or soften the type |
| "better", "nicer", "fresh" | ask one question first: which of these do they mean? Offer the words above as options |

## 7. Colour options

- **Strategies as options:** restrained (tinted neutrals + one accent), committed (one colour owns 30 to 60%), fields (flat full-bleed chapters), drenched (the surface is the colour). Apps and tills start from restrained.
- **Seed each palette from a scene** with real materials and light: "a Slemani bakery at 6am: flour white, oven black, the tin sign's red". Then a ground, one strong colour doing the brand's work, a deeper accent a step away, and a deliberate ink.
- **Light or dark** comes from a sentence about the real use: who, where, under what light.
- **The first palette that comes to mind is spent.** It is the category default. Use it only if the brand demands it.
- From the client's brand: keep their exact colours, and vary proportion and role instead (brand colour as the ground vs as the frame vs only on the action).
- Compute every contrast pair with `scripts/contrast.py` before it goes in a preview.

## 8. Type options (Latin and Kurdish together)

Offer type as **pairs across scripts**, matched by voice and weight, never a Latin face alone:

| Voice | Latin (examples) | Kurdish / Arabic (verify with glyph_check.py) |
|---|---|---|
| Heavy, loud food brand | Montserrat Black/ExtraBold (if the brand's), Anton, Archivo ExtraCondensed, Bricolage Grotesque 800 | UniSIRWAN Adelle ExtraBold (brand-licensed), Noto Kufi Arabic Black |
| Calm, precise, app UI | IBM Plex Sans, Hanken Grotesk, Public Sans, Switzer | IBM Plex Sans Arabic, Noto Sans Arabic, Vazirmatn |
| Formal, corporate | Libre Franklin, Source Serif 4 + Source Sans 3, Albert Sans | UniSIRWAN Somar/Ping (brand-licensed), Noto Naskh Arabic, IBM Plex Sans Arabic |
| Warm, rounded, friendly | Nunito (as the brand's), Figtree, Chillax | Zain-style rounded faces (check the joins by eye), Vazirmatn |
| Editorial, reading | Literata, Newsreader, EB Garamond | Noto Naskh Arabic, Vazirmatn for text + Noto Kufi Arabic for headings |

Overexposed defaults (Inter, Roboto, Poppins, Geist, Space Grotesk; Instrument Serif, Fraunces, Playfair as the premium shortcut) are not options unless the brand owns them. Each option states its Kurdish size factor (1.09 to 1.15x) and line height. The `catalogs.md` file has the full list of Arabic-script Google fonts to check.

## 9. The rut: defaults to steer away from

Recognise these when they appear in your own options, and replace them with something from the inventory:
- **Cafe, bakery, anything warm:** cream ground + serif display + terracotta/sage accent.
- **Tech, startup, AI:** dark ground + purple/blue gradient + glow + Inter.
- **Dashboard:** white 12px cards on light grey, Inter, a coloured sidebar, sparklines in KPI tiles.
- **Restaurant:** full-bleed food photo hero + centred script headline + "View menu" button.
- **Company/contractor:** a stock skyline photo + "Building the future" + three icon cards.
- **"Avoid the obvious" opposite:** brutalist black-and-white with huge mono type, applied to a family bakery.
- **Kurdish/Arabic side:** the Latin design with the text swapped and right-aligned, in a fallback font.
- **Logos:** the category's generic object (coffee bean, tooth, roof, leaf, chef's hat), a letter in a circle, a gradient swoosh.
- **Packs:** the shelf default (honey: a bee and hexagons on cream; sweets: gold on dark; organic: kraft and a green leaf; cosmetics: pastel and a thin serif).

The full list of tells is in `review.md` section 6.

## 10. Catalogues

`catalogs.md` holds condensed lists to grow options from: style families with their risks, palettes by trade (restaurant, cafe, POS, pharmacy, construction, manufacturing, portfolio, automotive, education, dashboards), type pairings, the Arabic-script Google fonts, and landing-page section patterns. Treat them as raw material. Shift any framework-default hex toward the client's brand before using it.
