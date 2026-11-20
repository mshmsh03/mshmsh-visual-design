# Free resources: tools, assets, references, learning

Everything here is free to use, or has a real free tier, as checked in November 2026. Free tiers and licences change: check the licence page before using an asset in client work, and prefer CC0, OFL, MIT or ISC. Credit authors when a licence asks for it, and never present a library asset or a generated image as the client's own photo or artwork.

## Contents
1. Design tools
2. Fonts
3. Colour
4. Icons
5. Illustration assets
6. Photos
7. Packaging and print
8. Identity, references and inspiration
9. Learning and practice (for the person)
10. Specs to check numbers against

---

## 1. Design tools

| Tool | For | Note |
|---|---|---|
| Affinity (by Canva) | vector, photo and layout in one desktop app (Windows, macOS) | free since October 2025; only its AI tools need a paid Canva plan; opens and exports PDF, SVG, EPS, PSD |
| Inkscape | vector illustration, logos, Trace Bitmap | free and open source; SVG native |
| Krita | painting and drawn illustration | free and open source |
| GIMP / Photopea | photo editing (Photopea runs in the browser and opens PSD files) | free (Photopea shows ads) |
| Scribus | page layout for print with CMYK, spot colours and PDF/X export | free and open source |
| Penpot / Figma | screens, components, templates | Penpot is open source; Figma has a free plan |
| Canva | quick layouts, templates, brand kits, social sizes | free plan; CMYK PDF export needs a paid plan (`graphic.md` section 8) |
| Blender | 3D packaging and product mockups | free and open source |
| SVGO, vtracer, Potrace | optimise SVG; trace bitmaps to vector | free command-line tools |

## 2. Fonts

- **Google Fonts** (OFL, free for logos, print and web). "Arabic" support doesn't mean Kurdish: use the checked list in `catalogs.md` section 4 and run `scripts/glyph_check.py` on anything else.
- **Fontshare** (by the Indian Type Foundry): free Latin families for personal and commercial use; check each family's licence page.
- Commercial and brand-licensed fonts (for example the UniSIRWAN family) only with the client's own licence.

## 3. Colour

- `scripts/contrast.py` in this skill for every text and background pair.
- Coolors and Adobe Color for exploring palettes; oklch.com for building even OKLCH ramps.
- Pantone values come from the printer's swatch book or Pantone's own tools; screen previews of Pantone colours are approximate.

## 4. Icons

- Lucide (ISC), Phosphor (MIT), Tabler Icons (MIT): one set per project, one stroke weight (`craft.md` section 6).

## 5. Illustration assets

Use these as raw material, recoloured and redrawn to the style sheet (`illustration.md` section 4), never untouched in client work.

| Library | Licence | Note |
|---|---|---|
| Open Peeps (Pablo Stanley) | CC0 | hand-drawn people to mix and match |
| Open Doodles (Pablo Stanley) | CC0 | loose hand-drawn scenes |
| unDraw (Katerina Limpitsouni) | free for commercial and personal use, no attribution; don't redistribute it as a pack or build a competing library | flat scenes, recolour on the site |

## 6. Photos

- **The client's own photos first.** A phone photo of their real shop beats any library.
- Unsplash and Pexels: free licences that allow commercial use without credit, but not selling unaltered copies; recognisable people, logos and buildings in a photo can still need care.
- Openverse and Wikimedia Commons: licences vary per file (CC0, public domain, CC BY, CC BY-SA); credit when required (`craft.md` section 6).

## 7. Packaging and print

- **templatemaker.nl:** free parametric dielines for boxes, bags and shapes, exported as PDF, SVG or DXF. Concepts only until the converter confirms (`packaging.md` section 3).
- **GoVisually free dieline generator:** cartons, mailers, labels and pouches with SVG, PDF, DXF or PNG export and a private 3D preview (one email verification).
- **Die Cut Templates** and **Pacdora:** template libraries and 3D mockups with free tiers and download limits.
- **GS1:** barcode size and placement guides (search "GS1 barcode size" on your country's or GS1 UK's site). The client's GTINs come only from a GS1 membership.
- **FEFCO code** (corrugated) and **ECMA code** (folding cartons): the standard names of box structures, useful with factories.
- Canva's help page "Use margins, bleed, rulers, and crop marks" for print exports from Canva.

## 8. Identity, references and inspiration

- **WIPO Global Brand Database** (branddb.wipo.int): free search of registered trademarks by name and image, for a sanity check before presenting marks (`identity.md` section 10).
- **Brand New** (UnderConsideration): reviews of new identities with the before and after.
- **Fonts In Use:** typefaces in real work, searchable by font, industry and format.
- **Logo Design Love** and **Identity Designed** (David Airey): logo process and identity case studies.
- **The Dieline** and **Packaging of the World:** packaging work from around the world.
- **NASA Graphics Standards Manual** (1976): a free PDF on nasa.gov and a classic example of what a guidelines document covers.
- **Behance:** case studies that show process (sketches, rejected routes, applications), not just final shots.
- Use references for what they teach (a structure, a hierarchy, a material), never to copy a look (`directions.md` section 9).

## 9. Learning and practice (for the person)

Share these when the person asks how to get better themselves, not inside client work.

- **Canva Design School:** free short courses and tutorials on layout, colour, type and branding.
- **CalArts Graphic Design Specialization** (Coursera): fundamentals, typography, imagemaking, history and a brand project; check the enrol page for a free audit or trial option.
- **YouTube:** The Futur (branding and the business of design), Satori Graphics (graphic and logo design), Will Paterson (logo design and lettering).
- **Practical Typography** (Matthew Butterick): a free online book on type that applies straight to posters, menus and guidelines.
- **Practice briefs:** Sharpen.design and FakeClients generate free design briefs (logos, posters, packaging) for daily practice and portfolio pieces.
- The best practice is real constraints: redesign a local shop's menu, label or sign as a study (never presented as commissioned work), in Kurdish and English, and print it.

## 10. Specs to check numbers against

- GS1 General Specifications (EAN-13 sizes, quiet zones, placement): `packaging.md` section 7.
- EU Regulation 1169/2011, Article 13 (minimum x-height for food information): `packaging.md` section 6.
- Instagram and Meta help and ads guides (sizes and safe zones): `graphic.md` section 4.
- The printer's own spec sheet beats every general number in this skill.
