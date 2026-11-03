#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Capture epdp.pages.dev cover screenshot -> site/img/pj-epdp.jpg (1000x625)."""
import asyncio
import os
from playwright.async_api import async_playwright
from PIL import Image

URL = 'https://epdp.pages.dev/'
RAW = '/tmp/pj-epdp-raw.png'
OUT = '/home/z/my-project/site/img/pj-epdp.jpg'


async def shot():
    async with async_playwright() as p:
        browser = await p.chromium.launch(args=['--no-sandbox'])
        page = await browser.new_page(viewport={'width': 1280, 'height': 800},
                                      device_scale_factor=1)
        await page.goto(URL, wait_until='networkidle', timeout=90000)
        await page.wait_for_timeout(2500)
        await page.screenshot(path=RAW, full_page=False)
        await browser.close()


asyncio.run(shot())

# cover-crop to 16:10 (1000x625) — same pipeline as other project covers
img = Image.open(RAW).convert('RGB')
W, H = 1000, 625
ratio = W / H
w, h = img.size
if w / h > ratio:
    nw = int(h * ratio)
    x = (w - nw) // 2
    img = img.crop((x, 0, x + nw, h))
else:
    nh = int(w / ratio)
    y = max(0, (h - nh) // 3)  # bias toward top (header)
    img = img.crop((0, y, w, y + nh))
img = img.resize((W, H), Image.LANCZOS)
img.save(OUT, 'JPEG', quality=78, optimize=True, progressive=True)
print('saved %s (%.0f KB)' % (OUT, os.path.getsize(OUT) / 1024))
