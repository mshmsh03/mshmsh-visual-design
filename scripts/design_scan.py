#!/usr/bin/env python3
"""
design_scan.py - find mechanical design problems in a web or Flutter project.

Standard library only. It looks for three kinds of problems:
  1. Right-to-left (Kurdish / Arabic) mistakes: physical left/right instead of
     start/end, letter-spacing on Arabic script, missing dir/lang, no Kurdish-capable font,
     Flutter widgets that ignore text direction.
  2. Quality-floor misses: removed focus rings, disabled zoom, images without alt,
     clickable divs, transition: all, no reduced-motion support, 100vh on phones.
  3. Default "AI look" tells: AI purple, gradient text, purple-to-blue gradients,
     untouched shadcn tokens, the cream + serif default, emoji or dingbats used as icons.

It only finds candidates. Every finding is something to OFFER the user as a choice,
not something to fix silently.

Usage:
    python design_scan.py <path>                  # report
    python design_scan.py <path> --rtl            # force right-to-left checks on
    python design_scan.py <path> --no-rtl         # force them off
    python design_scan.py <path> --severity high  # only high
    python design_scan.py <path> --json           # machine-readable
    python design_scan.py <path> --max 4          # examples shown per rule (default 6)

A line containing "dx-ignore" is skipped (use it for deliberate choices).
Exit code: number of high-severity findings (capped at 100).
"""
import argparse
import json
import os
import re
import sys

WEB_EXTS = {".html", ".htm", ".css", ".scss", ".sass", ".less", ".js", ".jsx", ".ts",
            ".tsx", ".vue", ".svelte", ".astro", ".mdx"}
CSS_EXTS = {".css", ".scss", ".sass", ".less"}
DART_EXTS = {".dart"}
TEXT_EXTS = WEB_EXTS | DART_EXTS | {".json", ".arb", ".md", ".yaml", ".yml"}
SKIP_DIRS = {"node_modules", ".git", "dist", "build", ".next", "out", "vendor", "coverage",
             ".svelte-kit", ".astro", ".turbo", ".cache", "__pycache__", ".dart_tool",
             "ios", "android", "macos", "linux", "windows", ".design-options", ".vercel",
             ".netlify", ".idea", ".vscode"}
SEV_ORDER = {"high": 0, "medium": 1, "low": 2}

ARABIC_SCRIPT = re.compile(r"[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFB50-\uFDFF\uFE70-\uFEFF]")
RTL_LOCALE = re.compile(r"""(?:['"](?:ar|ckb|fa|ku|ur|he|ar-[A-Za-z]{2}|ckb-[A-Za-z]{2})['"]|Locale\(\s*['"](?:ar|ckb|fa|ku)['"]|dir\s*=\s*["']rtl["'])""")
CLASS_CONTEXT = re.compile(r"""class(Name)?\s*=|\bcn\(|\bclsx\(|\bcva\(|\btw`|@apply|twMerge\(|class:""")

# Fonts known to contain Arabic-script glyphs. Not all of them cover every Kurdish letter:
# verify with glyph_check.py before shipping. Distinctive names count anywhere in the code
# (pubspec.yaml, string constants); ambiguous ones only on font-declaration lines.
# Names are compared with spaces, hyphens and underscores removed.
ARABIC_FONTS_DISTINCT = ["unisirwan", "vazirmatn", "vazir", "notosansarabic", "notokufiarabic",
                         "notonaskharabic", "ibmplexsansarabic", "rabar", "speda", "peshang", "tajawal",
                         "almarai", "readexpro", "scheherazade", "harmattan", "reemkufi", "elmessiri",
                         "baloobhaijaan", "lalezar", "lemonada", "marhey", "estedad", "samim", "shabnam",
                         "yekan", "kalameh", "markazi", "kufam", "beiruti", "fustat", "alyamama", "parastoo",
                         "arefruqaa", "playpensansarabic", "notosansarabicui"]
ARABIC_FONTS_GENERIC = ["alexandria", "cairo", "zain", "mada", "amiri", "rubik", "changa", "lateef",
                        "handjet", "sahel", "segoeui", "tahoma", "rudaw", "kurdish", "ckb", "arabic"]
