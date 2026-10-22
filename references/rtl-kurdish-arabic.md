# Kurdish, Arabic and right-to-left

Most of these rules come from real bilingual and trilingual client work (menus, business cards, letterheads, sites, point-of-sale apps). Every rule here was learned by getting it wrong once.

## Contents
1. The short version
2. Fonts
3. Size, line height and what never to do to Arabic script
4. Mirroring
5. Numbers, prices and mixed direction
6. Words: who writes the Kurdish
7. Web setup
8. Flutter setup
9. Word and PDF
10. Checks before showing anything

---

## 1. The short version

1. The client's brand fonts and files are the reference. Stand-ins have been rejected every time.
2. Judge nothing rendered in a substitute font. Load the real files first.
3. Kurdish and Arabic need optical size compensation, about **1.09x to 1.15x** the Latin size depending on the pair. Pick it by eye from side-by-side renders.
4. Never letter-space, fake-uppercase, stroke, italicise or split Arabic-script text into letters. Open the line height.
5. Use logical properties and directional widgets only. The right-to-left version is a true mirror of the left-to-right master, reading order included.
6. Western or Eastern digits is the client's call, asked once and recorded. Signed numbers, phones, URLs and Latin names live in isolated left-to-right runs.
7. Any Kurdish Claude writes is a draft for a native speaker's read. Never "correct" the client's spelling.

## 2. Fonts

**Sorani needs these letters beyond Arabic:** ڕ ڵ ێ ۆ ە ڤ پ چ ژ گ, plus the Kurdish forms ی ک (not Arabic ي ك). Check coverage with `scripts/glyph_check.py <font> --sets kurdish` and render a real Kurdish sentence, never lorem ipsum.

Seen working:

| Font | Use | Notes |
|---|---|---|
| Client's brand face (e.g. the UniSIRWAN family: Adelle, Somar, Ping) | Everything, when the brand has one | Licensed per client; ask, and don't write licence claims yourself. Somar has every Kurdish letter but no ®. Ping also has a full Latin set (one face can set a bilingual lockup), but no box-drawing glyphs. |
| IBM Plex Sans Arabic | App UI, safe default and fallback | Latin + Arabic + every Kurdish letter. Pairs with IBM Plex Mono for money. |
| Noto Kufi Arabic (headings) + Noto Sans Arabic (text) | Websites without a brand Arabic face | Free, wide coverage. |
| Vazirmatn (text) + Noto Kufi Arabic (headings) | Long reading, reports | |
| Rounded faces (e.g. Zain) to match a rounded Latin brand | Playful brands | Check joins by eye (a ک-ڕ join came apart until kerning was turned off). |

- **"Arabic" is not "Kurdish".** Many popular Arabic Google Fonts lack Sorani letters (checked 2026-10-22): Alexandria, Almarai, Cairo, Changa, El Messiri, Lalezar, Lemonada, Markazi Text, Rakkas and Rubik miss ڕ ڵ ە ۆ ێ, and Readex Pro and Tajawal miss even پ چ ژ ک گ ی. Full coverage list in `catalogs.md` section 4.
- **One family per script per document.** Never mix two Kurdish faces inside one language's content.
- **Pair by voice and weight.** A heavy food-brand Latin (Montserrat Black) wants a heavy Kurdish face (Adelle ExtraBold), not a light text face.
- **Symbols are font characters too.** ➜ ✎ ® • and box-drawing characters have printed as boxes or wrong shapes. Use SVG icons for UI symbols, and check every special character with `glyph_check.py --scan <src>`.
- Fallback stack: brand face, then a wide-coverage face (IBM Plex Sans Arabic or Noto Sans Arabic), then `system-ui`.

## 3. Size, line height and what never to do to Arabic script

