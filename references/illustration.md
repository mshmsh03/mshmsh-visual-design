# Illustration: style systems, drawing in code, characters, patterns

Illustration is worth its cost when it shows something a photo can't: an idea, a process, a product that doesn't exist yet, the mood of a place, a character people come back for. Used as filler it becomes the stock-illustration look, one of the clearest AI tells (`review.md` section 6). Every style decision below is an option the person picks (`choices.md`).

## Contents
1. When illustration is the right answer
2. The style sheet
3. Style families for options
4. Ways to produce it
5. Drawing SVG well
6. Characters and mascots
7. Patterns and motifs
8. Icons and spot illustrations
9. Generated images
10. Illustration for print and packs
11. Review checklist

---

## 1. When illustration is the right answer

- **Yes:** explaining how something works or is made; showing a product, place or scene that can't be photographed well; packaging that sells taste or origin; a brand character; kids, play and food fun; empty states and onboarding in apps; patterns that carry a brand.
- **No:** decorating a section that has nothing to say, replacing real photos of a real place or product, or a person at a laptop. If the client has good photos, photos usually win (`craft.md` section 6).
- When unsure, offer "real photo / illustration / type only" as the first option set for that piece.

## 2. The style sheet

Before the first finished illustration, the picked style is written down in DESIGN.md under "Illustration", so every later piece matches. A one-off drawing with no rules can't be repeated next month.

```
Illustration style: "Hawraman linocut"
Purpose        packaging fronts, Instagram posts, one hero on the site
Line           no outlines; shapes cut with rough 2-3 px edges at 1080 px
Fill           flat, 3 inks: honey #E3A21A, comb #3B2410, cream #FFF6E0
Shading        one darker tone of the same ink, light from top left
Perspective    flat, side views only
Shapes         chunky, rounded ends, no detail under 6 px at 1080 px
Figures        none; bees and flowers only, bee = 5 shapes
Texture        subtle paper grain on large fields only
Detail by size spot 120 px: 3 shapes / card 480 px: 10 / hero 1600 px: full scene
Exports        SVG master, PNG 2x for web, CMYK PDF for print
```

Decide each line as an option set when it matters (line or no line, flat or textured, how many colours). Keep the palette to the brand colours plus two or three support colours, about six at most.

## 3. Style families for options

Deal three families with `python scripts/deal.py --kind illustration --sector <trade> --have <assets>`, then ground each in the inventory (`directions.md` section 2): the client's objects, place, materials and ornament.

| Family | Look | Good for | Watch |
|---|---|---|---|
| Flat geometric | shapes from circles and rectangles, flat fills, no outlines | apps, explainers, signage | the "corporate flat" look (tiny heads, noodle limbs, purple people) is a tell |
| Monoline | one stroke weight, rounded joins, few fills | icons, menus, maps, elegant brands | thin lines vanish at small sizes |
| Grain and riso | flat shapes with grain or halftone, 2 to 3 inks, slight misregistration | posters, packs, food, culture | file size; texture can feel like a trend |
| Cut paper and collage | torn or cut edges, real paper, photo cut-outs | events, youth brands, editorial | needs real scans; fake paper texture is a tell |
| Ink and brush | hand-drawn lines and brush marks | food, craft, personal brands | best drawn by a person and scanned; generated "hand-drawn" looks fake |
| Linocut and stamp | bold carved shapes, 1 to 2 colours, rough edges | kraft packs, bakeries, honey, craft | heavy at small sizes |
| Technical plate | precise line drawings with labels, like a botanical or engineering plate | ingredients, machines, products with parts | must be accurate; labels in every language |
| Motif and pattern | built from local ornament (kilim, tile, embroidery) | identities, packs, backgrounds | cultural accuracy; low contrast behind text |
| Character world | a small cast of simple characters | kids, snacks, apps, campaigns | many poses to draw consistently |
| Isometric | 30° isometric objects and rooms | explaining a space or process | an overused tech tell outside that job |

## 4. Ways to produce it

Choose the route with the person; it's part of the option's cost.

1. **SVG written in code** (Claude draws it): best for flat, geometric, monoline, pattern, icon, map and diagram styles. Precise, small, recolourable, easy to keep consistent. Weak for painterly or very organic styles.
2. **The person or an illustrator draws it** from a brief: best for ink, brush, character and painterly styles. Write the brief from the style sheet: purpose, audience, the list of pieces with sizes and where they appear, references with what to take from each, what to avoid, formats, and the deadline.
3. **A generated image, then rebuilt** (section 9): useful for exploring compositions and moods fast. The chosen composition is then redrawn or traced into clean vector that follows the style sheet.
4. **An open library customised** to the style sheet: Open Peeps and Open Doodles (CC0), unDraw (free for commercial use, no redistribution as a pack). Recolour, redraw details and combine; never use them untouched in client work, because the stock look is recognisable.
5. **The client's own artwork:** a line drawing from their profile, a pattern from their old packaging, a sketch by the founder. Often the strongest and most specific source (`print.md` section 6).

## 5. Drawing SVG well

