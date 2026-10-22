# Catalogues: raw material for options

Lists to grow options from. They are starting points, never answers: ground every pick in the client's own material (`directions.md`), and shift framework-default hues toward the brand. Most data palettes are stock Tailwind colours (#DC2626, #2563EB, #059669, slate #0F172A, muted #475569), and used raw they look default. Contrast ratios below were computed (WCAG 2) and spot-checked. Palette, pairing and pattern data condensed from ui-ux-pro-max (MIT, Next Level Builder); see THIRD-PARTY-NOTICES.md.

An option is usually **style family + palette + type pair + page pattern**. Options should differ on at least two of: style family, palette (light/dark, warm/cool), type genre, density, layout.

## Contents
1. Style families
2. Palettes by trade
3. Type pairings (Latin + Kurdish/Arabic)
4. Arabic-script Google fonts
5. Page patterns
6. Print identity styles

---

## 1. Style families

RTL fit: **Good** survives Kurdish/Arabic; **Partial** relies on uppercase, tracking, italics or a Latin-only display face, so it needs an Arabic-script equivalent.

| Style | Look | Best for | Risk | RTL |
|---|---|---|---|---|
| Swiss minimal | strict grid, near-black on white, one accent, radius 0-4, no shadows | companies, pharmacy, invoices, back office | template-y without a strong typeface | Good |
| Poster minimal | one giant headline (clamp 3-12rem, 900), one hot accent, radius 0 | portfolio, launch, fashion | useless for catalogues and forms | Partial |
| Editorial magazine | asymmetric columns, pull quotes, big photos | story pages, menus with a story, reports | drop caps have no Arabic equivalent | Partial |
| Flat touch-first | solid colour blocks, zero shadow, 48px targets, press 0.97 | POS, kiosks, onboarding | can look unfinished; #3B82F6 fails white text (3.68), use #1D4ED8 | Good |
| Soft UI | low soft shadows, ~10px radius, calm colours | clinics, business tools | the generic "modern SaaS" look unless the palette is distinctive | Good |
| Bento grid | mixed-span rounded tiles on light grey | feature showcases, dashboards home | an overused template tell; bad for dense tables | Good |
| Brutalism | raw type, visible borders, instant states, radius 0 | design portfolios, counter-culture | clients may read it as broken | Good |
| Neubrutalism | thick black outlines, hard offset shadows, bright fills | youth shops, events, creative tools | a 2022-24 trend; playful only | Good |
| Bauhaus | red/blue/yellow geometric blocks, poster energy | studios, culture, brand-forward apps | abrupt 0ms states | Partial |
| Vibrant blocks | big saturated sections, large type, scroll-snap | food delivery, youth brands, events | the data's neons are garish; use brand hues | Good |
| Cinema dark | layered near-blacks, one accent, crisp borders | night-mode POS, dev tools, media | glow overuse is a tell; avoid pure #000 | Good |
| Data-dense dashboard | 12-column widgets, 36px rows, 12-14px text | POS back office, admin, analytics | cramped if used for marketing | Good |
| Material 3 | tonal surfaces, pill buttons, state layers | Flutter/Android apps, POS | the stock M3 purple is generic: seed your own colour | Good |
| Nature distilled | muted clay, sand, olive, soft organic radii | cafes, bakeries, organic, artisan | the cream+serif+sage "tasteful default" trap | Good |
| Paper / e-ink | paper off-white, ink black, no motion, reading first | text menus, documents, long reads | low energy for selling | Good |
| Vintage analog | faded film tones, grain, polaroid frames | cafes, photographers, retro brands | filters cost performance; can turn muddy | Good |
| Academia | mahogany dark, parchment, brass, serif | heritage restaurants, bars, premium courses | heavy and niche | Partial |
| Hand-drawn | paper texture, wobbly borders, marker type | kids, playful menus, craft | unprofessional for money or legal | Partial |
| Tactile skeuo | real materials, glossy pressable buttons | premium hardware, games | heavy, dated if overdone; imitation material is a tell | Good |
| 3D showcase | rotatable product on a studio backdrop | car dealers, furniture, electronics | heavy; needs photo + spec fallback | Good |
| Platform kits | Fluent, Polaris, Material as-is | apps living inside that platform | not a look to borrow outside it | Depends |

**Modifiers** (offer separately; combine with any style): motion intensity (none / subtle / standard), micro-interactions, kinetic headline, density (spacious / standard / dense, e.g. spacing 4/8/24/32/48/64/96 vs 2/4/8/12/16/24/32), accessibility-first (7:1 text, 3-4px focus rings).
**Avoid as defaults:** glassmorphism, aurora/mesh gradients, synthwave, Y2K, cyberpunk/terminal outside games and dev tools, claymorphism outside kids' products.

## 2. Palettes by trade

