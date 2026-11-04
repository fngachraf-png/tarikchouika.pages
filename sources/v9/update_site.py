#!/usr/bin/env python3
"""Update site for CMDP integration:
1. Pager: epdp.next -> cmdp ; natsup.prev -> cmdp  (8 langs)
2. Homepage: insert CMDP card after EPDP card (8 langs)
3. Project counts: seven/eight -> nine (meta, og, hero stat, about, subtitle, services) (8 langs)
4. Sitemap: add cmdp url block
"""
import re, os

SITE = '/home/z/my-project/site'
LANGS = ['ar', 'en', 'fr', 'es', 'it', 'de', 'nl', 'pt']
EPDP_NAME = {
 'ar': 'EPDP — كاتبك الرقمي', 'en': 'EPDP — Your Digital Scribe',
 'fr': 'EPDP — Votre scribe numérique', 'es': 'EPDP — Tu escriba digital',
 'it': 'EPDP — Il tuo scrivano digitale', 'de': 'EPDP — Dein digitaler Schreiber',
 'nl': 'EPDP — Jouw digitale griffier', 'pt': 'EPDP — O teu escriba digital',
}
CMDP_NAME = {
 'ar': 'CMDP — منصة إدارة التعاونيات', 'en': 'CMDP — Cooperative Management Platform',
 'fr': 'CMDP — Plateforme de gestion des coopératives', 'es': 'CMDP — Plataforma de gestión de cooperativas',
 'it': 'CMDP — Piattaforma di gestione delle cooperative', 'de': 'CMDP — Plattform für Genossenschaftsverwaltung',
 'nl': 'CMDP — Platform voor coöperatiebeheer', 'pt': 'CMDP — Plataforma de gestão de cooperativas',
}
TAG = {'ar': 'رقمنة التعاونيات المغربية', 'en': 'Digitizing Moroccan cooperatives',
 'fr': 'Numériser les coopératives marocaines', 'es': 'Digitalizar las cooperativas marroquíes',
 'it': 'Digitalizzare le cooperative marocchine', 'de': 'Marokkanische Genossenschaften digitalisieren',
 'nl': 'Marokkaanse coöperaties digitaliseren', 'pt': 'Digitalizar as cooperativas marroquinas'}
DESC = {'ar': 'منصة شاملة لإدارة التعاونيات وفق القانون 112.12: لوحة قيادة، الأعضاء والحصص، الجمع العام، المالية، وسجل الوثائق — مع تتبّع الجهات الوصية (ODCO والضرائب وCNSS) بتصميم مغربي عصري.',
 'en': 'A comprehensive platform for managing cooperatives under Law 112.12: dashboard, members & shares, general assembly, finances and a document registry — with supervisory-authority tracking (ODCO, taxes, CNSS) in a modern Moroccan design.',
 'fr': 'Une plateforme complète de gestion des coopératives conformément à la loi 112.12 : tableau de bord, membres et parts, assemblée générale, finances et registre des documents — avec suivi des autorités (ODCO, impôts, CNSS) dans un design marocain moderne.',
 'es': 'Una plataforma integral de gestión de cooperativas conforme a la ley 112.12: panel de control, socios y participaciones, asamblea general, finanzas y registro de documentos — con seguimiento de autoridades (ODCO, impuestos, CNSS) en un diseño marroquí moderno.',
 'it': 'Una piattaforma completa per la gestione delle cooperative ai sensi della legge 112.12: dashboard, soci e quote, assemblea generale, finanze e registro documenti — con tracciamento delle autorità (ODCO, imposte, CNSS) in un design marocchino moderno.',
 'de': 'Eine umfassende Plattform zur Genossenschaftsverwaltung gemäß Gesetz 112.12: Dashboard, Mitglieder und Anteile, Generalversammlung, Finanzen und Dokumentenregister — mit Verfolgung der Aufsichtsbehörden (ODCO, Steuern, CNSS) in modernem marokkanischem Design.',
 'nl': 'Een volledig platform voor coöperatiebeheer volgens wet 112.12: dashboard, leden en aandelen, algemene vergadering, financiën en documentenregister — met tracking van toezichthouders (ODCO, belastingen, CNSS) in een modern Marokkaans ontwerp.',
 'pt': 'Uma plataforma completa de gestão de cooperativas conforme a lei 112.12: painel, membros e quotas, assembleia geral, finanças e registo de documentos — com acompanhamento das autoridades (ODCO, impostos, CNSS) num design marroquino moderno.'}

