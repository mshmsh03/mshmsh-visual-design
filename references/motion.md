# Motion

Motion is a choice like any other, and "None" is often the best option. This file gives the gates that decide whether something should move, the values that make it feel right, and ready-made option sets for asking.

## Contents
1. The three gates
2. Easing and duration
3. Recipes (web)
4. Physics: origin, enter and exit, springs, interruptions
5. Pages: the one signature moment
6. Reduced motion
7. Performance
8. Right-to-left
9. Flutter
10. Option sets for asking
11. Names to use in options

---

## 1. The three gates

Run every candidate animation through these before offering it. If it fails a gate, don't offer it, or offer only "None" and "near-invisible".

**Frequency** (the master rule):

| How often the person sees it | What to offer |
|---|---|
| 100+ times a day: keyboard shortcuts, a command palette, core navigation, a till's item taps, qty +/-, the keypad | No animation. Press feedback at most (120ms, 3% scale). |
| Tens of times a day: hover, list navigation, frequent toggles, row selection | Remove, or near-invisible (under 150ms, opacity or colour only). |
| Occasionally: modals, drawers, toasts, sheets, settings | A standard animation. |
| Rarely: first run, empty states, a payment success, the end-of-day summary | The delight budget: longer beats, a little bounce, generous stagger. |

Keyboard-triggered actions never animate.

**Purpose.** Name it: feedback, spatial continuity (where it came from), state change, softening a jarring cut, explanation (marketing and onboarding only), or delight (rare moments only). If you can't name the purpose, don't offer it.

**Function.** Data people read or act on (prices, totals, charts, tables) never moves for style.

## 2. Easing and duration

```css
--ease-out:    cubic-bezier(0.23, 1, 0.32, 1);    /* UI enter and exit: the default */
--ease-in-out: cubic-bezier(0.77, 0, 0.175, 1);   /* something moving across the screen */
--ease-drawer: cubic-bezier(0.32, 0.72, 0, 1);    /* sheets and drawers (iOS feel) */
--ease-expo:   cubic-bezier(0.16, 1, 0.3, 1);     /* long reveals of 800ms and more on pages */
```
- **Hover and colour changes:** plain `ease`. **Constant motion** (marquee, progress, hold-to-fill): `linear`.
- **Never ease-in on UI.** It delays the part the person is watching, so a 300ms ease-in feels slower than a 300ms ease-out.
- Tailwind v4's built-in curves are weak (`--ease-out: cubic-bezier(0, 0, 0.2, 1)`, default transitions 150ms `cubic-bezier(0.4, 0, 0.2, 1)`). Override `--ease-out`, `--ease-in-out` and `--default-transition-timing-function` in `@theme` when motion is a picked option. Don't invent curves "that look familiar".

| Element | Duration |
|---|---|
| Button press | 100 to 160ms (120ms ceiling on things pressed all day) |
| Tooltip, small popover | 125 to 200ms |
| Dropdown, select, menu | 150 to 250ms |
| Toggle, chip, small state change | 150 to 200ms |
| Modal | 200 to 300ms |
| Drawer, sheet | 300 to 500ms (or a spring) |
| Route change | the platform default (iOS push ~350ms); "match the platform for navigation, beat it everywhere else" |
| Page reveals (marketing only) | 600 to 900ms; image openings 1,100 to 1,300ms |

**UI motion stays under 300ms** unless there is a stated reason. **Exits run at about 60 to 80% of the entrance**: the arrival deserves the time, the departure doesn't.

## 3. Recipes (web)

