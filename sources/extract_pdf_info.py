#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Extract text + metadata from all downloaded certificate files.

PDFs -> full text (first page) + doc info
JPGs -> reported for later VLM analysis
"""
import json
import os

import fitz  # PyMuPDF

RAW = '/home/z/my-project/certs_raw'
OUT_JSON = '/home/z/my-project/certs_analysis.json'

result = []
for name in sorted(os.listdir(RAW)):
    path = os.path.join(RAW, name)
    if not os.path.isfile(path) or name.startswith('_'):
        continue
    entry = {'file': name}
    if name.lower().endswith('.pdf'):
        try:
            doc = fitz.open(path)
            entry['pages'] = doc.page_count
            entry['meta'] = {k: v for k, v in (doc.metadata or {}).items() if v}
            text = ''
            for pno in range(min(2, doc.page_count)):
                text += doc[pno].get_text() + '\n---PAGE---\n'
            entry['text'] = text.strip()[:2500]
            doc.close()
        except Exception as e:
            entry['error'] = str(e)
    else:
        entry['note'] = 'image - needs VLM'
    result.append(entry)

with open(OUT_JSON, 'w', encoding='utf-8') as f:
    json.dump(result, f, ensure_ascii=False, indent=2)

for e in result:
    print('=' * 78)
    print('FILE:', e['file'])
    if 'meta' in e:
        print('META:', json.dumps(e['meta'], ensure_ascii=False)[:400])
    if 'text' in e:
        print('TEXT:')
        print(e['text'][:1300])
    if 'note' in e:
        print(e['note'])
print('\nsaved to', OUT_JSON)
