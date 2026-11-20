#!/usr/bin/env python3
"""
ean13.py - check a GTIN-13 and draw its EAN-13 barcode as an SVG at exact millimetre size.

For the client's real GS1 number only. It never invents a number. A wrong check digit almost
always means a typo in the brief, so the script stops and says which digit it expected.

Usage:
    python ean13.py 626123456789          # 12 digits: computes and appends the check digit
    python ean13.py 6261234567893         # 13 digits: verifies the check digit
    python ean13.py 6261234567893 --mag 100 --out barcode.svg
    python ean13.py 6261234567893 --mag 80 --no-text --out small.svg
    python ean13.py --check 6261234567893   # only verify, print the sizes, write nothing

Options:
    --mag N        magnification in percent, 80 to 200 (default 100). Nominal module 0.33 mm.
    --out FILE     write the SVG here (default: ean13-<number>.svg)
    --no-text      leave out the human-readable digits (only if the pack prints them elsewhere)
    --font NAME    font for the digits (default: OCR-B with monospace fallbacks)
    --bar COLOUR   bar colour (default #000000). Dark colours only; red, orange and yellow don't scan.
    --check        verify and print sizes only

Sizes follow the GS1 General Specifications: at 100% the symbol is 37.29 mm wide including the
quiet zones (11 modules left, 7 right), bars are 22.85 mm tall, guard bars 1.65 mm longer, and the
whole symbol with digits is 25.93 mm tall. Everything scales with --mag. Bars are drawn at nominal
width: ask the printer whether they want bar width reduction for their press, and test-scan the
printed proof.
"""
import argparse
import re
import sys

L = ["0001101", "0011001", "0010011", "0111101", "0100011",
     "0110001", "0101111", "0111011", "0110111", "0001011"]
G = ["0100111", "0110011", "0011011", "0100001", "0011101",
     "0111001", "0000101", "0010001", "0001001", "0010111"]
R = ["1110010", "1100110", "1101100", "1000010", "1011100",
     "1001110", "1010000", "1000100", "1001000", "1110100"]
PARITY = ["LLLLLL", "LLGLGG", "LLGGLG", "LLGGGL", "LGLLGG",
          "LGGLLG", "LGGGLL", "LGLGLG", "LGLGGL", "LGGLGL"]

MODULE_MM = 0.33          # X-dimension at 100%
QZ_LEFT, QZ_RIGHT = 11, 7  # quiet zones in modules
BAR_MM = 22.85            # normal bar height at 100%
GUARD_EXTRA_MM = 1.65     # guard bars extend 5 modules further down
TOTAL_H_MM = 25.93        # whole symbol with digits at 100%
DIGIT_MM = 2.75           # digit height at 100% (GS1 recommends OCR-B)


def check_digit(first12):
    total = sum(int(d) * (3 if i % 2 else 1) for i, d in enumerate(first12))
    return (10 - total % 10) % 10


def modules(code):
    first, left, right = int(code[0]), code[1:7], code[7:13]
    bits = "101"
    for digit, kind in zip(left, PARITY[first]):
        bits += (L if kind == "L" else G)[int(digit)]
    bits += "01010"
    for digit in right:
        bits += R[int(digit)]
    bits += "101"
    assert len(bits) == 95
    return bits


def guard_positions():
    # module indexes (within the 95) that belong to the start, centre and end guards
    return set(range(0, 3)) | set(range(45, 50)) | set(range(92, 95))


def looks_unscannable(colour):
    m = re.fullmatch(r"#?([0-9a-fA-F]{6})", colour.strip())
    if not m:
        return False
    r, g, b = (int(m.group(1)[i:i + 2], 16) for i in (0, 2, 4))
    lum = 0.2126 * r + 0.7152 * g + 0.0722 * b
    reddish = r > 150 and r > g + 40 and r > b + 40
    return lum > 110 or reddish