# count phrase replacements: (old, new) exact strings
COUNTS = {
 'ar': [('وثيّته بـ13 شهادة معتمدة (Google، HP LIFE، Huawei) وسبعة مشاريع رقمية حيّة،', 'وثيّته بـ13 شهادة معتمدة (Google، HP LIFE، Huawei) وتسعة مشاريع رقمية حيّة،'),
        ('في ثمانية مشاريع رقمية حيّة', 'في تسعة مشاريع رقمية حيّة'),
        ('>ثمانية مشاريع حيّة بنيتها', '>تسعة مشاريع حيّة بنيتها'),
        ('في ثمانية مشاريع رقمية تعمل الآن', 'في تسعة مشاريع رقمية تعمل الآن'),
        ('ثمانية مشاريع حية على الإنترنت', 'تسعة مشاريع حية على الإنترنت'),
        ('<b class="stat-v" dir="ltr">8</b>', '<b class="stat-v" dir="ltr">9</b>')],
 'en': [('seven live digital projects,', 'nine live digital projects,'),
        ('eight live digital projects', 'nine live digital projects'),
        ('>Eight live projects I built', '>Nine live projects I built'),
        ('eight digital projects running live', 'nine digital projects running live'),
        ('eight live projects on the internet', 'nine live projects on the internet'),
        ('<b class="stat-v" dir="ltr">8</b>', '<b class="stat-v" dir="ltr">9</b>')],
 'fr': [('sept projets numériques en ligne', 'neuf projets numériques en ligne'),
        ('huit projets numériques en ligne', 'neuf projets numériques en ligne'),
        ('>Huit projets en ligne', '>Neuf projets en ligne'),
        ('huit projets en ligne sur Internet', 'neuf projets en ligne sur Internet'),
        ('<b class="stat-v" dir="ltr">8</b>', '<b class="stat-v" dir="ltr">9</b>')],
 'es': [('siete proyectos digitales en línea', 'nueve proyectos digitales en línea'),
        ('ocho proyectos digitales en línea', 'nueve proyectos digitales en línea'),
        ('>Ocho proyectos en línea', '>Nueve proyectos en línea'),
        ('ocho proyectos en línea en Internet', 'nueve proyectos en línea en Internet'),
        ('<b class="stat-v" dir="ltr">8</b>', '<b class="stat-v" dir="ltr">9</b>')],
 'it': [('sette progetti digitali online', 'nove progetti digitali online'),
        ('otto progetti digitali online', 'nove progetti digitali online'),
        ('>Otto progetti online', '>Nove progetti online'),
        ('otto progetti online su Internet', 'nove progetti online su Internet'),
        ('<b class="stat-v" dir="ltr">8</b>', '<b class="stat-v" dir="ltr">9</b>')],
 'de': [('sieben Live-Digitalprojekten', 'neun Live-Digitalprojekten'),
        ('acht Live-Digitalprojekten', 'neun Live-Digitalprojekten'),
        ('>Acht Live-Projekte', '>Neun Live-Projekte'),
        ('acht digitalen Live-Projekten', 'neun digitalen Live-Projekten'),
        ('acht Live-Projekte im Internet', 'neun Live-Projekte im Internet'),
        ('<b class="stat-v" dir="ltr">8</b>', '<b class="stat-v" dir="ltr">9</b>')],
 'nl': [('zeven live digitale projecten', 'negen live digitale projecten'),
        ('acht live digitale projecten', 'negen live digitale projecten'),
        ('>Acht live projecten', '>Negen live projecten'),
        ('acht digitale projecten die nu live', 'negen digitale projecten die nu live'),
        ('acht live projecten op internet', 'negen live projecten op internet'),
        ('<b class="stat-v" dir="ltr">8</b>', '<b class="stat-v" dir="ltr">9</b>')],
 'pt': [('sete projetos digitais online', 'nove projetos digitais online'),
        ('oito projetos digitais online', 'nove projetos digitais online'),
        ('>Oito projetos online', '>Nove projetos online'),
        ('oito projetos digitais em linha', 'nove projetos digitais em linha'),
        ('oito projetos em linha na Internet', 'nove projetos em linha na Internet'),
        ('<b class="stat-v" dir="ltr">8</b>', '<b class="stat-v" dir="ltr">9</b>')],
}


def pf(lang):
    return '' if lang == 'ar' else f'/{lang}'


def homepage_path(lang):
    return f'{SITE}/index.html' if lang == 'ar' else f'{SITE}/{lang}/index.html'


report = {'pager': [], 'card': [], 'counts': [], 'sitemap': []}

