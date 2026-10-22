#!/usr/bin/env node
// shoot.mjs - screenshots of a page at phone / tablet / desktop sizes with headless Chrome.
// No dependencies: drives Chrome over the DevTools protocol (needs Node 22+ for WebSocket).
//
// Usage:
//   node shoot.mjs <url-or-file> [outDir] [options]
// Options:
//   --sizes=390x844,1440x900   viewport sizes (default: 390x844,1440x900). Widths < 768 emulate a phone.
//   --full                     capture the whole page height (scrolls first so reveal animations fire)
//   --dark                     emulate prefers-color-scheme: dark
//   --reduce-motion            emulate prefers-reduced-motion: reduce
//   --scale=2                  device pixel ratio (default 1)
//   --wait=1200                extra milliseconds after load and fonts
//   --name=shot                file name prefix (default: shot)
//   --css=option-a.css         inject this stylesheet after load (preview a token option on the real
//                              page without editing the project)
//   --dir=rtl                  force <html dir> (quick look at the right-to-left version)
//   --selector=".hero .btn"    capture only the first matching element (plus --pad, default 24px):
//                              close-ups for small decisions instead of whole pages
//   --jpeg                     write JPEG (quality 82) instead of PNG: about 5x smaller, fine for previews
//   --pdf                      print to PDF instead (print pieces): uses the page's CSS @page size, so set
//                              it to trim + bleed (e.g. @page { size: 91mm 61mm; margin: 0 }); backgrounds on
// Prints the paths of the PNG files it wrote.

import { spawn } from "node:child_process";
import fs from "node:fs";
import os from "node:os";
import path from "node:path";
import { pathToFileURL } from "node:url";

const args = process.argv.slice(2);
const opts = Object.fromEntries(args.filter(a => a.startsWith("--")).map(a => {
  const [k, v] = a.replace(/^--/, "").split("=");
  return [k, v === undefined ? true : v];
}));
const pos = args.filter(a => !a.startsWith("--"));
if (!pos[0]) {
  console.error("Usage: node shoot.mjs <url-or-file> [outDir] [--sizes=390x844,1440x900] [--full] [--dark] [--reduce-motion]");
  process.exit(2);
}
if (typeof WebSocket === "undefined") {
  console.error("This script needs Node 22 or newer (global WebSocket).");
  process.exit(2);
}

