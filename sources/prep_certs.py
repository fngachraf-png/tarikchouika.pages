#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Render the 13 certificates into optimized site images.

PDFs -> pdftoppm (page 1); JPGs -> direct. All letterboxed to 3:2 on white:
  full  -> site/certs/cXX.jpg  (1500x1000, q80)  [lightbox]
  thumb -> site/certs/th/cXX.jpg (660x440, q74)  [cards]
"""
import glob
import os
import subprocess

from PIL import Image, ImageOps

RAW = '/home/z/my-project/certs_raw'
OUT = '/home/z/my-project/site/certs'
TH = os.path.join(OUT, 'th')
TMP = '/home/z/my-project/certs_tmp'

# cert id -> source file (chronological order)
SRC = {
    'c01': 'digitalskills_certificate.pdf',
    'c02': 'IMG-20220415-WA0003.jpg',
    'c03': 'klt_1792419581859.jpg',
    'c04': 'T-c3.pdf',
    'c05': 'T-C2.pdf',
    'c06': 'T-C.pdf',
    'c07': 'الذكاء الاصطناعي للمهنيين في مجال الأعمال.pdf',
    'c08': 'القيادة الفعالة.pdf',
    'c09': 'الذكاء الاصطناعي للمبتدئين.pdf',
    'c10': 'التواصل المهني من أجل النمو الوظيفي.pdf',
    'c11': 'مواقع الويب الفعالة.pdf',
    'c12': 'البريد الإلكتروني للعمل.pdf',
    'c13': 'التخطيط الاستراتيجي في عصر الذكاء الاصطناعي.pdf',
}


def load_source(cid, name):
    path = os.path.join(RAW, name)
    if name.lower().endswith('.pdf'):
        os.makedirs(TMP, exist_ok=True)
        prefix = os.path.join(TMP, cid)
        subprocess.run(['pdftoppm', '-png', '-r', '120', '-f', '1', '-l', '1',
                        path, prefix], check=True)
        produced = sorted(glob.glob(prefix + '*.png'))
        if not produced:
            raise SystemExit('pdftoppm produced nothing for ' + name)
        img = Image.open(produced[0])
    else:
        img = Image.open(path)
        img = ImageOps.exif_transpose(img)
    return img.convert('RGB')


def letterbox(img, W, H):
    canvas = Image.new('RGB', (W, H), (255, 255, 255))
    im = ImageOps.contain(img, (W - 24, H - 24))
    x = (W - im.width) // 2
    y = (H - im.height) // 2
    canvas.paste(im, (x, y))
    return canvas


def main():
    os.makedirs(TH, exist_ok=True)
    total = 0
    for cid in sorted(SRC):
        img = load_source(cid, SRC[cid])
        full = letterbox(img, 1500, 1000)
        thumb = letterbox(img, 660, 440)
        f1 = os.path.join(OUT, cid + '.jpg')
        f2 = os.path.join(TH, cid + '.jpg')
        full.save(f1, 'JPEG', quality=80, optimize=True, progressive=True)
        thumb.save(f2, 'JPEG', quality=74, optimize=True, progressive=True)
        s = os.path.getsize(f1) + os.path.getsize(f2)
        total += s
        print('%s  %dx%d -> %5.0f KB (full) + %4.0f KB (thumb)'
              % (cid, img.width, img.height,
                 os.path.getsize(f1) / 1024, os.path.getsize(f2) / 1024))
    print('TOTAL: %.1f MB for 13 certificates' % (total / 1024 / 1024))


if __name__ == '__main__':
    main()