Format: primary (text on it) · secondary · accent (text on it) · background · text · border. Where white text failed on a data colour, the darker fix that passes is given instead, with the original in brackets.

**Restaurant / food / cafe** (avoid blue for appetite; always add an icon to errors when primary is red)
- A. Appetising red + gold: #DC2626 (white 4.83) · #F87171 · #A16207 (white 4.92) · bg #FEF2F2 · text #450A0A · border #FECACA
- B. Cafe brown + cream: #92400E (white 7.09) · #B45309 · accent of your own (the data collapsed it into primary) · bg #FEF3C7 · text #78350F · border #FDE68A
- C. Terracotta + herb green: #9A3412 (white 7.31) · #C2410C · #047857 (white 5.48) [#059669] · bg #FFFBEB · text #0F172A
- D. Dark roast: #3C2415 (white) · #6F4E37 · #A67B5B (decoration only) · bg #DEB887 · text #1A0F09 (10.1)
- E. Burgundy fine dining: #722F37 (white 9.65) · #800020 · #A52A2A (white 7.08) · bg #FDF5E6 · text #2C1810 (15.6)
- F. Earthy artisan: #8B4513 (white 7.10) · #6B7B3C (white 4.64) · clay #C67B5C (large text only) · bg #F5F0E1 · text #1A1A1A

**POS / retail** (no POS row in the data; built from inventory, invoice and kiosk rows; status colours always with an icon or text)
- A. Industrial slate + stock green: #334155 (white 10.35) · #475569 · #047857 [#059669] · bg #F8FAFC · text #0F172A
- B. Navy + paid green: #1E3A5F (white 11.5) · #2563EB · #047857 · bg #F8FAFC · text #0F172A · status Draft/Sent/Paid/Overdue
- C. Kiosk dark: surfaces #0F172A / #1E293B · action #B91C1C (white 6.47) [#EF4444] · bg #020617 · text #F8FAFC · targets 56px+
- D. Flat touch-first: #1D4ED8 (white 6.70) [#3B82F6] · #10B981 (black 8.28) · #F59E0B (black 9.78) · bg #FFFFFF · text #111827
- And the warm option from real work: neutrals mixed from the brand's own colours, the brand colour on the frame only, warm black (e.g. #16120F) for dark mode.

**Pharmacy / healthcare** (avoid red as the brand colour, avoid AI purple)
- A. Pharmacy green + trust blue: #15803D (white 5.02) · #22C55E · #0369A1 (white 5.93) · bg #F0FDF4 · text #14532D (8.7)
- B. Medical teal: #0E7490 (white 5.36) [#0891B2] · #22D3EE · #16A34A (black) · bg #F0FDFA · text #134E4A
- C. Clinical blue: #0369A1 (white 5.93) [#0284C7] · #0891B2 · #16A34A · bg #F0F9FF · text #0C4A6E
- D. Ocean teal calm: #008080 (white 4.77) · #20B2AA (decoration) · bg #E0FFFF · text #0F4C5C

**Construction / contracting / industrial**
- A. Industrial grey + safety orange: #64748B (white 4.76) · #94A3B8 · #C2410C (white 5.18) [#EA580C] · bg #F8FAFC · text #334155
- B. Orange-led: #F97316 (black 7.49; never white, 2.80) · #334155 (white 10.35) · #CA8A04 (black 7.15) · bg #FFFFFF · text #1F2937
- C. Black + gold (architecture): #171717 (white 17.9) · #404040 · #A16207 (white 4.92) · bg #FFFFFF
- D. Steel: #374151 (white 10.3) · #4B5563 · #9CA3AF (borders only) · bg #F9FAFB · text #111827
- E. Trust blue + urgent orange: #1E40AF (white 8.72) · #3B82F6 · #C2410C · bg #EFF6FF · text #1E3A8A

**Plastics / manufacturing** (built from manufacturing identity data; content usually needs product families, material grades, certifications, minimum order quantities, colour swatches, factory photos, request-a-quote)
- A. Industrial raw bold: #374151 (white 10.3) · #1F2937 · #F97316 (black 7.49) · bg #FFFFFF · surface #D6D3D1
- B. Warm grey raw: #374151 · #78716C (white 4.80) · #F97316 · bg #D6D3D1 · text #1F2937
- C. B2B navy + blue action: #0F172A · #334155 · #0369A1 (white 5.93) · bg #F8FAFC · text #020617
- D. Marine navy (clean polymer): #0C2461 (white 14.6) · #1B4F72 · #2E86AB (large text only) · bg #EBF5FB · text #0A1628

**Portfolio / developer**
- A. Monochrome + one blue: #18181B · #3F3F46 · #2563EB (white 5.17) · bg #FAFAFA · text #09090B
- B. Poster black + vermilion: #FF3D00 on #0A0A0A (5.58) · text #FAFAFA · muted #737373 (not for small text, 4.18)
- C. Monochrome editorial: #000 / #FFF / muted #525252 (7.81)