- **Size compensation.** Arabic-script letter bodies are short next to Latin capitals, so the same point size reads smaller. Factors that worked: about 1.15x in print and 1.14x on the web for a bold display pair, 1.1x in a Flutter theme, and 1.09x for a text face in Word. **This is a choice to offer**: render 3 sizes side by side (for example 1.06x / 1.10x / 1.14x) and let them pick. At a first, larger guess, the Kurdish was judged to look bigger than the English. Ink-height measurements mislead, so the eye decides.
- Don't scale Latin digits (prices) by the Kurdish factor.
- **Line height:** about 1.55 for headings and 1.6 to 1.85 for text. Latin-tight leading (1.05 to 1.15) made diacritics hit the line above.
- **Never:** letter-spacing (positive or negative, because it breaks the joins), uppercase emphasis (the script has no case), text stroke, synthetic italics, or letter-by-letter animation. Emphasise with weight, size or colour instead. Animate whole words or lines, or reveal intact text with a mask.
- Every tracked Latin style (eyebrows, buttons, labels) must reset under right-to-left: `ltr:tracking-wide`, or `:lang(ckb) { letter-spacing: normal }`.
- English labels that rely on spaced capitals become slightly larger plain text in Kurdish.
- **Room to grow:** Kurdish often runs longer (one English nav word became three). Use `whitespace-nowrap` where a label must stay on one line, give boxes room, and test overflow at 1.3x text scale.

## 4. Mirroring

- **Logical properties only.** Use `margin-inline`, `padding-inline`, `inset-inline-start`, `text-align: start`, and in Tailwind `ms-/me-/ps-/pe-/start-/end-/text-start/text-end/border-s/border-e/rounded-s/rounded-e`. Flutter: `EdgeInsetsDirectional`, `AlignmentDirectional`, `PositionedDirectional`, `BorderRadiusDirectional`, `TextAlign.start`. One stylesheet then serves both directions.
- **Don't add `flex-row-reverse` "for RTL".** Flex already follows `dir`, so it flips twice. Use `gap` rather than `space-x`.
- **Things that don't flip by themselves:** `translateX`, keyframes, `background-position`, shadow x-offsets, `scrollLeft`, rotations and tilts, gradient directions. Give them `rtl:` variants. A tilted sticker should lean the same way relative to the reading direction.
- **Mirror** arrows, chevrons, back buttons, progress, sliders, carousels and slide directions. **Never mirror** logos, play/pause and media controls, checkmarks, clocks, or a speaker icon.
- **Reading order mirrors too.** Timelines, step flows, table column order and cascades run right to left, and bullets, number badges and accent bars move with their text. Right-aligning text inside a left-to-right layout is not right-to-left. That was rejected as "the text is not in the right alignment".
- **Build the right-to-left page as an exact mirror of the master** (same grid, sizes and spacing). A Kurdish page built on its own overflowed and had to be rebuilt as a mirror.
- The brand panel or logo sits on the **leading edge**: left on the English side, right on the Kurdish/Arabic side. Use the logo pack's Arabic-led variant if it has one.
- A bilingual one-pager without mixing languages: English on the left, the price on the centre line, Kurdish on the right, one type scale, and never two languages inside one line.

## 5. Numbers, prices and mixed direction

- **Digits are a choice.** Offer Western (0-9) vs Eastern (٠-٩) once, and record the pick in DESIGN.md. One Kurdish menu used Western digits on purpose. `Intl` with `ckb` or `ar-IQ` gives Eastern digits by default, so set `numberingSystem: "latn"` or `"arab"` deliberately.
- Store and export ASCII digits. On input, normalise both ٠-٩ and ۰-۹ (the Persian forms some keyboards type).
- **Isolate** anything that must stay left-to-right inside Kurdish/Arabic text: signed numbers, percentages, phones, emails, URLs, times, codes and Latin names. On the web use `<bdi>`, `dir="ltr"` or `unicode-bidi: isolate`, and `dir="auto"` for user names. In Flutter strings use U+2066 ... U+2069 (write the escapes). A minus sign has flipped sides before.
- "·" next to Kurdish digits reads as the Kurdish zero ٠. Use a colon or parentheses.
- **Prices:** tabular figures at the inline end of the row, a non-breaking space between amount and unit, and no decimals for IQD. Pick "IQD" or "د.ع" once and keep it consistent. Never write "IQD · IQD", and drop redundant "all prices in IQD" lines.
- Proofread every Eastern-digit number. A misplaced separator once made a price read ten times too high.

## 6. Words: who writes the Kurdish

