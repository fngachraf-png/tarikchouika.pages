#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Optimize the 4 project screenshots into card images (1000x625 cover, q78)."""
import os

from PIL import Image

SRC = '/home/z/my-project/site/img'
OUT = '/home/z/my-project/site/img'
SITES = ['natsuptc', 'syda', 'dtsg', 'hrmp']

for s in SITES:
    src = os.path.join(SRC, 'pj-%s.png' % s)
    img = Image.open(src).convert('RGB')
    # cover-crop to 16:10
    W, H = 1000, 625
    ratio = W / H
    w, h = img.size
    if w / h > ratio:
        nw = int(h * ratio)
        x = (w - nw) // 2
        img = img.crop((x, 0, x + nw, h))
    else:
        nh = int(w / ratio)
        y = max(0, (h - nh) // 3)  # bias crop toward the top (headers)
        img = img.crop((0, y, w, y + nh))
    img = img.resize((W, H), Image.LANCZOS)
    dst = os.path.join(OUT, 'pj-%s.jpg' % s)
    img.save(dst, 'JPEG', quality=78, optimize=True, progressive=True)
    print('%s -> %.0f KB' % (dst, os.path.getsize(dst) / 1024))
    os.remove(src)
print('OK')
