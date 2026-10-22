# Stacks: where design decisions live

Every picked option has to land somewhere. Put it at the highest level that gives exactly the picked result, and say which level in the option ("changes the token, so all 14 buttons change" vs "only the hero button").

Order of preference: **design tokens → shared component → one instance.**

## Contents
1. Next.js + Tailwind v4 + shadcn/ui
2. Plain HTML / static sites
3. Flutter
4. Previewing options in each stack

---

## 1. Next.js + Tailwind v4 + shadcn/ui

**Tokens live in `app/globals.css`:**
- shadcn variables in `:root` and `.dark` (`--background`, `--foreground`, `--card`, `--primary`, `--primary-foreground`, `--muted`, `--accent`, `--border`, `--ring`, `--radius`...), mapped to utilities with `@theme inline`. Recent shadcn versions write them in OKLCH.
- Tailwind v4 tokens in `@theme { --color-*, --font-*, --radius-*, --ease-*, --spacing }`. There is no `tailwind.config.js` content array; use `@source` for classes in node_modules.
- **Theme before building.** Untouched shadcn defaults (slate/zinc neutrals, `--radius: 0.5rem`, the stock Card) are the most recognised "AI site" look. A palette, radius-by-role and type option should land here first.
- Components must use semantic tokens (`bg-primary text-primary-foreground`), never raw palette classes (`bg-indigo-600`) or hex.

**Fonts:**
- `next/font/local` for brand and Kurdish fonts (woff2 in the repo, or copied in at build if gitignored for licensing). Use `next/font/google` for Google families. Expose them as variables (`variable: "--font-ku"`) and map them in `@theme`.
- Kurdish/Arabic face and size factor per language:
  ```css
  :lang(ckb), :lang(ar) { font-family: var(--font-ku), var(--font-sans); font-size: calc(1em * var(--k, 1.12)); line-height: 1.7; letter-spacing: normal; }
  ```
  Apply it to text containers, not to `html`, so Latin digits and LTR islands aren't scaled.

**Right-to-left:**
- Locale segment (`app/[locale]/layout.tsx`) server-renders `<html lang={locale} dir={dir}>`.
- Wrap the app in Radix `DirectionProvider dir={dir}` so menus, sliders, tabs and arrow keys follow direction. Flip `Sheet side` and `DropdownMenu align` with the direction. Set Sonner's `dir`.
- Components added with `npx shadcn add` can contain physical classes (`ml-auto`, `left-2`, `pr-8`). Run `design_scan.py` on `components/ui` after adding.

**Component variants:** shadcn components are your code. Change a shared look in the component's `cva` variants (`components/ui/button.tsx`), not with one-off class overrides everywhere. Use `--dry-run` before re-adding a customised component.

**Images and pages:** `next/image` with width/height or `fill` + `sizes`, `priority` only on the hero image. Use `next/link` for internal links. Pair `loading.tsx` with skeletons sized like the real content.

**Dark mode:** `next-themes` with the class strategy, `color-scheme` on `<html>`, and a `themeColor` per scheme in the `viewport` export. Sonner's theme does not follow the OS by itself, so pass the resolved theme.

**Motion:** CSS first. Use `motion` (`motion/react`) for springs, exits, layout animation and gestures. `MotionConfig reducedMotion="user"`.

**Mobile baseline** (worth offering on any phone-facing site):
```html
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover, interactive-widget=resizes-content">
```
```css
html { -webkit-tap-highlight-color: transparent; -webkit-text-size-adjust: 100%; }
input, textarea, select { font-size: 16px; }
button, a, [role="button"] { touch-action: manipulation; }
```
Use `min-h-dvh` (app shells) / `svh` (heroes) instead of `h-screen`, and `env(safe-area-inset-*)` for bottom bars.

## 2. Plain HTML / static sites

- Tokens as CSS custom properties in one `:root` block (plus a `[data-theme="dark"]` or `prefers-color-scheme` block). Every colour, radius, font and duration comes from a variable.
- Tailwind via CDN: v4's browser build (`@tailwindcss/browser@4`) reads `<style type="text/tailwindcss">@theme { ... }</style>`. The old `cdn.tailwindcss.com` is v3 and uses `tailwind.config = {...}`. Fine for mockups, but not for a production site.
- Self-host fonts with `@font-face` + `unicode-range` per script (see `rtl-kurdish-arabic.md`).
- For a bilingual static site, use one page per language (`/index.html`, `/ckb/index.html`), each with its own `lang` and `dir`, sharing one stylesheet written with logical properties.

## 3. Flutter

**Tokens live in `ThemeData`:**
- `colorScheme`. `ColorScheme.fromSeed(seedColor: brand)` generates tones that can drift from the exact brand hex. When the brand colour must be exact, offer that as an option (`fromSeed(...).copyWith(primary: brand, onPrimary: ...)` or a hand-built `ColorScheme`).
- `textTheme` with the brand faces, plus `fontFamilyFallback` for mixed text. For Kurdish/Arabic locales, use `textTheme.apply(fontSizeFactor: 1.1)` (the picked factor).
- Component themes: `filledButtonTheme`, `elevatedButtonTheme`, `cardTheme`, `inputDecorationTheme`, `chipTheme`, `navigationRailTheme`. Style here, not per widget.
- `ThemeExtension<AppTokens>` for what Material has no slot for: spacing, radius by role, brand frame colour, money style.
- Ship a designed `darkTheme` (warm black with lighter cards, not inverted brand colours).

**Right-to-left and locales:** `localizationsDelegates` + `supportedLocales` (with a ckb fallback delegate), directional widgets everywhere, `Directionality` respected (see `rtl-kurdish-arabic.md` section 8).

**Tills and touch screens:**
- 48dp minimum targets (`minimumSize: Size(48, 48)`, `materialTapTargetSize`). Bigger for things tapped all day.
- One filled accent button per view (the next step). Other actions are tonal or outlined.
- Money in a tabular face (`FontFeature.tabularFigures()`, or a mono face).
- Visual density can tighten lists, but never shrink targets below 48.

**Where a change lands:** the theme for anything shared, a small reusable widget for a repeated pattern, the screen only for a true one-off.

## 4. Previewing options in each stack

| Stack | Small change | Big change |
|---|---|---|
| Next.js / Tailwind | text preview + before/after classes | CSS override per option shot over the running dev server (`shoot.mjs --css`), or self-contained mock pages |
| Plain HTML | text preview | copy the page per option into `.design-options/`, change the copy, compare |
| Flutter | text preview + before/after widget code | an HTML mock per option at the real device size (1366x768 till, 390x844 phone) built from the app's strings and colours. A debug-only theme switch in the app touches code, so ask first. |
| Print | text spec | render each option at true size to PNG/PDF and compare (see `print.md`) |

Always build previews with the real fonts. A Kurdish preview in a fallback font proves nothing.
