#!/usr/bin/env python3
"""Tests for mshmsh-visual-design. Run from anywhere: python3 tests/run.py

1. SKILL.md: valid name and description, every file it points to exists.
2. Every "`file.md` section N" reference in the skill points at a real section.
3. deal.py deals three directions for every kind, with unique ids and known asset needs.
4. ean13.py: check digits, wrong digits and sizes; the bars for a known number never change; random
   numbers drawn by the script decode back to the same number (when zxing-cpp and Pillow are installed).
5. The logo sheet and the pack mockup render in headless Chrome with the fixtures (when Node 22+
   and Chrome are found).
"""
import importlib.util, pathlib, random, re, shutil, subprocess, sys

root = pathlib.Path(__file__).resolve().parent.parent
out = root / "tests" / "out"
shutil.rmtree(out, ignore_errors=True)
out.mkdir(parents=True)
fails = []


def step(name, ok, detail=""):
    print(("ok   " if ok else "FAIL ") + name)
    if not ok:
        fails.append(name)
        if detail:
            print(str(detail).strip()[-3000:])


def skip(name, why):
    print(f"skip {name} ({why})")


def load(name):
    spec = importlib.util.spec_from_file_location(name, root / "scripts" / f"{name}.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def py(*args, cwd=None):
    return subprocess.run([sys.executable, *map(str, args)], cwd=cwd or out, capture_output=True, text=True)


# 1. SKILL.md
skill = (root / "SKILL.md").read_text(encoding="utf-8")
m = re.match(r'^---\nname: (.+)\ndescription: "(.*)"\n---\n', skill, re.S)
step("SKILL.md has name and description frontmatter", bool(m))
if m:
    name, desc = m.group(1).strip(), m.group(2).replace('\\"', '"')
    step("name is mshmsh-visual-design (lowercase, hyphens, 64 max)",
         name == "mshmsh-visual-design" and re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", name) and len(name) <= 64, name)
    step(f"description is at most 1,024 characters ({len(desc)}) with no angle brackets",
         len(desc) <= 1024 and "<" not in desc and ">" not in desc)
    step("description keeps the old name so it still triggers", "designa-xoshaka" in desc)
missing = []
for doc in ("SKILL.md", "README.md"):
    text = (root / doc).read_text(encoding="utf-8")
    for p in set(re.findall(r"(?<![\w/])((?:references|scripts|assets)/[\w.\-]+\.(?:md|py|mjs|html))", text)):
        if not (root / p).exists():
            missing.append(f"{doc}: {p}")
step("every file SKILL.md and README.md name exists", not missing, "\n".join(missing))

# 2. section references
heads = {f.name: {int(n) for n in re.findall(r"^## (\d+)\.", f.read_text(encoding="utf-8"), re.M)}
         for f in (root / "references").glob("*.md")}
bad = []
for f in [root / "SKILL.md", *(root / "references").glob("*.md")]:
    for ref in re.finditer(r"`([\w\-]+\.md)` sections? ([\d, and]+)", f.read_text(encoding="utf-8")):
        target = ref.group(1)
        if target == "DESIGN.md":
            continue
        for n in map(int, re.findall(r"\d+", ref.group(2))):
            if n not in heads.get(target, set()):
                bad.append(f"{f.name}: {ref.group(0)}")
step("every section reference points at a real section", not bad, "\n".join(bad))

# 3. deal.py
deal = load("deal")
ids = [x["id"] for x in deal.D]
step(f"deal.py has {len(ids)} directions with unique ids", len(ids) == len(set(ids)))
unknown = [f'{x["id"]}: {n}' for x in deal.D for n in x["needs"] if n not in deal.HAVE]
step("every direction's needs are known assets", not unknown, "\n".join(unknown))
for kind in deal.KINDS:
    r = py(root / "scripts" / "deal.py", "--kind", kind, "--no-history", "--seed", "7")
    dealt = re.findall(r"^[A-E]\. ", r.stdout, re.M)
    step(f"deal.py --kind {kind} deals 3 directions", r.returncode == 0 and len(dealt) == 3, r.stdout + r.stderr)

# 4. ean13.py
ean = root / "scripts" / "ean13.py"
r = py(ean, "400638133393", "--out", "a.svg")
svg = (out / "a.svg").read_text(encoding="utf-8") if (out / "a.svg").exists() else ""
step("ean13.py adds the check digit to 12 digits", r.returncode == 0 and "4006381333931" in r.stdout, r.stdout + r.stderr)
step("ean13.py draws 37.29 x 25.93 mm at 100%", 'width="37.290mm"' in svg and 'height="25.930mm"' in svg)
r = py(ean, "4006381333932", "--check")
step("ean13.py refuses a wrong check digit", r.returncode == 1 and "4006381333931" in r.stderr, r.stdout + r.stderr)
r = py(ean, "4006381333931", "--mag", "60", "--check")
step("ean13.py refuses sizes outside 80 to 200%", r.returncode == 2, r.stdout + r.stderr)
r = py(ean, "4006381333931", "--mag", "80", "--check")
step("ean13.py gives GS1's 80% size (29.83 mm wide)", r.returncode == 0 and "29.83 x" in r.stdout, r.stdout)
e = load("ean13")
known = "10100011010100111010111101111010001001011001101010100001010000101000010111010010000101100110101"
step("the bars for 4006381333931 match the verified pattern", e.modules("4006381333931") == known)
try:
    import zxingcpp
    from PIL import Image, ImageDraw
except ImportError:
    skip("random numbers decode back", "pip install zxing-cpp pillow to run it")
else:
    rng, wrong = random.Random(13), []
    for _ in range(30):
        first12 = "".join(rng.choice("0123456789") for _ in range(12))
        code = first12 + str(e.check_digit(first12))
        bits, unit = e.modules(code), 4
        img = Image.new("L", ((11 + 95 + 7) * unit, 300), 255)
        draw = ImageDraw.Draw(img)
        for i, b in enumerate(bits):
            if b == "1":
                draw.rectangle([(11 + i) * unit, 20, (12 + i) * unit - 1, 280], fill=0)
        got = [res.text for res in zxingcpp.read_barcodes(img)]
        if code not in got:
            wrong.append(f"{code} read as {got}")
    step("30 random numbers decode back to themselves", not wrong, "\n".join(wrong))

# 5. preview pages
node = shutil.which("node")
version = subprocess.run([node, "--version"], capture_output=True, text=True).stdout if node else ""
chrome = any(pathlib.Path(p).exists() for p in ("/usr/bin/google-chrome", "/usr/bin/google-chrome-stable",
                                                 "/usr/bin/chromium", "/usr/bin/chromium-browser"))
if not node or int(re.sub(r"\D", "", version.split(".")[0]) or 0) < 22 or not chrome:
    skip("preview pages render", "needs Node 22+ and Chrome or Chromium")
else:
    for f in (root / "tests" / "fixtures").glob("*.svg"):
        shutil.copy(f, out / f.name)
    sheet = (root / "assets" / "logo-sheet.html").read_text(encoding="utf-8")
    sheet = sheet.replace('  // "comp-1.png", "comp-2.png",', '  "comp-1.svg", "comp-2.svg",')
    (out / "sheet.html").write_text(sheet, encoding="utf-8")
    mock = (root / "assets" / "pack-mockup.html").read_text(encoding="utf-8")
    for n in ("box-front", "box-side", "box-top", "box-back", "jar-label"):
        mock = mock.replace(f"{n}.png", f"{n}.svg")
    (out / "mockup.html").write_text(mock, encoding="utf-8")
    shoot = root / "scripts" / "shoot.mjs"
    for page, size, name in (("sheet.html", "1600x1200", "logo"), ("mockup.html", "1200x900", "pack")):
        r = subprocess.run([node, str(shoot), page, "shots", f"--sizes={size}", "--full", f"--name={name}"],
                           cwd=out, capture_output=True, text=True, timeout=180)
        pngs = list((out / "shots").glob(f"{name}-*.png"))
        big = pngs and pngs[0].stat().st_size > 30_000
        step(f"{page} renders ({pngs[0].stat().st_size // 1024 if pngs else 0} KB)", r.returncode == 0 and big, r.stdout + r.stderr)

print()
if fails:
    print(f"{len(fails)} failed: " + "; ".join(fails))
    sys.exit(1)
print("All checks passed.")
