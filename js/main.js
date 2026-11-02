/* Tarik Chouika — portfolio interactions */
(function () {
  'use strict';

  var prefersReduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ---------- Typewriter ---------- */
  var tw = document.getElementById('typewriter');
  if (tw) {
    var roles = [];
    try { roles = JSON.parse(tw.getAttribute('data-roles') || '[]'); } catch (e) { roles = []; }
    if (roles.length) {
      if (prefersReduced) {
        tw.textContent = roles.join(' \u00b7 ');
      } else {
        var ri = 0, ci = 0, deleting = false;
        (function tick() {
          var word = roles[ri];
          ci += deleting ? -1 : 1;
          tw.textContent = word.slice(0, ci);
          var delay = deleting ? 32 : 72;
          if (!deleting && ci === word.length) { delay = 1900; deleting = true; }
          else if (deleting && ci === 0) { deleting = false; ri = (ri + 1) % roles.length; delay = 380; }
          window.setTimeout(tick, delay);
        })();
      }
    }
  }

  /* ---------- Header scroll state ---------- */
  var header = document.querySelector('.site-header');
  function onScrollHeader() {
    if (header) header.classList.toggle('scrolled', window.scrollY > 30);
  }
  window.addEventListener('scroll', onScrollHeader, { passive: true });
  onScrollHeader();

  /* ---------- Mobile menu ---------- */
  var toggle = document.getElementById('nav-toggle');
  var panel = document.getElementById('nav-panel');
  function closeMenu() {
    if (!panel) return;
    panel.classList.remove('open');
    if (toggle) toggle.setAttribute('aria-expanded', 'false');
    document.body.style.overflow = '';
  }
  if (toggle && panel) {
    toggle.addEventListener('click', function () {
      var open = panel.classList.toggle('open');
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
      document.body.style.overflow = open ? 'hidden' : '';
    });
    panel.querySelectorAll('a').forEach(function (a) {
      a.addEventListener('click', closeMenu);
    });
  }

  /* ---------- Reveal on scroll ---------- */
  var revealEls = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window && !prefersReduced) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible');
          io.unobserve(entry.target);
        }
      });
    }, { threshold: 0.12 });
    revealEls.forEach(function (el, i) {
      el.style.transitionDelay = ((i % 4) * 80) + 'ms';
      io.observe(el);
    });
  } else {
    revealEls.forEach(function (el) { el.classList.add('visible'); });
  }

  /* ---------- Scrollspy (active nav link) ---------- */
  var sections = Array.prototype.slice.call(document.querySelectorAll('main section[id]'));
  var navAnchors = Array.prototype.slice.call(document.querySelectorAll('.nav-links a, .nav-panel-links a'));
  if ('IntersectionObserver' in window && sections.length && navAnchors.length) {
    var spy = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          var id = '#' + entry.target.id;
          navAnchors.forEach(function (a) {
            a.classList.toggle('active', a.getAttribute('href') === id);
          });
        }
      });
    }, { rootMargin: '-38% 0px -55% 0px' });
    sections.forEach(function (s) { spy.observe(s); });
  }

  /* ---------- Back to top ---------- */
  var btt = document.getElementById('back-to-top');
  if (btt) {
    window.addEventListener('scroll', function () {
      btt.classList.toggle('visible', window.scrollY > 600);
    }, { passive: true });
    btt.addEventListener('click', function () {
      window.scrollTo({ top: 0, behavior: prefersReduced ? 'auto' : 'smooth' });
    });
  }

  /* ---------- Copy email ---------- */
  document.querySelectorAll('.copy-btn').forEach(function (btn) {
    btn.addEventListener('click', function () {
      var value = btn.getAttribute('data-copy') || '';
      var done = function () {
        var label = btn.querySelector('.copy-label');
        var copiedText = btn.getAttribute('data-copied') || 'OK';
        if (!label) return;
        var original = label.getAttribute('data-original') || label.textContent;
        label.setAttribute('data-original', original);
        label.textContent = copiedText;
        window.setTimeout(function () { label.textContent = original; }, 1600);
      };
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(value).then(done).catch(function () { fallbackCopy(value); done(); });
      } else {
        fallbackCopy(value);
        done();
      }
    });
  });
  function fallbackCopy(value) {
    var ta = document.createElement('textarea');
    ta.value = value;
    ta.style.position = 'fixed';
    ta.style.opacity = '0';
    document.body.appendChild(ta);
    ta.select();
    try { document.execCommand('copy'); } catch (e) {}
    ta.remove();
  }

  /* ---------- Language switcher ---------- */
  var langSwitch = document.getElementById('lang-switch');
  if (langSwitch) {
    langSwitch.addEventListener('change', function () {
      if (langSwitch.value) window.location.href = langSwitch.value;
    });
  }

  /* ---------- Theme toggle (dark <-> light) ---------- */
  var themeBtn = document.getElementById('theme-toggle');
  var themeMeta = document.querySelector('meta[name="theme-color"]');
  function syncThemeMeta() {
    var light = document.documentElement.getAttribute('data-theme') === 'light';
    if (themeMeta) themeMeta.setAttribute('content', light ? '#f6f1e7' : '#0b0d10');
  }
  syncThemeMeta();
  if (themeBtn) {
    themeBtn.addEventListener('click', function () {
      var root = document.documentElement;
      var next = root.getAttribute('data-theme') === 'light' ? 'dark' : 'light';
      if (next === 'dark') { root.removeAttribute('data-theme'); } else { root.setAttribute('data-theme', next); }
      try { localStorage.setItem('tc-theme', next); } catch (e) {}
      syncThemeMeta();
    });
  }

  /* ---------- Certificate field filter ---------- */
  var filterBar = document.querySelector('.filter-bar');
  var certCards = Array.prototype.slice.call(document.querySelectorAll('.certs-grid .cert-card'));
  if (filterBar && certCards.length) {
    filterBar.querySelectorAll('.f-chip').forEach(function (chip) {
      chip.addEventListener('click', function () {
        var f = chip.getAttribute('data-filter') || 'all';
        filterBar.querySelectorAll('.f-chip').forEach(function (c) {
          c.classList.toggle('active', c === chip);
        });
        certCards.forEach(function (card) {
          var match = f === 'all' || card.getAttribute('data-field') === f;
          card.classList.toggle('cert-hide', !match);
        });
      });
    });
  }

  /* ---------- Certificate lightbox ---------- */
  var lb = document.getElementById('cert-lb');
  var mediaBtns = Array.prototype.slice.call(document.querySelectorAll('.cert-media'));
  var lbIndex = -1;
  var lbLastFocus = null;
  function openLb(i) {
    var btn = mediaBtns[i];
    if (!btn || !lb) return;
    lbLastFocus = btn;
    document.getElementById('lb-img').src = btn.getAttribute('data-full') || '';
    document.getElementById('lb-img').alt = btn.getAttribute('data-title') || '';
    document.getElementById('lb-title').textContent = btn.getAttribute('data-title') || '';
    document.getElementById('lb-field').textContent = btn.getAttribute('data-field-label') || '';
    document.getElementById('lb-issuer').textContent = btn.getAttribute('data-issuer') || '';
    document.getElementById('lb-date').textContent = btn.getAttribute('data-date') || '';
    var cred = btn.getAttribute('data-cred') || '';
    var credRow = document.getElementById('lb-cred-row');
    if (cred) {
      if (credRow) credRow.style.display = '';
      document.getElementById('lb-cred').textContent = cred;
    } else if (credRow) {
      credRow.style.display = 'none';
    }
    var drive = document.getElementById('lb-drive');
    if (drive) {
      drive.href = 'https://drive.google.com/file/d/' + (btn.getAttribute('data-drive') || '') + '/view';
    }
    lbIndex = i;
    lb.hidden = false;
    document.body.style.overflow = 'hidden';
    var closeBtn = lb.querySelector('.lb-close');
    if (closeBtn) closeBtn.focus();
  }
  function closeLb() {
    if (!lb || lb.hidden) return;
    lb.hidden = true;
    document.body.style.overflow = '';
    if (lbLastFocus && lbLastFocus.focus) lbLastFocus.focus();
    lbIndex = -1;
  }
  function stepLb(delta) {
    if (lbIndex < 0) return;
    var next = (lbIndex + delta + mediaBtns.length) % mediaBtns.length;
    openLb(next);
  }
  if (lb) {
    mediaBtns.forEach(function (btn, i) {
      btn.addEventListener('click', function () { openLb(i); });
    });
    lb.querySelectorAll('[data-lb-close]').forEach(function (el) {
      el.addEventListener('click', closeLb);
    });
    var prev = document.getElementById('lb-prev');
    var next = document.getElementById('lb-next');
    if (prev) prev.addEventListener('click', function () { stepLb(-1); });
    if (next) next.addEventListener('click', function () { stepLb(1); });
    document.addEventListener('keydown', function (e) {
      if (lb.hidden) return;
      if (e.key === 'Escape') { closeLb(); }
      else if (e.key === 'ArrowLeft') { stepLb(document.documentElement.dir === 'rtl' ? 1 : -1); }
      else if (e.key === 'ArrowRight') { stepLb(document.documentElement.dir === 'rtl' ? -1 : 1); }
    });
  }

  /* ---------- Current year ---------- */
  document.querySelectorAll('[data-year]').forEach(function (el) {
    el.textContent = String(new Date().getFullYear());
  });
})();