def build_svg(code, mag, text=True, font=None, bar="#000000"):
    s = mag / 100.0
    x = MODULE_MM * s
    width = (QZ_LEFT + 95 + QZ_RIGHT) * x
    height = (TOTAL_H_MM if text else BAR_MM + GUARD_EXTRA_MM) * s
    bar_h = BAR_MM * s
    guard_h = (BAR_MM + GUARD_EXTRA_MM) * s
    bits = modules(code)
    guards = guard_positions()

    rects = []
    i = 0
    while i < 95:
        if bits[i] == "1":
            j = i
            while j < 95 and bits[j] == "1":
                j += 1
            is_guard = i in guards
            h = guard_h if is_guard else bar_h
            rects.append(f'<rect x="{(QZ_LEFT + i) * x:.4f}" y="0" width="{(j - i) * x:.4f}" height="{h:.4f}"/>')
            i = j
        else:
            i += 1

    parts = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width:.3f}mm" height="{height:.3f}mm" '
        f'viewBox="0 0 {width:.4f} {height:.4f}" shape-rendering="crispEdges">',
        f'<title>EAN-13 {code} at {mag:g}%</title>',
        f'<rect width="{width:.4f}" height="{height:.4f}" fill="#FFFFFF"/>',
        f'<g fill="{bar}">' + "".join(rects) + "</g>",
    ]
    if text:
        fam = font or "OCR-B, 'OCR B', 'OCR-B 10 BT', 'Courier New', monospace"
        size = DIGIT_MM * s / 0.72          # cap height of OCR-like faces is about 0.72 em
        base = bar_h + 0.3 * s + DIGIT_MM * s
        style = f'font-family:{fam};font-size:{size:.3f}px;fill:{bar}'
        # first digit in the left quiet zone, then two groups of six centred under their halves
        parts.append(f'<text x="{(QZ_LEFT - 1.2) * x:.4f}" y="{base:.4f}" text-anchor="end" style="{style}">{code[0]}</text>')
        left_c = (QZ_LEFT + 3 + 21) * x
        right_c = (QZ_LEFT + 50 + 21) * x
        group_w = 40 * x
        for centre, digits in ((left_c, code[1:7]), (right_c, code[7:13])):
            parts.append(f'<text x="{centre:.4f}" y="{base:.4f}" text-anchor="middle" textLength="{group_w:.4f}" '
                         f'lengthAdjust="spacing" style="{style}">{digits}</text>')
    parts.append("</svg>")
    return "\n".join(parts) + "\n", width, height


def main():
    ap = argparse.ArgumentParser(description="Check a GTIN-13 and draw its EAN-13 barcode as SVG.",
                                 formatter_class=argparse.RawDescriptionHelpFormatter, epilog=__doc__)
    ap.add_argument("number", help="12 digits (check digit added) or 13 digits (check digit verified)")
    ap.add_argument("--mag", type=float, default=100.0)
    ap.add_argument("--out")
    ap.add_argument("--no-text", action="store_true")
    ap.add_argument("--font")
    ap.add_argument("--bar", default="#000000")
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args()
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

    raw = re.sub(r"[\s-]", "", a.number)
    if not raw.isdigit() or len(raw) not in (12, 13):
        print(f"Not a GTIN-13: '{a.number}'. Give 12 or 13 digits (spaces and dashes are ignored).", file=sys.stderr)
        sys.exit(2)
    if len(raw) == 12:
        code = raw + str(check_digit(raw))
        print(f"Check digit computed: {code[-1]}  ->  {code}")
    else:
        expected = check_digit(raw[:12])
        if int(raw[-1]) != expected:
            print(f"Check digit is wrong: {raw} ends in {raw[-1]}, but the first 12 digits need {expected} "
                  f"({raw[:12]}{expected}). This is usually a typo in the number: confirm it with the client.",
                  file=sys.stderr)
            sys.exit(1)
        code = raw
        print(f"Check digit OK: {code}")
    if code.startswith("952"):
        print("Note: prefix 952 is GS1's range for demonstrations and examples, never for real products.")

    if not 80 <= a.mag <= 200:
        print(f"Magnification {a.mag:g}% is outside the GS1 retail range of 80 to 200%.", file=sys.stderr)
        sys.exit(2)
    if a.mag < 100:
        print(f"Warning: {a.mag:g}% leaves little print tolerance; use 100% if the pack has room.")
    if looks_unscannable(a.bar):
        print(f"Warning: bar colour {a.bar} is too light or too red to scan reliably. Use black or a dark colour.")

    svg, w, h = build_svg(code, a.mag, text=not a.no_text, font=a.font, bar=a.bar)
    x = MODULE_MM * a.mag / 100
    print(f"Size at {a.mag:g}%: {w:.2f} x {h:.2f} mm (module {x:.3f} mm), quiet zones "
          f"{QZ_LEFT * x:.2f} mm left / {QZ_RIGHT * x:.2f} mm right, bar height {BAR_MM * a.mag / 100:.2f} mm.")
    if a.check:
        return
    out = a.out or f"ean13-{code}.svg"
    with open(out, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"Wrote {out}. Place it at 100% scale (never stretch it), keep the white quiet zones clear, "
          f"print it in one solid dark ink, and test-scan the printed proof.")


if __name__ == "__main__":
    main()
