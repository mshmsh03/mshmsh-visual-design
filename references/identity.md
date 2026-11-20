# Brand and visual identity: logos, systems, guidelines

An identity is a set of marks and rules the client will use for years, mostly without you: on a shop sign at night, a 16px browser tab, a rubber stamp, a cup, an invoice. This file supplies the content of identity options. How they are asked is still `choices.md`: every mark, colour and rule is a pick.

## Contents
1. Before drawing
2. Mark architectures and the fallback set
3. Bilingual marks: Kurdish or Arabic with Latin
4. Drawing the mark
5. The tests every candidate passes
6. Colour, type and the rest of the system
7. Presenting and rounds
8. The guidelines document
9. The hand-off package
10. Originality and trademarks
11. Review checklist

---

## 1. Before drawing

Read what exists first (an old logo, the sign, the menu, the Instagram page, product photos). Then ask only what's missing, in one or two rounds:

- **The name, exactly, in every script.** Spelling, spacing and capitals in Latin, Kurdish and Arabic are facts only the client knows. Never transliterate or translate a name yourself (`rtl-kurdish-arabic.md` section 6).
- **Where the mark has to live.** The common set: shop sign, Instagram avatar (a circle), favicon, app icon, cup or bag, sticker, stamp, uniform embroidery, invoice, delivery box, vehicle. The smallest and harshest of these decide the architecture.
- **Who sees it, and in what state.** A customer glancing at a kiosk while walking past, a manager reading a quote. The audience's three seconds matter more than the founder's taste.
- **Personality as "this, not that".** Three pairs, each written by the client or picked from options: "warm, not cute", "serious, not cold", "local, not folkloric". Adjectives alone ("modern", "premium") mean nothing until a "not" pins them down.
- **The competitor wall.** Collect 6 to 12 marks of the nearest competitors in the same city and online, at the same size, in one image. Options are judged against this wall, not in isolation.
- **What's fixed.** Existing equity worth keeping (a colour customers know, a shape on the old sign), and hard constraints (must embroider, must work in one colour, must fit a round sticker).
- **Applications in budget.** Which pieces will actually be made in the next year. Design and test for those.

Fill the inventory in `directions.md` section 2. For identities it is the main source of ideas: the name's meaning, the place, the product's materials, the shop's rituals, the old sign.

## 2. Mark architectures and the fallback set

| Architecture | What it is | Strong when | Weak when |
|---|---|---|---|
| Wordmark | the name, set and adjusted, maybe one custom letter | the name is short and distinctive | the name is long; small sizes need another mark |
| Lockup | symbol + wordmark in a fixed arrangement | most new businesses | used everywhere, even where it can't fit |
| Letterform symbol | one letter drawn as the symbol | names with a letter that can carry the idea | the letter reads as only a letter, or only a picture |
| Monogram | two or three initials joined | heritage, legal, hospitality, family firms | the initials mean nothing to customers |
| Pictorial | a drawn object from the client's world | a specific object only they have | it's a generic object (a leaf, a cup, a roof) |
| Abstract | a shape or motif that suggests a quality | the shape has a clear logic and story | it looks like a hundred other geometric marks |
| Emblem / seal | the name inside a badge, ring or stamp | crafts, food, heritage, stamps on kraft | lots of small text; needs a simplified inner mark |
| Mascot | a character | kids, snacks, sweets, playful brands | formal clients; drawing many poses costs time |

**Every identity ships a set, not one drawing:**
- **Primary:** the full lockup for signs, letterheads, the website header.
- **Compact:** stacked or symbol-only for square and round places (avatar, app icon, sticker).
- **Smallest:** a favicon-grade mark that survives 16px and embroidery (often the letterform symbol or monogram).

All three come from the same drawing and share its shapes. If no clean smallest mark can be derived, the primary is over-detailed: simplify it rather than invent an unrelated icon.

**Choosing:** decide the architecture first, from the smallest place the mark must live and from what the name already does. Descriptive names (a mountain, a bee, a fire) invite a pictorial or letterform symbol; invented names want an abstract or type-led mark; family names suit monograms and seals. Options for the first identity question usually differ in architecture (`deal.py --kind identity`), not in colour.

## 3. Bilingual marks: Kurdish or Arabic with Latin

Most clients here need the name in two or three scripts. Treat that as one design problem, not a translation step.

