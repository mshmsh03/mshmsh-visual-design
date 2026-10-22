#!/usr/bin/env python3
"""
contrast.py - WCAG 2 contrast ratios, so palette previews never guess.

Usage:
    python contrast.py "#F3EDE4" "#16120F"                 # one pair (text, background)
    python contrast.py page=#16120F text=#F3EDE4 muted=#B8AC9C accent=#E0A040
                                                           # every pair, as a matrix
    python contrast.py --on page=#16120F text=#F3EDE4 muted=#B8AC9C
                                                           # every colour on the first one

Accepts #rgb, #rrggbb and rgb(r, g, b). Thresholds: 4.5 body text, 3 large text
(24px+, or 18.66px+ bold) and UI parts (borders, icons, focus rings), 7 AAA body text.
"""
import re
import sys


def parse(c):
    c = c.strip()
    m = re.fullmatch(r"#([0-9a-fA-F]{3}|[0-9a-fA-F]{6})", c)
    if m:
        h = m.group(1)
        if len(h) == 3:
            h = "".join(ch * 2 for ch in h)
        return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))
    m = re.fullmatch(r"rgba?\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)(?:\s*,\s*[\d.]+)?\s*\)", c)
    if m:
        return tuple(int(x) for x in m.groups())
    raise ValueError(f"Can't read colour: {c}")


def lum(rgb):
    def ch(v):
        v = v / 255
        return v / 12.92 if v <= 0.04045 else ((v + 0.055) / 1.055) ** 2.4
    r, g, b = (ch(v) for v in rgb)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def ratio(a, b):
    la, lb = lum(parse(a)), lum(parse(b))
    hi, lo = max(la, lb), min(la, lb)
    return (hi + 0.05) / (lo + 0.05)


def verdict(r):
    if r >= 7:
        return "AAA text"
    if r >= 4.5:
        return "AA text"
    if r >= 3:
        return "large text / UI only"
    return "FAIL"


def main():
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        sys.exit(2)
    on_first = False
    if args[0] == "--on":
        on_first, args = True, args[1:]
    named = []
    for i, a in enumerate(args):
        if "=" in a:
            k, v = a.split("=", 1)
        else:
            k, v = f"c{i + 1}", a
        named.append((k, v))
    try:
        for _, v in named:
            parse(v)
    except ValueError as e:
        print(e, file=sys.stderr)
        sys.exit(2)

    if len(named) == 2 and not on_first:
        (ka, a), (kb, b) = named
        r = ratio(a, b)
        print(f"{ka} {a} on {kb} {b}: {r:.2f}:1  {verdict(r)}")
        return
    if on_first:
        kb, b = named[0]
        for ka, a in named[1:]:
            r = ratio(a, b)
            print(f"{ka:>10} {a} on {kb} {b}: {r:5.2f}:1  {verdict(r)}")
        return
    w = max(len(k) for k, _ in named)
    print(" " * (w + 2) + "  ".join(f"{k:>{max(w, 6)}}" for k, _ in named))
    for ka, a in named:
        cells = []
        for kb, b in named:
            cells.append(f"{'-':>{max(w, 6)}}" if ka == kb else f"{ratio(a, b):>{max(w, 6)}.2f}")
        print(f"{ka:>{w}}  " + "  ".join(cells))
    print("\n4.5 body text, 3 large text and UI parts, 7 AAA.")


if __name__ == "__main__":
    main()