| Component | From state | Timing |
|---|---|---|
| Button press | `:active { transform: scale(0.97) }` (0.95 to 0.98) | 160ms ease-out (120ms on high-frequency controls) |
| Dropdown, popover, menu | opacity 0 + scale(0.95), origin at the trigger | 200ms ease-out |
| Tooltip | opacity 0 + scale(0.97), origin at the trigger; once one is open, neighbours open instantly | 125ms ease-out |
| Modal | opacity 0 + scale(0.96), origin centre; backdrop fades on the same timing | 250ms ease-out |
| Drawer, sheet | translateY(100%) to 0 | 500ms ease-drawer, or spring 0.8 / 0.3 |
| Toast | in and out by the same edge: translateY(100%), with `@starting-style` | 400ms `ease` (Sonner feel) or 300 in / 250 out |
| Accordion | `grid-template-rows: 0fr` to `1fr`, or a measured height; never to `auto` | 200 to 320ms ease-out |
| Stagger (a list the person asked for) | opacity 0 + translateY(8px) | 300ms, +40 to 50ms per item, at most 4 to 6 steps |
| Hold to confirm | `clip-path: inset(0 100% 0 0)` to `inset(0)` while held | hold 2s linear, release 200ms ease-out |
| Label or icon swap | blur(2px) + opacity 0.7 during the change | 200ms ease |

## 4. Physics: origin, enter and exit, springs, interruptions

- **Never start from scale(0).** Start at 0.9 to 0.97 plus a fade, "a balloon that has a shape even when deflated".
- **Popovers, menus and tooltips grow from their trigger** (`transform-origin` at the trigger; Radix exposes `--radix-popover-content-transform-origin` and the like). Modals are the exception: they grow from the centre.
- **Exit the way you entered.** A toast that came up from the bottom leaves through the bottom. That makes swipe-to-dismiss obvious.
- **Slow where the person decides, fast where the system responds:** hold 2s, release 200ms.
- **Springs only where a finger was involved:** drag with momentum, flick to dismiss, things that should feel alive. Motion: `{ type: "spring", duration: 0.4, bounce: 0 }` by default, and `bounce: 0.2` after a flick. Keep bounce at 0.3 or below, and never on a menu that simply faded in.
- **Interruptible:** use CSS transitions or springs (they retarget from where they are) for anything that can fire twice in a second (toasts, toggles), not keyframes (which restart from zero). Never lock input during a transition.
- **Drag to dismiss:** dismiss on distance past a threshold OR velocity above about 0.11 px/ms, so a quick flick is enough. Past an edge, rubber-band instead of hitting a wall.

## 5. Pages: the one signature moment

Persuade pages (landing, restaurant, portfolio) may move more than app screens. Even so:
- **One signature moment** carries the motion: one load sequence, one reveal, or one live interaction, picked from the subject. Examples: the menu's prices roll when the size switch changes, a headline rises line by line through a mask, a photo opens like a shutter, or the page simply stays still on purpose. If the move says nothing about the subject, it is decoration.
- **Section entrances, if any,** fire once, at about 85% down the viewport, rise 12 to 32px or use a line mask, and follow reading order. Nothing above the fold waits for scrolling. Nothing stays hidden longer than 900ms. The load sequence is done by 1.2s, with at most 4 elements, and the nav never animates.
- **Never offer:** a fade-up on every block, hover lift on every card, bounce/elastic on UI, meaningless loops (pulsing dots, shimmer for decoration, rotating badges), preloaders and counters, scroll-jacking, custom cursors, scramble or typewriter text, parallax over 8%, or anything moving across text being read.
- **App screens:** motion is feedback only. Nothing performs an entrance.

## 6. Reduced motion

**Fewer and gentler, not zero.** Keep opacity and colour changes that help understanding. Drop travel, scale, parallax, autoplay and overshoot, and turn screen transitions into fades. The reduced version is a finished design, shipped with the animation, not later:
```css
@media (prefers-reduced-motion: reduce) { .sheet { animation: fade 200ms ease; } }
```
When someone says "it isn't moving", check the computer's reduced-motion setting first.

## 7. Performance

