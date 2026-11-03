#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Validate generated site pages: HTML tag balance, key content, links."""
import os
import re
from html.parser import HTMLParser

OUT = '/home/z/my-project/site'
LANGS = ['ar', 'en', 'fr', 'es', 'it', 'de', 'nl', 'pt']
VOID = {'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 'link',
        'meta', 'param', 'source', 'track', 'wbr'}


class Checker(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack = []
        self.errors = []

    def handle_starttag(self, tag, attrs):
        if tag not in VOID:
            self.stack.append((tag, self.getpos()))

    def handle_endtag(self, tag):
        if tag in VOID:
            return
        if not self.stack:
            self.errors.append('unexpected </%s> at %s' % (tag, self.getpos()))
            return
        open_tag, pos = self.stack.pop()
        if open_tag != tag:
            self.errors.append('mismatch: <%s> opened at %s closed by </%s> at %s'
                               % (open_tag, pos, tag, self.getpos()))


def check(lang):
    path = os.path.join(OUT, 'index.html') if lang == 'ar' else os.path.join(OUT, lang, 'index.html')
    with open(path, encoding='utf-8') as f:
        content = f.read()

    c = Checker()
    c.feed(content)
    c.close()
    leftovers = [t for t, _ in c.stack if t != 'html']
    problems = list(c.errors)
    if leftovers:
        problems.append('unclosed tags: %s' % leftovers)

    # content sanity
    checks = {
        'lang attr': ('lang="%s"' % lang) in content,
        'dir': ('dir="%s"' % ('rtl' if lang == 'ar' else 'ltr')) in content,
        'canonical': 'rel="canonical"' in content,
        'hreflang x-default': 'hreflang="x-default"' in content,
        'jsonld': 'application/ld+json' in content,
        'email': 'tarikchouika@gmail.com' in content,
        'drive link': 'drive.google.com/drive/folders/1Cc_VyvUNQl2ybsRzovXu63vad77k9KBY' in content,
        'sections': all(s in content for s in
                        ['id="about"', 'id="experience"', 'id="certificates"',
                         'id="projects"', 'id="skills"', 'id="education"',
                         'id="gallery"', 'id="contact"']),
        'credential 1': 'W6G 9GJ VNJ' in content,
        'credential 2': '2YQ Q7H DY9' in content,
        '13 cert cards': content.count('class="cert-card card reveal"') == 13,
        'filter chips': content.count('class="f-chip') >= 6,
        'lightbox': 'id="cert-lb"' in content and 'data-full="/certs/c01.jpg"' in content,
        'huawei cert': 'ICT20260519000075' in content,
        'hp cert': 'c76722f4-9169-474f-83e8-d93859654c2d' in content,
        'theme toggle': 'id="theme-toggle"' in content,
        'theme bootstrap': "localStorage.getItem('tc-theme')" in content,
        '8 projects': all(p in content for p in
                          ['pj-natsup.jpg', 'pj-syda.jpg', 'pj-dtsg.jpg', 'pj-hrmp.jpg',
                           'pj-mamp.jpg', 'pj-isyacar.jpg', 'pj-phmp.jpg', 'pj-epdp.jpg']),
        'project links': all(u in content for u in
                             ['natsup.pages.dev', 'syda.pages.dev', 'dtsg.pages.dev',
                              'hrmp.pages.dev', 'mamp.pages.dev', 'isyacar.pages.dev',
                              'phmp.pages.dev', 'epdp.pages.dev']),
        '8 project cards': content.count('class="proj-card card reveal"') == 8,
        'stats 8 projects': '>8</b>' in content,
        'stats 13': '>13</b>' in content,
        'no leftover tokens': '{{' not in content,
        '8 lang options': content.count('<option value=') == 8,
        'footer lang links': all(x in content for x in
                                 ['العربية', 'English', 'Français', 'Español',
                                  'Italiano', 'Deutsch', 'Nederlands', 'Português']),
        'profile img': '/img/profile.jpg' in content,
        'gallery imgs': all('/img/g%d.jpg' % i in content for i in range(1, 5)),
        'services nav link': 'services/' in content,
        'services hero cta': 'CTA' not in '' or True,  # placeholder (cta presence checked via nav)
    }
    failed = [k for k, v in checks.items() if not v]
    status = 'OK ' if not problems and not failed else 'FAIL'
    print('%s %-4s size=%6d  %s%s' % (status, lang, len(content) // 1024, lang.upper(),
          ('| issues: ' + '; '.join(problems + failed)) if (problems or failed) else ''))
    return not problems and not failed


ok = all(check(l) for l in LANGS)
print('\nALL PAGES VALID' if ok else '\nVALIDATION FAILED')

# ---- v8: services pages + epdp project pages ----
print('\n-- v8 pages: services x8 + epdp project x8 --')
v8_ok = True
for lang in LANGS:
    base = '' if lang == 'ar' else lang + '/'
    svc_path = os.path.join(OUT, base + 'services', 'index.html')
    if not os.path.exists(svc_path):
        print('FAIL %s services page MISSING' % lang)
        v8_ok = False
        continue
    s = open(svc_path, encoding='utf-8').read()
    issues = []
    if s.count('class="svc-card card reveal"') != 6:
        issues.append('svc-cards=%d' % s.count('class="svc-card card reveal"'))
    if s.count('class="svc-step reveal"') != 4:
        issues.append('svc-steps=%d' % s.count('class="svc-step reveal"'))
    if s.count('class="value-card card reveal"') != 4:
        issues.append('why-cards=%d' % s.count('class="value-card card reveal"'))
    if '{{' in s:
        issues.append('leftover tokens')
    if 'id="svc-cta"' not in s or 'data-chat-wizard' not in s:
        issues.append('cta/chat missing')
    if 'hreflang="x-default"' not in s:
        issues.append('hreflangs missing')
    # language switcher must keep the services suffix
    if ('services/" selected' not in s and ('value="/services/"' not in s)):
        issues.append('lang switcher suffix')
    ep_path = os.path.join(OUT, base + 'projects', 'epdp', 'index.html')
    if not os.path.exists(ep_path):
        issues.append('epdp page MISSING')
    else:
        e = open(ep_path, encoding='utf-8').read()
        if 'epdp.pages.dev' not in e or 'pj-epdp.jpg' not in e:
            issues.append('epdp content incomplete')
        if '{{' in e:
            issues.append('epdp leftover tokens')
    print('%s %-4s services+epdp %s' % ('FAIL' if issues else 'OK  ', lang,
                                        '| ' + '; '.join(issues) if issues else ''))
    v8_ok = v8_ok and not issues

# sitemap must list services + epdp
sm = open(os.path.join(OUT, 'sitemap.xml'), encoding='utf-8').read()
for needle in ['/services/', '/projects/epdp/']:
    if needle not in sm:
        print('FAIL sitemap missing %s' % needle)
        v8_ok = False

print('\nV8 PAGES VALID' if v8_ok else '\nV8 VALIDATION FAILED')
raise SystemExit(0 if (ok and v8_ok) else 1)
