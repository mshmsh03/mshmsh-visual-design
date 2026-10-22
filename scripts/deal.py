#!/usr/bin/env python3
"""
deal.py - deal design directions at random, so the options are not the model's favourite default.

A model asked to invent three directions returns the category default three times. This script
deals them instead, from different families, filtered by what the client actually has. Claude
then grounds each dealt card in the client's own material (references/directions.md) and the
person picks. Idea adapted from taste-skill's dealer (leonxlnx, MIT); the directions are written
for this skill.

Usage:
    python deal.py --kind page --sector cafe --have photos,strong-name
    python deal.py --kind app --sector pos
    python deal.py --kind print --sector restaurant --options 4
    python deal.py --kind page --tone formal --seed 4821      # reproducible
    python deal.py --list [--kind page]                        # every direction, one line each
    python deal.py --show page-is-the-object                   # one full card

--have (what really exists): photos, many-photos, product-photo, strong-name, items, brand-art,
    both-languages, real-data, archive. Without --have nothing is filtered; needs are printed.
--tone: quiet, bold, warm, technical, playful, formal, luxury.
History of recent deals: ~/.designa-xoshaka/history.json (the last 5 per kind are skipped).
Use --no-history to neither read nor write it.
"""
import argparse
import json
import os
import random
import sys
import time

D = []


def d(kind, id, name, family, what, subject, layout, needs, fits, tones, watch, rtl=""):
    D.append(dict(kind=kind, id=id, name=name, family=family, what=what, subject=subject,
                  layout=layout, needs=needs, fits=fits, tones=tones, watch=watch, rtl=rtl))


# ---------------------------------------------------------------- pages
d("page", "name-as-monument", "Name as monument", "type-led",
  "The name, set enormous (16 to 24vw), cropped or stacked, carries the page; a photo can live inside a letter; the name returns full width at the end.",
  "What the name means or where it comes from becomes the picture (a mountain's ridge inside the letters, the street sign's lettering).",
  "First screen: the name edge to edge, one line saying what it is, one action. Calm typographic sections after.",
  ["strong-name"], ["cafe", "restaurant", "studio", "events", "shop", "brand", "any"], ["bold", "playful", "luxury"],
  "Below about 12vw it is just a big heading. Long names don't fit: test both scripts.",
  "Kurdish/Arabic names scale by weight and size, never letter-spacing; the crop mirrors.")
d("page", "sentence-as-layout", "Sentence as layout", "type-led",
  "One short sentence (4 to 7 words) at 9 to 13vw is the layout; one word is replaced by a photo or short clip in a slot.",
  "The sentence is the client's one claim; the picture in the slot proves it.",
  "First screen is the sentence. Sections continue its rhythm with real content.",
  ["photos"], ["cafe", "restaurant", "studio", "product", "any"], ["playful", "bold"],
  "A vague sentence kills it. Seven words or fewer in every language.",
  "Write the Kurdish sentence natively; keep the picture slot at the same word.")
d("page", "pinned-poster", "Pinned poster", "photo-led",
  "A title holds still while photos change beneath it; every scroll step is a new poster. Short page, under 6 screens.",
  "The client's best real photos, in the order of a visit (arrive, order, eat, leave).",
  "Pinned title over full-bleed photos, a calm closing section with the practical facts.",
  ["photos"], ["events", "restaurant", "venue", "portfolio", "hotel"], ["bold", "luxury"],
  "Weak photos sink it. Pins longer than 3 screens feel stuck; phones need a plain stacked fallback.")
d("page", "colour-chapters", "Colour chapters", "colour-led",
  "Each section is a flat full-bleed colour that stands for its chapter; hard cuts; 6 colours at most; the header ink follows the chapter.",
  "Colours sampled from the subject: packaging, shopfront paint, ingredients, uniforms.",
  "Chapters ordered like a story: open strong, rest, surprise, close very dark or very light.",
  [], ["food", "restaurant", "cafe", "retail", "events", "youth", "any"], ["playful", "bold", "warm"],
  "Neighbouring fields must differ in lightness, not just hue; every field needs its own checked text colour.")
d("page", "place-carries-it", "The place carries it", "photo-led",
  "One full-bleed photograph of where you'd stand (the street, the shopfront, the counter, the view), the name along the bottom edge like a film title.",
  "The real place, at the real time of day the client is busiest.",
  "First screen is the place. Practical facts (hours, where, how to order) follow in calm rows.",
  ["photos"], ["cafe", "restaurant", "hotel", "shop", "venue", "clinic"], ["warm", "quiet", "luxury"],
  "A stock photo of 'a cafe' is a lie: it needs the real place. Text over the photo needs a scrim.")
