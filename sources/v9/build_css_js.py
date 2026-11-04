#!/usr/bin/env python3
"""Append shots-gallery CSS to style.css and shots-lightbox JS to main.js.
Idempotent: skips if marker already present. Also bumps ?v=8 -> ?v=9 site-wide.
"""
import os, re, glob

SITE = '/home/z/my-project/site'
CSS = f'{SITE}/css/style.css'
JS = f'{SITE}/js/main.js'
CSS_MARKER = '/* PROJECT SHOTS GALLERY */'
JS_MARKER = "/* ---------- Project shots lightbox ---------- */"

CSS_BLOCK = '''
/* ============================================================
   PROJECT SHOTS GALLERY /* PROJECT SHOTS GALLERY */
   ============================================================ */
.shots { display: flex; flex-direction: column; gap: 1.05rem; margin-top: 0.3rem; }
.shot { margin: 0; display: flex; flex-direction: column; gap: 0.55rem; }
.shot figcaption { color: var(--muted); font-size: 0.84rem; line-height: 1.6; text-align: center; }
html[lang="ar"] .shot figcaption { font-family: var(--font-ar); }
.shot-zoom {
  display: block; width: 100%; padding: 0; border: 0; margin: 0;
  background: none; cursor: zoom-in; border-radius: 14px; text-align: start;
  font: inherit; color: inherit;
}
.shot-zoom:focus-visible { outline: 2px solid var(--gold); outline-offset: 3px; border-radius: 16px; }

/* --- browser window frame --- */
.browser {
  display: block; border-radius: 14px; overflow: hidden;
  border: 1px solid var(--border); background: var(--card);
  box-shadow: var(--shadow);
}
.b-bar {
  display: flex; align-items: center; gap: 0.38rem;
  padding: 0.52rem 0.75rem; background: var(--card-hi);
  border-bottom: 1px solid var(--border);
}
.b-bar i { width: 9px; height: 9px; border-radius: 50%; flex: none; opacity: 0.85; }
.b-bar i:nth-child(1) { background: #e0695f; }
.b-bar i:nth-child(2) { background: #dfa94e; }
.b-bar i:nth-child(3) { background: #6dbb7e; }
.b-url {
  flex: 1; min-width: 0; margin-inline-start: 0.35rem;
  background: var(--bg-2); border: 1px solid var(--border); border-radius: 999px;
  padding: 0.24rem 0.85rem; font-size: 0.72rem; color: var(--muted);
  direction: ltr; text-align: center;
  overflow: hidden; text-overflow: ellipsis; white-space: nowrap;
}
.browser img { display: block; width: 100%; object-fit: cover; object-position: center top; }
.shot-main .browser img { aspect-ratio: 16 / 10; }

/* --- tablet & phone frames --- */
.dev-tab {
  display: block; border-radius: 20px; overflow: hidden;
  border: 10px solid var(--card-hi); outline: 1px solid var(--border);
  background: var(--card-hi); box-shadow: var(--shadow);
}
.dev-tab img { display: block; width: 100%; object-fit: cover; object-position: center top; }
.dev-phone {
  position: relative; display: block; max-width: 212px; margin-inline: auto;
  border-radius: 26px; overflow: hidden;
  border: 7px solid var(--card-hi); outline: 1px solid var(--border);
  background: var(--card-hi); box-shadow: var(--shadow);
}
.dev-phone::after {
  content: ""; position: absolute; top: 0; inset-inline: 0; margin-inline: auto;
  width: 74px; height: 15px; background: var(--card-hi);
  border-radius: 0 0 10px 10px; border: 1px solid var(--border); border-top: 0;
}
.dev-phone img { display: block; width: 100%; object-fit: cover; object-position: center top; }

/* --- hover art --- */
.browser, .dev-tab, .dev-phone {
  transition: transform 0.35s ease, box-shadow 0.35s ease, border-color 0.35s ease, outline-color 0.35s ease;
}
.shot-zoom:hover .browser, .shot-zoom:focus-visible .browser,
.shot-zoom:hover .dev-tab, .shot-zoom:focus-visible .dev-tab,
.shot-zoom:hover .dev-phone, .shot-zoom:focus-visible .dev-phone {
  transform: translateY(-4px);
  border-color: var(--border-gold); outline-color: var(--border-gold);
  box-shadow: 0 24px 50px -18px rgba(0, 0, 0, 0.65), 0 0 0 1px rgba(217, 166, 72, 0.14);
}
html[data-theme="light"] .shot-zoom:hover .browser,
html[data-theme="light"] .shot-zoom:hover .dev-tab,
html[data-theme="light"] .shot-zoom:hover .dev-phone {
  box-shadow: 0 24px 48px -20px rgba(96, 72, 20, 0.42), 0 0 0 1px rgba(185, 135, 47, 0.2);
}

/* --- trio row --- */
.shot-row { display: grid; grid-template-columns: 5fr 4fr 3fr; gap: 1.05rem; align-items: start; }
.shot-row .browser img { height: 330px; }
.shot-row .dev-tab img { height: 318px; }
.shot-row .dev-phone img { height: 336px; }

/* --- shots lightbox --- */
.shot-lb {
  position: fixed; inset: 0; z-index: 400;
  display: flex; align-items: center; justify-content: center;
  padding: clamp(1rem, 4vw, 2.6rem);
}
.shot-lb[hidden] { display: none; }
.slb-body {
  position: relative; z-index: 1; margin: 0;
  max-width: min(1120px, 100%);
  display: flex; flex-direction: column; gap: 0.75rem;
  animation: lbIn 0.32s ease;
}
.slb-body img {
  display: block; max-width: 100%; max-height: calc(100vh - 8.5rem);
  width: auto; height: auto; margin-inline: auto;
  border-radius: 12px; border: 1px solid var(--border-gold);
  background: var(--card);
  box-shadow: 0 40px 90px -30px rgba(0, 0, 0, 0.8);
}
.slb-body figcaption {
  display: flex; align-items: center; justify-content: center; gap: 0.9rem;
  flex-wrap: wrap; color: #ece9e2; font-size: 0.94rem; text-align: center;
}
html[lang="ar"] .slb-body figcaption { font-family: var(--font-ar); }
.slb-count { color: var(--gold-2); font-size: 0.8rem; font-weight: 700; letter-spacing: 0.04em; }
html[dir="rtl"] .slb-prev .ic { transform: scaleX(-1); }
html[dir="rtl"] .slb-next .ic { transform: scaleX(-1); }

@media (max-width: 980px) {
  .shot-row { grid-template-columns: 1fr 1fr; }
  .shot-row .shot:first-child { grid-column: 1 / -1; }
  .shot-row .browser img { height: 300px; }
  .shot-row .dev-tab img { height: 300px; }
  .shot-row .dev-phone img { height: 316px; }
}
@media (max-width: 640px) {
  .shots { gap: 0.9rem; }
  .shot-row { grid-template-columns: 1fr; }
  .shot-row .browser img { height: 250px; }
  .shot-row .dev-tab img { height: 330px; }
  .dev-phone { max-width: 244px; }
  .shot-row .dev-phone img { height: 420px; }
}
@media print {
  .shot-lb { display: none !important; }
  .shot-zoom { cursor: default; }
}
'''

