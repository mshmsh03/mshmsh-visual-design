#!/usr/bin/env python3
"""
glyph_check.py - will any character render as a box? Check font files against Kurdish,
Arabic, Latin and UI-symbol sets, or against the characters a project actually uses.

Needs fontTools (and brotli for .woff2):
    python -m pip install fonttools brotli

Usage:
    python glyph_check.py Font-Regular.ttf                      # standard sets
    python glyph_check.py Kurdish.woff2 Latin.ttf --stack       # also: what neither covers
    python glyph_check.py fonts/*.ttf --scan src                # every char used in src/
    python glyph_check.py Font.otf --text "ڕێگای ئازادی ٢٠٢٦"     # a specific string
    python glyph_check.py Font.otf --sets kurdish,digits        # pick sets

Sets: kurdish, arabic, harakat, digits, digits-fa, punct-ar, latin, symbols.
Format characters (ZWNJ, LRM, RLM...) are skipped: the shaping engine handles them.
Exit code: 1 if anything in the requested text/sets is missing from the stack, else 0.
"""
import argparse
import os
import sys
import unicodedata

SETS = {
    # Sorani Kurdish alphabet (Arabic script), including both heh forms it uses.
    "kurdish": "ئابپتجچحخدرڕزژسشعغفڤقکگلڵمنھەوۆیێه",
    "arabic": "ءآأؤإئابةتثجحخدذرزسشصضطظعغفقكلمنهوىي",
    "harakat": "ًٌٍَُِّْ",
    "digits": "0123456789٠١٢٣٤٥٦٧٨٩",
    "digits-fa": "۰۱۲۳۴۵۶۷۸۹",
    "punct-ar": "،؛؟٪٫٬ـ«»",
    "latin": "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz.,:;!?'\"()[]-/&@#%+=“”‘’…–—•·×©",
    "symbols": "→←↑↓✓✕★☆●○▸▾➜✎✔✖",
}
DEFAULT_SETS = ["kurdish", "arabic", "digits", "punct-ar", "latin", "symbols"]
SCAN_EXTS = {".html", ".htm", ".jsx", ".tsx", ".js", ".ts", ".vue", ".svelte", ".astro", ".mdx",
             ".md", ".json", ".arb", ".dart", ".css", ".scss", ".txt", ".yaml", ".yml", ".po"}
SKIP_DIRS = {"node_modules", ".git", "dist", "build", ".next", "out", ".dart_tool", "ios", "android",
             "macos", "linux", "windows", "coverage", ".cache", ".design-options"}


def load_cmaps(path):
    """Return a list of (label, set_of_codepoints) for a font file or collection."""
    from fontTools.ttLib import TTFont, TTCollection
    out = []
    if path.lower().endswith((".ttc", ".otc")):
        coll = TTCollection(path, lazy=True)
        fonts = list(coll.fonts)
    else:
        fonts = [TTFont(path, lazy=True)]
    for f in fonts:
        cmap = f.getBestCmap() or {}
        name = f["name"]
        family = (name.getDebugName(16) or name.getDebugName(1) or os.path.basename(path))
        style = name.getDebugName(17) or name.getDebugName(2) or ""
        out.append((f"{family} {style}".strip() + f"  [{os.path.basename(path)}]", set(cmap.keys())))
    return out


def scan_chars(root):
    """Map every non-ASCII, visible character used under root to its first location."""
    found = {}
    paths = [root] if os.path.isfile(root) else []
    if not paths:
        for d, dirs, files in os.walk(root):
            dirs[:] = [x for x in dirs if x not in SKIP_DIRS and not x.startswith(".")]
            for fn in files:
                if os.path.splitext(fn)[1].lower() in SCAN_EXTS:
                    paths.append(os.path.join(d, fn))
    for p in paths:
        try:
            with open(p, encoding="utf-8", errors="ignore") as fh:
                for i, line in enumerate(fh, 1):
                    for ch in line:
                        if ord(ch) > 127 and ch not in found and visible(ch):
                            found[ch] = f"{os.path.relpath(p, root) if os.path.isdir(root) else p}:{i}"
        except OSError:
            pass
    return found


