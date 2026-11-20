# Graphic pieces: posters, flyers, social posts, banners, ads

A graphic piece has one job and a few seconds to do it: stop someone, say one thing, and tell them what to do. This file covers posters and flyers (read `print.md` for bleed and print files), social media posts, stories and carousels, banners and ads. Menus, cards and letterheads stay in `print.md`; packs in `packaging.md`.

## Contents
1. The job and the one message
2. Layout: grid, hierarchy, reading path
3. Type for distance and for phones
4. Sizes and safe zones
5. Series, templates and campaigns
6. Bilingual and right-to-left pieces
7. Photos, colour and contrast
8. Making the files (code, Canva, Figma)
9. Honest claims
10. Review checklist

---

## 1. The job and the one message

Before options, write three lines with the person (fact questions where only they know the answer):
- **The action:** what should the viewer do (come on Friday, order on WhatsApp, follow, call, scan).
- **The one message** in seven words or fewer, in each language. Everything else is supporting detail.
- **Where it's seen:** a phone feed while scrolling, a story tapped through in two seconds, a poster on a café wall at 2 m, a roll-up banner at an event, a flyer in the hand.

Then three levels of reading: **1 second** (the focal point: one image, word or number), **3 seconds** (the message and who it's from), **details** (date, place, price, contact, QR). If a poster needs more than three seconds to get, cut words before shrinking type.

## 2. Layout: grid, hierarchy, reading path

- **One focal point.** Make it win by scale (the headline at least three times the body size), by isolation (space around it) or by colour. Two equal focal points cancel out.
- **A grid under everything:** outer margins of about 5 to 8% of the short side, a column grid (4 to 6 columns for posters and posts, 12 on large formats) and a baseline for text blocks. Align edges to it; centring everything is a default, not a decision (`review.md` section 6).
- **Reading path:** Latin pieces read top left to bottom right (Z path); Kurdish and Arabic pieces mirror it, starting top right. Put the action where the path ends.
- **Group by proximity:** date, time and place together; contact details together. Fewer boxes and lines, more alignment and space (`craft.md` section 4).
- **Text over photos** gets a calm area of the photo, a solid panel or a scrim, and its contrast is measured on the real pixels.
- Offer layout options that differ in structure (type-led, photo-led, colour field, grid of information, collage), dealt with `python scripts/deal.py --kind graphic --sector <trade> --have <assets>`.

## 3. Type for distance and for phones

**Print, by viewing distance:** for comfortable reading, the capital height should be about 1/120 of the distance (25 mm at 3 m). Typical starting points:

| Piece | Seen from | Headline | Body / details |
|---|---|---|---|
| A5 flyer | in the hand, 40 cm | 28 to 48 pt | 9 to 11 pt |
| A3 poster | 1 to 2 m | 72 to 140 pt | 14 to 20 pt |
| A2 / A1 poster | 2 to 4 m | 140 pt and up | 24 to 36 pt |
| Roll-up banner | 3 to 6 m | 200 pt and up | 60 pt and up; few words |

**Phones:** a 1080 px wide post is shown about 2.5 to 3 times smaller on a phone. On a 1080 px canvas, nothing under about 32 px, details 36 to 48 px, headlines 80 px and up, at most about 20 words on a single post. Read the export at real phone size before showing it.

Kurdish and Arabic follow `rtl-kurdish-arabic.md`: 1.09 to 1.15x the Latin size, open line height, never letter-spaced or stretched to fill a line.

## 4. Sizes and safe zones

Platforms change these; check the platform's own help page before a big campaign (sizes below checked November 2026).

| Placement | Size (px) | Notes |
|---|---|---|
| Instagram feed post | 1080 x 1350 (4:5) | the reliable default, and the shape to use for boosted posts and ads |
| Instagram, matching the profile grid | 1080 x 1440 (3:4) | the profile grid shows every post as a 3:4 tile, so keep key content in a centred 3:4 area on 4:5 posts |
| Instagram square | 1080 x 1080 | still accepted; looks cropped in the 3:4 grid |
| Carousel | every slide the same ratio as the first | design seams so a continuous image breaks at slide edges cleanly |
| Stories, Reels, WhatsApp status, TikTok | 1080 x 1920 (9:16) | keep text and logos out of the top ~14% and bottom ~20% (stories) to ~35% (reels), and ~6% at each side; TikTok's buttons sit on the right |
| Meta ads | 1440 x 1800 feed, 1440 x 2560 stories and reels | Meta's recommended ad sizes, same safe zones |
| YouTube thumbnail | 1280 x 720 | the face or object and 3 to 4 words; readable at 200 px wide |

Print formats: A5 148 x 210 mm, A4 210 x 297, A3 297 x 420, A2 420 x 594, A1 594 x 841, plus 3 mm bleed on each edge. Roll-up banners vary (85 x 200 cm is common); take the size and safe area from the printer's template, because the bottom of a roll-up hides inside the stand.

## 5. Series, templates and campaigns

- **One key visual, many formats:** design the main piece once (the idea, the type treatment, the colour), then adapt it to each size with its own composition. A poster shrunk to a story is not an adaptation.
- **Fixed vs flexible:** write down what never changes (logo position, typefaces, colour roles, frame) and what changes per post (photo, headline, number). That list goes in DESIGN.md.
- **Templates the client can use:** when they will post by themselves, build the series as Canva templates (brand kit fonts and colours, locked frame elements, clear text boxes) or as an HTML template with the data at the top. Test each template with the longest real Kurdish and English text.
- **Profile grid:** plan nine posts together in the 3:4 grid; alternate photo-led and type-led posts so the grid breathes.
- **Campaign check:** put every format side by side on one sheet; they should read as one family at a glance.

## 6. Bilingual and right-to-left pieces

- **Which language leads** is a decision per piece; in the Kurdistan Region, Kurdish usually leads for local audiences.
- **Options:** one piece per language (cleanest for posters and posts), or one piece with a clear lead language and the second smaller, or a mirrored two-half layout (`deal.py` card "Mirrored bilingual"). Never two scripts inside one line.
- Kurdish and Arabic versions are mirrors of the Latin master, not the same layout with right-aligned text: the reading path, arrows, sequences, and the side the image sits on all flip (`rtl-kurdish-arabic.md` section 4).
- Dates, times, prices, phone numbers, handles and URLs sit in isolated left-to-right runs, with the digits the client picked.
- Every string Claude wrote goes on the "Text to check" list for a native read before anything is published or printed.

## 7. Photos, colour and contrast

- Real photos of the real place, product and people (`craft.md` section 6). One strong crop beats four weak photos.
- Strong, flat colour fields carry posters well; pick them from the brand and the inventory, not a trend.
- Contrast holds outdoors and under kiosk light: body text at least 4.5:1 and large text 3:1, measured on the real background. Go a step darker and heavier for print (`print.md` section 3).
- Bright screen colours dull in CMYK; check brand colours before promising them on a printed poster.

## 8. Making the files (code, Canva, Figma)

Where the piece is made is a decision for the person, asked once and recorded in DESIGN.md:

- **Code (HTML/CSS/SVG):** exact control, real fonts, easy variants and languages from one data block. Social: set the page to the exact pixel size and shoot it with `node scripts/shoot.mjs post.html <out> --sizes=1080x1350 --scale=1` (PNG for type-heavy pieces, `--jpeg` for photo-heavy ones). Print: `@page` size plus bleed and `--pdf` (`print.md` section 4).
- **Canva, when the person works there and a Canva connector is available:** the design can be generated or built from the brand kit or a brand template, edited, resized to every format and exported, so the client can keep editing it themselves. Know its limits and say them in the option's cost:
  - colours are HEX/RGB; there are no Pantone swatches, and a CMYK PDF export (PDF Print, CMYK profile) needs a paid Canva plan;
  - bleed and crop marks are fixed sizes (turn on "Show print bleed", export "PDF Print" with "Crop marks and bleed");
  - no dieline layers, spot inks or overprint, so final packaging files are better made elsewhere;
  - Kurdish needs a Kurdish-capable font in the brand kit (`catalogs.md` section 4); check the joins in the exported file, not the editor.
- **Figma, when a Figma connector is available and the work lives there:** components and variants suit series and templates; export SVG and PNG per frame.
- Whichever tool: export, open the exported file, and look at it at real size before showing it.

## 9. Honest claims

No fake urgency ("only 2 left" when it isn't true), invented reviews, follower counts, ratings or prices; no before-and-after photos that were edited. Sample text is fine while designing, listed for the client to replace (`craft.md` section 7).

## 10. Review checklist

- [ ] The one message and the action are clear in three seconds at real size (phone or viewing distance).
- [ ] One focal point; a grid underneath; reading path mirrored for Kurdish and Arabic.
- [ ] Type sizes fit the distance; nothing under about 32 px on a 1080 px post.
- [ ] Safe zones respected for stories, reels and ads; the 3:4 grid crop checked for feed posts.
- [ ] Contrast measured on the real background; print colours checked for CMYK.
- [ ] Dates, prices, phones and handles correct and isolated left-to-right; Kurdish and Arabic checked by a native speaker.
- [ ] Every format of a campaign seen side by side.
- [ ] QR codes and links tested from the exported file.

Sources this file learned from: the poster-designer skill in alterlab-ieu/alterlab-fc-skills (MIT), restated in this skill's words, with social sizes and safe zones from Instagram's and Meta's published guidance as summarised in November 2026; see THIRD-PARTY-NOTICES.md.