- The person's or the client's own Kurdish wording always wins. List every string Claude wrote in DESIGN.md under "Text to check".
- Keep the client's spelling exactly, including their keyboard letters. If they typed ی ک, don't swap in Arabic ي ك. Flag any deviation; never fix it silently.
- Never literally translate a brand name (one site invented an Arabic brand name the client had never used), and never transliterate a personal name (it invents a spelling). Latin names stay Latin.
- Kurdish Sorani is `ckb` (lang attribute and locale). Kurmanji in Latin script is `kmr` and runs left-to-right.

## 7. Web setup

- Give each language its own URL (`/en`, `/ckb`, `/ar`), and server-render `<html lang dir>`. Switching language is a full page load (a clean right-to-left first paint). Switcher links get `hrefLang`. A CSS-only language toggle meant search engines only saw English.
- Self-host fonts as woff2. Write one `@font-face` per script with `unicode-range: U+0600-06FF, U+0750-077F, U+08A0-08FF, U+FB50-FDFF, U+FE70-FEFF, U+200C-200F` so Kurdish files load only when Kurdish text is on the page. Don't preload Arabic faces on English pages, and keep switcher links from prefetching right-to-left routes.
- Arabic web fonts are the main speed cost on budget Android, and their arrival shifts layout. Font weights, `preload` and `font-display` strategy are choices to offer.
- If font files are gitignored (licensing), a fresh clone and the host's build fall back silently. Make sure the build gets the files.
- After every layout change, check 390px and 1440px in each language. Nothing may scroll sideways at any width.

## 8. Flutter setup

- Flutter ships no Material localizations for `ckb`. Add `localizationsDelegates` with a fallback delegate that serves Arabic Material strings for `ckb`, plus `supportedLocales: [Locale('ckb'), Locale('ar'), Locale('en')]`. Without it, the app renders left-to-right.
- Use directional widgets only (section 4). Material's own back/forward arrows flip by themselves. Custom or asset icons don't: wrap them in `Transform.flip(flipX: Directionality.of(context) == TextDirection.rtl)`.
- Theme the size factor once (`TextTheme.apply(fontSizeFactor: 1.1)` for ckb/ar), then check every Kurdish layout for overflow at 1.3x text scale. A layout overflow should fail a test.
- Bundle the fonts in `pubspec.yaml`. Use `fontFamilyFallback` for mixed text, money in a mono face with `FontFeature.tabularFigures()`.
- Thermal receipts and kitchen tickets: print them as images (thermal code pages can't shape Sorani). A4 documents go through a PDF with an embedded Arabic-script font.
- Take a screenshot tour of every screen (English, Kurdish, phone, dark) with the real fonts loaded.

## 9. Word and PDF

- **python-docx:** `font.size` writes `w:sz`, but right-to-left runs take their size from `w:szCs` (bold `w:bCs`, italic `w:iCs`). Without it, every Kurdish size change silently does nothing. Kurdish paragraphs need paragraph-level `w:bidi`, and then `w:jc` left/right mean start/end. Check bracket direction by zooming the render, not by reasoning about it.
- **Fonts in PDFs:** verify embedding with `pdffonts`. A `.ttf` can be CFF inside, and Word may still substitute it. `fsType = 4` (preview and print) means the PDF is the deliverable and the .docx is a working file.
- **Make PDFs from HTML** (WeasyPrint or Chrome) so shaping and bidi are handled. If you must draw text yourself (PyMuPDF), reshape with `arabic_reshaper` and reorder with `python-bidi`, then wrap lines yourself.
- In a sandbox, embed fonts as base64 woff2: a blocked font host falls back silently.

## 10. Checks before showing anything

- `python scripts/design_scan.py <project>`: physical left/right, letter-spacing on Kurdish, missing `dir`/`lang`, no Kurdish-capable font, Flutter widgets that ignore direction.
- `python scripts/glyph_check.py <font files> --scan <src>`: every character the project uses, against the real font stack.
- `node scripts/shoot.mjs <url> <out> --dir=rtl`: a quick look at the mirrored layout. Do a proper check per language route at 390 and 1440.
- Read the Kurdish renders yourself: joins intact, no clipped diacritics, digits as chosen, isolated runs in the right place.
