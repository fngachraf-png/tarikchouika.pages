#!/usr/bin/env python3
"""v5 responsive audit: DOM overflow + layout invariants on key pages x viewports.
Run:  python3 qa_audit.py [port]
"""
import json
import subprocess
import sys
import time

PORT = sys.argv[1] if len(sys.argv) > 1 else '8901'
BASE = 'http://localhost:%s' % PORT

PAGES = [
    ('/', 'ar-home'),
    ('/certs/digital-marketing-english/', 'ar-cert'),
    ('/projects/syda/', 'ar-proj'),
    ('/pt/certs/digital-marketing-english/', 'pt-cert'),
    ('/en/', 'en-home'),
    ('/de/projects/natsup/', 'de-proj'),
    ('/projects/mamp/', 'ar-mamp'),
    ('/en/projects/isyacar/', 'en-isyacar'),
    ('/projects/phmp/', 'ar-phmp'),
    ('/en/projects/phmp/', 'en-phmp'),
]
VIEWPORTS = [
    ('360x800', 360, 800),      # small phone portrait
    ('414x896', 414, 896),      # large phone portrait
    ('800x360', 800, 360),      # phone landscape
    ('768x1024', 768, 1024),    # tablet portrait
    ('1280x800', 1280, 800),    # laptop
    ('1366x768', 1366, 768),    # desktop
    ('1920x1080', 1920, 1080), # full desktop
]

AUDIT_JS = r"""JSON.stringify((function(){
  var bad = [];
  var de = document.documentElement;
  var hscroll = de.scrollWidth - de.clientWidth;
  if (hscroll > 1) bad.push('H-SCROLL ' + hscroll + 'px (scrollWidth=' + de.scrollWidth + ' clientWidth=' + de.clientWidth + ')');
  var vw = window.innerWidth;
  function rect(el){ return el.getBoundingClientRect(); }
  function decorative(e){
    var c = e.classList ? e.classList : null;
    if (!c) return false;
    return c.contains('hero-glow') || c.contains('hero-grid-bg');
  }
  // fixed chrome elements
  var header = document.querySelector('.site-header');
  var hb = rect(header);
  var crumbs = document.querySelector('.crumbs');
  var cb = crumbs ? rect(crumbs) : null;
  if (cb && cb.y < hb.bottom - 2) bad.push('CRUMBS UNDER HEADER: crumbsY=' + Math.round(cb.y) + ' headerBottom=' + Math.round(hb.bottom));
  var lead = document.querySelector('.page-lead');
  if (lead) { var lb = rect(lead); if (lb.y < hb.bottom) bad.push('LEAD UNDER HEADER y=' + Math.round(lb.y)); }
  // horizontal overflow of visible elements
  var all = document.querySelectorAll('body *');
  var seen = {};
  for (var i = 0; i < all.length; i++) {
    var e = all[i];
    if (decorative(e)) continue;
    var s = getComputedStyle(e);
    if (s.display === 'none' || s.visibility === 'hidden' || s.position === 'fixed') continue;
    var b = e.getBoundingClientRect();
    if (b.width === 0 || b.height === 0) continue;
    if (b.left < -1 || b.right > vw + 1) {
      var k = e.className && typeof e.className === 'string' ? e.tagName + '.' + e.className.split(' ')[0] : e.tagName;
      if (!seen[k]) { seen[k] = 1; bad.push('OVERFLOW ' + k + ' left=' + Math.round(b.left) + ' right=' + Math.round(b.right) + ' vw=' + vw); }
    }
  }
  // header items inside viewport
  ['.brand', '.nav-actions'].forEach(function(sel){
    var e = document.querySelector(sel);
    if (!e) return;
    var b = rect(e);
    if (b.left < 0 || b.right > vw) bad.push('HEADER ' + sel + ' outside viewport: ' + Math.round(b.left) + '..' + Math.round(b.right));
  });
  var actions = document.querySelector('.nav-actions');
  var brand = document.querySelector('.brand');
  if (actions && brand) {
    var ab = rect(actions), bb2 = rect(brand);
    var edgeGap = document.dir === 'rtl' ? Math.round(ab.left) : Math.round(vw - ab.right);
    if (edgeGap > 40 && vw < 1180) bad.push('HEADER actions not at edge: edgeGap=' + edgeGap);
  }
  return bad.length ? bad.join(' || ') : 'OK';
})())"""

CHAT_OPEN_JS = r"""(function(){ document.querySelector('.cb-fab').click(); return 'opened'; })()"""

CHAT_MEASURE_JS = r"""JSON.stringify((function(){
  var out = [];
  var panel = document.querySelector('.cb-panel');
  var b = panel.getBoundingClientRect();
  var vw = window.innerWidth, vh = window.innerHeight;
  if (b.left < 0 || b.right > vw + 1) out.push('PANEL H-OVERFLOW left=' + Math.round(b.left) + ' right=' + Math.round(b.right));
  if (b.top < 0) out.push('PANEL ABOVE VP top=' + Math.round(b.top));
  var input = panel.querySelector('.cb-text').getBoundingClientRect();
  if (input.bottom > vh) out.push('INPUT BELOW VP bottom=' + Math.round(input.bottom) + ' vh=' + vh);
  var fab = document.querySelector('.cb-fab').getBoundingClientRect();
  var btt = document.querySelector('.back-to-top');
  if (btt) {
    var bt = btt.getBoundingClientRect();
    var cs = getComputedStyle(btt);
    if (cs.opacity !== '0') out.push('BTT not hidden with chat open');
    if (!(b.right < bt.left - 5 || b.left > bt.right + 5 || b.bottom < bt.top - 5 || b.top > bt.bottom + 5)) out.push('BTT overlaps panel');
  }
  if (fab.top < b.bottom - 2) out.push('FAB hidden behind panel');
  var io = panel.querySelector('.cb-input').getBoundingClientRect();
  if (io.bottom > vh) out.push('INPUT-ROW below viewport');
  return out.length ? out.join(' || ') : 'OK';
})())"""


def run(session, cmd):
    r = subprocess.run(['agent-browser', '--session', session] + cmd,
                       capture_output=True, text=True, timeout=120)
    return (r.stdout + r.stderr).strip()


def main():
    session = 'qa5'
    failures = 0
    for vp_name, w, h in VIEWPORTS:
        for path, label in PAGES:
            run(session, ['open', BASE + path])
            run(session, ['set', 'viewport', str(w), str(h)])
            run(session, ['wait', '--load', 'networkidle'])
            time.sleep(0.4)
            res = run(session, ['eval', AUDIT_JS])
            status = 'OK' if 'OK' in res else 'FAIL'
            if status == 'FAIL':
                failures += 1
            print('[%s] %s %s -> %s' % (status, vp_name, label, res[:400]))
            # chatbot check on a subset
            if label in ('ar-home', 'pt-cert') and w in (360, 414, 800, 1366):
                run(session, ['eval', CHAT_OPEN_JS])
                time.sleep(0.8)
                res2 = run(session, ['eval', CHAT_MEASURE_JS])
                status2 = 'OK' if 'OK' in res2 else 'FAIL'
                if status2 == 'FAIL':
                    failures += 1
                print('[%s] %s %s CHAT -> %s' % (status2, vp_name, label, res2[:300]))
                run(session, ['eval', "document.querySelector('.cb-close').click()"])
                time.sleep(0.4)
    run(session, ['close'])
    print('\nTOTAL FAILURES: %d' % failures)
    sys.exit(1 if failures else 0)


if __name__ == '__main__':
    main()