JS_BLOCK = '''
  /* ---------- Project shots lightbox ---------- */
  var slb = document.getElementById('shot-lb');
  var shotBtns = Array.prototype.slice.call(document.querySelectorAll('.shot-zoom'));
  var slbIndex = -1, slbLastFocus = null;
  function openSlb(i) {
    var btn = shotBtns[i];
    if (!btn || !slb) return;
    slbLastFocus = btn;
    var img = document.getElementById('slb-img');
    if (img) {
      img.src = btn.getAttribute('data-full') || '';
      img.alt = btn.getAttribute('data-alt') || '';
    }
    var cap = document.getElementById('slb-cap');
    if (cap) cap.textContent = btn.getAttribute('data-cap') || '';
    var cnt = document.getElementById('slb-count');
    if (cnt) cnt.textContent = (i + 1) + ' / ' + shotBtns.length;
    slbIndex = i;
    slb.hidden = false;
    document.body.style.overflow = 'hidden';
    var c = slb.querySelector('.slb-close');
    if (c) c.focus();
  }
  function closeSlb() {
    if (!slb || slb.hidden) return;
    slb.hidden = true;
    document.body.style.overflow = '';
    if (slbLastFocus && slbLastFocus.focus) slbLastFocus.focus();
    slbIndex = -1;
  }
  function stepSlb(delta) {
    if (slbIndex < 0) return;
    openSlb((slbIndex + delta + shotBtns.length) % shotBtns.length);
  }
  if (slb && shotBtns.length) {
    shotBtns.forEach(function (btn, i) {
      btn.addEventListener('click', function () { openSlb(i); });
    });
    slb.querySelectorAll('[data-slb-close]').forEach(function (el) {
      el.addEventListener('click', closeSlb);
    });
    var slbPrev = document.getElementById('slb-prev');
    var slbNext = document.getElementById('slb-next');
    if (slbPrev) slbPrev.addEventListener('click', function () { stepSlb(-1); });
    if (slbNext) slbNext.addEventListener('click', function () { stepSlb(1); });
    document.addEventListener('keydown', function (e) {
      if (slb.hidden) return;
      if (e.key === 'Escape') { closeSlb(); }
      else if (e.key === 'ArrowLeft') { stepSlb(document.documentElement.dir === 'rtl' ? 1 : -1); }
      else if (e.key === 'ArrowRight') { stepSlb(document.documentElement.dir === 'rtl' ? -1 : 1); }
    });
  }

'''

# ---------- CSS ----------
css = open(CSS, encoding='utf-8').read()
if CSS_MARKER in css:
    print('CSS: already patched, skip')
else:
    css = css.rstrip() + '\n' + CSS_BLOCK.strip() + '\n'
    open(CSS, 'w', encoding='utf-8').write(css)
    print('CSS: appended shots gallery block')

# ---------- JS ----------
js = open(JS, encoding='utf-8').read()
if JS_MARKER in js:
    print('JS: already patched, skip')
else:
    anchor = "  /* ---------- Current year ---------- */"
    assert anchor in js, 'JS anchor not found'
    js = js.replace(anchor, JS_BLOCK + anchor, 1)
    open(JS, 'w', encoding='utf-8').write(js)
    print('JS: inserted shots lightbox block')

# ---------- version bump v8 -> v9 (style.css + main.js only) ----------
bumped = 0
for f in glob.glob(f'{SITE}/**/*.html', recursive=True) + glob.glob(f'{SITE}/*.html'):
    html = open(f, encoding='utf-8').read()
    new = html.replace('/css/style.css?v=8', '/css/style.css?v=9').replace('/js/main.js?v=8', '/js/main.js?v=9')
    if new != html:
        open(f, 'w', encoding='utf-8').write(new)
        bumped += 1
print(f'version bump v8->v9: {bumped} files updated')