# ---------- 1. pagers ----------
for lang in LANGS:
    pref = pf(lang)
    # epdp page: next -> cmdp
    p = f'{SITE}/projects/epdp/index.html' if lang == 'ar' else f'{SITE}/{lang}/projects/epdp/index.html'
    h = open(p, encoding='utf-8').read()
    h2 = h.replace(f'pager-card next" href="{pref}/projects/natsup/"', f'pager-card next" href="{pref}/projects/cmdp/"')
    h2 = re.sub(r'(pager-card next"[\s\S]*?<span class="ttl">)NATSUP(</span>)', r'\1CMDP\2', h2)
    if h2 != h:
        open(p, 'w', encoding='utf-8').write(h2)
        report['pager'].append(f'epdp.next {lang}')
    # natsup page: prev -> cmdp
    p = f'{SITE}/projects/natsup/index.html' if lang == 'ar' else f'{SITE}/{lang}/projects/natsup/index.html'
    h = open(p, encoding='utf-8').read()
    h2 = h.replace(f'pager-card prev" href="{pref}/projects/epdp/"', f'pager-card prev" href="{pref}/projects/cmdp/"')
    h2 = h2.replace(f'<span class="ttl">{EPDP_NAME[lang]}</span>', '<span class="ttl">CMDP</span>')
    if h2 != h:
        open(p, 'w', encoding='utf-8').write(h2)
        report['pager'].append(f'natsup.prev {lang}')

# ---------- 2. homepage cards ----------
for lang in LANGS:
    p = homepage_path(lang)
    h = open(p, encoding='utf-8').read()
    if 'pj-cmdp.jpg' in h:
        report['card'].append(f'skip {lang} (already)')
        continue
    # extract epdp card block
    m = re.search(r'<article class="proj-card card reveal">\s*<a class="proj-media" href="https://epdp\.pages\.dev.*?</article>', h, re.S)
    assert m, 'epdp card not found ' + lang
    card = m.group(0)
    new = card
    new = new.replace('https://epdp.pages.dev', 'https://cmdp.pages.dev')
    new = new.replace('epdp.pages.dev', 'cmdp.pages.dev')
    new = new.replace('pj-epdp.jpg', 'pj-cmdp.jpg')
    new = new.replace(EPDP_NAME[lang], CMDP_NAME[lang])
    new = new.replace(f'href="{pf(lang)}/projects/epdp/"', f'href="{pf(lang)}/projects/cmdp/"')
    # tag + desc: replace inside new card
    new = re.sub(r'(<span class="proj-tag">)[^<]*(</span>)', lambda mm: mm.group(1) + TAG[lang] + mm.group(2), new)
    new = re.sub(r'(<p class="proj-desc">)[^<]*(</p>)', lambda mm: mm.group(1) + DESC[lang] + mm.group(2), new)
    assert '112.12' in new, 'desc not replaced ' + lang
    h = h[:m.end()] + '\n' + new + h[m.end():]
    open(p, 'w', encoding='utf-8').write(h)
    report['card'].append(f'inserted {lang}')

# ---------- 3. counts ----------
for lang in LANGS:
    for path in [homepage_path(lang), f'{SITE}/services/index.html' if lang == 'ar' else f'{SITE}/{lang}/services/index.html']:
        h = open(path, encoding='utf-8').read()
        hits = 0
        for old, new in COUNTS[lang]:
            if old in h:
                h = h.replace(old, new)
                hits += 1
        open(path, 'w', encoding='utf-8').write(h)
        report['counts'].append(f'{os.path.relpath(path, SITE)}: {hits} replacements')

# ---------- 4. sitemap ----------
sm = open(f'{SITE}/sitemap.xml', encoding='utf-8').read()
if '/projects/cmdp/' not in sm:
    m = re.search(r'  <url>\s*<loc>https://tarikchouika\.pages\.dev/projects/epdp/</loc>.*?</url>', sm, re.S)
    assert m, 'epdp sitemap block not found'
    block = m.group(0).replace('/projects/epdp/', '/projects/cmdp/').replace('/en/projects/epdp/', '/en/projects/cmdp/')
    # the simple replace handles all hreflang lines since they all contain /projects/epdp/ patterns per lang
    block = block.replace(f'{lang}/projects/epdp/', 'PLACEHOLDER')  # noop safeguard
    sm = sm[:m.end()] + '\n' + block + sm[m.end():]
    open(f'{SITE}/sitemap.xml', 'w', encoding='utf-8').write(sm)
    report['sitemap'].append('cmdp block added')
else:
    report['sitemap'].append('skip (already)')

print('PAGER  :', len([x for x in report['pager']]), report['pager'][:4], '...')
print('CARD   :', report['card'])
print('COUNTS :', report['counts'])
print('SITEMAP:', report['sitemap'])