# Checked 2026-10-22 against the full Sorani alphabet (google/fonts repo + glyph_check.py).
KURDISH_COMPLETE = ["notosansarabic", "notokufiarabic", "notonaskharabic", "ibmplexsansarabic", "vazirmatn",
                    "mada", "beiruti", "fustat", "estedad", "zain", "kufam", "reemkufi", "amiri", "scheherazade",
                    "lateef", "harmattan", "parastoo", "playpensansarabic", "arefruqaa", "jomhuria", "katibeh",
                    "unisirwan", "rabar", "speda", "peshang"]
NOT_KURDISH = {"alexandria": "ڕ ڵ ە ۆ ێ", "almarai": "ڕ ڵ ە ۆ ێ", "cairo": "ڕ ڵ ە ۆ ێ", "changa": "ڕ ڵ ە ۆ ێ",
               "elmessiri": "ڕ ڵ ە ۆ ێ", "lalezar": "ڕ ڵ ە ۆ ێ", "lemonada": "ڕ ڵ ە ۆ ێ",
               "markazitext": "ڕ ڵ ە ۆ ێ", "rakkas": "ڕ ڵ ە ۆ ێ", "rubik": "ڕ ڵ ھ ە ۆ ێ",
               "baloobhaijaan": "ڕ ڵ ۆ ێ", "alyamama": "ە", "readexpro": "پ چ ڕ ژ ک گ ڵ ھ ە ۆ ی ێ",
               "tajawal": "چ ڕ ژ ک گ ڵ ھ ە ۆ ی ێ"}
KURDISH_ONLY_LETTERS = re.compile("[ڕڵەۆێڤ]")  # ڕ ڵ ە ۆ ێ ڤ

EMOJI_OR_DINGBAT = re.compile("[\U0001F300-\U0001FAFF\u2600-\u27BF\u2B00-\u2BFF\u2190-\u21FF]")


def rule(rid, sev, msg, fix, pats, exts, rtl_only=False, needs_class_ctx=False, unless=None):
    return {"id": rid, "sev": sev, "msg": msg, "fix": fix,
            "pats": [re.compile(p, re.I) for p in pats], "exts": exts,
            "rtl_only": rtl_only, "class_ctx": needs_class_ctx,
            "unless": re.compile(unless, re.I) if unless else None}


