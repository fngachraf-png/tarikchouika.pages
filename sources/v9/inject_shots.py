#!/usr/bin/env python3
"""Inject the shots gallery section + lightbox markup into all existing
project detail pages (9 slugs x 8 languages = 72 pages).
Idempotent: skips files already containing id="pp-shots".
"""
import os, re, sys

SITE = '/home/z/my-project/site'
SLUGS = ['natsup', 'natsuptc', 'syda', 'dtsg', 'hrmp', 'mamp', 'isyacar', 'phmp', 'epdp']
LANGS = ['ar', 'en', 'fr', 'es', 'it', 'de', 'nl', 'pt']

UI = {
 'ar': dict(h2='المشروع بالصور — على كل الأجهزة',
   lead='لقطات حقيقية من الموقع المباشر كما تظهر على الحاسوب واللوحي والهاتف — اضغط أي صورة لمشاهدتها بالحجم الكامل.',
   c1='الواجهة الرئيسية على شاشة الحاسوب', c2='من محتوى الموقع على الحاسوب',
   c3='العرض على اللوحي', c4='العرض على الهاتف الذكي',
   close='إغلاق العارض', prev='الصورة السابقة', next='الصورة التالية'),
 'en': dict(h2='The project in pictures — across every device',
   lead='Real screenshots from the live site as it appears on desktop, tablet and phone — click any image to view it full size.',
   c1='Home page on a desktop screen', c2='Inside the site content on desktop',
   c3='Tablet view', c4='Smartphone view',
   close='Close viewer', prev='Previous image', next='Next image'),
 'fr': dict(h2='Le projet en images — sur tous les écrans',
   lead='De vraies captures du site en ligne, telles qu\u2019elles apparaissent sur ordinateur, tablette et téléphone — cliquez sur une image pour l\u2019agrandir.',
   c1='Page d\u2019accueil sur écran d\u2019ordinateur', c2='Au cœur du contenu sur ordinateur',
   c3='Vue sur tablette', c4='Vue sur smartphone',
   close='Fermer la visionneuse', prev='Image précédente', next='Image suivante'),
 'es': dict(h2='El proyecto en imágenes — en todos los dispositivos',
   lead='Capturas reales del sitio en vivo tal como se ve en ordenador, tableta y móvil — pulsa cualquier imagen para verla en grande.',
   c1='Página principal en pantalla de ordenador', c2='Dentro del contenido en ordenador',
   c3='Vista en tableta', c4='Vista en el móvil',
   close='Cerrar visor', prev='Imagen anterior', next='Imagen siguiente'),
 'it': dict(h2='Il progetto in immagini — su tutti i dispositivi',
   lead='Vere istantanee dal sito dal vivo così come appaiono su computer, tablet e telefono — clicca un\u2019immagine per vederla a schermo intero.',
   c1='Home page sullo schermo del computer', c2='Dentro i contenuti su computer',
   c3='Vista su tablet', c4='Vista su smartphone',
   close='Chiudi visore', prev='Immagine precedente', next='Immagine successiva'),
 'de': dict(h2='Das Projekt in Bildern — auf allen Geräten',
   lead='Echte Screenshots der Live-Website, wie sie auf Desktop, Tablet und Smartphone erscheint — klicken Sie auf ein Bild, um es in voller Größe zu sehen.',
   c1='Startseite auf dem Desktop-Bildschirm', c2='Ein Blick in die Inhalte am Desktop',
   c3='Ansicht auf dem Tablet', c4='Ansicht auf dem Smartphone',
   close='Betrachter schließen', prev='Vorheriges Bild', next='Nächstes Bild'),
 'nl': dict(h2='Het project in beeld — op elk apparaat',
   lead='Echte schermafbeeldingen van de live site, zoals die op desktop, tablet en telefoon verschijnt — klik op een afbeelding om deze volledig te bekijken.',
   c1='Startpagina op een desktopscherm', c2='Binnen de inhoud op desktop',
   c3='Weergave op tablet', c4='Weergave op smartphone',
   close='Viewer sluiten', prev='Vorige afbeelding', next='Volgende afbeelding'),
 'pt': dict(h2='O projeto em imagens — em todos os dispositivos',
   lead='Capturas de ecrã reais do site ao vivo, tal como aparecem no computador, tablet e telemóvel — clique numa imagem para a ver em tamanho grande.',
   c1='Página inicial no ecrã do computador', c2='Dentro do conteúdo no computador',
   c3='Vista no tablet', c4='Vista no smartphone',
   close='Fechar visualizador', prev='Imagem anterior', next='Imagem seguinte'),
}

# special d2 caption for phmp (login modal shot)
PHMP_D2 = {
 'ar': 'نافذة الدخول إلى الحساب على الحاسوب', 'en': 'Account sign-in window on desktop',
 'fr': 'Fenêtre de connexion sur ordinateur', 'es': 'Ventana de inicio de sesión en ordenador',
 'it': 'Finestra di accesso su computer', 'de': 'Anmeldefenster am Desktop',
 'nl': 'Inlogvenster op desktop', 'pt': 'Janela de início de sessão no computador',
}