d("page", "page-is-the-object", "The page is the object", "object-led",
  "The page IS an artefact from the client's world: the menu itself, a price board, a receipt, a ticket, a card, a folder with tabs.",
  "Take the client's existing printed piece and make it work: a size switch reprices the whole board, the bag adds up on a paper ticket.",
  "One working object fills the first screen; everything else hangs off it.",
  [], ["restaurant", "cafe", "food", "events", "shop", "services", "any"], ["playful", "warm", "bold"],
  "Borrow the structure and type of the object, not fake materials (paper texture, bevels read as machine-made).")
d("page", "one-motif", "One motif", "structure-led",
  "One shape from the subject (the logo's curve, a tile pattern, a bottle cap, an arch from the street) runs through buttons, image masks, section edges and the loader.",
  "Find the shape in the client's logo, building, packaging or city.",
  "A normal, calm structure where the motif is the only ornament, used at one scale system.",
  ["brand-art"], ["any"], ["playful", "warm", "luxury"],
  "If the shape means nothing to the client, it's decoration. One shape only.",
  "Check the motif still reads when mirrored.")
d("page", "product-performs", "The product performs", "interactive",
  "Small, true working pieces of the product respond to the visitor: a calculator, a configurator, a live price, a bag that adds up, a slot picker.",
  "The client's real logic: their prices, their sizes, their opening hours, their service area.",
  "The working piece sits on the first or second screen, with the explanation beside it.",
  ["real-data"], ["services", "retail", "restaurant", "tools", "software", "any"], ["technical", "playful"],
  "Fake interactivity is worse than none. Thumb-usable, real numbers, a no-JS fallback.")
d("page", "quiet-instrument", "Quiet instrument", "type-led",
  "Radical understatement: the headline barely bigger than body text, one narrow column, exact facts, precise small demonstrations.",
  "The client's precise facts: numbers, standards, processes, certifications.",
  "One column, generous margins, small exact figures and diagrams; nothing loud.",
  [], ["pharmacy", "clinic", "consultancy", "software", "company", "professional"], ["quiet", "technical", "formal"],
  "Reads as unfinished if the content is thin. Needs specific, real words.")
d("page", "hero-object", "Hero object", "object-led",
  "One object shown far bigger than reasonable, cropped by the screen's edges: the burger, the bottle, the car's grille, the tool.",
  "The one product people come for.",
  "The object owns the first screen; sections zoom out to the rest of the range.",
  ["product-photo"], ["food", "auto", "retail", "manufacturing", "product"], ["bold", "luxury"],
  "Needs a genuinely good high-resolution cut-out. Generic stock objects kill it.")
d("page", "specimen-catalogue", "Specimen catalogue", "object-led",
  "Items shown like field-guide specimens: each on a flat colour tile, same scale and angle, with a label like a museum card.",
  "The client's actual range: dishes, products, parts, pills, colours of plastic.",
  "A strict grid of specimens, one featured large, details on tap.",
  ["items"], ["restaurant", "retail", "manufacturing", "pharmacy", "product", "menu"], ["quiet", "playful", "technical"],
  "With three items it's just a feature row; photos must share angle and light.")
d("page", "borrowed-category", "Borrowed category", "structure-led",
  "Dress the client as a more vivid category: a pharmacy as a field guide, a contractor as an annual report, a plastics factory as a museum catalogue, a cafe as a train timetable.",
  "Name the borrowed category in one word first, then map the client's real content onto its structure.",
  "The borrowed category's structure and type, with the client's real content and offer obvious in 5 seconds.",
  [], ["any"], ["playful", "bold"],
  "The costume must not hide the real offer. Brave clients only: say so honestly.")
d("page", "contact-sheet", "Contact sheet", "photo-led",
  "Everything at once, small, in strict rows like a photographer's contact sheet; tap to open large.",
  "The client's whole archive of work.",
  "A dense grid of real images with tiny captions; one line of intro.",
  ["many-photos"], ["portfolio", "events", "photography", "construction", "architecture"], ["technical", "quiet"],
  "Without 20+ real photos it's empty.")