- **Which script leads** is a decision (recommend from the market: Kurdish first for a local shop in the Kurdistan Region, where signs and menus are expected to lead in Kurdish; Latin first for an export or tech brand). Record it.
- **Lockups to offer:** stacked (one script above the other), side by side (the leading script on the reading start side), or separate marks per language with a shared symbol. Side-by-side lockups get a mirrored version for right-to-left layouts.
- **Match the voice and the mass.** Same weight class and contrast (a heavy geometric Latin wants a heavy Kufi-style Kurdish face, not a light Naskh). Size the Kurdish or Arabic about 1.09 to 1.15x for optical balance and decide by eye from renders (`rtl-kurdish-arabic.md` section 3).
- **Align deliberately.** Either share a baseline, or centre both scripts on one optical axis; Arabic-script bodies sit lower and taller than Latin x-heights, so a shared baseline often looks unbalanced. Offer both as options when it matters.
- **Let the lengths differ.** Don't stretch letters, add tatweel (ـ) or letter-space either script to force equal widths. Balance the pair by mass and position instead.
- **Start custom lettering from a real Kurdish-capable face** (`catalogs.md` section 4), keep its joining logic, and check every join, dot and the Kurdish letters ڕ ڵ ێ ۆ ە by eye at small size. A stand-in font rendering is never judged.
- **No faux script.** Latin letters dressed as Arabic (or Arabic letters bent to look Latin) read as a cliché. A shared element (a dot, a stroke ending, the symbol) ties the two scripts together better.
- Everything written in Kurdish or Arabic by Claude goes on the "Text to check" list in DESIGN.md.

## 4. Drawing the mark