- Animate only `transform`, `opacity` and `clip-path` (plus `filter` sparingly; blur under 20px). Accordions via `grid-template-rows`. Never width, height, top, left, margin or padding.
- **Never `transition: all`.** List the properties.
- Motion that plays while the page is busy (route change, data loading) belongs in CSS or WAAPI, not a JS-driven loop.
- `will-change` only on the animating element, only after you have seen a real problem.
- Never leave a resting transform, filter or `will-change` on a layer that holds text: the lettering goes soft.
- Judge smoothness on a mid-range phone, not on the development machine.

## 8. Right-to-left

- `translateX`, keyframes, `clip-path: inset()`, `background-position` and slide directions are physical: mirror them under `[dir="rtl"]` / `rtl:`. A hold-to-fill should run in the reading direction, and "forward" slides come from the left in right-to-left.
- **Never animate Kurdish or Arabic letter by letter** (typewriter, text morph, split text): it breaks the joins. Animate whole words or lines, or reveal intact text with a mask.

## 9. Flutter

- Curves: `Cubic(0.23, 1, 0.32, 1)` (= `Curves.easeOutQuint`) for enter and exit, `Cubic(0.77, 0, 0.175, 1)` for moves, `Cubic(0.32, 0.72, 0, 1)` for sheets. No `Curves.easeIn*` on UI.
- Springs: `SpringDescription.withDampingRatio(mass: 1, stiffness: (2π / response)², ratio: ζ)`. Default ζ 1.0 / response 0.4 gives stiffness ≈ 247; a sheet with ζ 0.8 / 0.3 gives ≈ 439.
- Press: `AnimatedScale(scale: pressed ? 0.97 : 1, duration: 120ms)` driven by `Listener` pointer down/up. `GestureDetector.onTapDown` inside scrollables can wait 100ms.
- **Till (POS) frequency map:** item taps, qty, keypad and scan-to-add get press feedback only, with no fly-to-cart. Payment success or the end-of-day summary may celebrate.
- Tabs and bottom nav switch instantly (`IndexedStack`), never slide. Routes use the platform transitions.
- Don't animate `ListView.builder` items (they re-fire on rebuild). Animate the container once, and use `AnimatedList` for inserts and removals.
- Animate with `FadeTransition` / `ScaleTransition` / `SlideTransition` / `Transform`, not `AnimatedContainer` size or padding. Wrap animating parts in `RepaintBoundary`.
- Reduced motion: `MediaQuery.disableAnimationsOf(context)`, then fade or change instantly.
- Countertop terminals often have no vibration motor, so haptics are never the only feedback.

## 10. Option sets for asking

Each option is a named motion plus exact values. Include "None" whenever the frequency gate says tens per day or more.

- **Button press:** A. Press scale 0.97, 120ms (Recommended for things pressed all day) · B. Colour/opacity change only · C. None.
- **Popover / menu:** A. Scale in from the trigger (0.95 + fade, 200ms ease-out) · B. Fade only (150ms) · C. None (instant).
- **Modal:** A. Scale in, centred (0.96 + fade, 250ms) · B. Fade with a dimming scrim · C. Bottom sheet on phones (drawer curve or spring).
- **Toast:** A. Slide in and out by the same edge (400ms `ease`) · B. Crisp slide + fade (300 in / 250 out) · C. Fade only.
- **List or grid that appears:** A. Stagger fade-up (8px, 300ms, 40ms steps) · B. One fade of the whole container · C. None (a list seen all day).
- **Page signature moment:** A. A move from the subject (named, e.g. "prices roll when the size changes") · B. One masked headline rise on load · C. Stillness (no entrances, only feedback).

## 11. Names to use in options

Fade in/out · Slide in · Scale in · Pop in (slight overshoot) · Reveal (clip-path, hard edge) vs Mask (soft edge) · Stagger · Crossfade · Morph · Shared element transition · Layout animation · Accordion · Scroll reveal · Scroll-driven animation · Parallax · View transition · Press feedback · Hold to confirm · Swipe to dismiss · Rubber-banding · Shake (error) · Number ticker · Marquee · Skeleton. Lead an option with the name, then the values.