WEB_NOCSS = WEB_EXTS - CSS_EXTS
LINE_RULES = [
    # ---------- right-to-left ----------
    rule("rtl-tw-physical", "medium",
         "Physical left/right Tailwind class in a right-to-left project",
         "Use logical classes: ms-/me-, ps-/pe-, start-/end-, border-s/e, rounded-s/e, "
         "rounded-ss/se/es/ee, text-start/end. They flip automatically with dir.",
         [r"(?<![\w\-\[])-?(?:m[lr]|p[lr]|scroll-m[lr]|scroll-p[lr])-(?:\d|\[|auto|px)",
          r"(?<![\w\-\[])-?(?:left|right)-(?!1/2)(?:\d|\[|auto|px|full)",
          r"(?<![\w\-\[])(?:border-[lr]|rounded-[lr]|rounded-[tb][lr])(?![\w])",
          r"(?<![\w\-\[])(?:border-[lr]|rounded-[lr]|rounded-[tb][lr])-",
          r"(?<![\w\-\[])text-(?:left|right)\b", r"(?<![\w\-\[])float-(?:left|right)\b"],
         WEB_NOCSS, rtl_only=True, needs_class_ctx=True, unless=r"\b(rtl|ltr):"),
    rule("rtl-tw-space-x", "low",
         "space-x-* in a right-to-left project",
         "Prefer gap-* on the flex/grid parent; it works in both directions.",
         [r"(?<![\w:\-])space-x-\d"], WEB_NOCSS, rtl_only=True, needs_class_ctx=True,
         unless=r"space-x-reverse"),
    rule("rtl-css-physical", "medium",
         "Physical left/right CSS property in a right-to-left project",
         "Use margin-inline-start/end, padding-inline-start/end, border-inline-start/end, "
         "inset-inline-start/end, text-align: start/end, float: inline-start/end.",
         [r"(?<![\w\-])(?:margin|padding|border)-(?:left|right)\s*:",
          r"text-align\s*:\s*(?:left|right)\b", r"(?<![\w\-])float\s*:\s*(?:left|right)\b",
          r"\b(?:marginLeft|marginRight|paddingLeft|paddingRight|borderLeft|borderRight)\s*:"],
         WEB_EXTS, rtl_only=True, unless=r"\[dir=|:dir\(|\brtl\b"),
    rule("rtl-letter-spacing", "medium",
         "Letter-spacing in a right-to-left project",
         "Letter-spacing breaks the joins between Arabic-script letters. Keep it off Kurdish/"
         "Arabic text: scope it to Latin (ltr:tracking-wide, :lang(en)) or remove it.",
         [r"(?<![\w:\-])tracking-(?:wide|wider|widest)\b",
          r"(?<![\w:\-])tracking-\[(?!-)(?!0(?:em|px|rem)?\])",
          r"letter-spacing\s*:\s*(?:0?\.\d*[1-9]|[1-9])",
          r"letterSpacing\s*:\s*(?:0?\.\d*[1-9]|[1-9])"],
         WEB_EXTS, rtl_only=True,
         unless=r"\bltr:|:lang\((?:en|kmr)\)|\[lang=.?(?:en|kmr)|\[dir=.?ltr|:dir\(ltr\)"),
    rule("rtl-letter-spacing", "medium",
         "Letter-spacing in a right-to-left Flutter app",
         "Letter-spacing breaks the joins between Kurdish/Arabic letters. Keep it off text styles "
         "that can show Kurdish, or apply it only for Latin locales. (Tiny Material defaults under "
         "0.5 and monospace digit fields are not flagged.)",
         [r"letterSpacing\s*:\s*(?:0?\.[5-9]\d*|[1-9]\d*(?:\.\d+)?)"],
         DART_EXTS, rtl_only=True, unless=r"mono|pin\b|code|digit|otp|number|\bltr\b|latin"),
    rule("rtl-icon-mirror", "low",
         "Directional arrow/chevron icon without a right-to-left mirror",
         "Arrows that mean back/next/forward should flip in RTL (e.g. className='rtl:-scale-x-100'). "
         "Leave it if it points at a physical direction (a map, a media 'play').",
         [r"\b(?:Arrow(?:Right|Left)|Chevron(?:Right|Left)|ArrowForward|ArrowBack|"
          r"arrow-(?:right|left)|chevron-(?:right|left))\b"],
         WEB_NOCSS, rtl_only=True, unless=r"rtl:|scale-x-|mirror|flip"),
    rule("rtl-dart-alignment", "medium",
         "Alignment with Left/Right in a right-to-left Flutter app",
         "Use AlignmentDirectional.centerStart / topEnd / ... so it follows text direction.",
         [r"\bAlignment\.(?:top|center|bottom)(?:Left|Right)\b"], DART_EXTS, rtl_only=True),
    rule("rtl-dart-textalign", "medium",
         "TextAlign.left/right in a right-to-left Flutter app",
         "Use TextAlign.start / TextAlign.end.",
         [r"\bTextAlign\.(?:left|right)\b"], DART_EXTS, rtl_only=True),
    rule("rtl-dart-radius", "low",
         "BorderRadius/Border with left/right in a right-to-left Flutter app",
         "Use BorderRadiusDirectional.only(topStart:, ...) and BorderDirectional(start:, end:).",
         [r"\bBorderRadius\.only\([^)]*\b(?:top|bottom)(?:Left|Right)\s*:",
          r"\bBorderRadius\.horizontal\(", r"\bBorder\([^)]*\b(?:left|right)\s*:"],
         DART_EXTS, rtl_only=True),
    # ---------- quality floor ----------
    rule("zoom-disabled", "high",
         "Pinch-zoom is disabled", "Remove user-scalable=no / maximum-scale=1.",
         [r"user-scalable\s*=\s*[\"']?(?:no|0)", r"maximum-scale\s*=\s*[\"']?1(?:\.0)?\b",
          r"userScalable\s*:\s*false", r"maximumScale\s*:\s*1\b"], WEB_EXTS),
    rule("transition-all", "medium",
         "transition: all / transition-all",
         "List the properties (transform, opacity, background-color...). 'all' animates layout "
         "by accident and costs performance.",
         [r"(?<![\w\-])transition-all\b", r"transition\s*:\s*all\b"], WEB_EXTS),
    rule("div-click", "medium",
         "Click handler on a div/span",
         "Use <button> for actions and <a>/<Link> for navigation (keyboard + screen reader).",
         [r"<(?:div|span)\b[^>]*\bonClick="], WEB_NOCSS),
    rule("vh-height", "low",
         "100vh / h-screen height",
         "On phones the address bar makes 100vh too tall. Use min-h-dvh / 100dvh (svh for hero).",
         [r"(?<![\w:\-])(?:min-)?h-screen\b", r"(?<![\w\-])(?:min-)?height\s*:\s*100vh"],
         WEB_EXTS),
    rule("three-dots", "low",
         "Three dots instead of an ellipsis in UI text",
         "Use the ellipsis character: 'Loading…', 'Saving…'.",
         [r"[\"'>][^\"'<>{}]*\w\.\.\.[\"'<]"], WEB_NOCSS),
    # ---------- default 'AI look' tells ----------
    rule("ai-purple", "high",
         "Indigo/violet/purple used as a main colour",
         "Offer brand-based colour options instead. Keep purple only if it is a real brand choice "
         "(then add dx-ignore).",
         [r"(?<![\w\-])(?:bg|text|from|via|to|border|ring|fill|stroke|outline|decoration)-"
          r"(?:indigo|violet|purple|fuchsia)-(?:400|500|600|700|800)\b",
          r"#(?:6366f1|4f46e5|818cf8|7c3aed|6d28d9|8b5cf6|a855f7|9333ea|7e22ce|c026d3|d946ef)\b"],
         WEB_EXTS),
    rule("gradient-text", "high",
         "Gradient-filled text",
         "Solid colour for headings and copy. Gradient text is one of the strongest AI tells.",
         [r"bg-clip-text[^\"'`]*text-transparent", r"text-transparent[^\"'`]*bg-clip-text",
          r"-webkit-background-clip\s*:\s*text", r"(?<![\w\-])background-clip\s*:\s*text"],
         WEB_EXTS),
    rule("purple-blue-gradient", "high",
         "Purple-to-blue/pink gradient",
         "Default to solid fills. One quiet, analogous gradient at most, chosen on purpose.",
         [r"from-(?:purple|violet|indigo|fuchsia)-\d+\s+(?:via-[a-z]+-\d+\s+)?to-(?:blue|indigo|pink|cyan|sky)-\d+",
          r"linear-gradient\([^)]*#(?:6366f1|7c3aed|8b5cf6|a855f7)[^)]*\)"], WEB_EXTS),
    rule("shadcn-defaults", "medium",
         "Untouched shadcn theme defaults",
         "Theme the tokens (primary, radius, neutral ramp) before building, so the UI is not the "
         "shadcn docs look.",
         [r"--radius\s*:\s*0\.5rem", r"\"baseColor\"\s*:\s*\"(?:slate|zinc|gray|neutral|stone)\"",
          r"rounded-lg\s+border\s+bg-card\s+text-card-foreground\s+shadow-sm"],
         WEB_EXTS | {".json"}),
    rule("tasteful-default", "medium",
         "Cream background or overexposed serif (the 'tasteful AI' default)",
         "Fine as a real brand decision (add dx-ignore). As a fallback it reads as AI-made.",
         [r"#(?:faf8f5|f5f1e8|f3eee3|fdfbf7|f7f3ec|faf6ef|f6f1e7|fbf7f0|f4efe4|f4f1ea)\b",
          r"\b(?:Instrument[\s_]*Serif|Fraunces|Playfair[\s_]*Display|Cormorant|DM[\s_]*Serif)\b"],
         WEB_EXTS),
    rule("flutter-default-purple", "medium",
         "Flutter's template purple used as the app colour",
         "Colors.deepPurple is the 'flutter create' default. Offer brand-based seed colours instead "
         "(add dx-ignore if purple really is the brand).",
         [r"\bColors\.(?:deepPurple|purple|indigo)\b"], DART_EXTS),
    rule("glow", "low",
         "Neon glow shadow",
         "Remove glow nobody asked for. Dark themes work with contrast and spacing.",
         [r"(?:drop-)?shadow-\[0_0_", r"text-shadow\s*:\s*0(?:px)?\s+0(?:px)?\s+\d+px"], WEB_EXTS),
]