- **Canvas:** set the `viewBox` to the subject so it fills at least about 85% of the frame. Draw on a grid (8 or 4 units) and snap key points to it.
- **Few, simple shapes:** prefer `<circle>`, `<rect>`, `<ellipse>` and short paths with smooth curves over hundreds of tiny segments. Group by part (`<g id="bee-wing">`), name ids with a slug prefix.
- **One stroke weight per set,** chosen for the output size (for example 2 px at 24 px icons, 3 to 4 px in a 1080 px post). Pick round or sharp caps and joins and keep them everywhere.
- **Colours as tokens:** `fill="var(--ink-1)"` or a small fixed palette documented in the style sheet, so a later recolour is one change.
- **No text inside illustrations,** especially Kurdish or Arabic. Set text in HTML or as a separate layer with a real Kurdish-capable font, so it can be translated and shapes correctly.
- **Direction:** characters and arrows face into the content. In right-to-left layouts, mirror those illustrations (never mirror logos, text, clocks or anything with writing; `rtl-kurdish-arabic.md` section 4).
- **Clean and check:** run SVGO (`npx svgo in.svg -o out.svg --multipass`, with `prefixIds` when several SVGs share a page), then render at the real sizes with `scripts/shoot.mjs` and look at them. If an illustration needs more than a few hundred path points, it's probably the wrong route for code.
- **From a bitmap:** trace with Inkscape's Trace Bitmap, vtracer or Potrace, then clean by hand: merge segments, remove specks, unify strokes, recolour to the palette.

## 6. Characters and mascots

- **Silhouette first:** the character must be recognisable as a solid black shape. Build it from three to five simple shapes with one signature feature (the ears, the hat, the stripes).
- **Model sheet** before any campaign: front, three-quarter, side and back views; six expressions; four to six poses; the colour values; the line and proportion rules. Every new drawing is checked against it.
- **Proportions stay fixed** (for example "head is 1/3 of height, eyes on the halfway line").
- **Local and respectful:** clothing, gestures and food that make sense to the audience; check gestures that are rude locally. Not a copy or near-copy of a known character, in shape, colours or pose.
- **Logo use:** the head or a simple pose as the compact mark; test it like any mark (`identity.md` section 5).

## 7. Patterns and motifs

- **Repeat tile:** design one tile and repeat it (straight, half-drop or brick). Check a 3 x 3 grid for seams, gaps and accidental lines. Size the motif relative to the object (a cup vs a shopping bag vs a wall).
- **Local ornament** (Kurdish kilim diamonds, tile stars, embroidery borders) gives identities and packs a place. Start from real references (museum and archive photos, the client's own textiles), simplify with care, and say where the motif comes from in the rationale.
- **Geometric patterns** are constructed, not eyeballed: compass-and-straightedge grids (circles divided into 6, 8 or 12) give the classic star and rosette families. Build them in SVG from the grid so they tile exactly.
- **Never use Quranic verses, religious calligraphy or the names of God as decoration,** and avoid sacred symbols on packs that get thrown away.
- **Behind text,** patterns drop to low contrast (one tone step), or stop behind a calm panel.

## 8. Icons and spot illustrations

- Icons follow `craft.md` section 6: one set, one stroke weight, sized by token. Custom icons sit on a 24 px grid with about 2 px padding, one or two paths each, `currentColor` fills.
- Spot illustrations (empty states, onboarding, packs' side panels) use the style sheet at the "spot" detail level: three to five shapes, no tiny details, readable at 120 to 200 px.
- Mirror directional icons and spot scenes in right-to-left layouts.

## 9. Generated images

- **Write a brief, not a vibe:** subject, action, composition and crop, viewpoint, light, palette (hex values), style family from the sheet, background, aspect ratio, and "no text, no logos". Save the prompts and settings in DESIGN.md so later pieces can match.
- **Never** name living artists or studios, known characters, brands or copyrighted works in a prompt, and don't steer toward a recognisable artist's style.
- **Inspect every result by eye:** hands, eyes, letters and symbols, flags and clothing, food that looks wrong, cultural details. Generated Kurdish or Arabic lettering is almost always broken; replace it with real text.
- **Avoid the generated look** that clients now recognise: plastic lighting, over-smooth skin, glowing edges, everything perfectly centred. Rebuilding the composition as vector in the style sheet removes most of it.
- Label generated images as generated when you show them, and never present them as photos of the client's real place, product or people.

## 10. Illustration for print and packs

- Vector for anything printed with line art or flat colour; raster art at 300 ppi at final size.
- Convert to the printer's colour mode: CMYK, or spot inks when the pack prints with them (`packaging.md` section 8). Bright RGB greens, blues and oranges dull in CMYK; check them early.
- Outline strokes in the final print file, and keep lines at least 0.25 pt (thicker for flexo, kraft and embroidery).
- Small black detail in 100% K, overprinted, so it doesn't misregister.
- For wraps and boxes, extend the illustration into the bleed and across folds, keeping faces and focal points away from folds.

## 11. Review checklist

- [ ] Illustration is doing a job a photo or type couldn't.
- [ ] A style sheet exists in DESIGN.md and every piece follows it (line, palette, shading, perspective, detail by size).
- [ ] No stock or generated look left untouched; no known characters or artists imitated.
- [ ] Kurdish and Arabic text set as real text, outside the drawing.
- [ ] Characters and arrows face into the content in both directions; logos and writing never mirrored.
- [ ] SVGs are clean (few paths, tokens for colour, optimised) and checked at real sizes.
- [ ] Print versions are vector or 300 ppi, in the right colour mode, with safe line weights.

Sources this file learned from: the art-direction illustration brief in rampstackco/claude-skills and the static SVG craft notes in dvy1987/agent-loom (both MIT), restated in this skill's words; see THIRD-PARTY-NOTICES.md.