IMG_DIMS = {'d1': (1600, 1000), 'd2': (1600, 1000), 't': (900, 1200), 'm': (720, 1558)}

SVG_X = '<svg class="ic" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>'
SVG_PREV = '<svg class="ic" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="15 18 9 12 15 6"/></svg>'
SVG_NEXT = '<svg class="ic" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="9 18 15 12 9 6"/></svg>'


def browser_figure(slug, kind, domain, name, cap, extra_cls=''):
    w, h = IMG_DIMS[kind]
    src = f'/img/shots/{slug}-{kind}.jpg'
    alt = f'{name} — {cap}'
    return f'''<figure class="shot {extra_cls}reveal">
            <button class="shot-zoom" type="button" data-full="{src}" data-alt="{alt}" data-cap="{cap}">
              <span class="browser"><span class="b-bar"><i></i><i></i><i></i><span class="b-url">{domain}</span></span><img src="{src}" alt="{alt}" width="{w}" height="{h}" loading="lazy"></span>
            </button>
            <figcaption>{cap}</figcaption>
          </figure>'''


def device_figure(slug, kind, dev_cls, name, cap):
    w, h = IMG_DIMS[kind]
    src = f'/img/shots/{slug}-{kind}.jpg'
    alt = f'{name} — {cap}'
    return f'''<figure class="shot reveal">
            <button class="shot-zoom" type="button" data-full="{src}" data-alt="{alt}" data-cap="{cap}">
              <span class="dev {dev_cls}"><img src="{src}" alt="{alt}" width="{w}" height="{h}" loading="lazy"></span>
            </button>
            <figcaption>{cap}</figcaption>
          </figure>'''


def build_section(slug, lang, name):
    ui = UI[lang]
    domain = f'{slug}.pages.dev'
    c2 = PHMP_D2[lang] if slug == 'phmp' else ui['c2']
    main = browser_figure(slug, 'd1', domain, name, ui['c1'], extra_cls='shot-main ')
    d2 = browser_figure(slug, 'd2', domain, name, c2)
    tab = device_figure(slug, 't', 'dev-tab', name, ui['c3'])
    phone = device_figure(slug, 'm', 'dev-phone', name, ui['c4'])
    return f'''
      <section class="dsec" id="pp-shots">
        <h2>{ui['h2']}</h2>
        <p class="dsec-lead">{ui['lead']}</p>
        <div class="shots">
          {main}
          <div class="shot-row">
            {d2}
            {tab}
            {phone}
          </div>
        </div>
      </section>
'''


def build_lightbox(lang):
    ui = UI[lang]
    return f'''<div class="shot-lb" id="shot-lb" hidden>
  <div class="lb-backdrop" data-slb-close></div>
  <figure class="slb-body">
    <img id="slb-img" alt="">
    <figcaption><span id="slb-cap"></span><span class="slb-count" id="slb-count"></span></figcaption>
  </figure>
  <button class="lb-close slb-close" type="button" data-slb-close aria-label="{ui['close']}">{SVG_X}</button>
  <button class="lb-nav lb-prev slb-prev" id="slb-prev" type="button" aria-label="{ui['prev']}">{SVG_PREV}</button>
  <button class="lb-nav lb-next slb-next" id="slb-next" type="button" aria-label="{ui['next']}">{SVG_NEXT}</button>
</div>

'''


def process(slug, lang):
    d = f'{SITE}/projects/{slug}/index.html' if lang == 'ar' else f'{SITE}/{lang}/projects/{slug}/index.html'
    if not os.path.exists(d):
        return ('missing', d)
    html = open(d, encoding='utf-8').read()
    if 'id="pp-shots"' in html:
        return ('skip', d)
    m = re.search(r'<h1 class="reveal">(.*?)</h1>', html)
    name = m.group(1) if m else slug.upper()

    # inject gallery after pp-about section
    pv = html.find('<section class="dsec" id="pp-value">')
    if pv < 0:
        return ('no-pp-value', d)
    end_about = html.rfind('</section>', 0, pv)
    if end_about < 0:
        return ('no-about-end', d)
    ins = end_about + len('</section>')
    html = html[:ins] + '\n' + build_section(slug, lang, name).rstrip() + html[ins:]

    # inject lightbox before main.js script
    ms = html.find('<script src="/js/main.js')
    if ms < 0:
        return ('no-mainjs', d)
    html = html[:ms] + build_lightbox(lang) + html[ms:]

    open(d, 'w', encoding='utf-8').write(html)
    return ('ok', d)


counts = {}
for slug in SLUGS:
    for lang in LANGS:
        st, d = process(slug, lang)
        counts[st] = counts.get(st, 0) + 1
        if st not in ('ok', 'skip'):
            print('PROBLEM', st, d)
print('RESULT:', counts)