FILE_RULE_INFO = {
    "img-alt": ("high", "Image without alt text",
                "Add alt (describe it) or alt=\"\" if purely decorative."),
    "img-size": ("low", "<img> without width and height",
                 "Set width/height (or aspect-ratio) to stop layout shift."),
    "emoji-icon": ("medium", "Emoji or dingbat used as an icon",
                   "Use an SVG icon set (Lucide, Phosphor, Tabler). Dingbats like ➜ ✎ ✓ are often "
                   "missing from the font and print as boxes."),
    "outline-none": ("high", "Focus outline removed with no focus-visible replacement",
                     "Keep a visible focus ring: focus-visible:ring-2 / :focus-visible { outline: ... }."),
    "html-dir": ("high", "<html> has no dir attribute in a right-to-left project",
                 "Set dir (and lang) on <html>, switched per locale (dir=\"rtl\" lang=\"ckb\")."),
    "html-lang": ("medium", "<html> has no lang attribute",
                  "Set lang (en, ckb, ar...). Screen readers and fonts depend on it."),
    "dart-color-sprawl": ("medium", "Many hard-coded colours outside the theme",
                          "Move colours into ThemeData/ColorScheme (and ThemeExtension) so a palette "
                          "change happens in one place."),
    "dart-tap-target": ("medium", "Button smaller than 48 px",
                        "Material minimum touch target is 48x48 (44 on iOS). POS screens want more."),
    "dart-no-l10n": ("high", "MaterialApp without localizations in a right-to-left app",
                     "Add localizationsDelegates (GlobalMaterialLocalizations...) and supportedLocales "
                     "so Directionality and widgets switch to RTL."),
}

