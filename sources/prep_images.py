#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Prepare optimized images for Tarik Chouika's portfolio site."""
import os
from PIL import Image, ImageOps

UP = '/home/z/my-project/upload'
OUT = '/home/z/my-project/site/img'
os.makedirs(OUT, exist_ok=True)


def load(path):
    im = Image.open(path)
    im = ImageOps.exif_transpose(im)
    return im.convert('RGB')


def save(im, name, quality=84):
    dst = os.path.join(OUT, name)
    im.save(dst, 'JPEG', quality=quality, optimize=True, progressive=True)
    return dst


# --- Profile photo (square, from the selfie) ---
im = load(os.path.join(UP, 'FB_IMG_1792908849571.jpg'))
save(ImageOps.fit(im, (760, 760), Image.LANCZOS, centering=(0.5, 0.42)), 'profile.jpg')

# --- Gallery photos (4:3, max ~1100px wide) ---
def gallery(src, name, centering=(0.5, 0.5), trim_bottom=0.0):
    im = load(os.path.join(UP, src))
    if trim_bottom:
        w, h = im.size
        im = im.crop((0, 0, w, int(h * (1 - trim_bottom))))
    save(ImageOps.fit(im, (1100, 825), Image.LANCZOS, centering=centering), name, quality=82)

# pool with child
gallery('FB_IMG_1792908926840.jpg', 'g1.jpg')
# family evening photo
gallery('FB_IMG_1792908861686.jpg', 'g2.jpg', centering=(0.5, 0.45))
# man with dog (phone screenshot: trim android nav bar)
gallery('Screenshot_20261025_061120_Facebook.jpg', 'g3.jpg', centering=(0.5, 0.42), trim_bottom=0.10)
# lake sunset
gallery('FB_IMG_1792908559233.jpg', 'g4.jpg')

for f in sorted(os.listdir(OUT)):
    print(f, round(os.path.getsize(os.path.join(OUT, f)) / 1024), 'KB')