def visible(ch):
    cat = unicodedata.category(ch)
    return not (cat.startswith("C") or cat.startswith("Z"))


def describe(ch):
    try:
        name = unicodedata.name(ch)
    except ValueError:
        name = "UNNAMED"
    return f"{ch}  U+{ord(ch):04X}  {name}"


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("fonts", nargs="+", help="font files (.ttf .otf .woff .woff2 .ttc)")
    ap.add_argument("--sets", help="comma-separated sets (default: %s)" % ",".join(DEFAULT_SETS))
    ap.add_argument("--text", help="check this exact text")
    ap.add_argument("--scan", help="check every character used in this folder or file")
    ap.add_argument("--stack", action="store_true", help="treat the fonts as one fallback stack")
    a = ap.parse_args()

    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    try:
        import fontTools  # noqa: F401
    except ImportError:
        print("fontTools is not installed. Run:  python -m pip install fonttools brotli", file=sys.stderr)
        sys.exit(2)

    fonts = []
    for path in a.fonts:
        if not os.path.exists(path):
            print(f"Font not found: {path}", file=sys.stderr)
            sys.exit(2)
        try:
            fonts.extend(load_cmaps(path))
        except Exception as e:  # unreadable or needs brotli
            hint = " (install brotli for .woff2)" if path.lower().endswith(".woff2") else ""
            print(f"Could not read {path}: {e}{hint}", file=sys.stderr)
            sys.exit(2)

    # what to check: label -> {char: where}
    checks = {}
    if a.text:
        checks["text"] = {ch: "--text" for ch in a.text if visible(ch) and ord(ch) > 32}
    if a.scan:
        checks["project"] = scan_chars(a.scan)
    if a.sets or not checks:
        names = [s.strip() for s in (a.sets.split(",") if a.sets else DEFAULT_SETS)]
        for n in names:
            if n not in SETS:
                print(f"Unknown set '{n}'. Choose from: {', '.join(SETS)}", file=sys.stderr)
                sys.exit(2)
            checks[n] = {ch: n for ch in SETS[n]}

    any_missing_in_stack = False
    for label, cps in fonts:
        print(f"\n{label}  ({len(cps)} characters mapped)")
        for cname, chars in checks.items():
            missing = [ch for ch in chars if ord(ch) not in cps]
            total = len(chars)
            mark = "OK " if not missing else "!! "
            line = f"  {mark}{cname}: {total - len(missing)}/{total}"
            if missing:
                line += "  missing: " + " ".join(missing[:40]) + (" ..." if len(missing) > 40 else "")
            print(line)

    if len(fonts) > 1 or a.stack:
        union = set().union(*[cps for _, cps in fonts])
        print("\nAs one stack (first font that has the character wins):")
        for cname, chars in checks.items():
            missing = [ch for ch in chars if ord(ch) not in union]
            if missing:
                any_missing_in_stack = True
                print(f"  !! {cname}: {len(missing)} character(s) in NO font:")
                for ch in missing[:60]:
                    print(f"     {describe(ch)}   ({chars[ch]})")
            else:
                print(f"  OK {cname}: every character is covered")
    else:
        cps = fonts[0][1]
        for cname, chars in checks.items():
            missing = [ch for ch in chars if ord(ch) not in cps]
            if missing and cname in ("text", "project"):
                any_missing_in_stack = True
                print(f"\nMissing from this font ({cname}):")
                for ch in missing[:60]:
                    print(f"  {describe(ch)}   ({chars[ch]})")
            elif missing and cname in ("kurdish", "arabic", "digits", "latin"):
                any_missing_in_stack = True

    print("\nMissing characters fall back to another font (mixed look) or print as boxes in PDFs."
          " Swap the font, add a fallback that has them, or replace the symbol with an SVG icon.")
    sys.exit(1 if any_missing_in_stack else 0)


if __name__ == "__main__":
    main()