Build marks as SVG in code (or in the person's vector tool), on a grid, from few and simple shapes.

- **Black on white first.** Design the one-colour version; colour is the last layer. A mark that needs colour to be recognised fails on stamps, foil, embroidery and faxed invoices.
- **Geometry, then optics.** Construct with circles, rectangles and consistent angles on a grid, then correct by eye: round letters and shapes overshoot the baseline and cap line by about 1 to 3%, horizontal strokes are slightly thinner than vertical ones, and acute joins get small ink traps if the mark will be printed small.
- **One idea.** A mark can carry one idea, sometimes two. Three metaphors in one symbol read as committee work.
- **Stroke and detail by smallest size.** Nothing thinner than the smallest application allows: no line under about 0.3 mm at the smallest print size (foil and rubber stamps need more), about 1 mm for embroidery, and no detail that disappears at 32px.
- **Wordmarks:** pick a face for a reason (`craft.md` section 2), set it at display size, kern by eye in pairs, adjust one letter only if it solves a real problem or carries the idea. Keep a live-text source file and deliver outlined paths.
- **SVG hygiene:** a tight `viewBox` around the mark, no transforms left on paths, colours as named CSS variables or a small fixed palette, ids prefixed with the brand slug, and the file run through SVGO. Text converted to paths in delivered files.
- **AI images are never the logo.** A generated image can feed a mood board or a sketch round, labelled as generated, but the mark itself is drawn as clean vector by you or the person. Generated marks can't be cleanly reproduced, scaled, embroidered or registered.

## 5. The tests every candidate passes

A candidate becomes an option only after these. Render them with `assets/logo-sheet.html` (fill its CONFIG with the SVG files and brand colours, then `node scripts/shoot.mjs <sheet> <out> --sizes=1600x1200 --full`) and look at the sheet yourself.

| Test | Pass when |
|---|---|
| 16px and 32px (browser tab) | the compact mark is still recognisable, not a smudge |
| App icon and avatar | it sits inside a circle and a rounded square without touching the edges |
| One colour, black on white | it reads with no colour at all |
| Reversed, white on dark | it doesn't turn into a different shape or lose cutouts |
| On the brand colour | the right variant exists and passes contrast |
| Blur (squint) | the silhouette is still distinctive |
| Real print size | at 25 mm wide (a sticker, a card) the wordmark is legible |
| Embroidery and stamp | no hairlines, no tiny counters, at most 4 to 6 colours |
| Sign at distance | readable at the distance customers see the shop from |
| Competitor wall | it doesn't look like a neighbour at the same size |

Also run two human tests when the person can: show it for two seconds and ask what they remember (the remembered parts are doing the work), and ask someone to draw it from memory (if they can't, it's too detailed).

A candidate that fails three or more tests is at best a secondary mark. Say which tests each option passes in its option card.

## 6. Colour, type and the rest of the system

**Colour:**
- One or two core brand colours, a neutral pair (dark and light, tinted from the brand), and at most one or two accents. Grow them from the inventory (`directions.md` section 7), never the category default.
- **Every colour gets four values:** HEX and RGB for screens, CMYK for print (ask the printer which profile; converted values shift, so proof them), and a Pantone reference only when something will be printed with spot inks (packaging, bags, signage). Canva and screens can't hold Pantone or true CMYK, so record the values in DESIGN.md and the guidelines.
- Compute the contrast of every text and background pair with `scripts/contrast.py` and list the allowed pairs.
- A one-colour rule: which colour the mark takes when only one ink is available.

**Type:**
- One display and one text family per script, at most. Latin and Kurdish/Arabic chosen as pairs (`catalogs.md` section 3), with the Kurdish size factor recorded.
- Licences: Google Fonts are OFL and safe for logos, print and web. Commercial fonts need the client's own licence; never deliver a commercial font file.

**Supporting elements** (only the ones the budget will use): a pattern grown from the mark or a local motif, an icon style, a photography direction (real, never stock), an illustration style (`illustration.md`), a layout grid for posts and print, and five lines on tone of voice.

## 7. Presenting and rounds

- **Same fidelity for every option**, each first alone on a plain ground at a generous size, then the compact mark at small size, then in 3 to 5 applications from the client's own world (their shopfront photo, their cup, their Instagram grid, an invoice). Mockups are labelled as mockups; real photos only when they are the client's.
- **Black and white before colour.** The first identity round compares architectures and shapes; colour comes as its own question once a shape is picked.
- **Rationale from the inventory,** one or two sentences per option ("the dot of the ڕ is the honey drop from their jar label"), plus which tests it passes and its cost. No adjective soup.
- **Rounds narrow:** three directions, then one direction refined with two or three variations, then production. Never a wall of twelve similar wordmarks; that makes the choice impossible.
- Build the round as a comparison page (`choices.md` section 5) or a PDF deck for clients who decide offline (`print.md` section 6).

## 8. The guidelines document

Small businesses need 8 to 20 pages, written for the cashier who makes the Instagram post and the print shop that makes the sign:

1. The idea in two lines, and the logo set (primary, compact, smallest).
2. **Clear space,** given as a multiple of a part of the mark (for example the height of the letter ک or of the symbol), drawn on the logo.
3. **Minimum sizes** in px for screens and mm for print, per variant.
4. Colour variants and when each is used (full colour, one colour black, one colour white, on brand colour).
5. **Colour values:** HEX, RGB, CMYK and Pantone where needed, with the allowed text pairs.
6. Typography per script, with sizes, weights and the Kurdish factor.
7. **Misuse:** stretching, recolouring outside the set, outlines or shadows, rotating, placing on busy photos without a panel, retyping the name in another font, rearranging the lockup.
8. Supporting elements, and 3 to 6 real applications.
9. Where the files are, and who to ask.

Make it as a doc or design artifact (or a PDF built from HTML with `shoot.mjs --pdf`). If the client works in Canva, also set up their brand kit (logos, colours, fonts) so templates stay on brand.

## 9. The hand-off package

```
<brand>-identity/
  01-logo/
    primary/   full-colour, one-colour-black, one-colour-white, on-brand  (SVG, PDF, PNG 512/1024/2048, JPG for email)
    compact/   same set
    smallest/  same set
  02-digital/  favicon.ico (16/32/48), apple-touch-icon 180, icon-192, icon-512, social avatar 1080 (circle-safe)
  03-print/    CMYK PDFs of the logo set, Pantone notes if any
  04-fonts/    links and licences (OFL files only)
  05-guidelines/  the guidelines PDF
  06-applications/  the mockups and any finished pieces
  README  what's where, colour values, contacts
```

- File names say variant, colour and size: `hawraman-primary-black-1024.png`.
- Vector is the source of truth; every PNG and JPG is exported from it. Never deliver only raster.
- PNGs are trimmed to the visible edge (no invisible padding), on transparent backgrounds.
- Check every exported file opens and looks right, and list what you couldn't check (embroidery, sign material, print colour).

## 10. Originality and trademarks

- Before presenting, search the competitor wall, Instagram in the client's city, and the free WIPO Global Brand Database (branddb.wipo.int) by name and by image for close matches. Say plainly that this is a sanity check, not legal clearance.
- Never trace, adapt or "remix" an existing mark, and never imitate a known brand's style closely enough to be confused with it.
- Generic symbols (a coffee bean, a house roof, a tooth, a swoosh) make weak, hard-to-protect marks. Prefer something only this client has.
- Registration (in Iraq or the Kurdistan Region, or abroad) is the client's lawyer's job; offer the files they need.

## 11. Review checklist

- [ ] Architecture chosen for the smallest place it must live; primary, compact and smallest marks exist and share shapes.
- [ ] Works in one colour, reversed, at 16px, at 25 mm, blurred, and on the competitor wall.
- [ ] Kurdish/Arabic lockup matched in weight and optical size, joins checked by eye in the real font, spelling confirmed by the client.
- [ ] Every colour has HEX, RGB, CMYK (and Pantone where printed with spot inks); allowed text pairs computed.
- [ ] Fonts licensed for the use; only OFL files delivered.
- [ ] Guidelines cover clear space, minimum sizes, colour values, misuse and applications.
- [ ] Package complete, files open, names consistent, vector sources included.
- [ ] Sanity search done and stated as not legal advice.

Sources this file learned from: the logo-design and brand-identity skills in rampstackco/claude-skills (MIT) for the architecture, application-context and hand-off ideas, restated here; see THIRD-PARTY-NOTICES.md.
