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
        '7 projects': all(p in content for p in
                          ['pj-natsup.jpg', 'pj-syda.jpg', 'pj-dtsg.jpg', 'pj-hrmp.jpg',
                           'pj-mamp.jpg', 'pj-isyacar.jpg', 'pj-phmp.jpg']),
        'project links': all(u in content for u in
                             ['natsup.pages.dev', 'syda.pages.dev', 'dtsg.pages.dev',
                              'hrmp.pages.dev', 'mamp.pages.dev', 'isyacar.pages.dev',
                              'phmp.pages.dev']),
        '7 project cards': content.count('class="proj-card card reveal"') == 7,
        'stats 13': '>13</b>' in content,
        'no leftover tokens': '{{' not in content,
        '8 lang options': content.count('<option value=') == 8,
        'footer lang links': all(x in content for x in
                                 ['العربية', 'English', 'Français', 'Español',
                                  'Italiano', 'Deutsch', 'Nederlands', 'Português']),
        'profile img': '/img/profile.jpg' in content,
        'gallery imgs': all('/img/g%d.jpg' % i in content for i in range(1, 5)),
    }
    failed = [k for k, v in checks.items() if not v]
    status = 'OK ' if not problems and not failed else 'FAIL'
    print('%s %-4s size=%6d  %s%s' % (status, lang, len(content) // 1024, lang.upper(),
          ('| issues: ' + '; '.join(problems + failed)) if (problems or failed) else ''))
    return not problems and not failed


ok = all(check(l) for l in LANGS)
print('\nALL PAGES VALID' if ok else '\nVALIDATION FAILED')
raise SystemExit(0 if ok else 1)