let target = pos[0];
if (!/^[a-z]+:\/\//i.test(target)) target = pathToFileURL(path.resolve(target)).href;
const outDir = path.resolve(pos[1] || ".design-options/shots");
fs.mkdirSync(outDir, { recursive: true });
const sizes = String(opts.sizes || "390x844,1440x900").split(",").map(s => s.split("x").map(Number));
const scale = Number(opts.scale || 1);
const extraWait = Number(opts.wait || 1200);
const prefix = String(opts.name || "shot");
const injectCss = opts.css ? fs.readFileSync(path.resolve(String(opts.css)), "utf8") : "";
const forceDir = opts.dir ? String(opts.dir) : "";

function findChrome() {
  if (process.env.CHROME_PATH && fs.existsSync(process.env.CHROME_PATH)) return process.env.CHROME_PATH;
  const pf = process.env["PROGRAMFILES"] || "C:\\Program Files";
  const pf86 = process.env["PROGRAMFILES(X86)"] || "C:\\Program Files (x86)";
  const local = process.env.LOCALAPPDATA || "";
  const list = [
    `${pf}\\Google\\Chrome\\Application\\chrome.exe`, `${pf86}\\Google\\Chrome\\Application\\chrome.exe`,
    `${local}\\Google\\Chrome\\Application\\chrome.exe`, `${pf86}\\Microsoft\\Edge\\Application\\msedge.exe`,
    `${pf}\\Microsoft\\Edge\\Application\\msedge.exe`,
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge",
    "/usr/bin/google-chrome", "/usr/bin/google-chrome-stable", "/usr/bin/chromium", "/usr/bin/chromium-browser",
  ];
  return list.find(p => p && fs.existsSync(p));
}

const chrome = findChrome();
if (!chrome) {
  console.error("Chrome or Edge not found. Set CHROME_PATH to the browser executable.");
  process.exit(2);
}

const profile = fs.mkdtempSync(path.join(os.tmpdir(), "dx-shoot-"));
const proc = spawn(chrome, [
  "--headless=new", "--remote-debugging-port=0", `--user-data-dir=${profile}`, "--no-first-run",
  "--no-default-browser-check", "--disable-gpu", "--hide-scrollbars", "--mute-audio",
  "--disable-extensions", "about:blank",
], { stdio: "ignore" });

const sleep = ms => new Promise(r => setTimeout(r, ms));

async function devtoolsUrl() {
  const file = path.join(profile, "DevToolsActivePort");
  for (let i = 0; i < 150; i++) {
    if (fs.existsSync(file)) {
      const [port, wsPath] = fs.readFileSync(file, "utf8").trim().split("\n");
      if (port && wsPath) return `ws://127.0.0.1:${port}${wsPath}`;
    }
    await sleep(100);
  }
  throw new Error("Chrome did not start (no DevToolsActivePort).");
}

let ws, nextId = 1;
const pending = new Map();
const listeners = [];
function send(method, params = {}, sessionId) {
  const id = nextId++;
  ws.send(JSON.stringify({ id, method, params, ...(sessionId ? { sessionId } : {}) }));
  return new Promise((resolve, reject) => pending.set(id, { resolve, reject, method }));
}
function waitEvent(name, sessionId, timeout = 30000) {
  return new Promise(resolve => {
    const l = { name, sessionId, resolve };
    listeners.push(l);
    setTimeout(() => { const i = listeners.indexOf(l); if (i >= 0) { listeners.splice(i, 1); resolve(null); } }, timeout);
  });
}

async function main() {
  ws = new WebSocket(await devtoolsUrl());
  await new Promise((res, rej) => { ws.onopen = res; ws.onerror = rej; });
  ws.onmessage = ev => {
    const msg = JSON.parse(typeof ev.data === "string" ? ev.data : ev.data.toString());
    if (msg.id && pending.has(msg.id)) {
      const p = pending.get(msg.id); pending.delete(msg.id);
      msg.error ? p.reject(new Error(`${p.method}: ${msg.error.message}`)) : p.resolve(msg.result);
    } else if (msg.method) {
      for (const l of [...listeners]) {
        if (l.name === msg.method && (!l.sessionId || l.sessionId === msg.sessionId)) {
          listeners.splice(listeners.indexOf(l), 1); l.resolve(msg.params);
        }
      }
    }
  };

  const written = [];
  for (const [w, h] of sizes) {
    const { targetId } = await send("Target.createTarget", { url: "about:blank" });
    const { sessionId } = await send("Target.attachToTarget", { targetId, flatten: true });
    const s = (m, p) => send(m, p, sessionId);
    const mobile = w < 768;
    await s("Page.enable");
    await s("Emulation.setDeviceMetricsOverride", { width: w, height: h, deviceScaleFactor: scale, mobile });
    if (mobile) await s("Emulation.setTouchEmulationEnabled", { enabled: true, maxTouchPoints: 5 });
    await s("Emulation.setEmulatedMedia", { features: [
      { name: "prefers-color-scheme", value: opts.dark ? "dark" : "light" },
      { name: "prefers-reduced-motion", value: opts["reduce-motion"] ? "reduce" : "no-preference" },
    ] });
    const loaded = waitEvent("Page.loadEventFired", sessionId);
    await s("Page.navigate", { url: target });
    await loaded;
    if (forceDir) {
      await s("Runtime.evaluate", { expression: `document.documentElement.setAttribute("dir", ${JSON.stringify(forceDir)})` });
    }
    if (injectCss) {
      await s("Runtime.evaluate", { expression: `(() => { const st = document.createElement("style");
        st.setAttribute("data-dx-option", ""); st.textContent = ${JSON.stringify(injectCss)};
        document.head.appendChild(st); return true; })()` });
    }
    await s("Runtime.evaluate", { expression: "document.fonts ? document.fonts.ready.then(() => true) : true", awaitPromise: true });
    if (opts.pdf) {
      await sleep(extraWait);
      const pdf = await s("Page.printToPDF", { printBackground: true, preferCSSPageSize: true,
        marginTop: 0, marginBottom: 0, marginLeft: 0, marginRight: 0 });
      const file = path.join(outDir, `${prefix}.pdf`);
      fs.writeFileSync(file, Buffer.from(pdf.data, "base64"));
      written.push(file);
      await send("Target.closeTarget", { targetId });
      break;
    }
    let clip;
    if (opts.selector) {
      const pad = Number(opts.pad ?? 24);
      const r = await s("Runtime.evaluate", { returnByValue: true, expression: `(() => {
        const el = document.querySelector(${JSON.stringify(String(opts.selector))});
        if (!el) return null;
        el.scrollIntoView({ block: "center" });
        const b = el.getBoundingClientRect();
        return { x: b.left + scrollX, y: b.top + scrollY, w: b.width, h: b.height };
      })()` });
      const b = r.result && r.result.value;
      if (!b) throw new Error(`No element matches ${opts.selector}`);
      clip = { x: Math.max(0, b.x - pad), y: Math.max(0, b.y - pad), width: b.w + pad * 2, height: b.h + pad * 2, scale: 1 };
    } else if (opts.full) {
      await s("Runtime.evaluate", { awaitPromise: true, expression: `(async () => {
        const step = innerHeight * 0.8;
        for (let y = 0; y < document.documentElement.scrollHeight; y += step) { scrollTo(0, y); await new Promise(r => setTimeout(r, 120)); }
        scrollTo(0, 0); await new Promise(r => setTimeout(r, 300)); return true; })()` });
      const m = await s("Page.getLayoutMetrics");
      const size = m.cssContentSize || m.contentSize;
      clip = { x: 0, y: 0, width: w, height: Math.min(Math.ceil(size.height), 16000), scale: 1 };
    }
    await sleep(extraWait);
    const fmt = opts.jpeg ? "jpeg" : "png";
    const shot = await s("Page.captureScreenshot", { format: fmt, ...(opts.jpeg ? { quality: 82 } : {}),
      ...(clip ? { clip, captureBeyondViewport: true } : {}) });
    const tag = opts.selector ? "-el" : opts.full ? "-full" : "";
    const file = path.join(outDir, `${prefix}-${w}x${h}${tag}${opts.dark ? "-dark" : ""}.${opts.jpeg ? "jpg" : "png"}`);
    fs.writeFileSync(file, Buffer.from(shot.data, "base64"));
    written.push(file);
    await send("Target.closeTarget", { targetId });
  }
  for (const f of written) console.log(f);
}

main()
  .catch(e => { console.error(e.message || e); process.exitCode = 1; })
  .finally(async () => {
    try { await send("Browser.close"); } catch {}
    try { ws && ws.close(); } catch {}
    await sleep(300);
    try { proc.kill(); } catch {}
    try { fs.rmSync(profile, { recursive: true, force: true }); } catch {}
    setTimeout(() => process.exit(process.exitCode || 0), 200);
  });
