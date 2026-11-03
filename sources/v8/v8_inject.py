#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""v8 injector: EPDP project + services page + counts + chatbot updates.
Applies to scripts/site_src/t_*.py (8 languages) and chatbot_strings.py.
Every step is verified by re-parsing the modified source."""
import importlib.util
import re
import sys

sys.path.insert(0, '/home/z/my-project/scripts')
from v8_data_epdp import EPDP
from v8_data_svc import SVC

SRC = '/home/z/my-project/scripts/site_src'
LANGS = ['ar', 'en', 'fr', 'es', 'it', 'de', 'nl', 'pt']

# ---------------- python literal serializer (site style) ----------------
def py_str(s):
    return "'" + str(s).replace('\\', '\\\\').replace("'", "\\'") + "'"


def py_lit(obj, indent):
    pad = ' ' * indent
    if isinstance(obj, dict):
        if not obj:
            return '{}'
        items = []
        for k, v in obj.items():
            items.append(pad + '    ' + py_str(k) + ': ' + py_lit(v, indent + 4))
        return '{\n' + ',\n'.join(items) + '\n' + pad + '}'
    if isinstance(obj, (list, tuple)):
        if not obj:
            return '[]' if isinstance(obj, list) else '()'
        items = [pad + '    ' + py_lit(v, indent + 4) for v in obj]
        open_b, close_b = ('[', ']') if isinstance(obj, list) else ('(', ')')
        return open_b + '\n' + ',\n'.join(items) + '\n' + pad + close_b
    return py_str(obj)


def insert_into_list(src, key, entry_src):
    """Insert entry into the list 'key'. The list closes either with
    '\\n    ],' or '\\n    ]' (last key, no trailing comma). Entries are
    indented 8+ spaces, so a 4-space close is always the list end."""
    start = src.index("'%s': [" % key)
    end_marker = '\n    ]'
    end = src.index(end_marker, start)
    entry = ',\n        ' + entry_src + '\n    ]'
    return src[:end] + entry + src[end + len(end_marker):]


def replace_line_field(src, field, new_value, lang):
    """Replace the full line "    'field': ..." with a new literal."""
    pat = re.compile(r"^(?P<ind>[ \t]*)'%s': .*$" % field, re.M)
    m = pat.search(src)
    assert m, 'field %s not found (%s)' % (field, lang)
    return pat.sub(lambda mm: mm.group('ind') + "'%s': %s," % (field, py_str(new_value)), src, count=1)


def load_T(path):
    spec = importlib.util.spec_from_file_location('tcheck', path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.T


def check(cond, msg):
    if not cond:
        raise SystemExit('CHECK FAILED: ' + msg)


# ---------------- 1) inject EPDP + svc into t_*.py ----------------
for lang in LANGS:
    path = '%s/t_%s.py' % (SRC, lang)
    try:
        T = load_T(path)
        if (len(T['projects']) == 8 and len(T['project_tools']) == 8
                and 'svc' in T and 'services' in T['nav']):
            print('t_%s.py already injected — skip' % lang)
            continue
    except Exception:
        pass
    src = open(path, encoding='utf-8').read()
    d = EPDP[lang]
    svc = SVC[lang]

    # a. append EPDP entries to the 4 lists
    src = insert_into_list(src, 'projects', py_lit(d['card'], 8))
    src = insert_into_list(src, 'project_pages', py_lit(d['page'], 8))
    src = insert_into_list(src, 'project_v4', py_lit(d['v4'], 8))
    src = insert_into_list(src, 'project_tools', py_lit(d['tools'], 8))

    # b. stats 7 -> 8 (multi-line list layout: scope to the stats block)
    s_start = src.index("'stats': [")
    s_end = src.index('\n    ],', s_start)
    seg = src[s_start:s_end]
    check(seg.count("'7',") == 1, "stats '7' count=%d in %s" % (seg.count("'7',"), lang))
    src = src[:s_start] + seg.replace("'7',", "'8',", 1) + src[s_end:]

    # c. pj_sub (line replace)
    new_pjsub = {'ar': 'ثمانية مشاريع حيّة بنيتها ضمن رحلتي في تعلّم المهارات الرقمية',
                 'en': 'Eight live projects I built as part of my digital skills journey',
                 'fr': "Huit projets en ligne que j'ai réalisés dans le cadre de mon parcours d'apprentissage numérique",
                 'es': 'Ocho proyectos en línea que construí como parte de mi camino de aprendizaje digital',
                 'it': 'Otto progetti online realizzati nel mio percorso di apprendimento digitale',
                 'de': 'Acht Live-Projekte, die ich im Rahmen meiner digitalen Lernreise entwickelt habe',
                 'nl': 'Acht live projecten die ik heb gebouwd als onderdeel van mijn digitale leerreis',
                 'pt': 'Oito projetos online que construí como parte da minha jornada de aprendizagem digital'}[lang]
    src = replace_line_field(src, 'pj_sub', new_pjsub, lang)

    # d. about_p2 (line replace)
    new_about_p2 = {
        'ar': 'والفرق عندي أنني لا أكتفي بالتعلّم؛ بل أبني. وظّفت ما اكتسبته في ثمانية مشاريع رقمية حيّة طوّرتها بمساعدة نماذج الذكاء الاصطناعي — من المتاجر والمنصات الخدمية إلى أدوات إدارية مغربية متخصصة للجمعيات والصيدليات والوثائق الرسمية — من الفكرة إلى النشر على Cloudflare Pages.',
        'en': "My difference is that I don't just learn; I build. I put what I gained into eight live digital projects developed with the help of AI models — from stores and service platforms to specialized Moroccan administrative tools for associations, pharmacies and official documents — from idea to deployment on Cloudflare Pages.",
        'fr': "Ma différence : je n'apprends pas seulement, je construis. J'ai mis en pratique ce que j'ai acquis dans huit projets numériques en ligne développés avec l'aide de l'IA — des boutiques et plateformes de services aux outils administratifs marocains spécialisés pour les associations, les pharmacies et les documents officiels — de l'idée au déploiement sur Cloudflare Pages.",
        'es': 'Mi diferencia es que no solo aprendo: construyo. Puse en práctica lo adquirido en ocho proyectos digitales en línea desarrollados con ayuda de la IA — de tiendas y plataformas de servicios a herramientas administrativas marroquíes especializadas para asociaciones, farmacias y documentos oficiales — de la idea al despliegue en Cloudflare Pages.',
        'it': "La mia differenza è che non mi limito a imparare: costruisco. Ho messo in pratica ciò che ho acquisito in otto progetti digitali online sviluppati con l'aiuto dell'IA — da negozi e piattaforme di servizi a strumenti amministrativi marocchini specializzati per associazioni, farmacie e documenti ufficiali — dall'idea alla pubblicazione su Cloudflare Pages.",
        'de': 'Mein Unterschied: Ich lerne nicht nur — ich baue. Was ich erworben habe, habe ich in acht Live-Digitalprojekten umgesetzt, die mit Hilfe von KI-Modellen entstanden — von Shops und Serviceplattformen bis zu spezialisierten marokkanischen Verwaltungstools für Vereine, Apotheken und offizielle Dokumente — von der Idee bis zur Veröffentlichung auf Cloudflare Pages.',
        'nl': 'Mijn verschil: ik leer niet alleen, ik bouw. Wat ik heb opgedaan zette ik in in acht live digitale projecten die tot stand kwamen met hulp van AI-modellen — van winkels en serviceplatformen tot gespecialiseerde Marokkaanse administratieve tools voor verenigingen, apotheken en officiële documenten — van idee tot publicatie op Cloudflare Pages.',
        'pt': 'A minha diferença é que não me limito a aprender: construo. Pus em prática o que adquiri em oito projetos digitais online desenvolvidos com a ajuda da IA — de lojas e plataformas de serviços a ferramentas administrativas marroquinas especializadas para associações, farmácias e documentos oficiais — da ideia à publicação no Cloudflare Pages.',
    }[lang]
    src = replace_line_field(src, 'about_p2', new_about_p2, lang)

    # e. nav: add services item after projects
    nav_svc = svc['nav']
    pat = re.compile(r"('projects': '[^']*',)")
    m = pat.search(src)
    check(bool(m), 'nav projects key not found in %s' % lang)
    src = pat.sub(lambda mm: mm.group(1) + " 'services': %s," % py_str(nav_svc), src, count=1)

    # f. cta_services after cta_cv line
    pat = re.compile(r"^(?P<ind>[ \t]*)'cta_cv': .*$", re.M)
    m = pat.search(src)
    check(bool(m), 'cta_cv not found in %s' % lang)
    src = pat.sub(lambda mm: mm.group(0) + '\n' + mm.group('ind') + "'cta_services': %s," % py_str(svc['cta_services']), src, count=1)

    # g. append svc dict before final closing brace of T
    assert src.rstrip().endswith('}'), 'unexpected file end in %s' % lang
    body = src.rstrip()
    body = body[:-1].rstrip()
    if not body.endswith(','):
        body += ','
    src = body + '\n\n    # v8: digital services page\n    \'svc\': ' + py_lit(svc, 4).lstrip() + '\n}\n'

    open(path, 'w', encoding='utf-8').write(src)

    # verify by re-parsing
    T = load_T(path)
    check(len(T['projects']) == 8, 'projects != 8 in %s' % lang)
    check(len(T['project_pages']) == 8, 'project_pages != 8 in %s' % lang)
    check(len(T['project_v4']) == 8, 'project_v4 != 8 in %s' % lang)
    check(len(T['project_tools']) == 8, 'project_tools != 8 in %s' % lang)
    check(T['stats'][3][0] == '8', 'stats[3] != 8 in %s' % lang)
    check('services' in T['nav'], 'nav.services missing in %s' % lang)
    check('svc' in T and len(T['svc']['items']) == 6, 'svc missing in %s' % lang)
    check('cta_services' in T, 'cta_services missing in %s' % lang)
    print('t_%s.py OK  (8 projects, svc x%d, nav+cta)' % (lang, len(T['svc']['items'])))

# ---------------- 2) chatbot_strings.py updates ----------------
CB = '%s/chatbot_strings.py' % SRC
src = open(CB, encoding='utf-8').read()

COUNT_FIX = {
    'ar': ('سبعة مشاريع رقمية حية', 'ثمانية مشاريع رقمية حية'),
    'en': ('Seven live digital projects', 'Eight live digital projects'),
    'fr': ('Sept projets numériques en ligne', 'Huit projets numériques en ligne'),
    'es': ('Siete proyectos digitales en línea', 'Ocho proyectos digitales en línea'),
    'it': ('Sette progetti digitali online', 'Otto progetti digitali online'),
    'de': ('Sechs Live-Projekte', 'Acht Live-Projekte'),
    'nl': ('Zes live digitale projecten', 'Acht live digitale projecten'),
    'pt': ('Sete projetos digitais online', 'Oito projetos digitais online'),
}
EPDP_BULLET = {
    'ar': '• <a href="https://epdp.pages.dev" target="_blank" rel="noopener">EPDP</a> — كاتبك الرقمي: +1180 وثيقة إدارية مغربية رسمية ودليل البوابات<br>',
    'en': '• <a href="https://epdp.pages.dev" target="_blank" rel="noopener">EPDP</a> — your digital scribe: 1,180+ official Moroccan administrative forms and an official-portals guide<br>',
    'fr': '• <a href="https://epdp.pages.dev" target="_blank" rel="noopener">EPDP</a> — votre scribe numérique : 1 180+ documents administratifs marocains officiels et guide des portails<br>',
    'es': '• <a href="https://epdp.pages.dev" target="_blank" rel="noopener">EPDP</a> — tu escriba digital: 1.180+ documentos administrativos marroquíes oficiales y guía de portales<br>',
    'it': '• <a href="https://epdp.pages.dev" target="_blank" rel="noopener">EPDP</a> — il tuo scrivano digitale: 1.180+ documenti amministrativi marocchini ufficiali e guida ai portali<br>',
    'de': '• <a href="https://epdp.pages.dev" target="_blank" rel="noopener">EPDP</a> — dein digitaler Schreiber: 1.180+ offizielle marokkanische Verwaltungsdokumente und Portal-Leitfaden<br>',
    'nl': '• <a href="https://epdp.pages.dev" target="_blank" rel="noopener">EPDP</a> — jouw digitale griffier: 1.180+ officiële Marokkaanse administratieve documenten en portalengids<br>',
    'pt': '• <a href="https://epdp.pages.dev" target="_blank" rel="noopener">EPDP</a> — o teu escriba digital: 1.180+ documentos administrativos marroquinos oficiais e guia de portais<br>',
}
TAIL_MARK = {
    'ar': 'التفاصيل الكاملة', 'en': 'Full details', 'fr': 'Détails complets',
    'es': 'Detalles completos', 'it': 'Dettagli completi', 'de': 'Alle Details',
    'nl': 'Volledige details', 'pt': 'Detalhes completos',
}
SVC7_FIX = {
    'ar': ('7 مشاريع حية', '8 مشاريع حية'), 'en': ('7 live projects', '8 live projects'),
    'fr': ('7 projets en ligne', '8 projets en ligne'), 'es': ('7 proyectos en línea', '8 proyectos en línea'),
    'it': ('7 progetti online', '8 progetti online'), 'de': ('7 Live-Projekte', '8 Live-Projekte'),
    'nl': ('7 live projecten', '8 live projecten'), 'pt': ('7 projetos online', '8 projetos online'),
}
SVC_END_FIX = {
    'ar': ('لطلب أي منها اضغط «حجز/استفسار».', 'لطلب أي منها اضغط «حجز/استفسار» — وكل التفاصيل في <a href="{L}services/" target="_self">صفحة الخدمات الرقمية</a>.'),
    'en': ('Press “Book/Inquire” to request any of them.', 'Press “Book/Inquire” to request any of them — full details on the <a href="{L}services/" target="_self">digital services page</a>.'),
    'fr': ('Appuyez sur « Réserver/Demander » pour en profiter.', 'Appuyez sur « Réserver/Demander » pour en profiter — tous les détails sur la <a href="{L}services/" target="_self">page des services numériques</a>.'),
    'es': ('Pulsa «Reservar/Consultar» para solicitar cualquiera de ellos.', 'Pulsa «Reservar/Consultar» para solicitar cualquiera de ellos — todos los detalles en la <a href="{L}services/" target="_self">página de servicios digitales</a>.'),
    'it': ('Premi «Prenota/Chiedi» per richiederne uno.', 'Premi «Prenota/Chiedi» per richiederne uno — tutti i dettagli nella <a href="{L}services/" target="_self">pagina dei servizi digitali</a>.'),
    'de': ('Klicke auf „Buchen/Anfragen“, um etwas davon anzufragen.', 'Klicke auf „Buchen/Anfragen“, um etwas davon anzufragen — alle Details auf der <a href="{L}services/" target="_self">Seite der digitalen Leistungen</a>.'),
    'nl': ('Druk op «Boeken/Vragen» om er een aan te vragen.', 'Druk op «Boeken/Vragen» om er een aan te vragen — alle details op de <a href="{L}services/" target="_self">pagina met digitale diensten</a>.'),
    'pt': ('Prime «Marcar/Perguntar» para pedir qualquer um deles.', 'Prime «Marcar/Perguntar» para pedir qualquer um deles — todos os detalhes na <a href="{L}services/" target="_self">página de serviços digitais</a>.'),
}

# parse current chatbot values
spec = importlib.util.spec_from_file_location('cbs', CB)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
CHAT = mod.CHAT

for lang in LANGS:
    # ---- a_projects ----
    old = CHAT[lang]['a_projects']
    oldc, newc = COUNT_FIX[lang]
    check(oldc in old, 'count phrase missing in a_projects(%s): %s' % (lang, old[:80]))
    new = old.replace(oldc, newc, 1)
    tm = TAIL_MARK[lang]
    check(tm in new, 'tail mark missing in a_projects(%s)' % lang)
    new = new.replace(tm, EPDP_BULLET[lang] + tm, 1)
    # replace the line in source
    pat = re.compile(r"^(?P<ind>[ \t]*)'a_projects': .*$", re.M)
    matches = list(pat.finditer(src))
    check(len(matches) == 8, 'expected 8 a_projects lines, got %d' % len(matches))
    # replace sequentially per language order
    idx = LANGS.index(lang)
    m = matches[idx]
    line_new = m.group('ind') + "'a_projects': " + py_str(new) + ','
    src = src[:m.start()] + line_new + src[m.end():]

    # ---- a_services ----
    old = CHAT[lang]['a_services']
    o7, n8 = SVC7_FIX[lang]
    check(o7 in old, '7-projects phrase missing in a_services(%s)' % lang)
    new = old.replace(o7, n8, 1)
    oe, ne = SVC_END_FIX[lang]
    check(oe in new, 'end phrase missing in a_services(%s): ...%s' % (lang, new[-90:]))
    new = new.replace(oe, ne, 1)
    pat = re.compile(r"^(?P<ind>[ \t]*)'a_services': .*$", re.M)
    matches = list(pat.finditer(src))
    check(len(matches) == 8, 'expected 8 a_services lines, got %d' % len(matches))
    m = matches[idx]
    line_new = m.group('ind') + "'a_services': " + py_str(new) + ','
    src = src[:m.start()] + line_new + src[m.end():]
    print('chatbot %s OK (a_projects 8 links + a_services services link)' % lang)

open(CB, 'w', encoding='utf-8').write(src)

# re-verify chatbot file parses and has 8 links in every language
spec = importlib.util.spec_from_file_location('cbs2', CB)
mod2 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod2)
for lang in LANGS:
    ap = mod2.CHAT[lang]['a_projects']
    check(ap.count('https://epdp.pages.dev') == 1, 'epdp link missing in %s' % lang)
    check(ap.count('pages.dev"') >= 8, 'project links < 8 in %s' % lang)
    asv = mod2.CHAT[lang]['a_services']
    check('{L}services/' in asv, 'services link missing in %s' % lang)
print('chatbot_strings.py verified for all languages')
print('\nALL INJECTIONS DONE AND VERIFIED')
