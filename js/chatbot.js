/* Tarik Chouika — deterministic multilingual chatbot (text + voice, no hallucination).
   Answers come ONLY from the curated knowledge base in chatbot-i18n.js, and links
   are a fixed whitelist of real URLs. Inquiries/consultations/bookings are sent to
   the owner's official Telegram bot (client-side, static-site friendly). */
(function () {
  'use strict';

  if (!window.TC_CHAT) { return; }
  var TG = window.TC_CHAT_TG; /* {token, chat_id, bot_url} injected by chatbot-i18n.js */
  var lang = (document.documentElement.lang || 'ar').slice(0, 2);
  var L = window.TC_CHAT[lang] ? lang : 'ar';
  var S = window.TC_CHAT[L];
  var SPEECH = window.TC_CHAT_SPEECH || {};
  var LANG_PATH = (L === 'ar') ? '/' : '/' + L + '/';
  var lp = function (s) { return s.replace(/\{L\}/g, LANG_PATH); };

  /* ---------- helpers ---------- */
  function el(tag, cls, html) {
    var e = document.createElement(tag);
    if (cls) { e.className = cls; }
    if (html !== undefined) { e.innerHTML = html; }
    return e;
  }
  function esc(s) {
    return String(s).replace(/[&<>"']/g, function (c) {
      return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c];
    });
  }
  function normalize(s) {
    return String(s || '').toLowerCase()
      .replace(/[\u064B-\u065F\u0670\u06D6-\u06ED]/g, '') /* Arabic diacritics */
      .replace(/[\u0622\u0623\u0625]/g, '\u0627') /* alef variants -> alef */
      .replace(/\u0649/g, '\u064A') /* alef maqsura -> ya */
      .replace(/\u0629/g, '\u0647') /* ta marbuta -> ha */
      .replace(/[äâà]/g, 'a').replace(/[éèêë]/g, 'e').replace(/[íïî]/g, 'i')
      .replace(/[óôö]/g, 'o').replace(/[úüû]/g, 'u').replace(/ç/g, 'c')
      .replace(/\s+/g, ' ').trim();
  }

  /* ---------- state ---------- */
  var opened = false;
  var voiceOn = false; /* speak replies */
  var wiz = null; /* wizard state object or null */

  /* ---------- DOM ---------- */
  var fab = el('button', 'cb-fab');
  fab.type = 'button';
  fab.setAttribute('aria-label', S.open);
  fab.innerHTML = '<span class="cb-fab-dot" aria-hidden="true"></span>' +
    '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg>';

  var panel = el('div', 'cb-panel');
  panel.setAttribute('role', 'dialog');
  panel.setAttribute('aria-label', S.name);
  panel.dir = (L === 'ar') ? 'rtl' : 'ltr';
  panel.innerHTML =
    '<div class="cb-head">' +
      '<div class="cb-avatar" aria-hidden="true">TC</div>' +
      '<div class="cb-id"><b>' + esc(S.name) + '</b><span class="cb-status"><span class="cb-on" aria-hidden="true"></span>' + esc(S.status) + '</span></div>' +
      '<button class="cb-speak" type="button" aria-label="' + esc(S.speak_on) + '" title="' + esc(S.speak_on) + '" aria-pressed="false">' +
        '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M15.54 8.46a5 5 0 0 1 0 7.07"/><path d="M19.07 4.93a10 10 0 0 1 0 14.14"/></svg>' +
      '</button>' +
      '<button class="cb-close" type="button" aria-label="' + esc(S.close) + '">' +
        '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>' +
      '</button>' +
    '</div>' +
    '<div class="cb-msgs" id="cb-msgs" aria-live="polite"></div>' +
    '<div class="cb-chips" id="cb-chips"></div>' +
    '<div class="cb-input">' +
      '<input class="cb-text" type="text" placeholder="' + esc(S.placeholder) + '" maxlength="500" aria-label="' + esc(S.placeholder) + '">' +
      '<button class="cb-mic" type="button" aria-label="' + esc(S.mic) + '" title="' + esc(S.mic) + '">' +
        '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 1a3 3 0 0 0-3 3v8a3 3 0 0 0 6 0V4a3 3 0 0 0-3-3z"/><path d="M19 10v2a7 7 0 0 1-14 0v-2"/><line x1="12" y1="19" x2="12" y2="23"/></svg>' +
      '</button>' +
      '<button class="cb-send" type="button" aria-label="' + esc(S.send) + '">' +
        '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><line x1="22" y1="2" x2="11" y2="13"/><polygon points="22 2 15 22 11 13 2 9 22 2"/></svg>' +
      '</button>' +
    '</div>' +
    '<p class="cb-privacy">' + esc(S.privacy) + '</p>';
  document.body.appendChild(fab);
  document.body.appendChild(panel);

  var msgs = panel.querySelector('.cb-msgs');
  var chips = panel.querySelector('.cb-chips');
  var input = panel.querySelector('.cb-text');
  var micBtn = panel.querySelector('.cb-mic');
  var sendBtn = panel.querySelector('.cb-send');
  var speakBtn = panel.querySelector('.cb-speak');
  var closeBtn = panel.querySelector('.cb-close');

  /* ---------- messages ---------- */
  function addMsg(html, who, speak) {
    var m = el('div', 'cb-msg ' + who);
    m.innerHTML = '<div class="cb-bubble">' + html + '</div>';
    msgs.appendChild(m);
    msgs.scrollTop = msgs.scrollHeight;
    if (who === 'bot' && voiceOn && speak) { speakText(speak); }
    return m;
  }
  function speakText(text) {
    try {
      if (!('speechSynthesis' in window)) { return; }
      var plain = String(text).replace(/<[^>]+>/g, ' ').replace(/\s+/g, ' ').trim();
      if (!plain) { return; }
      var u = new SpeechSynthesisUtterance(plain);
      u.lang = SPEECH[L] || L;
      var v = window.speechSynthesis.getVoices().filter(function (x) {
        return x.lang && x.lang.toLowerCase().indexOf((SPEECH[L] || L).split('-')[0]) === 0;
      });
      if (v.length) { u.voice = v[0]; }
      window.speechSynthesis.cancel();
      window.speechSynthesis.speak(u);
    } catch (e) {}
  }
  function setChips(list) {
    chips.innerHTML = '';
    (list || S.quick).forEach(function (q) {
      var b = el('button', 'cb-chip', esc(q[0]));
      b.type = 'button';
      b.addEventListener('click', function () {
        if (q[1] === 'book') { startWizard(); }
        else { addMsg(esc(q[0]), 'user'); answer(q[1]); }
      });
      chips.appendChild(b);
    });
  }

  /* ---------- intents (deterministic, whitelisted links only) ---------- */
  var INTENT_ORDER = ['book', 'pricing', 'certs', 'projects', 'expertise', 'experience',
    'education', 'avail', 'contact', 'services', 'thanks', 'greet'];
  var ANSWER = {
    services: 'a_services', certs: 'a_certs', projects: 'a_projects',
    expertise: 'a_expertise', experience: 'a_experience', education: 'a_education',
    pricing: 'a_pricing', avail: 'a_avail', contact: 'a_contact',
    greet: 'a_greet', thanks: 'a_thanks',
  };
  function matchIntent(text) {
    var t = normalize(text);
    if (!t) { return null; }
    for (var i = 0; i < INTENT_ORDER.length; i++) {
      var kws = (S.kw && S.kw[INTENT_ORDER[i]]) || [];
      for (var j = 0; j < kws.length; j++) {
        if (t.indexOf(normalize(kws[j])) !== -1) { return INTENT_ORDER[i]; }
      }
    }
    return null;
  }
  function answer(intent, rawText) {
    if (intent === 'book') { startWizard(); return; }
    var key = ANSWER[intent] || 'a_fallback';
    var html = lp(S[key]);
    addMsg(html, 'bot', S[key]);
    if (key === 'a_fallback') { setChips(); }
  }
  function handleUserText(text) {
    addMsg(esc(text), 'user');
    if (wiz) { wizStep(text); return; }
    var intent = matchIntent(text);
    if (intent) { answer(intent, text); }
    else { answer(null, text); }
  }

  /* ---------- input events ---------- */
  sendBtn.addEventListener('click', function () {
    var v = input.value.trim();
    if (!v) { return; }
    input.value = '';
    handleUserText(v);
  });
  input.addEventListener('keydown', function (e) {
    if (e.key === 'Enter') { sendBtn.click(); }
  });

  /* ---------- voice input ---------- */
  var SR = window.SpeechRecognition || window.webkitSpeechRecognition;
  var rec = null;
  if (SR) {
    rec = new SR();
    rec.lang = SPEECH[L] || L;
    rec.interimResults = false;
    rec.maxAlternatives = 1;
    rec.onresult = function (e) {
      var t = e.results[0][0].transcript;
      if (t) { handleUserText(t); }
    };
    rec.onstart = function () {
      micBtn.classList.add('listening');
      input.placeholder = S.listening;
    };
    rec.onend = function () {
      micBtn.classList.remove('listening');
      input.placeholder = S.placeholder;
    };
    micBtn.addEventListener('click', function () {
      try { rec.start(); } catch (e) {}
    });
  } else {
    micBtn.addEventListener('click', function () {
      addMsg(esc(S.mic_off), 'bot');
    });
    micBtn.classList.add('cb-off');
  }

  /* ---------- voice output toggle ---------- */
  speakBtn.addEventListener('click', function () {
    voiceOn = !voiceOn;
    speakBtn.setAttribute('aria-pressed', voiceOn ? 'true' : 'false');
    speakBtn.setAttribute('aria-label', voiceOn ? S.speak_off : S.speak_on);
    speakBtn.title = voiceOn ? S.speak_off : S.speak_on;
    speakBtn.classList.toggle('active', voiceOn);
    if (!voiceOn) { try { window.speechSynthesis.cancel(); } catch (e) {} }
  });

  /* ---------- open / close ---------- */
  function openChat(withWizard) {
    opened = true;
    panel.classList.add('open');
    fab.classList.add('open');
    fab.setAttribute('aria-label', S.close);
    if (!msgs.childElementCount) {
      addMsg(lp(S.welcome), 'bot', S.welcome);
      setChips();
    }
    if (withWizard) { startWizard(); }
    setTimeout(function () { input.focus(); }, 60);
  }
  function closeChat() {
    opened = false;
    panel.classList.remove('open');
    fab.classList.remove('open');
    fab.setAttribute('aria-label', S.open);
    try { window.speechSynthesis.cancel(); } catch (e) {}
  }
  fab.addEventListener('click', function () { opened ? closeChat() : openChat(false); });
  closeBtn.addEventListener('click', closeChat);
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape' && opened) { closeChat(); }
  });
  document.querySelectorAll('[data-chat-open]').forEach(function (b) {
    b.addEventListener('click', function (e) {
      e.preventDefault();
      openChat(b.hasAttribute('data-chat-wizard'));
    });
  });

  /* ---------- booking / inquiry / consultation wizard ---------- */
  function startWizard() {
    wiz = { step: 'type', data: { type: '', name: '', contact: '', details: '', when: '' } };
    var m = el('div', 'cb-msg bot');
    m.innerHTML = '<div class="cb-bubble"><b>' + esc(S.wiz_title) + '</b><br>' + esc(S.wiz_intro) + '<br><span class="cb-q">' + esc(S.wiz_type_q) + '</span></div>';
    msgs.appendChild(m);
    msgs.scrollTop = msgs.scrollHeight;
    var w = el('div', 'cb-wiz');
    [['inq', S.wiz_inquiry], ['con', S.wiz_consult], ['book', S.wiz_book]].forEach(function (o) {
      var b = el('button', 'cb-chip', esc(o[1]));
      b.type = 'button';
      b.addEventListener('click', function () {
        addMsg(esc(o[1]), 'user');
        wiz.data.type = o[0];
        wiz.step = 'name';
        ask(S.wiz_name_q);
      });
      w.appendChild(b);
    });
    var cancel = el('button', 'cb-chip cb-chip-ghost', esc(S.wiz_cancel));
    cancel.type = 'button';
    cancel.addEventListener('click', function () {
      addMsg(esc(S.wiz_cancel), 'user');
      wiz = null;
      answer('greet');
    });
    w.appendChild(cancel);
    msgs.appendChild(w);
    msgs.scrollTop = msgs.scrollHeight;
  }
  function ask(q, ph) {
    input.value = '';
    input.placeholder = ph || q;
    input.focus();
    addMsg('<span class="cb-q">' + esc(q) + '</span>', 'bot', q);
  }
  function wizStep(text) {
    var d = wiz.data;
    if (wiz.step === 'name') {
      d.name = text;
      wiz.step = 'contact';
      ask(S.wiz_contact_q);
    } else if (wiz.step === 'contact') {
      d.contact = text;
      if (d.type === 'book') {
        wiz.step = 'details';
        ask(S.wiz_details_con);
      } else if (d.type === 'con') {
        wiz.step = 'details';
        ask(S.wiz_details_con);
      } else {
        wiz.step = 'details';
        ask(S.wiz_details_inq);
      }
    } else if (wiz.step === 'details') {
      d.details = text;
      if (d.type === 'book') {
        wiz.step = 'when';
        ask(S.wiz_when_q);
      } else { wiz.step = 'confirm'; showSummary(); }
    } else if (wiz.step === 'when') {
      d.when = text;
      wiz.step = 'confirm';
      showSummary();
    }
  }
  function typeLabel(t) {
    return t === 'inq' ? S.wiz_inquiry : (t === 'con' ? S.wiz_consult : S.wiz_book);
  }
  function showSummary() {
    var d = wiz.data;
    var rows = [
      [S.wiz_type_q, typeLabel(d.type)],
      [S.wiz_name_q, d.name],
      [S.wiz_contact_q, d.contact],
      [d.type === 'inq' ? S.wiz_details_inq : S.wiz_details_con, d.details],
    ];
    if (d.type === 'book') { rows.push([S.wiz_when_q, d.when]); }
    var html = '<div class="cb-summary"><b>' + esc(S.wiz_title) + '</b>' +
      rows.map(function (r) { return '<div><span>' + esc(r[0]) + '</span><b>' + esc(r[1]) + '</b></div>'; }).join('') +
      '</div>';
    var m = addMsg(html, 'bot');
    var w = el('div', 'cb-wiz');
    var ok = el('button', 'cb-chip cb-chip-go', esc(S.wiz_confirm));
    ok.type = 'button';
    ok.addEventListener('click', sendToTelegram);
    var cancel = el('button', 'cb-chip cb-chip-ghost', esc(S.wiz_cancel));
    cancel.type = 'button';
    cancel.addEventListener('click', function () {
      wiz = null;
      input.placeholder = S.placeholder;
      answer('greet');
    });
    w.appendChild(ok); w.appendChild(cancel);
    m.appendChild(w);
    msgs.scrollTop = msgs.scrollHeight;
  }
  function sendToTelegram() {
    if (!wiz || !TG) { return; }
    var d = wiz.data;
    addMsg('<span class="cb-q">' + esc(S.wiz_sending) + '</span>', 'bot');
    var langName = { ar: 'العربية', en: 'English', fr: 'Français', es: 'Español', it: 'Italiano', de: 'Deutsch', nl: 'Nederlands', pt: 'Português' }[L] || L;
    var lines = [
      '🟢 <b>طلب جديد من الموقع</b> (New website request)',
      '🌐 ' + esc(langName) + ' · ' + location.hostname + location.pathname,
      '📌 <b>النوع / Type:</b> ' + esc(typeLabel(d.type)),
      '👤 <b>الاسم / Name:</b> ' + esc(d.name),
      '📞 <b>التواصل / Contact:</b> ' + esc(d.contact),
      '📝 <b>التفاصيل / Details:</b> ' + esc(d.details),
    ];
    if (d.type === 'book') { lines.push('🗓 <b>الموعد المقترح / Preferred time:</b> ' + esc(d.when)); }
    lines.push('— via Tarik Chouika website assistant');
    fetch('https://api.telegram.org/bot' + TG.token + '/sendMessage', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        chat_id: TG.chat_id,
        text: lines.join('\n'),
        disable_web_page_preview: true,
      }),
    }).then(function (r) { return r.json(); }).then(function (j) {
      wiz = null;
      input.placeholder = S.placeholder;
      setChips();
      if (j && j.ok) { addMsg(lp(S.wiz_sent), 'bot', S.wiz_sent); }
      else { addMsg(lp(S.wiz_fail), 'bot'); }
    }).catch(function () {
      wiz = null;
      input.placeholder = S.placeholder;
      setChips();
      addMsg(lp(S.wiz_fail), 'bot');
    });
  }
})();
