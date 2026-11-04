#!/usr/bin/env python3
"""Local QA with measurement: serve site, load key pages at 3 viewports in
both themes, assert: no horizontal overflow, all images load, no JS errors,
shots gallery + lightbox work. Prints a measurement report."""
import json, subprocess, time, os, sys
from playwright.sync_api import sync_playwright

SITE = '/home/z/my-project/site'
PORT = 8901

server = subprocess.Popen([sys.executable, '-m', 'http.server', str(PORT)],
                          cwd=SITE, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
time.sleep(1.2)

BASE = f'http://localhost:{PORT}'
VIEWPORTS = {'desktop': (1440, 900), 'tablet': (768, 1024), 'mobile': (390, 844)}

PAGES = [
    '/', '/projects/cmdp/', '/projects/syda/', '/projects/phmp/',
    '/en/', '/en/projects/cmdp/', '/en/projects/epdp/', '/de/projects/cmdp/',
    '/projects/natsup/', '/projects/epdp/',
]

report, failures = [], []

def check(name, cond, detail=''):
    (report if cond else failures).append(f'{"PASS" if cond else "FAIL"} {name} {detail}')

try:
    with sync_playwright() as pw:
        b = pw.chromium.launch()
        for vname, (w, h) in VIEWPORTS.items():
            ctx = b.new_context(viewport={'width': w, 'height': h})
            pg = ctx.new_page()
            errors = []
            pg.on('pageerror', lambda e: errors.append(str(e)))
            for path in PAGES:
                pg.goto(BASE + path, wait_until='networkidle', timeout=30000)
                pg.wait_for_timeout(400)
                url = pg.url
                m = pg.evaluate('''() => {
                    const de = document.documentElement;
                    const overflowX = de.scrollWidth - de.clientWidth;
                    const imgs = [...document.images];
                    const broken = imgs.filter(i => (i.getAttribute('src') || '').trim() !== '' && i.complete && i.naturalWidth === 0).map(i => i.src);
                    return {overflowX, total: imgs.length, broken,
                            h1: document.querySelector('h1') ? document.querySelector('h1').textContent.trim().slice(0,40) : ''};
                }''')
                tag = f'{vname} {path}'
                check(f'no-overflow {tag}', m['overflowX'] <= 1, f'(overflow={m["overflowX"]}px)')
                check(f'images-load {tag}', len(m['broken']) == 0, f'({m["total"]} imgs, broken={m["broken"][:2]})')
                if errors:
                    check(f'no-js-errors {tag}', False, str(errors[:1]))
                    errors = []
            ctx.close()

        # --- functional: shots gallery + lightbox on cmdp AR (desktop) ---
        ctx = b.new_context(viewport={'width': 1440, 'height': 900})
        pg = ctx.new_page()
        pg.goto(BASE + '/projects/cmdp/', wait_until='networkidle')
        pg.wait_for_timeout(600)
        n = pg.evaluate('document.querySelectorAll(".shot-zoom").length')
        check('gallery present (4 shots)', n == 4, f'(found {n})')
        # scroll to gallery to trigger reveal
        pg.evaluate('document.getElementById("pp-shots").scrollIntoView()')
        pg.wait_for_timeout(700)
        # click first shot -> lightbox opens
        pg.click('.shot-zoom >> nth=0')
        pg.wait_for_timeout(500)
        st = pg.evaluate('''() => {
            const lb = document.getElementById('shot-lb');
            const img = document.getElementById('slb-img');
            return {hidden: lb.hidden, src: img.src, loaded: img.complete && img.naturalWidth > 0,
                    count: document.getElementById('slb-count').textContent,
                    cap: document.getElementById('slb-cap').textContent.trim().slice(0,40)};
        }''')
        check('lightbox opens', st['hidden'] is False)
        check('lightbox image loads', st['loaded'], f'(src={st["src"].split("/")[-1]})')
        check('lightbox counter', st['count'] == '1 / 4', f'({st["count"]})')
        # navigate next
        pg.click('#slb-next')
        pg.wait_for_timeout(350)
        st2 = pg.evaluate('''() => ({count: document.getElementById('slb-count').textContent,
            src: document.getElementById('slb-img').src})''')
        check('lightbox next works', st2['count'] == '2 / 4', f'({st2["count"]}, {st2["src"].split("/")[-1]})')
        # close via Escape
        pg.keyboard.press('Escape')
        pg.wait_for_timeout(300)
        check('lightbox closes (Esc)', pg.evaluate('document.getElementById("shot-lb").hidden') is True)

        # --- light theme visual check: no broken styling (bg changed) ---
        pg.evaluate("document.documentElement.setAttribute('data-theme','light')")
        pg.wait_for_timeout(300)
        bg = pg.evaluate('getComputedStyle(document.body).backgroundColor')
        check('light theme applies', bg == 'rgb(246, 241, 231)', f'({bg})')

        # --- measure gallery layout on mobile ---
        ctx2 = b.new_context(viewport={'width': 390, 'height': 844})
        pg2 = ctx2.new_page()
        pg2.goto(BASE + '/projects/cmdp/', wait_until='networkidle')
        pg2.wait_for_timeout(500)
        dims = pg2.evaluate('''() => {
            const row = document.querySelector('.shot-row');
            const phone = document.querySelector('.dev-phone');
            const main = document.querySelector('.shot-main img');
            const r = row.getBoundingClientRect();
            const p = phone.getBoundingClientRect();
            const m = main.getBoundingClientRect();
            return {rowW: Math.round(r.width), rowCols: getComputedStyle(row).gridTemplateColumns.split(' ').length,
                    phoneW: Math.round(p.width), phoneH: Math.round(p.height),
                    mainW: Math.round(m.width), mainH: Math.round(m.height), vw: innerWidth};
        }''')
        check('mobile gallery single column', dims['rowCols'] == 1, f'(cols={dims["rowCols"]})')
        check('mobile phone frame sized', 150 <= dims['phoneW'] <= 330 and dims['phoneH'] > 300,
              f'(phone={dims["phoneW"]}x{dims["phoneH"]})')
        check('mobile main shot fits', dims['mainW'] <= dims['vw'], f'(main={dims["mainW"]} vw={dims["vw"]})')
        # tablet: 2 columns
        ctx3 = b.new_context(viewport={'width': 768, 'height': 1024})
        pg3 = ctx3.new_page()
        pg3.goto(BASE + '/projects/cmdp/', wait_until='networkidle')
        pg3.wait_for_timeout(400)
        cols = pg3.evaluate("getComputedStyle(document.querySelector('.shot-row')).gridTemplateColumns.split(' ').length")
        check('tablet gallery 2 columns', cols == 2, f'(cols={cols})')
        b.close()
finally:
    server.terminate()

print(f'\n===== QA REPORT: {len(report)} passed, {len(failures)} failed =====')
for f in failures:
    print(f)
if not failures:
    print('ALL CHECKS PASSED')