d("page", "editorial-report", "Editorial report", "structure-led",
  "A printed annual report: masthead, oversized title, one strict column line, two-colour blocks, real numbers set large.",
  "The client's real record: projects finished, years, square metres, tonnes, staff.",
  "Masthead, then chapters with big real figures and project photos on a strict column line.",
  ["real-data"], ["construction", "contracting", "industrial", "manufacturing", "company", "ngo"], ["formal", "quiet", "technical"],
  "Hairlines and fake-newspaper labels are a known tell; keep it a real report with real content.")
d("page", "loud-flat-poster", "Loud flat poster", "colour-led",
  "A street poster: flat saturated brand colour, the heaviest type, cut-out photos, a strict grid, no gradients.",
  "The brand's own loudest colour and its signature item.",
  "Big type blocks and cut-outs on flat colour; the menu or offer in a strict list.",
  [], ["street-food", "food", "restaurant", "events", "youth", "sports", "retail"], ["bold", "playful"],
  "Colours must come from the brand, not a trend. Heavy Latin needs an equally heavy Kurdish face.")
d("page", "split-stage", "Split stage", "photo-led",
  "Half the screen holds a fixed photo or object; the other half is a calm scrolling column; the photo changes per section.",
  "One real photo per chapter of the client's story or offer.",
  "50/50 or 40/60 split, full height, the photo touching the outer edge.",
  ["photos"], ["hotel", "restaurant", "clinic", "real-estate", "services", "any"], ["warm", "quiet", "luxury"],
  "On phones it becomes photo-then-text, not a squeezed split.",
  "The photo side mirrors in right-to-left.")
d("page", "dense-tiles", "Dense tiles", "structure-led",
  "One board of filled tiles edge to edge, no hero, no bands: everything visible at once like a shop window or newsstand.",
  "Every item the client sells, at once.",
  "A tight tile board with one type system and strict alignment.",
  ["items"], ["retail", "menu", "marketplace", "news", "restaurant"], ["playful", "bold"],
  "Needs strict alignment and one type system, or it becomes noise.")
d("page", "uneven-photographs", "Uneven photographs", "photo-led",
  "Photos hung like prints on a gallery wall at uneven sizes, every edge on a column line, captions small.",
  "The client's best real photos, each with a one-line true caption.",
  "An uneven but strictly gridded wall; text in short captions and one intro.",
  ["photos"], ["portfolio", "architecture", "construction", "restaurant", "hotel"], ["quiet", "luxury"],
  "Unequal heights look broken unless every edge sits on the grid.")
d("page", "dark-room", "Dark room", "colour-led",
  "One dark field with lit exhibits: sparse light type, low-key photos, things appear like objects under spotlights.",
  "The client's products photographed against dark, lit from one side.",
  "Dark ground, each section one lit object and two lines of text.",
  ["photos"], ["bar", "venue", "luxury", "auto", "perfume", "evening"], ["luxury", "quiet"],
  "Near-black plus neon glow is a known tell: light comes from the photos, not glow. Muted text still 4.5:1.")
d("page", "type-only-statement", "Type-only statement", "type-led",
  "The first screen is only words, colour and space; pictures come later, large and few.",
  "The client's own sentence about what they do, in their words.",
  "A statement screen, then plain sections with few large pictures.",
  [], ["services", "ngo", "consultancy", "company", "any"], ["quiet", "bold", "formal"],
  "The words must be specific and short, or it's an empty page with good manners.")
d("page", "mirrored-bilingual", "Mirrored bilingual", "structure-led",
  "English and Kurdish (or Arabic) as two equal halves mirrored around a centre line; prices, dates and numbers sit on the axis.",
  "The client really works in two languages; the page shows both as equals.",
  "Two columns, one type scale, same line counts; the shared facts on the centre line.",
  ["both-languages"], ["menu", "restaurant", "company", "events", "formal"], ["formal", "quiet", "warm"],
  "Both halves need the same line counts; never two languages inside one line.",
  "This is the right-to-left showcase: each half is native, not a translation layout.")
d("page", "city-archive", "City archive", "photo-led",
  "The client's city is the visual world: old postcards, maps and street photos (open-licence archives) beside the client's present-day photos.",
  "The street, district or trade the client belongs to, then and now.",
  "Archive picture and today's photo paired per section; captions with dates and credits.",
  ["archive", "photos"], ["cafe", "heritage", "family-business", "tourism", "restaurant", "local"], ["warm", "quiet"],
  "Archive images are credited and never passed off as the client's. Licence check (CC0, public domain, CC BY).")