PROJECT_RULE_INFO = {
    "no-reduced-motion": ("medium", "Animations but no reduced-motion support anywhere",
                          "Add motion-reduce: variants / @media (prefers-reduced-motion) / "
                          "useReducedMotion, and keep the UI usable with motion off."),
    "no-arabic-font": ("high", "Kurdish/Arabic text but no Arabic-script font declared",
                       "The OS fallback font will be used. Pick a Kurdish-capable font "
                       "(references/rtl-kurdish-arabic.md) and verify it with glyph_check.py."),
    "kurdish-font-gap": ("high", "Kurdish text, but the declared Arabic-script font lacks Kurdish letters",
                         "Those letters fall back to another font, so words mix two shapes. Use a font that "
                         "covers Sorani (catalogs.md section 4: Noto Sans/Kufi/Naskh Arabic, IBM Plex Sans "
                         "Arabic, Vazirmatn, Mada...) and confirm with glyph_check.py."),
    "hover-scale-everywhere": ("low", "Scale-on-hover on many elements",
                               "Uniform hover-grow reads as template motion. Keep it where it means "
                               "something."),
    "reveal-everywhere": ("low", "Fade/slide-in on scroll on many sections",
                          "One orchestrated moment beats a fade on every section."),
}


def selector_context(lines):
    """For each line, the CSS selectors it sits inside (so a rule scoped to [dir=rtl] or
    :lang(en) counts as handled even when the declaration is on its own line)."""
    ctx, stack, pending = [], [], ""
    for ln in lines:
        ctx.append(" ".join(stack))
        buf = pending
        for ch in ln:
            if ch == "{":
                stack.append(buf.strip()[-200:])
                buf = ""
            elif ch == "}":
                if stack:
                    stack.pop()
                buf = ""
            elif ch == ";":
                buf = ""
            else:
                buf += ch
        pending = buf + " "
    return ctx


def walk(root):
    if os.path.isfile(root):
        yield root
        return
    for d, dirs, files in os.walk(root):
        dirs[:] = [x for x in dirs if x not in SKIP_DIRS and not x.startswith(".")]
        for f in files:
            if os.path.splitext(f)[1].lower() in TEXT_EXTS:
                yield os.path.join(d, f)


def read(path):
    try:
        with open(path, encoding="utf-8", errors="replace") as fh:
            return fh.read()
    except OSError:
        return ""


