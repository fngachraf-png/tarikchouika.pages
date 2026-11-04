#!/usr/bin/env python3
"""Fix 3 defective shots:
- natsup-m / natsuptc-m : blank because scroll-through broke mobile view -> no scroll, longer wait
- phmp-d2 : page has no scroll -> capture the account/login modal instead
"""
import time
from playwright.sync_api import sync_playwright
from PIL import Image

BASE = '/home/z/my-project/site/img/shots'


def save(raw, dst, tw):
    im = Image.open(raw).convert('RGB')
    w, h = im.size
    if w > tw:
        im = im.resize((tw, round(h * tw / w)), Image.LANCZOS)
    im.save(dst, 'JPEG', quality=82, optimize=True, progressive=True)


with sync_playwright() as pw:
    b = pw.chromium.launch(args=['--force-color-profile=srgb', '--hide-scrollbars'])

    # ---- natsup + natsuptc mobile (no scroll-through) ----
    for slug, url in [('natsup', 'https://natsup.pages.dev/'),
                      ('natsuptc', 'https://natsuptc.pages.dev/')]:
        ctx = b.new_context(viewport={'width': 390, 'height': 844}, device_scale_factor=3,
                            is_mobile=True, has_touch=True, locale='ar-MA',
                            timezone_id='Africa/Casablanca')
        pg = ctx.new_page()
        pg.goto(url, wait_until='domcontentloaded', timeout=45000)
        try:
            pg.wait_for_load_state('networkidle', timeout=25000)
        except Exception:
            pass
        try:
            pg.evaluate('document.fonts && document.fonts.ready.then(() => true)')
        except Exception:
            pass
        pg.wait_for_timeout(2500)
        raw = f'/tmp/{slug}-m-fix.png'
        pg.screenshot(path=raw, type='png')
        save(raw, f'{BASE}/{slug}-m.jpg', 720)
        print('fixed', slug, '-m', flush=True)
        ctx.close()

    # ---- phmp d2: account modal ----
    ctx = b.new_context(viewport={'width': 1440, 'height': 900}, device_scale_factor=2,
                        locale='ar-MA', timezone_id='Africa/Casablanca')
    pg = ctx.new_page()
    pg.goto('https://phmp.pages.dev/', wait_until='domcontentloaded', timeout=45000)
    try:
        pg.wait_for_load_state('networkidle', timeout=25000)
    except Exception:
        pass
    pg.wait_for_timeout(2000)
    pg.click('text=حسابي')
    pg.wait_for_timeout(1600)
    raw = '/tmp/phmp-d2-fix.png'
    pg.screenshot(path=raw, type='png')
    save(raw, f'{BASE}/phmp-d2.jpg', 1600)
    print('fixed phmp-d2 (login modal)', flush=True)
    ctx.close()
    b.close()

print('ALL FIXED')