d("page", "formal-symmetric", "Formal symmetric (classic, done well)", "structure-led",
  "The conservative option, executed perfectly: symmetric, orthogonal grid, equal margins to the pixel, brand panel on the leading edge, one accent, real photos of the work.",
  "The client's real projects and credentials, presented with restraint.",
  "Centred masthead, symmetric sections, real project photography in a strict grid.",
  [], ["construction", "contracting", "law", "government", "company", "formal", "any"], ["formal", "quiet"],
  "Say honestly that this is the safe option. It must be perfectly executed or it looks like a template.",
  "The brand panel moves to the right on the Kurdish/Arabic side.")

# ---------------------------------------------------------------- apps
d("app", "quiet-register", "Quiet register", "warm-neutral",
  "Calm warm neutrals mixed from the brand's own colours; the brand colour on the frame only; one filled accent button per view (the next step); money in a tabular face; 48px+ targets; the live order drawn as a thermal receipt.",
  "The shop's real receipt, real items and real prices.",
  "Item grid + receipt column; one filled button (Pay / Next); everything else tonal or outlined.",
  [], ["pos", "till", "cafe", "restaurant", "retail", "pharmacy"], ["warm", "quiet"],
  "Neutrals must come from the brand, not cool default greys.")
d("app", "achromatic-ledger", "Achromatic ledger", "mono",
  "No colour in the chrome at all; one hue only on the main data element (under 1% of the screen); greys and black do everything else.",
  "The data itself is the colour: today's total, the stock line.",
  "Plain rows and type; one coloured mark per screen.",
  [], ["back-office", "finance", "inventory", "pharmacy", "pos", "accounting"], ["quiet", "technical"],
  "Can feel cold for consumer apps; keep at least one human element (the shop's name and logo in the shell).")
d("app", "framed-sheet", "Framed sheet", "frame",
  "A tinted L-frame (sidebar + top bar) around a white working sheet inset 8px with radius 16; no shadows.",
  "The frame takes its tint from the brand's world.",
  "Frame + sheet; content on the sheet only.",
  [], ["admin", "dashboard", "settings", "back-office", "pos"], ["quiet", "warm"],
  "Never a dark or saturated sidebar on a light canvas.")
d("app", "accent-ladder", "Accent ladder", "tint",
  "The full brand hue only on small marks (badges, the selected row line, the active tab); pale tints of the same hue on areas.",
  "One brand hue in a ladder of strengths.",
  "Calm layout; colour strength tells importance.",
  [], ["booking", "education", "clinic", "consumer", "dashboard"], ["warm", "playful"],
  "Tints must still pass contrast for any text on them.")
d("app", "editorial-greeting", "Editorial greeting", "type",
  "A calm title row with a real sentence about the data ('Tuesday: 214 orders, 12 more than last Tuesday'), generous type, few blocks.",
  "The owner's daily question, answered in words first.",
  "Sentence answer on top, 3 to 5 blocks below.",
  ["real-data"], ["owner-dashboard", "summary", "reports"], ["quiet", "warm"],
  "Needs real computed sentences, never filler like 'Welcome back'.")
d("app", "pastel-consumer", "Pastel consumer", "tint",
  "Pale same-hue tiles, radius 20, friendly type, big touch targets.",
  "The brand's colour softened into a family of tiles.",
  "Tiles and lists; one strong action colour.",
  [], ["consumer", "education", "kids", "loyalty"], ["playful"],
  "Too soft for a busy till; check text contrast on every pastel.")
d("app", "true-black-flat", "True black flat", "dark",
  "Black and two near-blacks (#000 / #111 / #2a2a2a), a white pill primary, no shadows, no glow.",
  "Night use: a kitchen display, a bar, a car.",
  "Flat black layers, white type, one white action.",
  [], ["kitchen-display", "bar", "night", "auto", "pos"], ["bold", "luxury"],
  "Glow and neon are tells; light grey text must still pass 4.5:1.")
d("app", "data-terminal", "Data terminal", "dense",
  "Dense rows, tabular figures everywhere, every selection marked by one 1px accent line, keyboard first.",
  "The power user's workload: stock, warehouse, accounting.",
  "Tables and split panes; shortcuts shown.",
  [], ["warehouse", "stock", "accounting", "power-users", "back-office"], ["technical"],
  "Too dense for touch tills; keep it for keyboard and mouse.")

# ---------------------------------------------------------------- print
d("print", "price-board-menu", "Price board menu", "board",
  "One board: items as rows, sizes as columns, prices on one line; categories as bold bands.",
  "The way the counter already talks about sizes and prices.",
  "A single strong grid; the signature items marked once.",
  [], ["fast-food", "street-food", "cafe", "restaurant", "menu"], ["bold", "playful"],
  "Prices tabular and aligned; the longest dish name in each language must fit.")
