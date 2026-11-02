#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""v7: add PHMP (7th project) to all 8 translation modules + chatbot KB + certs_data.
Safe method: load each module, modify the dict in memory, rewrite the file with a
deterministic serializer (files are pure data — T = {...} — so nothing is lost)."""
import importlib.util
import re
import sys

sys.path.insert(0, '/home/z/my-project/scripts')
from v7_phmp_content import PHMP, COUNT_FIX, A_PROJECTS_BULLET, A_PROJECTS_TAIL_MARK, KW_ADD

SRC = '/home/z/my-project/scripts/site_src'
LANGS = ['ar', 'en', 'fr', 'es', 'it', 'de', 'nl', 'pt']


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def fmt(value, indent=1):
    pad = '    ' * indent
    if isinstance(value, dict):
        if not value:
            return '{}'
        items = []
        for k, v in value.items():
            items.append('%s%s: %s' % (pad, repr(k), fmt(v, indent + 1)))
        return '{\n' + ',\n'.join(items) + '\n' + '    ' * (indent - 1) + '}'
    if isinstance(value, list):
        if not value:
            return '[]'
        items = ['%s%s' % (pad, fmt(v, indent + 1)) for v in value]
        return '[\n' + ',\n'.join(items) + '\n' + '    ' * (indent - 1) + ']'
    if isinstance(value, tuple):
        if not value:
            return '()'
        items = ['%s%s' % (pad, fmt(v, indent + 1)) for v in value]
        return '(\n' + ',\n'.join(items) + ',\n' + '    ' * (indent - 1) + ')'
    return repr(value)


def rewrite_t_file(lang, T):
    path = '%s/t_%s.py' % (SRC, lang)
    original = open(path, encoding='utf-8').read()
    header_lines = []
    for line in original.splitlines():
        if line.startswith('#'):
            header_lines.append(line)
        else:
            break
    header = '\n'.join(header_lines) + ('\n\n' if header_lines else '')
    with open(path, 'w', encoding='utf-8') as f:
        f.write(header + 'T = ' + fmt(T) + '\n')


def apply_counts(obj, pairs):
    """Apply six->seven replacements across every string in the structure."""
    n = 0
    if isinstance(obj, str):
        for old, new in pairs:
            if old in obj:
                obj = obj.replace(old, new)
                n += 1
        return obj, n
    if isinstance(obj, list):
        out = []
        for v in obj:
            v2, k = apply_counts(v, pairs)
            n += k
            out.append(v2)
        return out, n
    if isinstance(obj, tuple):
        out = []
        for v in obj:
            v2, k = apply_counts(v, pairs)
            n += k
            out.append(v2)
        return tuple(out), n
    if isinstance(obj, dict):
        out = {}
        for k, v in obj.items():
            v2, c = apply_counts(v, pairs)
            n += c
            out[k] = v2
        return out, n
    return obj, 0


# ---------- 1. certs_data.py: PROJECTS gets phmp ----------
cd_path = '%s/certs_data.py' % SRC
s = open(cd_path, encoding='utf-8').read()
if "('phmp'" not in s:
    old = "    ('isyacar', '/img/pj-isyacar.jpg', 'https://isyacar.pages.dev'),\n]"
    new = ("    ('isyacar', '/img/pj-isyacar.jpg', 'https://isyacar.pages.dev'),\n"
           "    ('phmp', '/img/pj-phmp.jpg', 'https://phmp.pages.dev'),\n]")
    assert old in s, 'certs_data PROJECTS anchor not found'
    s = s.replace(old, new)
    open(cd_path, 'w', encoding='utf-8').write(s)
    print('certs_data.py: PHMP added to PROJECTS')
else:
    print('certs_data.py: PHMP already present')

# ---------- 2. translation modules ----------
for lang in LANGS:
    path = '%s/t_%s.py' % (SRC, lang)
    m = load(path, 't_' + lang)
    T = m.T
    P = PHMP[lang]

    # 2a. card entry
    names = [p['name'] for p in T['projects']]
    if 'PHMP' not in names:
        T['projects'].append(dict(P['card']))
    # 2b. project_pages
    if len(T['project_pages']) == 6:
        T['project_pages'].append(dict(P['page']))
    # 2c. project_v4
    if len(T['project_v4']) == 6:
        v4 = dict(P['v4'])
        v4['values'] = [tuple(x) for x in v4['values']]
        v4['effort_stats'] = [tuple(x) for x in v4['effort_stats']]
        T['project_v4'].append(v4)
    # 2d. project_tools
    if len(T['project_tools']) == 6:
        T['project_tools'].append([tuple(x) for x in P['tools']])
    # 2e. stats: projects count 6 -> 7
    fixed_stats = 0
    for stat in T['stats']:
        if stat[0] == '6':
            stat[0] = '7'
            fixed_stats += 1
    # 2f. wording fixes (pj_sub, desc, ...)
    T, nfix = apply_counts(T, COUNT_FIX[lang])
    rewrite_t_file(lang, T)
    print('t_%s.py: projects=%d pages=%d v4=%d tools=%d stats7=%d textfixes=%d'
          % (lang, len(T['projects']), len(T['project_pages']), len(T['project_v4']),
             len(T['project_tools']), fixed_stats, nfix))

# ---------- 3. chatbot_strings.py ----------
cs_path = '%s/chatbot_strings.py' % SRC
cs = load(cs_path, 'chatbot_strings')
CHAT = cs.CHAT
for lang in LANGS:
    S = CHAT[lang]
    ap = S['a_projects']
    if 'phmp.pages.dev' not in ap:
        mark = A_PROJECTS_TAIL_MARK[lang]
        idx = ap.find(mark)
        assert idx != -1, 'a_projects tail mark missing for ' + lang
        ap = ap[:idx] + A_PROJECTS_BULLET[lang] + ap[idx:]
    for old, new in COUNT_FIX[lang]:
        ap = ap.replace(old, new)
    S['a_projects'] = ap
    for key in ('a_services',):
        if key in S:
            v = S[key]
            for old, new in COUNT_FIX[lang]:
                v = v.replace(old, new)
            S[key] = v
    kws = S['kw'].get('projects', [])
    for k in KW_ADD[lang]:
        if k not in kws:
            kws.append(k)
    S['kw']['projects'] = kws

# rewrite chatbot_strings.py preserving header comments + SPEECH_LANG
original = open(cs_path, encoding='utf-8').read()
header_lines = []
for line in original.splitlines():
    if line.startswith('#'):
        header_lines.append(line)
    else:
        break
header = '\n'.join(header_lines) + ('\n\n' if header_lines else '')
with open(cs_path, 'w', encoding='utf-8') as f:
    f.write(header + 'CHAT = ' + fmt(CHAT) + '\n\n# speech recognition / synthesis locale per language\nSPEECH_LANG = ' + fmt(cs.SPEECH_LANG) + '\n')
print('chatbot_strings.py: a_projects/a_services counts fixed, PHMP bullet + keywords added')

print('v7 content applied OK')
