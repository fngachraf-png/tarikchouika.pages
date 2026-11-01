#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Download all files from Tarik's Google Drive certificates folder.

gdown can list the folder but its download step is blocked by Drive's
public-link wall; the drive.usercontent.google.com endpoint works.
Run with the python that has gdown: /usr/bin/python3.13
"""
import json
import os
import shutil
import subprocess
import sys
import urllib.parse

import gdown

FOLDER_URL = 'https://drive.google.com/drive/folders/1Cc_VyvUNQl2ybsRzovXu63vad77k9KBY'
OUT = '/home/z/my-project/certs_raw'
UA = ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
      '(KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36')


def list_files():
    files = gdown.download_folder(url=FOLDER_URL, skip_download=True, quiet=True)
    out = []
    for f in files:
        out.append({'id': f.id, 'name': f.path})
    return out


def download(fid, name):
    safe = name.replace('/', '_').replace('\\', '_')
    dst = os.path.join(OUT, safe)
    if os.path.exists(dst) and os.path.getsize(dst) > 1024:
        return dst, 'cached'
    url = ('https://drive.usercontent.google.com/download?id=%s&export=download&confirm=t'
           % urllib.parse.quote(fid))
    r = subprocess.run(['curl', '-sL', '--max-time', '120', '-A', UA,
                        '-o', dst, url], capture_output=True, text=True)
    if not os.path.exists(dst) or os.path.getsize(dst) < 1024:
        return dst, 'FAILED (empty)'
    with open(dst, 'rb') as fh:
        head = fh.read(8)
    if not (head.startswith(b'%PDF') or head.startswith(b'\xff\xd8') or head.startswith(b'\x89PNG')):
        return dst, 'NOT A FILE (html/permission page?)'
    return dst, 'ok'


def main():
    os.makedirs(OUT, exist_ok=True)
    files = list_files()
    print('FOUND %d items' % len(files))
    manifest = []
    for f in files:
        dst, status = download(f['id'], f['name'])
        size = os.path.getsize(dst) if os.path.exists(dst) else 0
        print('%-70s %10d bytes  [%s]' % (f['name'], size, status))
        manifest.append({'id': f['id'], 'name': f['name'], 'local': dst,
                         'size': size, 'status': status})
    with open(os.path.join(OUT, '_manifest.json'), 'w', encoding='utf-8') as fh:
        json.dump(manifest, fh, ensure_ascii=False, indent=2)
    ok = sum(1 for m in manifest if m['status'] in ('ok', 'cached'))
    print('DONE: %d/%d downloaded' % (ok, len(manifest)))


if __name__ == '__main__':
    main()
