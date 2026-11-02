#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build the multilingual portfolio site of Tarik Chouika (v3).

Reads the templates + 8 translation modules, renders static HTML pages:
  - index page per language (root = Arabic, /xx/ for the others)
  - 13 certificate detail pages per language  (/certs/<slug>/)
  - 6 project detail pages per language       (/projects/<key>/)
Total: 8 x (1 + 13 + 6) = 160 pages, plus assets.
"""
import html
import importlib.util
import json
import os
import re
import shutil

SRC = '/home/z/my-project/scripts/site_src'
OUT = '/home/z/my-project/site'

SITE_URL = 'https://tarikchouika.pages.dev'
EMAIL = 'tarikchouika@gmail.com'
DRIVE_URL = 'https://drive.google.com/drive/folders/1Cc_VyvUNQl2ybsRzovXu63vad77k9KBY'
NAME_LATIN = 'Tarik Chouika'

LANGS = ['ar', 'en', 'fr', 'es', 'it', 'de', 'nl', 'pt']
LANG_PATH = {'ar': '/'}
for _l in LANGS[1:]:
    LANG_PATH[_l] = '/' + _l + '/'

LANG_NATIVE = {
    'ar': 'العربية', 'en': 'English', 'fr': 'Français', 'es': 'Español',
    'it': 'Italiano', 'de': 'Deutsch', 'nl': 'Nederlands', 'pt': 'Português',
}
OG_LOCALE = {
    'ar': 'ar_MA', 'en': 'en_US', 'fr': 'fr_FR', 'es': 'es_ES',
    'it': 'it_IT', 'de': 'de_DE', 'nl': 'nl_NL', 'pt': 'pt_PT',
}
SKIP = {
    'ar': 'تخطَّ إلى المحتوى', 'en': 'Skip to content', 'fr': 'Aller au contenu',
    'es': 'Saltar al contenido', 'it': 'Salta al contenuto', 'de': 'Zum Inhalt springen',
    'nl': 'Naar inhoud springen', 'pt': 'Ir para o conteúdo',
}
COPY_SHORT = {
    'ar': 'نسخ', 'en': 'Copy', 'fr': 'Copier', 'es': 'Copiar', 'it': 'Copia',
    'de': 'Kopieren', 'nl': 'Kopiëren', 'pt': 'Copiar',
}
LOCATION = {
    'ar': 'حان، الرباط، المغرب', 'en': 'Han, Rabat, Morocco', 'fr': 'Han, Rabat, Maroc',
    'es': 'Han, Rabat, Marruecos', 'it': 'Han, Rabat, Marocco', 'de': 'Han, Rabat, Marokko',
    'nl': 'Han, Rabat, Marokko', 'pt': 'Han, Rabat, Marrocos',
}

MONTHS = {
    'ar': ['يناير', 'فبراير', 'مارس', 'أبريل', 'مايو', 'يونيو', 'يوليو', 'أغسطس', 'سبتمبر', 'أكتوبر', 'نوفمبر', 'ديسمبر'],
    'en': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
    'fr': ['janvier', 'février', 'mars', 'avril', 'mai', 'juin', 'juillet', 'août', 'septembre', 'octobre', 'novembre', 'décembre'],
    'es': ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre'],
    'it': ['gennaio', 'febbraio', 'marzo', 'aprile', 'maggio', 'giugno', 'luglio', 'agosto', 'settembre', 'ottobre', 'novembre', 'dicembre'],
    'de': ['Januar', 'Februar', 'März', 'April', 'Mai', 'Juni', 'Juli', 'August', 'September', 'Oktober', 'November', 'Dezember'],
    'nl': ['januari', 'februari', 'maart', 'april', 'mei', 'juni', 'juli', 'augustus', 'september', 'oktober', 'november', 'december'],
    'pt': ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro'],
}
DATE_FMT = {
    'ar': '{d} {m} {y}', 'en': '{M} {d}, {y}', 'fr': '{d} {m} {y}',
    'es': '{d} de {m} de {y}', 'it': '{d} {m} {y}', 'de': '{d}. {M} {y}',
    'nl': '{d} {m} {y}', 'pt': '{d} de {m} de {y}',
}

ICONS = {
    'globe': '<circle cx="12" cy="12" r="10"/><line x1="2" y1="12" x2="22" y2="12"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/>',
    'menu': '<line x1="3" y1="6" x2="21" y2="6"/><line x1="3" y1="12" x2="21" y2="12"/><line x1="3" y1="18" x2="21" y2="18"/>',
    'close': '<line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/>',
    'pin': '<path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/>',
    'mail': '<rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"/>',
    'send': '<line x1="22" y1="2" x2="11" y2="13"/><polygon points="22 2 15 22 11 13 2 9 22 2"/>',
    'download': '<path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/>',
    'copy': '<rect x="9" y="9" width="13" height="13" rx="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/>',
    'up': '<line x1="12" y1="19" x2="12" y2="5"/><polyline points="5 12 12 5 19 12"/>',
    'award': '<circle cx="12" cy="8" r="7"/><polyline points="8.21 13.89 7 23 12 20 17 23 15.79 13.88"/>',
    'folder': '<path d="M22 19a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h5l2 3h9a2 2 0 0 1 2 2z"/>',
    'ext': '<path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"/><polyline points="15 3 21 3 21 9"/><line x1="10" y1="14" x2="21" y2="3"/>',
    'book': '<path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"/><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"/>',
    'check': '<path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/>',
    'coffee': '<path d="M18 8h1a4 4 0 0 1 0 8h-1"/><path d="M2 8h16v9a4 4 0 0 1-4 4H6a4 4 0 0 1-4-4V8z"/><line x1="6" y1="1" x2="6" y2="4"/><line x1="10" y1="1" x2="10" y2="4"/><line x1="14" y1="1" x2="14" y2="4"/>',
    'shield': '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>',
    'code': '<polyline points="16 18 22 12 16 6"/><polyline points="8 6 2 12 8 18"/>',
    'sun': '<circle cx="12" cy="12" r="4"/><path d="M12 2v2"/><path d="M12 20v2"/><path d="m4.93 4.93 1.41 1.41"/><path d="m17.66 17.66 1.41 1.41"/><path d="M2 12h2"/><path d="M20 12h2"/><path d="m6.34 17.66-1.41 1.41"/><path d="m19.07 4.93-1.41 1.41"/>',
    'moon': '<path d="M12 3a6 6 0 0 0 9 9 9 9 0 1 1-9-9z"/>',
    'zoom': '<circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/><line x1="11" y1="8" x2="11" y2="14"/><line x1="8" y1="11" x2="14" y2="11"/>',
    'prev': '<polyline points="15 18 9 12 15 6"/>',
    'next': '<polyline points="9 18 15 12 9 6"/>',
    'printer': '<polyline points="6 9 6 2 18 2 18 9"/><path d="M6 18H4a2 2 0 0 1-2-2v-5a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v5a2 2 0 0 1-2 2h-2"/><rect x="6" y="14" width="12" height="8"/>',
    'back': '<line x1="19" y1="12" x2="5" y2="12"/><polyline points="12 19 5 12 12 5"/>',
    'phone': '<path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/>',
    'landmark': '<line x1="3" y1="22" x2="21" y2="22"/><line x1="6" y1="18" x2="6" y2="11"/><line x1="10" y1="18" x2="10" y2="11"/><line x1="14" y1="18" x2="14" y2="11"/><line x1="18" y1="18" x2="18" y2="11"/><polygon points="12 2 20 7 4 7"/>',
    'quote': '<path d="M3 21c3 0 7-1 7-8V5c0-1.25-.756-2.017-2-2H4c-1.25 0-2 .75-2 1.972V11c0 1.25.75 2 2 2 1 0 1 0 1 1v1c0 1-1 2-2 2s-1 .008-1 1.031V20c0 1 0 1 1 1z"/><path d="M15 21c3 0 7-1 7-8V5c0-1.25-.757-2.017-2-2h-4c-1.25 0-2 .75-2 1.972V11c0 1.25.75 2 2 2h.75c0 2.25.25 4-2.75 4v3c0 1 0 1 1 1z"/>',
}

# brand glyphs (Tabler Icons, MIT — outline style to match the site's icon system)
BRAND_ICONS = {
    'wa': '<path d="M3 21l1.65 -3.8a9 9 0 1 1 3.4 2.9l-5.05 .9"/><path d="M9 10a.5 .5 0 0 0 1 0v-1a.5 .5 0 0 0 -1 0v1a5 5 0 0 0 5 5h1a.5 .5 0 0 0 0 -1h-1a.5 .5 0 0 0 0 1"/>',
    'li': '<path d="M8 11v5"/><path d="M8 8v.01"/><path d="M12 16v-5"/><path d="M16 16v-3a2 2 0 1 0 -4 0"/><path d="M3 7a4 4 0 0 1 4 -4h10a4 4 0 0 1 4 4v10a4 4 0 0 1 -4 4h-10a4 4 0 0 1 -4 -4l0 -10"/>',
    'fb': '<path d="M7 10v4h3v7h4v-7h3l1 -4h-4v-2a1 1 0 0 1 1 -1h3v-4h-3a5 5 0 0 0 -5 5v2h-3"/>',
    'tg': '<path d="M15 10l-4 4l6 6l4 -16l-18 7l4 2l2 6l3 -4"/>',
}


def esc(s):
    return html.escape(str(s), quote=True)


def icon(name):
    return ('<svg class="ic" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
            'stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" '
            'aria-hidden="true">' + ICONS[name] + '</svg>')


def brand_icon(name):
    return ('<svg class="ic" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
            'stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" '
            'aria-hidden="true">' + BRAND_ICONS[name] + '</svg>')


_TR_CACHE = {}


def load_tr(lang):
    if lang not in _TR_CACHE:
        spec = importlib.util.spec_from_file_location('t_' + lang, os.path.join(SRC, 't_' + lang + '.py'))
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        _TR_CACHE[lang] = mod.T
    return _TR_CACHE[lang]


def load_mod(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


_cd = load_mod('certs_data', os.path.join(SRC, 'certs_data.py'))
CERTS = _cd.CERTS
FIELDS = _cd.FIELDS
CERTS_EN = _cd.CERTS_EN
SLUGS = _cd.SLUGS
PROJECTS = _cd.PROJECTS
REVIEWS = _cd.REVIEWS
OFFICIAL = _cd.OFFICIAL
TRUSTED_PLATFORMS = _cd.TRUSTED_PLATFORMS
CONTACT = _cd.CONTACT
GOV = _cd.GOV
TELEGRAM = _cd.TELEGRAM

_cs = load_mod('chatbot_strings', os.path.join(SRC, 'chatbot_strings.py'))
CHAT = _cs.CHAT
SPEECH_LANG = _cs.SPEECH_LANG

TRUSTED_NAMES = {
    'grow': 'Grow with Google', 'life': 'HP LIFE', 'huawei_talent': 'Huawei Talent',
    'coursera': 'Coursera', 'edx': 'edX', 'linkedin_learning': 'LinkedIn Learning',
}
# icon used per official-link key
LINK_ICON = {
    'credential': 'check', 'course': 'book', 'grow': 'globe', 'platform': 'globe',
    'academy': 'award', 'talent': 'award', 'maroc': 'landmark', 'spub': 'landmark',
}

# page suffix helpers
CERT_SUFFIX = ['certs/%s/' % SLUGS[c[0]] for c in CERTS]
PROJ_SUFFIX = ['projects/%s/' % p[0] for p in PROJECTS]


def fmt_date(lang, y, m, d):
    name = MONTHS[lang][m - 1]
    return DATE_FMT[lang].format(d=d, m=name, M=name, y=y)


def cert_url(lang, idx):
    return LANG_PATH[lang] + CERT_SUFFIX[idx]


def proj_url(lang, idx):
    return LANG_PATH[lang] + PROJ_SUFFIX[idx]


# ---------------- shared HTML fragments ----------------
def nav_links(t, lang, detail=False):
    n = t['nav']
    items = [('about', n['about']), ('certificates', n['certificates']),
             ('skills', n['skills']), ('projects', n['projects']),
             ('experience', n['experience']), ('gallery', n['gallery']),
             ('contact', n['contact'])]
    pre = LANG_PATH[lang] if detail else ''
    return '\n'.join('<a href="%s#%s">%s</a>' % (pre, i, esc(x)) for i, x in items)


def lang_options_html(current, suffix=''):
    out = []
    for l in LANGS:
        sel = ' selected' if l == current else ''
        out.append('<option value="%s"%s>%s</option>' % (LANG_PATH[l] + suffix, sel, LANG_NATIVE[l]))
    return '\n'.join(out)


def footer_langs_html(suffix=''):
    links = ['<a href="%s">%s</a>' % (LANG_PATH[l] + suffix, LANG_NATIVE[l]) for l in LANGS]
    return '<span class="sep">·</span>'.join(links)


def hreflangs_html(suffix=''):
    out = ['<link rel="alternate" hreflang="%s" href="%s%s">' % (l, SITE_URL, LANG_PATH[l] + suffix)
           for l in LANGS]
    out.append('<link rel="alternate" hreflang="x-default" href="%s%s">' % (SITE_URL, LANG_PATH['ar'] + suffix))
    return '\n'.join(out)


def footer_tokens(t, lang, suffix=''):
    return {
        'FOOTER_RIGHTS': esc(t['footer_rights']),
        'FOOTER_BUILT': esc(t['footer_built']),
        'FOOTER_LANGS': footer_langs_html(suffix),
        'NAME_LATIN': NAME_LATIN,
        'ICON_UP': icon('up'),
        'TOP': esc(t['top']),
    }


def head_tokens(lang, title, desc, canonical, suffix, og_image, og_type, jsonld):
    return {
        'LANG': lang,
        'DIR': 'rtl' if lang == 'ar' else 'ltr',
        'TITLE': esc(title),
        'DESC': esc(desc),
        'CANONICAL': canonical,
        'HREFLANGS': hreflangs_html(suffix),
        'OG_LOCALE': OG_LOCALE[lang],
        'OG_IMAGE': og_image,
        'SITE_URL': SITE_URL,
        'JSONLD': jsonld,
    }


def chrome_tokens(t, lang, detail=False):
    pre = LANG_PATH[lang] if detail else ''
    quick_items = [('about', t['nav']['about']), ('certificates', t['nav']['certificates']),
                   ('skills', t['nav']['skills']), ('projects', t['nav']['projects']),
                   ('experience', t['nav']['experience']), ('gallery', t['nav']['gallery']),
                   ('contact', t['nav']['contact'])]
    footer_quick = ''.join('<li><a href="%s#%s">%s</a></li>' % (pre, i, esc(x)) for i, x in quick_items)
    gov_links = '\n'.join(
        '<li><a href="%s" target="_blank" rel="noopener">%s<span class="g-dom" dir="ltr">%s</span></a></li>'
        % (url, esc(t['gov'][key]), url.replace('https://www.', '').replace('https://', ''))
        for key, url in GOV)
    return {
        'HOME_URL': LANG_PATH[lang],
        'BRAND': esc(t['brand']),
        'MENU': esc(t['menu']),
        'LANG_ARIA': esc(t['lang_aria']),
        'NAV_ARIA': esc(t['nav_aria']),
        'THEME_ARIA': esc(t['theme_aria']),
        'ICON_SUN': icon('sun'),
        'ICON_MOON': icon('moon'),
        'ICON_GLOBE': icon('globe'),
        'ICON_MENU': icon('menu'),
        'ICON_CLOSE': icon('close'),
        'ICON_PHONE': icon('phone'),
        'ICON_WA': brand_icon('wa'),
        'ICON_TG': brand_icon('tg'),
        'ICON_LI': brand_icon('li'),
        'ICON_FB': brand_icon('fb'),
        'ICON_MAIL': icon('mail'),
        'SKIP': esc(SKIP[lang]),
        'EMAIL': CONTACT['email'],
        'PHONE': CONTACT['phone'],
        'PHONE_HREF': CONTACT['phone_href'],
        'WA_HREF': CONTACT['whatsapp_href'],
        'TG_URL': CONTACT['telegram'],
        'LI_URL': CONTACT['linkedin'],
        'FB_URL': CONTACT['facebook'],
        'CT_PHONE': esc(t['ct_phone']),
        'CT_WHATSAPP': esc(t['ct_whatsapp']),
        'CT_TELEGRAM': esc(t['ct_telegram']),
        'CT_LINKEDIN': esc(t['ct_linkedin']),
        'CT_FACEBOOK': esc(t['ct_facebook']),
        'HD_BOOK': esc(t['hd_book']),
        'FT_TAGLINE': esc(t['ft_tagline']),
        'FT_QUICK': esc(t['ft_quick']),
        'FT_CONTACT': esc(t['ft_contact']),
        'FT_GOV': esc(t['ft_gov']),
        'FT_GOV_NOTE': esc(t['ft_gov_note']),
        'FOOTER_QUICK': footer_quick,
        'GOV_LINKS': gov_links,
        'AVAIL': esc(t['avail']),
    }


def apply_tokens(template, tokens, label):
    page = template
    for k, v in tokens.items():
        page = page.replace('{{' + k + '}}', v)
    leftover = re.findall(r'\{\{([A-Z_0-9]+)\}\}', page)
    if leftover:
        raise SystemExit('Unresolved tokens (%s): %s' % (label, sorted(set(leftover))))
    return page


# ---------------- index page ----------------
def stats_html(t):
    out = []
    for v, l in t['stats']:
        out.append('<div class="stat"><b class="stat-v" dir="ltr">%s</b>'
                   '<span class="stat-l">%s</span></div>' % (esc(v), esc(l)))
    return '\n'.join(out)


def facts_html(t, lang):
    items = [
        ('pin', t['fact_loc_l'], esc(LOCATION[lang])),
        ('mail', t['fact_email_l'], '<bdi>%s</bdi>' % EMAIL),
        ('check', t['fact_status_l'], esc(t['fact_status_v'])),
    ]
    out = []
    for k, label, value in items:
        out.append('<div class="fact card">%s<div><span class="fact-l">%s</span>'
                   '<span class="fact-v">%s</span></div></div>' % (icon(k), esc(label), value))
    return '\n'.join(out)


def experience_html(t):
    out = []
    for j in t['jobs']:
        lis = '\n'.join('<li>%s</li>' % esc(b) for b in j['bullets'])
        out.append(
            '<article class="tl-item card reveal">\n'
            '<span class="period" dir="ltr">%s</span>\n'
            '<h3>%s</h3>\n'
            '<p class="org">%s</p>\n'
            '<ul class="bullets">%s</ul>\n'
            '</article>' % (esc(j['period']), esc(j['title']), esc(j['org']), lis))
    return '\n'.join(out)


def certs_html(t, lang):
    out = []
    for i, (c, tr) in enumerate(zip(CERTS, t['certs'])):
        img, field, issuer_key, y, m, d, cred, drive_id = c
        title = tr['title']
        desc = tr.get('desc', '')
        field_label = t['fields'][field]
        issuer = t['issuers'][issuer_key]
        date_s = fmt_date(lang, y, m, d)
        cred_row = ''
        if cred:
            cred_row = ('<div><dt>' + esc(t['l_cred']) + '</dt><dd dir="ltr">'
                        + esc(cred) + '</dd></div>')
        out.append(
            '<article class="cert-card card reveal" data-field="' + field + '">\n'
            '<button type="button" class="cert-media" data-full="/certs/' + img + '.jpg" '
            'data-title="' + esc(title) + '" data-issuer="' + esc(issuer) + '" '
            'data-date="' + esc(date_s) + '" data-cred="' + esc(cred) + '" '
            'data-drive="' + esc(drive_id) + '" data-field-label="' + esc(field_label) + '" '
            'aria-label="' + esc(t['l_view']) + ': ' + esc(title) + '">\n'
            '<img src="/certs/th/' + img + '.jpg" alt="' + esc(title) + '" '
            'loading="lazy" width="660" height="440">\n'
            '<span class="cert-zoom">' + icon('zoom') + '<span>' + esc(t['l_view']) + '</span></span>\n'
            '</button>\n'
            '<div class="cert-body">\n'
            '<span class="cert-field">' + esc(field_label) + '</span>\n'
            '<h3>' + esc(title) + '</h3>\n'
            '<p class="cert-desc">' + esc(desc) + '</p>\n'
            '<dl class="cert-meta">\n'
            '<div><dt>' + esc(t['l_issuer']) + '</dt><dd>' + esc(issuer) + '</dd></div>\n'
            '<div><dt>' + esc(t['l_date']) + '</dt><dd>' + esc(date_s) + '</dd></div>\n'
            + cred_row + '\n'
            '</dl>\n'
            '<a class="cert-more" href="' + cert_url(lang, i) + '"><span>' + esc(t['l_details'])
            + '</span>' + icon('next') + '</a>\n'
            '</div>\n'
            '</article>')
    return '\n'.join(out)


def filter_bar_html(t):
    counts = {'all': len(CERTS)}
    for c in CERTS:
        counts[c[1]] = counts.get(c[1], 0) + 1
    out = []
    for f in FIELDS:
        if f != 'all' and counts.get(f, 0) == 0:
            continue
        active = ' active' if f == 'all' else ''
        out.append('<button class="f-chip' + active + '" type="button" data-filter="' + f + '">'
                   + esc(t['fields'][f]) + '<span class="n" dir="ltr">'
                   + str(counts.get(f, 0)) + '</span></button>')
    return '\n'.join(out)


def projects_html(t, lang):
    out = []
    for i, ((key, img, url), tr) in enumerate(zip(PROJECTS, t['projects'])):
        domain = url.replace('https://', '')
        out.append(
            '<article class="proj-card card reveal">\n'
            '<a class="proj-media" href="' + url + '" target="_blank" rel="noopener" '
            'aria-label="' + esc(t['pj_visit']) + ': ' + esc(tr['name']) + '">\n'
            '<img src="' + img + '" alt="' + esc(tr['name']) + '" loading="lazy" width="1000" height="625">\n'
            '<span class="proj-open">' + icon('ext') + '<span>' + esc(t['pj_visit']) + '</span></span>\n'
            '</a>\n'
            '<div class="proj-body">\n'
            '<div class="proj-head-row"><h3>' + esc(tr['name']) + '</h3>'
            '<span class="proj-tag">' + esc(tr['tag']) + '</span></div>\n'
            '<p class="proj-desc">' + esc(tr['desc']) + '</p>\n'
            '<a class="proj-url" href="' + url + '" target="_blank" rel="noopener">'
            + icon('ext') + domain + '</a>\n'
            '<a class="proj-more" href="' + proj_url(lang, i) + '"><span>' + esc(t['l_pj_details'])
            + '</span>' + icon('next') + '</a>\n'
            '</div>\n'
            '</article>')
    return '\n'.join(out)


def skills_html(t):
    out = []
    for cat in t['cats']:
        chips = '\n'.join('<li class="chip">%s</li>' % esc(i) for i in cat['items'])
        out.append('<article class="skill-card card reveal">\n'
                   '<div class="skill-icon">%s</div>\n'
                   '<h3>%s</h3>\n'
                   '<ul class="chips">%s</ul>\n'
                   '</article>' % (icon(cat['icon']), esc(cat['title']), chips))
    return '\n'.join(out)


def gallery_html(t):
    out = []
    for i, caption in enumerate(t['gal'], 1):
        out.append('<figure class="g-item reveal">\n'
                   '<img src="/img/g%d.jpg" alt="%s" loading="lazy" width="1100" height="825">\n'
                   '<figcaption>%s</figcaption>\n'
                   '</figure>' % (i, esc(caption), esc(caption)))
    return '\n'.join(out)


# ---------------- v4: contact channels ----------------
def channels_html(t):
    defs = [
        ('phone', CONTACT['phone_href'], False, icon('phone'), t['ct_phone'], CONTACT['phone']),
        ('wa', CONTACT['whatsapp_href'], True, brand_icon('wa'), t['ct_whatsapp'], CONTACT['phone']),
        ('mail', 'mailto:' + CONTACT['email'], False, icon('mail'), t['fact_email_l'], CONTACT['email']),
        ('li', CONTACT['linkedin'], True, brand_icon('li'), t['ct_linkedin'], 'Tarik Chouika'),
        ('fb', CONTACT['facebook'], True, brand_icon('fb'), t['ct_facebook'], 'Tarik Chouika'),
        ('tg', CONTACT['telegram'], True, brand_icon('tg'), t['ct_telegram'], '@tarikchouika_bot'),
    ]
    out = []
    for key, href, ext, ic, label, value in defs:
        tgt = ' target="_blank" rel="noopener"' if ext else ''
        out.append(
            '<a class="channel card" href="%s"%s>\n'
            '<span class="ch-icon">%s</span>\n'
            '<span class="ch-body"><span class="ch-l">%s</span><span class="ch-v" dir="ltr">%s</span></span>\n'
            '<span class="ch-go">%s</span>\n'
            '</a>' % (href, tgt, ic, esc(label), esc(value), icon('next')))
    return '\n'.join(out)


# ---------------- v4: certificate reviews + official links ----------------
def reviews_sec_html(t, idx):
    cid = CERTS[idx][0]
    revs = REVIEWS.get(cid) or []
    if not revs:
        return ''
    cards = []
    for author, src_key, url, qlang, quote in revs:
        cards.append(
            '<figure class="review-card card reveal">\n'
            '<blockquote lang="%s" dir="ltr">%s</blockquote>\n'
            '<figcaption>\n'
            '<span class="rv-author">%s</span>\n'
            '<span class="rv-src">%s</span>\n'
            '<a class="rv-link" href="%s" target="_blank" rel="noopener">%s%s</a>\n'
            '</figcaption>\n'
            '</figure>' % (qlang, quote, esc(author), esc(t['sources'][src_key]), url,
                           esc(t['cp_view_source']), icon('ext')))
    return ('<section class="dsec" id="cp-reviews">\n'
            '<h2>%s%s</h2>\n'
            '<p class="dsec-note">%s</p>\n'
            '<div class="reviews-grid">\n%s\n</div>\n'
            '</section>' % (icon('quote'), esc(t['cp_reviews']), esc(t['cp_reviews_note']), '\n'.join(cards)))


def links_sec_html(t, idx):
    issuer_key = CERTS[idx][2]
    links = OFFICIAL.get(issuer_key) or []
    cards = []
    for key, url in links:
        cards.append(
            '<a class="offlink card" href="%s" target="_blank" rel="noopener">\n'
            '<span class="ol-icon">%s</span>\n'
            '<span class="ol-l">%s</span>\n'
            '%s\n'
            '</a>' % (url, icon(LINK_ICON[key]), esc(t['links'][key]), icon('ext')))
    trusted = '\n'.join(
        '<li class="chip"><a href="%s" target="_blank" rel="noopener">%s</a></li>' % (url, TRUSTED_NAMES[key])
        for key, url in TRUSTED_PLATFORMS)
    return ('<section class="dsec" id="cp-links">\n'
            '<h2>%s</h2>\n'
            '<div class="offlinks">\n%s\n</div>\n'
            '<p class="chips-label">%s</p>\n'
            '<ul class="chips reveal">\n%s\n</ul>\n'
            '</section>' % (esc(t['cp_links']), '\n'.join(cards), esc(t['links']['trusted']), trusted))


def jsonld_person():
    creds = [
        {'@type': 'EducationalOccupationalCredential', 'name': CERTS_EN[c[0]],
         'url': 'https://drive.google.com/file/d/' + c[7] + '/view',
         **({'credentialID': c[6]} if c[6] else {})}
        for c in CERTS
    ]
    data = {
        '@context': 'https://schema.org',
        '@type': 'Person',
        'name': 'Tarik Chouika',
        'alternateName': 'طارق شويكة',
        'url': SITE_URL + '/',
        'image': SITE_URL + '/img/profile.jpg',
        'email': 'mailto:' + EMAIL,
        'jobTitle': 'Certified Digital Skills Professional | Operations & Customer Service',
        'address': {'@type': 'PostalAddress', 'addressLocality': 'Han, Rabat', 'addressCountry': 'MA'},
        'knowsLanguage': ['ar', 'en'],
        'hasCredential': creds,
    }
    return json.dumps(data, ensure_ascii=False)


def render_index(lang, template):
    t = load_tr(lang)
    tokens = {}
    tokens.update(head_tokens(lang, t['title'], t['desc'], SITE_URL + LANG_PATH[lang],
                              '', SITE_URL + '/img/profile.jpg', 'profile', jsonld_person()))
    tokens.update(chrome_tokens(t, lang))
    tokens.update({
        'NAV_LINKS': nav_links(t, lang),
        'NAV_LINKS_MOBILE': nav_links(t, lang),
        'LANG_OPTIONS': lang_options_html(lang),
        'GREETING': esc(t['greeting']),
        'NAME': esc(t['name']),
        'NAME_ALT': esc(t['name_alt']),
        'ROLES': esc(json.dumps(t['roles'], ensure_ascii=False)),
        'ROLES_TEXT': esc(' · '.join(t['roles'])),
        'ALT_PROFILE': esc(t['alt_profile']),
        'EMAIL': EMAIL,
        'LOCATION': esc(LOCATION[lang]),
        'ICON_PIN': icon('pin'),
        'ICON_MAIL': icon('mail'),
        'ICON_SEND': icon('send'),
        'ICON_DOWNLOAD': icon('download'),
        'ICON_COPY': icon('copy'),
        'CTA_CONTACT': esc(t['cta_contact']),
        'CTA_CV': esc(t['cta_cv']),
        'STATS': stats_html(t),
        'ABOUT_TITLE': esc(t['about_title']),
        'ABOUT_SUB': esc(t['about_sub']),
        'ABOUT_P1': esc(t['about_p1']),
        'ABOUT_P2': esc(t['about_p2']),
        'ABOUT_P3': esc(t['about_p3']),
        'ABOUT_P4': esc(t['about_p4']),
        'FACTS': facts_html(t, lang),
        'EXP_TITLE': esc(t['exp_title']),
        'EXP_SUB': esc(t['exp_sub']),
        'EXPERIENCE': experience_html(t),
        'CERT_TITLE': esc(t['cert_title']),
        'CERT_SUB': esc(t['cert_sub']),
        'FILT_ARIA': esc(t['filt_aria']),
        'FILTER_BAR': filter_bar_html(t),
        'CERTS': certs_html(t, lang),
        'DRIVE_URL': DRIVE_URL,
        'DRIVE_TITLE': esc(t['drive_title']),
        'DRIVE_TEXT': esc(t['drive_text']),
        'DRIVE_CTA': esc(t['drive_cta']),
        'ICON_FOLDER': icon('folder'),
        'ICON_EXT': icon('ext'),
        'SK_TITLE': esc(t['sk_title']),
        'SK_SUB': esc(t['sk_sub']),
        'SKILLS': skills_html(t),
        'PJ_TITLE': esc(t['pj_title']),
        'PJ_SUB': esc(t['pj_sub']),
        'PJ_NOTE': esc(t['pj_note']),
        'PJ_VISIT': esc(t['pj_visit']),
        'PROJECTS': projects_html(t, lang),
        'ICON_BOOK': icon('book'),
        'EDU_TITLE': esc(t['edu_title']),
        'EDU_SUB': esc(t['edu_sub']),
        'EDU_LEVEL': esc(t['edu_level']),
        'EDU_NOTE': esc(t['edu_note']),
        'GAL_TITLE': esc(t['gal_title']),
        'GAL_SUB': esc(t['gal_sub']),
        'GALLERY': gallery_html(t),
        'CT_TITLE': esc(t['ct_title']),
        'CT_SUB': esc(t['ct_sub']),
        'AVAIL': esc(t['avail']),
        'EMAIL_CTA': esc(t['email_cta']),
        'COPY': esc(t['copy']),
        'COPIED': esc(t['copied']),
        'COPY_SHORT': esc(COPY_SHORT[lang]),
        'CT_NOTE': esc(t['ct_note']),
        'CHANNELS': channels_html(t),
        'LB_CLOSE': esc(t['lb_close']),
        'LB_PREV': esc(t['lb_prev']),
        'LB_NEXT': esc(t['lb_next']),
        'LB_DRIVE': esc(t['lb_drive']),
        'L_ISSUER': esc(t['l_issuer']),
        'L_DATE': esc(t['l_date']),
        'L_CRED': esc(t['l_cred']),
        'ICON_PREV': icon('prev'),
        'ICON_NEXT': icon('next'),
    })
    tokens.update(footer_tokens(t, lang))
    return apply_tokens(template, tokens, 'index-' + lang)


# ---------------- certificate detail page ----------------
def jsonld_cert(idx, t, lang, cp):
    c = CERTS[idx]
    data = {
        '@context': 'https://schema.org',
        '@type': 'EducationalOccupationalCredential',
        'name': cp.get('name_en', CERTS_EN[c[0]]),
        'alternateName': t['certs'][idx]['title'],
        'description': cp['overview'],
        'url': SITE_URL + LANG_PATH[lang] + CERT_SUFFIX[idx],
        'competencyRequired': cp['skills'],
        'recognizedBy': {'@type': 'Organization', 'name': t['issuers'][c[2]]},
        'sameAs': 'https://drive.google.com/file/d/' + c[7] + '/view',
    }
    if c[6]:
        data['identifier'] = c[6]
    return json.dumps(data, ensure_ascii=False)


def related_certs_html(t, lang, idx):
    field = CERTS[idx][1]
    related = [i for i, c in enumerate(CERTS) if c[1] == field and i != idx]
    if not related:
        return ''
    cards = []
    for i in related[:3]:
        c = CERTS[i]
        cards.append(
            '<a class="rel-card" href="%s">\n'
            '<img src="/certs/th/%s.jpg" alt="%s" loading="lazy" width="660" height="440">\n'
            '<div class="rel-body"><p class="rel-t">%s</p></div>\n'
            '</a>' % (cert_url(lang, i), c[0], esc(t['certs'][i]['title']), esc(t['certs'][i]['title'])))
    return ('<section class="dsec" id="cp-related">\n'
            '<h2>' + esc(t['cp_related']) + '</h2>\n'
            '<div class="related-grid">\n' + '\n'.join(cards) + '\n</div>\n'
            '</section>')


def render_cert_page(lang, idx, template):
    t = load_tr(lang)
    c = CERTS[idx]
    cp = t['cert_pages'][idx]
    trc = t['certs'][idx]
    suffix = CERT_SUFFIX[idx]
    canonical = SITE_URL + LANG_PATH[lang] + suffix
    field_label = t['fields'][c[1]]
    issuer = t['issuers'][c[2]]
    date_s = fmt_date(lang, c[3], c[4], c[5])
    title = trc['title'] + ' | ' + t['brand']
    desc = cp['overview']
    cred_row = ''
    if c[6]:
        cred_row = ('<div><dt>' + esc(t['l_cred']) + '</dt><dd dir="ltr">' + esc(c[6]) + '</dd></div>')
    skills_list = '\n'.join('<li>' + icon('check') + '<span>' + esc(s) + '</span></li>' for s in cp['skills'])
    roles_chips = '\n'.join('<li class="chip">%s</li>' % esc(r) for r in cp['roles'])
    prev_i = (idx - 1) % len(CERTS)
    next_i = (idx + 1) % len(CERTS)
    tokens = {}
    tokens.update(head_tokens(lang, title, desc, canonical, suffix,
                              SITE_URL + '/certs/%s.jpg' % c[0], 'article', jsonld_cert(idx, t, lang, cp)))
    tokens.update(chrome_tokens(t, lang, detail=True))
    tokens.update({
        'NAV_LINKS': nav_links(t, lang, detail=True),
        'NAV_LINKS_MOBILE': nav_links(t, lang, detail=True),
        'LANG_OPTIONS': lang_options_html(lang, suffix),
        'REVIEWS_SEC': reviews_sec_html(t, idx),
        'LINKS_SEC': links_sec_html(t, idx),
        'CP_HOME': esc(t['cp_home']),
        'CP_CERTS': esc(t['cp_certs']),
        'CERTS_URL': LANG_PATH[lang] + '#certificates',
        'CERT_TITLE': esc(trc['title']),
        'FIELD_LABEL': esc(field_label),
        'LEAD': esc(issuer + ' — ' + date_s),
        'CERT_IMG': '/certs/%s.jpg' % c[0],
        'CERT_IMG_FULL': SITE_URL + '/certs/%s.jpg' % c[0],
        'CP_VIEW_IMG': esc(t['cp_view_img']),
        'ICON_ZOOM': icon('zoom'),
        'ALT_CERT': esc(trc['title']),
        'CP_ABOUT': esc(t['cp_about']),
        'OVERVIEW': esc(cp['overview']),
        'CP_SKILLS': esc(t['cp_skills']),
        'SKILLS_LIST': skills_list,
        'CP_PROSPECTS': esc(t['cp_prospects']),
        'PROSPECTS': esc(cp['prospects']),
        'CP_ROLES': esc(t['cp_roles']),
        'ROLES_CHIPS': roles_chips,
        'RELATED_SEC': related_certs_html(t, lang, idx),
        'CP_META': esc(t['cp_meta']),
        'ICON_AWARD': icon('award'),
        'L_ISSUER': esc(t['l_issuer']),
        'L_DATE': esc(t['l_date']),
        'L_CRED': esc(t['l_cred']),
        'L_FIELD': esc(t['cp_certs']),
        'ISSUER': esc(issuer),
        'DATE_S': esc(date_s),
        'CRED_ROW': cred_row,
        'CP_VERIFY': esc(t['cp_verify']),
        'CP_PRINT': esc(t['cp_print']),
        'DRIVE_URL': 'https://drive.google.com/file/d/%s/view' % c[7],
        'ICON_EXT': icon('ext'),
        'ICON_PRINTER': icon('printer'),
        'ICON_BACK': icon('back'),
        'CP_BACK': esc(t['cp_back']),
        'CP_PREV': esc(t['cp_prev']),
        'CP_NEXT': esc(t['cp_next']),
        'ICON_PREV': icon('prev'),
        'ICON_NEXT': icon('next'),
        'PREV_URL': cert_url(lang, prev_i),
        'NEXT_URL': cert_url(lang, next_i),
        'PREV_TITLE': esc(t['certs'][prev_i]['title']),
        'NEXT_TITLE': esc(t['certs'][next_i]['title']),
    })
    tokens.update(footer_tokens(t, lang, suffix))
    tokens['NAME'] = esc(t['name'])
    return apply_tokens(template, tokens, 'cert-%s-%s' % (lang, c[0]))


# ---------------- project detail page ----------------
def jsonld_project(idx, t, lang, pp):
    key, img, url = PROJECTS[idx]
    tr = t['projects'][idx]
    data = {
        '@context': 'https://schema.org',
        '@type': 'CreativeWork',
        'name': tr['name'],
        'description': pp['about'],
        'url': SITE_URL + LANG_PATH[lang] + PROJ_SUFFIX[idx],
        'image': SITE_URL + img,
        'inLanguage': lang,
        'author': {'@type': 'Person', 'name': 'Tarik Chouika', 'url': SITE_URL + '/'},
        'about': tr['tag'],
    }
    return json.dumps(data, ensure_ascii=False)


def render_project_page(lang, idx, template):
    t = load_tr(lang)
    pp = t['project_pages'][idx]
    key, img, url = PROJECTS[idx]
    tr = t['projects'][idx]
    suffix = PROJ_SUFFIX[idx]
    canonical = SITE_URL + LANG_PATH[lang] + suffix
    domain = url.replace('https://', '')
    title = tr['name'] + ' | ' + t['brand']
    desc = tr['desc']
    tech_chips = '\n'.join('<li class="chip">%s</li>' % esc(x) for x in pp['tech'])
    feature_list = '\n'.join('<li>' + icon('check') + '<span>' + esc(f) + '</span></li>' for f in pp['features'])
    prev_i = (idx - 1) % len(PROJECTS)
    next_i = (idx + 1) % len(PROJECTS)
    pv = t['project_v4'][idx]
    value_cards = '\n'.join(
        '<article class="value-card card reveal">\n<h3>%s</h3>\n<p>%s</p>\n</article>'
        % (esc(vt), esc(vd)) for vt, vd in pv['values'])
    effort_stats = '\n'.join(
        '<div><dt>%s</dt><dd>%s</dd></div>' % (esc(l), esc(v)) for l, v in pv['effort_stats'])
    ops_chips = '\n'.join('<li class="chip">%s</li>' % esc(x) for x in pv['ops'])
    tool_cards = '\n'.join(
        '<article class="tool-card reveal">\n<h3>%s</h3>\n<p>%s</p>\n</article>'
        % (esc(tn), esc(td)) for tn, td in t['project_tools'][idx])
    tokens = {}
    tokens.update(head_tokens(lang, title, desc, canonical, suffix,
                              SITE_URL + img, 'article', jsonld_project(idx, t, lang, pp)))
    tokens.update(chrome_tokens(t, lang, detail=True))
    tokens.update({
        'NAV_LINKS': nav_links(t, lang, detail=True),
        'NAV_LINKS_MOBILE': nav_links(t, lang, detail=True),
        'LANG_OPTIONS': lang_options_html(lang, suffix),
        'PP_HOME': esc(t['pp_home']),
        'PP_PROJECTS': esc(t['pp_projects']),
        'PROJECTS_URL': LANG_PATH[lang] + '#projects',
        'PJ_NAME': esc(tr['name']),
        'PJ_TAG': esc(tr['tag']),
        'PJ_DESC': esc(tr['desc']),
        'PJ_URL': url,
        'PJ_IMG': img,
        'PJ_DOMAIN': esc(domain),
        'PP_VISIT': esc(t['pp_visit']),
        'ICON_EXT': icon('ext'),
        'PP_ABOUT': esc(t['pp_about']),
        'P_ABOUT': esc(pp['about']),
        'PP_VALUE': esc(t['pp_value']),
        'VALUE_INTRO': esc(pv['value_intro']),
        'VALUE_CARDS': value_cards,
        'PP_EFFORT': esc(t['pp_effort']),
        'P_EFFORT': esc(pv['effort']),
        'EFFORT_STATS': effort_stats,
        'PP_TECH_BUILD': esc(t['pp_tech_build']),
        'PP_TECH_OPS': esc(t['pp_tech_ops']),
        'OPS_CHIPS': ops_chips,
        'PP_COSTS': esc(t['pp_costs']),
        'COST_BUILD': esc(t['cost_build']),
        'COST_OPS': esc(t['cost_ops']),
        'COST_SELF': esc(t['cost_self']),
        'COST_MARKET': esc(t['cost_market']),
        'COST_NOW': esc(t['cost_now']),
        'COST_SCALE': esc(t['cost_scale']),
        'COST_SELF_V': esc(pv['cost_self']),
        'COST_MARKET_V': esc(pv['cost_market']),
        'COST_NOW_V': esc(pv['cost_now']),
        'COST_SCALE_V': esc(pv['cost_scale']),
        'COST_NOTE': esc(t['cost_note']),
        'PP_TECH': esc(t['pp_tech']),
        'TECH_CHIPS': tech_chips,
        'PP_TOOLS': esc(t['pp_tools']),
        'PP_TOOLS_NOTE': esc(t['pp_tools_note']),
        'TOOL_CARDS': tool_cards,
        'PP_FEATURES': esc(t['pp_features']),
        'FEATURE_LIST': feature_list,
        'PP_LEARNED': esc(t['pp_learned']),
        'P_LEARNED': esc(pp['learned']),
        'CP_META': esc(t['cp_meta']),
        'ICON_CODE': icon('code'),
        'PP_STATUS': esc(t['pp_status']),
        'PP_LIVE': esc(t['pp_live']),
        'PP_DOMAIN': esc(t['pp_domain']),
        'PP_HOST': esc(t['pp_host']),
        'PP_BUILT_LABEL': esc(t['pp_built_label']),
        'PP_BUILT': esc(t['pp_built']),
        'CP_PRINT': esc(t['cp_print']),
        'ICON_PRINTER': icon('printer'),
        'ICON_BACK': icon('back'),
        'PP_BACK': esc(t['pp_back']),
        'PP_PREV': esc(t['pp_prev']),
        'PP_NEXT': esc(t['pp_next']),
        'ICON_PREV': icon('prev'),
        'ICON_NEXT': icon('next'),
        'PREV_URL': proj_url(lang, prev_i),
        'NEXT_URL': proj_url(lang, next_i),
        'PREV_TITLE': esc(t['projects'][prev_i]['name']),
        'NEXT_TITLE': esc(t['projects'][next_i]['name']),
    })
    tokens.update(footer_tokens(t, lang, suffix))
    tokens['NAME'] = esc(t['name'])
    return apply_tokens(template, tokens, 'proj-%s-%s' % (lang, key))


# ---------------- static assets ----------------

FAVICON = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">
<rect width="64" height="64" rx="14" fill="#0b0d10"/>
<rect x="1.5" y="1.5" width="61" height="61" rx="12.5" fill="none" stroke="#d9a648" stroke-width="3"/>
<text x="32" y="44" font-family="Georgia, 'Times New Roman', serif" font-size="36" font-weight="700" fill="#d9a648" text-anchor="middle">T</text>
</svg>
'''

ROBOTS = 'User-agent: *\nAllow: /\nSitemap: %s/sitemap.xml\n' % SITE_URL


def sitemap_xml():
    lines = ['<?xml version="1.0" encoding="UTF-8"?>',
             '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
             'xmlns:xhtml="http://www.w3.org/1999/xhtml">']

    def emit(suffix, priority):
        lines.append('  <url>')
        lines.append('    <loc>%s%s</loc>' % (SITE_URL, LANG_PATH['ar'] + suffix))
        for l in LANGS:
            lines.append('    <xhtml:link rel="alternate" hreflang="%s" href="%s%s"/>'
                         % (l, SITE_URL, LANG_PATH[l] + suffix))
        lines.append('    <xhtml:link rel="alternate" hreflang="x-default" href="%s%s"/>'
                     % (SITE_URL, LANG_PATH['ar'] + suffix))
        lines.append('    <changefreq>monthly</changefreq>')
        lines.append('    <priority>%s</priority>' % priority)
        lines.append('  </url>')

    emit('', '1.0')
    for s in CERT_SUFFIX:
        emit(s, '0.7')
    for s in PROJ_SUFFIX:
        emit(s, '0.6')
    lines.append('</urlset>')
    return '\n'.join(lines)


NOT_FOUND = '''<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>404 — طارق شويكة | Tarik Chouika</title>
<meta name="robots" content="noindex">
<link rel="icon" type="image/svg+xml" href="/favicon.svg">
<style>
body{margin:0;min-height:100vh;display:grid;place-items:center;background:#0b0d10;color:#ece9e2;
font-family:system-ui,-apple-system,"Segoe UI","Cairo",sans-serif;text-align:center;padding:2rem}
.box{max-width:520px}
.code{font-size:5rem;font-weight:800;color:#d9a648;margin:0;line-height:1}
h1{font-size:1.4rem;margin:1rem 0 .4rem}
p{color:#a3a9b4;margin:0 0 1.8rem}
a{display:inline-block;background:linear-gradient(135deg,#e8c06a,#b9872f);color:#1a1408;
font-weight:700;padding:.85rem 2rem;border-radius:999px;text-decoration:none}
</style>
</head>
<body>
<div class="box">
<p class="code">404</p>
<h1>الصفحة غير موجودة — Page not found</h1>
<p>عذراً، الصفحة التي تبحث عنها غير متوفرة · Sorry, the page you are looking for does not exist.</p>
<a href="/">العودة إلى الرئيسية — Back to home</a>
</div>
</body>
</html>
'''

HEADERS = '''/*
  X-Content-Type-Options: nosniff
  Referrer-Policy: strict-origin-when-cross-origin
/img/*
  Cache-Control: public, max-age=86400
/certs/*
  Cache-Control: public, max-age=86400
/css/*
  Cache-Control: public, max-age=3600, must-revalidate
/js/*
  Cache-Control: public, max-age=3600, must-revalidate
'''


# v6: the natsup project moved from /projects/natsuptc/ to /projects/natsup/ —
# keep old indexed/shared links working (301, per language).
def redirects_file():
    lines = []
    for lang in LANGS:
        base = LANG_PATH[lang]
        lines.append('%sprojects/natsuptc/* %sprojects/natsup/:splat 301' % (base, base))
    return '\n'.join(lines) + '\n'


# ---------------- validation ----------------
VOID_TAGS = {'meta', 'link', 'img', 'br', 'hr', 'input', 'source', 'wbr'}


def check_tags(page, label):
    stripped = re.sub(r'<script.*?</script>', '', page, flags=re.S)
    stripped = re.sub(r'<style.*?</style>', '', stripped, flags=re.S)
    stack = []
    for m in re.finditer(r'<(/?)([a-zA-Z][a-zA-Z0-9-]*)((?:"[^"]*"|\'[^\']*\'|[^>"\'])*)>', stripped):
        closing, tag, attrs = m.group(1), m.group(2).lower(), m.group(3)
        selfclose = attrs.rstrip().endswith('/')
        if tag in VOID_TAGS or selfclose:
            continue
        if not closing:
            stack.append(tag)
        else:
            if not stack or stack[-1] != tag:
                raise SystemExit('TAG MISMATCH (%s): </%s> vs %s' % (label, tag, stack[-3:]))
            stack.pop()
    if stack:
        raise SystemExit('UNCLOSED TAGS (%s): %s' % (label, stack))


def check_assets(page, label):
    refs = re.findall(r'(?:src|href)="(/[^"#]+)"', page)
    for r in refs:
        if r.startswith('//'):
            continue
        path = r.split('?')[0]
        if not os.path.exists(os.path.join(OUT, path.lstrip('/'))):
            raise SystemExit('MISSING ASSET (%s): %s' % (label, r))


# ---------------- main ----------------
def write_page(rel_path, content, counter):
    dst = os.path.join(OUT, rel_path)
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    with open(dst, 'w', encoding='utf-8') as f:
        f.write(content)
    counter.append(dst)


def main():
    os.makedirs(OUT, exist_ok=True)
    with open(os.path.join(SRC, 'template.html'), encoding='utf-8') as f:
        index_tpl = f.read()
    with open(os.path.join(SRC, 'cert_page.html'), encoding='utf-8') as f:
        cert_tpl = f.read()
    with open(os.path.join(SRC, 'project_page.html'), encoding='utf-8') as f:
        proj_tpl = f.read()

    pages = []
    for lang in LANGS:
        write_page('index.html' if lang == 'ar' else lang + '/index.html',
                   render_index(lang, index_tpl), pages)
        for i in range(len(CERTS)):
            write_page(LANG_PATH[lang].lstrip('/') + CERT_SUFFIX[i] + 'index.html',
                       render_cert_page(lang, i, cert_tpl), pages)
        for i in range(len(PROJECTS)):
            write_page(LANG_PATH[lang].lstrip('/') + PROJ_SUFFIX[i] + 'index.html',
                       render_project_page(lang, i, proj_tpl), pages)
    print('rendered %d pages' % len(pages))

    # assets
    os.makedirs(os.path.join(OUT, 'css'), exist_ok=True)
    os.makedirs(os.path.join(OUT, 'js'), exist_ok=True)
    shutil.copy(os.path.join(SRC, 'style.css'), os.path.join(OUT, 'css', 'style.css'))
    shutil.copy(os.path.join(SRC, 'main.js'), os.path.join(OUT, 'js', 'main.js'))
    shutil.copy(os.path.join(SRC, 'chatbot.js'), os.path.join(OUT, 'js', 'chatbot.js'))
    chatbot_i18n = (
        '/* generated by build_site.py from chatbot_strings.py */\n'
        'window.TC_CHAT = %s;\n'
        'window.TC_CHAT_SPEECH = %s;\n'
        'window.TC_CHAT_TG = %s;\n'
        % (json.dumps(CHAT, ensure_ascii=False),
           json.dumps(SPEECH_LANG, ensure_ascii=False),
           json.dumps({'bot_url': TELEGRAM['bot_url'], 'worker': TELEGRAM['worker']},
                      ensure_ascii=False)))
    with open(os.path.join(OUT, 'js', 'chatbot-i18n.js'), 'w', encoding='utf-8') as f:
        f.write(chatbot_i18n)
    for name, content in [('favicon.svg', FAVICON), ('robots.txt', ROBOTS),
                           ('sitemap.xml', sitemap_xml()), ('404.html', NOT_FOUND),
                           ('_headers', HEADERS), ('_redirects', redirects_file())]:
        with open(os.path.join(OUT, name), 'w', encoding='utf-8') as f:
            f.write(content)
    print('assets written: css, js (main + chatbot + chatbot-i18n), favicon, robots, sitemap, 404, _headers')

    # validate every generated page
    for p in pages:
        rel = os.path.relpath(p, OUT)
        with open(p, encoding='utf-8') as f:
            content = f.read()
        check_tags(content, rel)
        check_assets(content, rel)
    print('validation OK: tag balance + assets on %d pages' % len(pages))
    print('BUILD OK')


if __name__ == '__main__':
    main()
