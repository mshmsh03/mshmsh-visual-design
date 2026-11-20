# Print: menus, business cards, letterheads, bags, flyers

Print forgives nothing after the run. This file covers building print pieces with code (HTML/CSS to PDF with WeasyPrint or Chrome, or python-docx for editable letters), checking them, and handing over files a print shop can use. Boxes, labels, pouches, cups and printed bags add their own rules in `packaging.md`; posters, flyers and banners add theirs in `graphic.md`; logos and stationery systems start in `identity.md`.

## Contents
1. Before designing
2. Sizes, bleed and safe zones
3. Type and colour on paper
4. Building the files
5. Checking the files
6. Options and client rounds
7. Handing over

---

## 1. Before designing

- **Start from the client's own artefacts.** Their blank template is the format reference, their website is the live brand system, and their printed menu is the north star. Three letterhead versions drawn from a brochure cover were rejected.
- **Match their fields exactly.** Don't add fields they declined, even if formal custom suggests them. Keep their spellings, titles and the order of names. Honorific titles always go with a person's name.
- **Ask the shop early** (as a question for the person): the cut size (local shops may cut 90x50 instead of 85x55), whether they want bleed and crop marks, the colour mode, and the paper.
- **Logo files:** use the real files, never a redrawn or retyped wordmark. Trim transparent padding to the visible edges, or the logo prints tiny. Know the "full lockup" from the "mark only".

## 2. Sizes, bleed and safe zones

| Piece | Trim | With 3 mm bleed |
|---|---|---|
| Business card (EU) | 85 x 55 mm | 91 x 61 mm |
| Business card (shop variant) | 90 x 50 mm | 96 x 56 mm |
| A4 menu / letter | 210 x 297 mm | 216 x 303 mm |
| A5 flyer | 148 x 210 mm | 154 x 216 mm |

- **3 mm bleed** on anything that touches the edge. Set the TrimBox in the PDF.
- **Safe zone:** keep text and logos at least 4 to 5 mm inside the trim (cards), and 8 to 10 mm on A4.
- WeasyPrint page setup: `@page { size: 85mm 55mm; margin: 0; bleed: 3mm; marks: crop; }`. `size` is the trim, and `bleed` grows the sheet around it. Draw the artwork to the bleed edge, keep content inside the safe zone, and confirm the boxes with `pdfinfo -box`.

## 3. Type and colour on paper

- **Minimum sizes:** nothing below 7.5 pt on a business card (a first scale was too small and was raised twice), 9 to 10 pt body on menus, and prices at least body size and bold enough to scan.
- Kurdish and Arabic sizing and line height follow `rtl-kurdish-arabic.md` (about 1.15x in print for bold display pairs).
- **Contrast is worse on paper.** Light grey text and thin weights disappear, so go a step darker and heavier than on screen. "Not very clear" meant darker and larger.
- **Colour:** screens are RGB and presses are CMYK. Brand colours can shift, especially bright oranges, greens and blues. Ask for one printed proof before the run. For spot-colour work (bags, stickers), the ink is the colour and the file only marks where it goes.
- **Images:** 300 dpi at final size. Vector for logos and line art.
- **QR codes:** keep the quiet zone (at least four modules of white around the code) and test-scan the printed proof.
- **Never print a year into a date field.** It goes stale.
- **Artwork behind text** needs a faded edge so it doesn't slice through a rule or line of text.

## 4. Building the files

- **HTML + CSS to PDF** handles Kurdish/Arabic shaping and bidi properly. Keep the data at the top of the file so text fixes are one-line edits.
  - **Chrome (easiest on Windows):** `node <skill>/scripts/shoot.mjs card.html <out> --pdf --name=card`. Set `@page { size: 91mm 61mm; margin: 0 }` (trim + bleed), draw backgrounds to the page edge, keep text inside the safe zone, and give each side its own page with `break-after: page`. Chrome writes no TrimBox or crop marks: tell the shop the trim size (85 x 55), or draw crop marks yourself in the bleed area.
  - **WeasyPrint** (where it installs): `@page { size: 85mm 55mm; bleed: 3mm; marks: crop }` writes TrimBox and crop marks for you.
- **Embed the real fonts** (`@font-face` with local files). In a sandbox, embed as base64 woff2, because a blocked font host falls back silently.
- **Browser print traps:** JavaScript-revealed content never appears in a programmatic PDF, background colours are off by default, and a dark-mode machine has printed a black page. So force the light palette in print CSS, use `break-inside: avoid` per card, and pre-split long lists with a continuation label.
- **Imposition (office printing):** an 8-up A4 sheet with crop marks. For duplex, flip on the long edge and mirror the back columns. Check each back page by eye (on the right-to-left side, the panel goes on the right).
- **Editable letters (.docx):** decoration goes in the header/footer as one anchored artwork behind text, never in the text flow. See `rtl-kurdish-arabic.md` section 9 for the right-to-left traps (`w:szCs`, `w:bidi`).
- **Canva** (when the person works there): turn on "Show print bleed", export "PDF Print" with "Crop marks and bleed" and, on a paid plan, the CMYK colour profile. Bleed and crop marks have fixed sizes and there are no spot colours, so check the shop accepts that (`graphic.md` section 8).

## 5. Checking the files

Measure; don't eyeball:
- `pdfinfo file.pdf` for page size and boxes, `pdffonts file.pdf` for every font embedded (subset is fine).
- Render each page to PNG at 300 dpi and look at it: Kurdish joins, digits, the logo's edge, and nothing in the bleed that should be inside.
- Pixel-scan margins when symmetry matters ("margins not equal" was a rejection).
- Read values back from the saved file, not from the build script. A patch that failed halfway once left the old logo size in the file while the log said it had changed.

## 6. Options and client rounds

- Show options as a PDF deck: an overview page with all options at the same scale, then one page per option at true size.
- Rounds narrow: five options, two liked, one chosen, then text-fix rounds. Read short client feedback ("the upper part is too simple") against the approved parts, and change only what it names.
- "Too simple" was fixed by adding the brand's real artwork (a line drawing taken from their own profile PDF), not by adding more rules and boxes.
- Anything beyond the brief is marked "beyond the brief: ask the client first".

## 7. Handing over

- One folder named `FINAL - Ready to Print` with:
  - the print-shop PDF (bleed, crop marks if asked, fonts embedded),
  - an A4 PDF for proofing or office printing,
  - 300 dpi PNG previews (re-export these whenever the PDF changes),
  - the overview sheet of options if the client is still choosing.
- Mark superseded files clearly ("outdated, don't print from these") or move them out. Use versioned file names, and update every note that names a file.
- Recommend printing one proof sheet before the full run, and say what you could not check (paper, ink shift, the shop's cutter).