**Automotive**
- A. Premium dark + action red: #1E293B (white 14.6) · #334155 · #DC2626 (white 4.83) · bg #F8FAFC
- B. Bold dynamic: #DC2626 · #1E3A8A (white 10.4) · #F97316 (black) · bg #FFFFFF · text #000
- C. Obsidian dark: #0B1215 · #1C2833 · #566573 (decoration) · bg #212F3D · text #ECF0F1 (11.9)

**Education / courses**
- A. Progress teal + achievement orange: #0F766E (white 5.47) [#0D9488] · #2DD4BF · #EA580C (black) · bg #F0FDFA · text #134E4A
- B. Kids learning: #2563EB (white 5.17) · #F59E0B · #EC4899 (black) · bg #EFF6FF
- C. Academia (premium): brass #C9A962 on #1C1714 (7.90) · #8B2635 (white 8.65) · text #E8DFD4

**Dashboards**
- A. Analytics blue + amber: #1E40AF (white 8.72) · #3B82F6 · #D97706 (black) · bg #F8FAFC · text #1E3A8A
- B. Dark finance: surfaces #0F172A / #1E293B · #22C55E (dark text 7.83) · bg #020617 · text #F8FAFC
- C. Achromatic ledger: greys + black, one brand hue only on the main data element

## 3. Type pairings (Latin + Kurdish/Arabic)

★ = a real sibling: the same family or a shared designer, so the two scripts match by design. Every Kurdish/Arabic face below was **checked against the full Sorani alphabet** (section 4). Popular fonts that lack Kurdish letters are left out on purpose.

| Voice | Latin | Kurdish/Arabic partner (all cover every Sorani letter) |
|---|---|---|
| Data, UI, POS, invoices | IBM Plex Sans | ★ IBM Plex Sans Arabic |
| Corporate, healthcare, manufacturing | Source Sans 3 | ★ Mada (shares a designer with Source Sans) |
| Clinics, pharmacy | Figtree + Noto Sans | ★ Noto Sans Arabic |
| Brands already using Montserrat | Montserrat | the client's own Kurdish face, or Noto Kufi Arabic / Beiruti at a matching weight (Alexandria, Montserrat's Arabic sibling, lacks Kurdish letters) |
| Retail, e-commerce | Nunito Sans, Figtree | Vazirmatn, Fustat, Beiruti |
| Playful, kids, rounded brands | Baloo 2 / Fredoka | Playpen Sans Arabic, Zain (check joins by eye) |
| Restaurant, menus, elegant | a characterful serif with a reason | Amiri or Noto Naskh Arabic headings + Vazirmatn body |
| Bold statement, events, construction | Bebas Neue / Barlow Condensed + Source Sans 3 | Noto Kufi Arabic Black, Kufam, or Noto Sans Arabic at narrow width (wdth 62.5) + Mada |
| Editorial, reading | Literata, Crimson Pro, EB Garamond | Noto Naskh Arabic, Vazirmatn (+ Parastoo as its serif), Scheherazade New |
| Luxury | Bodoni Moda + Jost | Amiri or Noto Naskh Arabic headings + Vazirmatn light body |
| Heritage, calligraphic accent | Abril Fatface (hero only) | Aref Ruqaa display + Noto Naskh Arabic |

Generic defaults that don't count as a designed option: Inter + Inter, Poppins + Open Sans, Roboto (except a deliberate Material look).

## 4. Arabic-script Google fonts

All are OFL. Google's `arabic` subset tag does **not** mean a font can write Kurdish. On 2026-10-22 every font below was downloaded from the official google/fonts repository and checked with `glyph_check.py` against all 34 Sorani letters, Eastern digits, Arabic punctuation and Latin.

**Cover every Sorani letter (safe for Kurdish):**

| Family | Weights | Variable | Best role |
|---|---|---|---|
| Noto Sans Arabic | 100-900 | wght + width 62.5-100 | UI workhorse; condensed for tight spaces |
| Noto Kufi Arabic | 100-900 | wght | geometric headings and UI, heavy weights for food brands |
| Noto Naskh Arabic | 400-700 | wght | reading serif, formal |
| IBM Plex Sans Arabic | 100-700 | no | UI, data, POS (pairs with IBM Plex Sans) |
| Vazirmatn | 100-900 | wght | UI body and headings, long text |
| Mada | 200-900 | wght | UI (Source Sans sibling) |
| Beiruti | 200-900 | wght | UI and headings |
| Fustat | 200-800 | wght | UI |
| Estedad | 100-900 | wght | UI |
| Zain | 200-900 + italics | no | rounded UI (check joins by eye) |
| Kufam | 400-900 | wght | geometric headings |
| Reem Kufi | 400-700 | wght | geometric Kufi headings (lacks some Arabic punctuation) |
| Amiri | 400/700 | no | classical Naskh, formal, menus |
| Scheherazade New, Lateef, Harmattan | various | no | reading text (SIL) |
| Parastoo | 400-700 | wght | serif partner for Vazirmatn |
| Playpen Sans Arabic | 100-800 | wght | playful, handwritten |
| Aref Ruqaa | 400/700 | no | calligraphic headings (lacks some Arabic punctuation) |
| Jomhuria, Katibeh | 400 | no | display only |