d("print", "mirrored-bilingual-menu", "Mirrored bilingual menu", "bilingual",
  "English on the left, the price on the centre line, Kurdish on the right; one type scale; same line counts.",
  "Both languages as equals.",
  "Three columns per row: English name, price, Kurdish name; descriptions forced to the same line count.",
  ["both-languages"], ["menu", "restaurant", "cafe"], ["formal", "quiet", "warm"],
  "Never mix languages inside one line; Kurdish set about 1.15x for optical match.")
d("print", "specimen-menu", "Specimen menu", "specimen",
  "Dishes as specimens: a drawing or cut-out photo at one scale, the name, one line, the price.",
  "The real dishes, drawn or photographed the same way.",
  "A grid of specimens with a few featured large.",
  ["items"], ["menu", "restaurant", "bakery", "cafe"], ["quiet", "playful"],
  "Needs consistent images; mismatched photos ruin it.")
d("print", "poster-menu", "Poster menu", "poster",
  "Loud flat brand colour, the heaviest type, the hero dish huge; secondary items in a strict list.",
  "The brand's loudest colour and its signature dish.",
  "Hero dish + headline on top half, strict list below.",
  [], ["street-food", "fast-food", "events", "menu"], ["bold", "playful"],
  "Heavy Kurdish face needed to match the Latin weight.")
d("print", "split-card", "Split card", "panel",
  "A brand-colour panel with the white logo on the leading edge; the details centred on white; the Kurdish/Arabic side mirrored.",
  "The brand colour and logo, nothing else.",
  "Panel about 1/3 of the width; name, title, contacts centred in the rest.",
  [], ["business-card", "company", "formal"], ["formal", "quiet"],
  "Nothing below 7.5 pt; panel on the right for the right-to-left side.")
d("print", "letterhead-strip", "Letterhead strip", "strip",
  "A slim full-bleed brand strip on the top edge, a white masthead, a footer bar; the typing area protected.",
  "The brand's colour and real artwork in the strip.",
  "Strip + masthead + generous body area + footer with contacts.",
  [], ["letterhead", "company", "formal"], ["formal", "quiet"],
  "Decoration lives in the header/footer, never in the text flow.")
d("print", "brand-art-ground", "Brand art ground", "art",
  "The brand's own artwork (a line drawing from their material) behind the content, with a faded edge, quiet type on top.",
  "Artwork taken from the client's own material, not invented.",
  "Artwork in one region, content clear of it.",
  ["brand-art"], ["letterhead", "menu", "card", "flyer"], ["warm", "formal"],
  "The faded edge keeps it from slicing through text or rules.")
d("print", "formal-centred", "Formal centred", "classic",
  "Centred, symmetric, one accent rule, generous equal margins.",
  "The client's formality, done well.",
  "Everything on the centre axis; hierarchy by size and weight only.",
  [], ["letterhead", "card", "certificate", "company", "formal"], ["formal", "quiet"],
  "Honest conservative option; margins must be equal to the millimetre.")

TONES = ["quiet", "bold", "warm", "technical", "playful", "formal", "luxury"]
HAVE = ["photos", "many-photos", "product-photo", "strong-name", "items", "brand-art", "both-languages",
        "real-data", "archive"]
HIST = os.path.join(os.path.expanduser("~"), ".designa-xoshaka", "history.json")


def satisfied(needs, have):
    for n in needs:
        if n == "photos" and not ({"photos", "many-photos"} & have):
            return False
        if n != "photos" and n not in have:
            return False
    return True


def card(letter, x, show_rtl=True):
    lines = [f"{letter}. {x['name']}  [{x['id']} | {x['family']}]",
             f"   What:    {x['what']}",
             f"   Subject: {x['subject']}",
             f"   Layout:  {x['layout']}",
             f"   Needs:   {', '.join(x['needs']) or 'nothing special'}   Fits: {', '.join(x['fits'])}   Tones: {', '.join(x['tones'])}",
             f"   Watch:   {x['watch']}"]
    if show_rtl and x.get("rtl"):
        lines.append(f"   RTL:     {x['rtl']}")
    return "\n".join(lines)


def load_hist():
    try:
        with open(HIST, encoding="utf-8") as f:
            return json.load(f)
    except (OSError, ValueError):
        return {}