def line_of(text, idx):
    return text.count("\n", 0, idx) + 1


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("path")
    g = ap.add_mutually_exclusive_group()
    g.add_argument("--rtl", action="store_true", help="force right-to-left checks on")
    g.add_argument("--no-rtl", action="store_true", help="force right-to-left checks off")
    ap.add_argument("--severity", choices=["high", "medium", "low"], default="low")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--max", type=int, default=6)
    a = ap.parse_args()

    if not os.path.exists(a.path):
        print(f"Path not found: {a.path}", file=sys.stderr)
        sys.exit(2)

    files = list(walk(a.path))
    texts = {p: read(p) for p in files}

    rtl_reason = None
    if a.rtl:
        rtl_reason = "forced with --rtl"
    elif not a.no_rtl:
        for p, t in texts.items():
            if ARABIC_SCRIPT.search(t):
                rtl_reason = f"Arabic-script text found ({os.path.relpath(p, a.path) if os.path.isdir(a.path) else p})"
                break
            if RTL_LOCALE.search(t):
                rtl_reason = f"right-to-left locale or dir found ({os.path.relpath(p, a.path) if os.path.isdir(a.path) else p})"
                break
    rtl = rtl_reason is not None

    findings = []

    def add(rid, sev, msg, fix, path, line, snippet):
        findings.append({"rule": rid, "severity": sev, "message": msg, "fix": fix,
                         "file": path, "line": line, "snippet": snippet.strip()[:160]})

    anim_seen = reduced_seen = False
    hover_scale = []
    reveal = []
    font_blob = []
    has_arabic_text = False

    for p, t in texts.items():
        ext = os.path.splitext(p)[1].lower()
        lines = t.splitlines()
        if ARABIC_SCRIPT.search(t):
            has_arabic_text = True
        ctx = selector_context(lines) if ext in CSS_EXTS | {".html", ".htm", ".vue", ".svelte", ".astro"} else None
        # line rules
        for i, ln in enumerate(lines, 1):
            if "dx-ignore" in ln:
                continue
            for r in LINE_RULES:
                if ext not in r["exts"] or (r["rtl_only"] and not rtl):
                    continue
                if r["class_ctx"] and not CLASS_CONTEXT.search(ln):
                    continue
                if r["unless"] and (r["unless"].search(ln) or (ctx and r["unless"].search(ctx[i - 1]))):
                    continue
                if any(pt.search(ln) for pt in r["pats"]):
                    add(r["id"], r["sev"], r["msg"], r["fix"], p, i, ln)
            # signals for project-level rules
            if re.search(r"@keyframes|(?<![\w\-])animate-[a-z]|framer-motion|motion/react|whileInView|"
                         r"data-aos|AnimatedContainer|AnimationController|transition-(?:transform|opacity|colors)", ln):
                anim_seen = True
            if re.search(r"prefers-reduced-motion|motion-reduce:|motion-safe:|useReducedMotion|"
                         r"reducedMotion|disableAnimations|MediaQuery\.of\([^)]*\)\.disableAnimations", ln):
                reduced_seen = True
            if re.search(r"hover:scale-1(?:0[2-9]|[1-9]\d)|whileHover=\{\{\s*scale", ln):
                hover_scale.append((p, i, ln))
            if re.search(r"whileInView|data-aos=|initial=\{\{\s*opacity:\s*0", ln):
                reveal.append((p, i, ln))
            if re.search(r"font-?family|fontFamily|next/font|--font|fonts\.googleapis|@font-face|"
                         r"family:\s|fontFamily:|fonts?\.", ln, re.I):
                font_blob.append(re.sub(r"[\s_\-]", "", ln.lower()))
        squashed = re.sub(r"[\s_\-]", "", t.lower())
        if any(n in squashed for n in ARABIC_FONTS_DISTINCT):
            font_blob.append("distinct-arabic-font-found")

        if ext in WEB_NOCSS:
            for m in re.finditer(r"<img\b[^>]*>", t, re.S):
                tag = m.group(0)
                ln_no = line_of(t, m.start())
                if "dx-ignore" in tag:
                    continue
                if not re.search(r"\balt\s*=", tag):
                    info = FILE_RULE_INFO["img-alt"]
                    add("img-alt", info[0], info[1], info[2], p, ln_no, tag)
                if not (re.search(r"\bwidth\s*=", tag) and re.search(r"\bheight\s*=", tag)) and "aspect-" not in tag:
                    info = FILE_RULE_INFO["img-size"]
                    add("img-size", info[0], info[1], info[2], p, ln_no, tag)
            for i, ln in enumerate(lines, 1):
                if "dx-ignore" in ln or not EMOJI_OR_DINGBAT.search(ln):
                    continue
                e = EMOJI_OR_DINGBAT.pattern
                icon_slot = re.search(r">\s*(?:" + e + r")+\s*<", ln)
                adorned = re.search(r"<(?:h[1-6]|button|Button|a|Link|span|div|li|label)\b", ln) and (
                    re.search(r">\s*(?:" + e + r")\s*[^<\s]", ln) or re.search(r"[^>\s]\s*(?:" + e + r")\s*<", ln))
                if icon_slot or adorned or re.search(r"icon|Icon|title=", ln):
                    info = FILE_RULE_INFO["emoji-icon"]
                    add("emoji-icon", info[0], info[1], info[2], p, i, ln)

        if ext in WEB_EXTS:
            has_focus_visible = re.search(r"focus-visible|:focus\b", t) is not None
            for i, ln in enumerate(lines, 1):
                if "dx-ignore" in ln:
                    continue
                if re.search(r"(?<![\w\-])outline-none\b|outline\s*:\s*(?:none|0)\b", ln):
                    if not re.search(r"focus-visible|focus:ring|focus:shadow|focus:border|focus-within:ring", ln) and not (ext in CSS_EXTS and has_focus_visible):
                        info = FILE_RULE_INFO["outline-none"]
                        add("outline-none", info[0], info[1], info[2], p, i, ln)
            for m in re.finditer(r"<html\b[^>]*>", t, re.S):
                tag = m.group(0)
                ln_no = line_of(t, m.start())
                if rtl and not re.search(r"\bdir\s*=", tag):
                    info = FILE_RULE_INFO["html-dir"]
                    add("html-dir", info[0], info[1], info[2], p, ln_no, tag)
                if not re.search(r"\blang\s*=", tag):
                    info = FILE_RULE_INFO["html-lang"]
                    add("html-lang", info[0], info[1], info[2], p, ln_no, tag)

        if ext in DART_EXTS:
            relp = os.path.relpath(p, a.path).lower() if os.path.isdir(a.path) else os.path.basename(p).lower()
            if rtl:
                # EdgeInsets with different left and right values (equal ones look the same in RTL)
                for i, ln in enumerate(lines, 1):
                    if "dx-ignore" in ln:
                        continue
                    for m in re.finditer(r"\bEdgeInsets\.fromLTRB\(\s*([^,]+),\s*([^,]+),\s*([^,]+),", ln):
                        if m.group(1).strip() != m.group(3).strip():
                            add("rtl-dart-edgeinsets", "medium",
                                "EdgeInsets with different left/right values in a right-to-left Flutter app",
                                "Use EdgeInsetsDirectional.fromSTEB(...) / .only(start:, end:) so the sides swap in RTL.",
                                p, i, ln)
                    for m in re.finditer(r"\bEdgeInsets\.only\(([^)]*)\)", ln):
                        args = dict(re.findall(r"\b(left|right|top|bottom)\s*:\s*([^,)]+)", m.group(1)))
                        if ("left" in args or "right" in args) and args.get("left", "").strip() != args.get("right", "").strip():
                            add("rtl-dart-edgeinsets", "medium",
                                "EdgeInsets with different left/right values in a right-to-left Flutter app",
                                "Use EdgeInsetsDirectional.only(start:, end:) so the sides swap in RTL.",
                                p, i, ln)
            if not re.search(r"theme|token|colou?r|palette|brand|style", relp):
                hits = [(i, ln) for i, ln in enumerate(lines, 1)
                        if re.search(r"\bColor\(0x[0-9A-Fa-f]{8}\)|\bColors\.(?!transparent)\w+", ln) and "dx-ignore" not in ln]
                if len(hits) >= 8:
                    info = FILE_RULE_INFO["dart-color-sprawl"]
                    add("dart-color-sprawl", info[0], f"{info[1]} ({len(hits)} in this file)", info[2], p, hits[0][0], hits[0][1])
            for i, ln in enumerate(lines, 1):
                m = re.search(r"minimumSize\s*:\s*(?:const\s+)?Size\(\s*(\d+(?:\.\d+)?)\s*,\s*(\d+(?:\.\d+)?)", ln)
                # 0 means "no minimum" on that axis, so only real sizes below 48 count
                if m and any(0 < float(v) < 48 for v in m.groups()) and "dx-ignore" not in ln:
                    info = FILE_RULE_INFO["dart-tap-target"]
                    add("dart-tap-target", info[0], info[1], info[2], p, i, ln)
            if rtl:
                for m in re.finditer(r"\b(?:MaterialApp|CupertinoApp)(?:\.router)?\(", t):
                    chunk = t[m.start(): m.start() + 4000]
                    if "localizationsDelegates" not in chunk or "supportedLocales" not in chunk:
                        info = FILE_RULE_INFO["dart-no-l10n"]
                        add("dart-no-l10n", info[0], info[1], info[2], p, line_of(t, m.start()), m.group(0))
                for m in re.finditer(r"\bPositioned\(", t):
                    chunk = t[m.start(): m.start() + 300]
                    end = chunk.find(")")
                    if re.search(r"\b(?:left|right)\s*:", chunk[: end if end > 0 else 300]):
                        add("rtl-dart-positioned", "medium",
                            "Positioned with left/right in a right-to-left Flutter app",
                            "Use PositionedDirectional(start:, end:).", p, line_of(t, m.start()), "Positioned(")

    # project-level rules
    def proj(rid, where):
        sev, msg, fix = PROJECT_RULE_INFO[rid]
        p, i, ln = where if where else ("(whole project)", 0, "")
        add(rid, sev, msg, fix, p, i, ln)

    if anim_seen and not reduced_seen:
        proj("no-reduced-motion", None)
    if len(hover_scale) >= 3:
        proj("hover-scale-everywhere", hover_scale[0])
    if len(reveal) >= 4:
        proj("reveal-everywhere", reveal[0])
    if rtl and has_arabic_text:
        blob = " ".join(font_blob)
        if "distinct-arabic-font-found" not in blob and not any(n in blob for n in ARABIC_FONTS_GENERIC):
            proj("no-arabic-font", None)
        has_kurdish = any(KURDISH_ONLY_LETTERS.search(t) for t in texts.values())
        gaps = [f"{n} (missing {m})" for n, m in NOT_KURDISH.items() if n in blob]
        if has_kurdish and gaps and not any(n in blob for n in KURDISH_COMPLETE):
            sev, msg, fix = PROJECT_RULE_INFO["kurdish-font-gap"]
            add("kurdish-font-gap", sev, f"{msg}: {', '.join(gaps)}", fix, "(whole project)", 0, "")

    # filter + sort
    limit = SEV_ORDER[a.severity]
    findings = [f for f in findings if SEV_ORDER[f["severity"]] <= limit]
    findings.sort(key=lambda f: (SEV_ORDER[f["severity"]], f["rule"], f["file"], f["line"]))
    high = sum(1 for f in findings if f["severity"] == "high")

    root = a.path if os.path.isdir(a.path) else os.path.dirname(a.path) or "."
    for f in findings:
        if f["file"].startswith("("):
            continue
        try:
            f["file"] = os.path.relpath(f["file"], root)
        except ValueError:
            pass

    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    if a.json:
        print(json.dumps({"rtl": rtl, "rtl_reason": rtl_reason, "files_scanned": len(files),
                          "counts": {s: sum(1 for f in findings if f["severity"] == s) for s in SEV_ORDER},
                          "findings": findings}, ensure_ascii=False, indent=2))
        sys.exit(min(high, 100))

    print(f"design_scan: {len(files)} files, right-to-left checks {'ON (' + rtl_reason + ')' if rtl else 'OFF'}")
    if not findings:
        print("No findings. (This scanner only sees mechanical problems: still look at the screens.)")
        sys.exit(0)
    by_rule = {}
    for f in findings:
        by_rule.setdefault(f["rule"], []).append(f)
    for rid, items in sorted(by_rule.items(), key=lambda kv: (SEV_ORDER[kv[1][0]["severity"]], kv[0])):
        f0 = items[0]
        print(f"\n[{f0['severity'].upper()}] {rid}: {f0['message']}  ({len(items)})")
        print(f"  fix: {f0['fix']}")
        for f in items[: a.max]:
            loc = f"{f['file']}:{f['line']}" if f["line"] else f["file"]
            print(f"  {loc}  {f['snippet']}")
        if len(items) > a.max:
            print(f"  ... and {len(items) - a.max} more")
    counts = {s: sum(1 for f in findings if f["severity"] == s) for s in SEV_ORDER}
    print(f"\nTotal: {counts['high']} high, {counts['medium']} medium, {counts['low']} low. "
          "Offer each fix to the user as a choice; do not apply them silently.")
    sys.exit(min(high, 100))


if __name__ == "__main__":
    main()