**Lack Kurdish letters (don't offer for Kurdish text):** each falls back to another font for the missing letters, which gives mixed shapes inside words.

| Family | Missing |
|---|---|
| Alexandria, Almarai, Cairo, Changa, El Messiri, Lalezar, Lemonada, Markazi Text, Rakkas | ڕ ڵ ە ۆ ێ |
| Rubik | ڕ ڵ ھ ە ۆ ێ |
| Baloo Bhaijaan 2 | ڕ ڵ ۆ ێ |
| Alyamama | ە |
| Readex Pro | پ چ ڕ ژ ک گ ڵ ھ ە ۆ ی ێ (Arabic only) |
| Tajawal | چ ڕ ژ ک گ ڵ ھ ە ۆ ی ێ (Arabic only) |

These are fine for Arabic-only pages. Fonts not listed here haven't been checked: run `glyph_check.py <font> --sets kurdish` first, and render `بەخێربێن بۆ چێشتخانەکەمان · ڕۆژ · گوڵ · ڤیدیۆ · پارە · ھ`.

Brand-licensed Kurdish families seen in real client work (not on Google Fonts): the UniSIRWAN family (Adelle, Somar, Ping). Use only with the client's licence.

## 5. Page patterns

| Pattern | Order | Use when |
|---|---|---|
| Hero-centric | full-bleed hero, value strip, key proof, action | visual-led: restaurants, cars, construction (only with real photos) |
| Trust and authority | credibility hero, proof (certificates, numbers), solution, contact/quote | pharmacy, clinics, B2B, manufacturing, contractors |
| Minimal single column | headline, short description, 3 benefits at most, action | one offer, a freelancer, a consultant |
| Product demo | hero, the product working, breakdown, action | easier shown than told |
| Before/after | problem, slider comparison, how it works, results | renovation, cleaning, design work (buttons as a drag alternative) |
| Marketplace / directory | search hero, categories, featured, trust | car stock, listings: search is the action |
| Portfolio grid | name and role, grid, about, contact | designers, developers, photographers |
| Event | date/place/countdown, programme, register | events; the deadline written as text |
| Pricing | value, plans with real totals, compare, FAQ | price is the decision |
| Storytelling | hook, problem, journey, solution, action | brand story; must read fine without effects |
| App showcase | device, real screenshots, features, download | a POS companion or customer app |

Rules for all: CTA text at 4.5:1 on its fill, proof only when real and dated, and every carousel, video, countdown or ticker can pause and has a still state under reduced motion.

## 6. Print identity styles

Business card 85x55 mm, print-ready PDF, 3 to 5 mm bleed, 300 dpi, two typefaces at most. Mirror the layout on the Kurdish/Arabic side.

| Style | Colours | Type | Finish | For / not for |
|---|---|---|---|---|
| Corporate minimal | #0F172A #1E3A8A white / #64748B #E2E8F0 | geometric sans | matte, spot UV | consulting, legal / youth |
| Classic traditional | #0F172A #1E3A8A #D4AF37 | traditional serif | emboss, gold | heritage, law / startups |
| Swiss minimal | white #000 #DC2626 | grid sans | matte | architecture, corporate / ornate |
| Monochrome elegant | #000 white #D4AF37 | serif + sans | foil, emboss | luxury, photography / playful |
| Dark premium | #0F0F0F #1A1A1A #D4AF37 | bold sans | matte + metallic | nightlife, premium cars / medical |
| Industrial raw | #374151 #78716C #F97316 | condensed bold | raw textures | manufacturing, construction / luxury |
| Bold dynamic | #DC2626 #F97316 #FBBF24 | condensed bold | gloss | sports, automotive / calm corporate |
| Warm organic | #8B4513 #228B22 #DEB887 | friendly serif | kraft, uncoated | organic food, cafes / tech |
| Retro vintage | #8B4513 #CA8A04 #DC2626 | vintage serif | letterpress | food, beverage, artisan / tech |
| Fresh modern | #10B981 #0EA5E9 white | rounded sans | matte | pharmacy, clinics / heavy industry |

Avoid as defaults: "modern tech" (indigo/violet gradients) and "gradient modern": both are AI-look tells in print too.
