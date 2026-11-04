#!/usr/bin/env python3
"""Re-capture d2 shots as SQUARE (1000x1000) so the cover-crop in the trio row
doesn't cut content mid-word. Square ratio (1.0) matches the cell ratio (~0.97)."""
import time
from playwright.sync_api import sync_playwright
from PIL import Image

BASE = '/home/z/my-project/site/img/shots'

PROJECTS = {
    'natsup': 'https://natsup.pages.dev/', 'natsuptc': 'https://natsuptc.pages.dev/',
    'syda': 'https://syda.pages.dev/', 'dtsg': 'https://dtsg.pages.dev/',
    'hrmp': 'https://hrmp.pages.dev/', 'mamp': 'https://mamp.pages.dev/',
    'isyacar': 'https://isyacar.pages.dev/', 'phmp': 'https://phmp.pages.dev/',
    'epdp': 'https://epdp.pages.dev/', 'cmdp': 'https://cmdp.pages.dev/',
}

with sync_playwright() as pw:
    b = pw.chromium.launch(args=['--force-color-profile=srgb', '--hide-scrollbars'])
    for slug, url in PROJECTS.items():
        ctx = b.new_context(viewport={'width': 1000, 'height': 1000}, device_scale_factor=2,
                            locale='en-US' if slug == 'isyacar' else 'ar-MA',
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
        if slug == 'phmp':
            pg.wait_for_timeout(2000)
            pg.click('text=حسابي')
            pg.wait_for_timeout(1600)
        else:
            # gentle single scroll to content, then settle (no fast scroll-through:
            # it blanked natsup mobile before)
            try:
                pg.evaluate('window.scrollTo(0, Math.round(window.innerHeight * 1.55))')
                time.sleep(1.2)
            except Exception:
                pass
        raw = f'/tmp/{slug}-d2sq.png'
        pg.screenshot(path=raw, type='png')
        im = Image.open(raw).convert('RGB')
        if im.width > 1000:
            im = im.resize((1000, 1000), Image.LANCZOS)
        im.save(f'{BASE}/{slug}-d2.jpg', 'JPEG', quality=82, optimize=True, progressive=True)
        print('square d2:', slug, im.size, flush=True)
        ctx.close()
    b.close()

# quick sanity: pixel variance
import os
from PIL import ImageStat
for slug in PROJECTS:
    p = f'{BASE}/{slug}-d2.jpg'
    im = Image.open(p).convert('L'); im.thumbnail((300, 300))
    st = ImageStat.Stat(im)
    ok = st.stddev[0] > 10
    print(f'{"OK " if ok else "SUSPECT"} {slug}-d2 size={Image.open(p).size} std={st.stddev[0]:.1f}')