def save_hist(h):
    try:
        os.makedirs(os.path.dirname(HIST), exist_ok=True)
        with open(HIST, "w", encoding="utf-8") as f:
            json.dump(h, f, indent=1)
    except OSError:
        pass


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--kind", choices=["page", "app", "print"], default="page")
    ap.add_argument("--sector", help="e.g. cafe, restaurant, pos, construction, pharmacy, menu, letterhead")
    ap.add_argument("--have", help="comma list of: " + ", ".join(HAVE))
    ap.add_argument("--tone", choices=TONES)
    ap.add_argument("--options", type=int, default=3)
    ap.add_argument("--seed", type=int)
    ap.add_argument("--exclude", help="comma list of ids to leave out (already shown or declined)")
    ap.add_argument("--no-history", action="store_true")
    ap.add_argument("--list", action="store_true")
    ap.add_argument("--show")
    a = ap.parse_args()
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

    if a.show:
        x = next((x for x in D if x["id"] == a.show), None)
        if not x:
            print(f"No direction '{a.show}'. Use --list.", file=sys.stderr)
            sys.exit(2)
        print(card("*", x))
        return
    if a.list:
        for x in D:
            if not a.kind or x["kind"] == a.kind:
                print(f"{x['kind']:5} {x['id']:24} {x['family']:14} {x['what'][:90]}")
        return

    seed = a.seed if a.seed is not None else int(time.time() * 1000) % 100000
    rng = random.Random(seed)
    pool = [x for x in D if x["kind"] == a.kind]
    notes = []
    excluded = set(s.strip() for s in (a.exclude or "").split(",") if s.strip())
    pool = [x for x in pool if x["id"] not in excluded]

    if a.have is not None:
        have = set(h.strip() for h in a.have.split(",") if h.strip())
        unknown = have - set(HAVE)
        if unknown:
            print(f"Unknown --have: {', '.join(sorted(unknown))}. Choose from: {', '.join(HAVE)}", file=sys.stderr)
            sys.exit(2)
        kept = [x for x in pool if satisfied(x["needs"], have)]
        notes.append(f"{len(pool) - len(kept)} dropped for missing assets")
        pool = kept
    if a.sector:
        s = a.sector.lower()
        match = [x for x in pool if s in x["fits"]]
        rest = [x for x in pool if s not in x["fits"] and "any" in x["fits"]]
        if len(match) + len(rest) >= a.options:
            pool = match + rest
            notes.append(f"sector '{s}': {len(match)} direct matches")
        else:
            notes.append(f"sector '{s}': too few matches, dealing from all")
    if a.tone:
        toned = [x for x in pool if a.tone in x["tones"]]
        if len(toned) >= a.options:
            pool = toned
        else:
            notes.append(f"tone '{a.tone}': too few matches, tone ignored")

    hist = {} if a.no_history else load_hist()
    recent = hist.get(a.kind, [])[-5:]
    fresh = [x for x in pool if x["id"] not in recent]
    if len(fresh) >= a.options:
        if len(fresh) < len(pool):
            notes.append(f"skipped {len(pool) - len(fresh)} dealt recently")
        pool = fresh

    if len(pool) < a.options:
        print(f"Only {len(pool)} direction(s) fit. Loosen --have/--sector/--tone or --exclude.", file=sys.stderr)
        if not pool:
            sys.exit(1)

    rng.shuffle(pool)
    dealt, families = [], set()
    for x in pool:                      # first pass: one per family
        if len(dealt) == a.options:
            break
        if x["family"] not in families:
            dealt.append(x)
            families.add(x["family"])
    for x in pool:                      # fill up if families ran out
        if len(dealt) == a.options:
            break
        if x not in dealt:
            dealt.append(x)

    if not a.no_history:
        hist[a.kind] = (hist.get(a.kind, []) + [x["id"] for x in dealt])[-15:]
        save_hist(hist)

    head = f"Deal {seed} ({a.kind}"
    head += f", sector={a.sector}" if a.sector else ""
    head += f", have={a.have}" if a.have is not None else ""
    head += f", tone={a.tone}" if a.tone else ""
    head += f"): {len(dealt)} options"
    print(head + (f"   [{'; '.join(notes)}]" if notes else ""))
    print()
    for i, x in enumerate(dealt):
        print(card("ABCDE"[i], x))
        print()
    print("Next: ground each card in the client's own material (directions.md section 2), name the cost of each,\n"
          "build them as real mockups, and let the person pick. Redeal with --exclude <ids> if a card can't work.")


if __name__ == "__main__":
    main()
