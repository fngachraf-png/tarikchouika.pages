#!/usr/bin/env python3
"""Capture professional screenshots of all project sites.
4 shots per project: desktop hero, desktop content, tablet, mobile.
Saved to /home/z/my-project/site/img/shots/ then downscaled/optimized.
"""
import os, sys, time, json
from playwright.sync_api import sync_playwright
from PIL import Image

BASE = '/home/z/my-project/site/img/shots'
RAW = '/tmp/shots_raw'
os.makedirs(BASE, exist_ok=True)
os.makedirs(RAW, exist_ok=True)

PROJECTS = {
    'natsup':    'https://natsup.pages.dev/',
    'syda':      'https://syda.pages.dev/',
    'dtsg':      'https://dtsg.pages.dev/',
    'hrmp':      'https://hrmp.pages.dev/',
    'mamp':      'https://mamp.pages.dev/',
    'isyacar':   'https://isyacar.pages.dev/',
    'phmp':      'https://phmp.pages.dev/',
    'epdp':      'https://epdp.pages.dev/',
    'natsuptc':  'https://natsuptc.pages.dev/',
    'cmdp':      'https://cmdp.pages.dev/',
}

DESKTOP = {'width': 1440, 'height': 900}
TABLET  = {'width': 768,  'height': 1024}
MOBILE  = {'width': 390,  'height': 844}


def settle(page):
    """Wait for network quiet + fonts, scroll through page to trigger reveal
    animations, then scroll back to top."""
    try:
        page.wait_for_load_state('networkidle', timeout=25000)
    except Exception:
        pass
    try:
        page.evaluate('document.fonts && document.fonts.ready.then(() => true)')
    except Exception:
        pass
    # scroll through the page to trigger lazy/reveal content
    try:
        page.evaluate('''async () => {
            const h = Math.max(document.body.scrollHeight, document.documentElement.scrollHeight);
            const step = Math.round(window.innerHeight * 0.85);
            for (let y = 0; y <= h; y += step) {
                window.scrollTo(0, y);
                await new Promise(r => setTimeout(r, 120));
            }
            window.scrollTo(0, 0);
        }''')
    except Exception:
        pass
    time.sleep(0.7)


def shot(page, path):
    page.screenshot(path=path, type='jpeg', quality=90)


def capture_project(pw, slug, url):
    out = {}
    browser = pw.chromium.launch(args=['--force-color-profile=srgb', '--hide-scrollbars'])
    try:
        # ---------- DESKTOP ----------
        ctx = browser.new_context(viewport=DESKTOP, device_scale_factor=2,
                                  locale='ar-MA' if slug not in ('isyacar',) else 'en-US',
                                  timezone_id='Africa/Casablanca')
        page = ctx.new_page()
        page.goto(url, wait_until='domcontentloaded', timeout=45000)
        settle(page)
        d1 = f'{RAW}/{slug}-d1.png'
        shot(page, d1)
        # content shot: scroll to 1.7 viewports deep (mid content), re-settle reveals
        try:
            page.evaluate(f"window.scrollTo(0, Math.round(window.innerHeight * 1.7))")
            time.sleep(0.9)
        except Exception:
            pass
        d2 = f'{RAW}/{slug}-d2.png'
        shot(page, d2)
        ctx.close()
        out['d1'], out['d2'] = d1, d2

        # ---------- TABLET ----------
        ctx = browser.new_context(viewport=TABLET, device_scale_factor=2,
                                  locale='ar-MA', timezone_id='Africa/Casablanca')
        page = ctx.new_page()
        page.goto(url, wait_until='domcontentloaded', timeout=45000)
        settle(page)
        t = f'{RAW}/{slug}-t.png'
        shot(page, t)
        ctx.close()
        out['t'] = t

        # ---------- MOBILE ----------
        ctx = browser.new_context(viewport=MOBILE, device_scale_factor=3,
                                  locale='ar-MA', timezone_id='Africa/Casablanca',
                                  is_mobile=True, has_touch=True)
        page = ctx.new_page()
        page.goto(url, wait_until='domcontentloaded', timeout=45000)
        settle(page)
        m = f'{RAW}/{slug}-m.png'
        shot(page, m)
        ctx.close()
        out['m'] = m
    finally:
        browser.close()

    # ---------- optimize ----------
    sizes = {'d1': 1600, 'd2': 1600, 't': 900, 'm': 720}
    for k, raw in out.items():
        im = Image.open(raw).convert('RGB')
        w, h = im.size
        tw = sizes[k]
        if w > tw:
            im = im.resize((tw, round(h * tw / w)), Image.LANCZOS)
        dst = f'{BASE}/{slug}-{k}.jpg'
        im.save(dst, 'JPEG', quality=82, optimize=True, progressive=True)
    return {k: f'{BASE}/{slug}-{k}.jpg' for k in out}


def main():
    only = sys.argv[1:] if len(sys.argv) > 1 else list(PROJECTS)
    results = {}
    with sync_playwright() as pw:
        for slug in only:
            url = PROJECTS[slug]
            t0 = time.time()
            try:
                res = capture_project(pw, slug, url)
                results[slug] = res
                print(f'OK  {slug:10s} {time.time()-t0:5.1f}s -> ' +
                      ', '.join(os.path.basename(v) for v in res.values()), flush=True)
            except Exception as e:
                print(f'ERR {slug:10s} {type(e).__name__}: {e}', flush=True)
    with open('/tmp/shots_report.json', 'w') as f:
        json.dump(results, f, indent=1)
    print('DONE', len(results), '/', len(only))


if __name__ == '__main__':
    main()
