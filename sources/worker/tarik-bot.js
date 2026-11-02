/**
 * tarik-bot — Telegram backend for Tarik Chouika (tarikchouika.pages.dev)
 * ---------------------------------------------------------------------
 * Endpoints:
 *   POST /webhook  — Telegram updates (verified via X-Telegram-Bot-Api-Secret-Token)
 *                    · /start /help /id /links commands (ar / fr / en)
 *                    · owner messages  → live acknowledgement
 *                    · visitor messages → forwarded to the owner + friendly ack
 *   POST /notify   — website chatbot gateway (CORS-restricted to the site,
 *                    validated, length-capped, rate-limited). The bot token
 *                    stays server-side — it is no longer exposed in client JS.
 *   GET  /healthz  — liveness probe.
 */

const BOT_TOKEN = "PUT-YOUR-BOT-TOKEN-HERE"; // set the real token when deploying (kept out of the public repo)
const API = 'https://api.telegram.org/bot' + BOT_TOKEN;
const OWNER_ID = 5700612979;
const WEBHOOK_SECRET = "PUT-YOUR-WEBHOOK-SECRET-HERE";
const SITE = 'https://tarikchouika.pages.dev';
const WA = 'https://wa.me/212766672027';
const MAIL = 'mailto:tarikchouika@gmail.com';
const LI = 'https://www.linkedin.com/in/tarik-chouika-588863140';

const SITE_ORIGIN_RE = /^https:\/\/([a-z0-9-]+\.)?tarikchouika\.pages\.dev$/;

/* ---------------- i18n (ar / fr / en — Morocco + international) ---------------- */
const T = {
  ar: {
    welcome: 'أهلاً {name} 👋\nأنا البوت الرسمي لطارق شويكة — محترف في التشغيل وخدمة العملاء، ومطوّر مواقع ومنصات رقمية.\n\n✍️ اكتب رسالتك الآن وستصل إلى طارق مباشرة على هاتفه.\nأو استعمل الأزرار بالأسفل للوصول السريع.',
    help: 'كيف أعمل؟\n\n• اكتب أي رسالة — تصل إلى طارق فوراً وهو من يردّ عليك بنفسه.\n• طلبات الموقع (استشارة / استفسار / حجز موعد) تصلني أيضاً وأحيلها إليه مباشرة.\n\nالأوامر المتاحة:\n/start — بدء المحادثة\n/links — الروابط المهمة\n/id — معرّف المحادثة',
    owner: 'وصلتني رسالتك يا طارق ✅\nالبوت يعمل الآن بكامل قدرته: أستقبل رسائل الزوار وطلبات الموقع (استشارة / استفسار / حجز موعد) وأوصلها إليك هنا فوراً.\n\nالأوامر: /help · /links · /id',
    ack: 'شكراً {name} 🙏\nوصلت رسالتك إلى طارق وسيجيبك قريباً.\nللتواصل الفوري: واتساب أو الموقع من الأزرار بالأسفل.',
    links: 'الروابط المهمة:\n\n🌐 الموقع الرسمي: tarikchouika.pages.dev\n💬 واتساب: +212 766 672 027\n✉️ البريد: tarikchouika@gmail.com\n💼 لينكدإن: Tarik Chouika',
    idtxt: 'معرّف هذه المحادثة (Chat ID): {id}',
    unknown: 'لم أفهم هذا الأمر 🤔\nاكتب /help لعرض ما يمكنني فعله، أو أرسل رسالتك مباشرة — ستصل إلى طارق.',
    fwdLabel: 'رسالة جديدة من زائر البوت',
    reqLabel: 'طلب جديد من الموقع',
    site: '🌐 الموقع',
    wa: '💬 واتساب',
    mail: '✉️ البريد',
  },
  fr: {
    welcome: 'Bonjour {name} 👋\nJe suis le bot officiel de Tarik Chouika — professionnel des opérations et du service client, développeur de sites et de plateformes numériques.\n\n✍️ Écrivez votre message : il arrive directement sur le téléphone de Tarik.\nOu utilisez les boutons ci-dessous pour un accès rapide.',
    help: 'Comment ça marche ?\n\n• Écrivez n\'importe quel message — il parvient immédiatement à Tarik, qui vous répond lui-même.\n• Les demandes du site (conseil / question / rendez-vous) m\'arrivent aussi et je les transmets directement.\n\nCommandes :\n/start — démarrer la discussion\n/links — liens utiles\n/id — identifiant de la conversation',
    owner: 'Message bien reçu, Tarik ✅\nLe bot est pleinement opérationnel : je reçois les messages des visiteurs et les demandes du site (conseil / question / rendez-vous) et je te les transmets ici immédiatement.\n\nCommandes : /help · /links · /id',
    ack: 'Merci {name} 🙏\nVotre message est arrivé à Tarik, il vous répondra bientôt.\nPour un contact immédiat : WhatsApp ou le site via les boutons ci-dessous.',
    links: 'Liens utiles :\n\n🌐 Site officiel : tarikchouika.pages.dev\n💬 WhatsApp : +212 766 672 027\n✉️ E-mail : tarikchouika@gmail.com\n💼 LinkedIn : Tarik Chouika',
    idtxt: 'Identifiant de cette conversation (Chat ID) : {id}',
    unknown: 'Je n\'ai pas compris cette commande 🤔\nÉcrivez /help pour voir ce que je peux faire, ou envoyez directement votre message — il parviendra à Tarik.',
    fwdLabel: 'Nouveau message d\'un visiteur du bot',
    reqLabel: 'Nouvelle demande du site web',
    site: '🌐 Site web',
    wa: '💬 WhatsApp',
    mail: '✉️ E-mail',
  },
  en: {
    welcome: 'Hello {name} 👋\nI am the official bot of Tarik Chouika — operations and customer-service professional, builder of websites and digital platforms.\n\n✍️ Write your message now and it will reach Tarik directly on his phone.\nOr use the buttons below for quick access.',
    help: 'How I work:\n\n• Write any message — it reaches Tarik instantly, and he replies to you personally.\n• Website requests (consultation / inquiry / booking) also arrive here and are forwarded to him right away.\n\nCommands:\n/start — start the chat\n/links — useful links\n/id — this chat\'s ID',
    owner: 'Message received, Tarik ✅\nThe bot is now fully operational: I receive visitors\' messages and website requests (consultation / inquiry / booking) and deliver them to you here instantly.\n\nCommands: /help · /links · /id',
    ack: 'Thank you {name} 🙏\nYour message has reached Tarik and he will reply soon.\nFor immediate contact: WhatsApp or the website via the buttons below.',
    links: 'Useful links:\n\n🌐 Official website: tarikchouika.pages.dev\n💬 WhatsApp: +212 766 672 027\n✉️ Email: tarikchouika@gmail.com\n💼 LinkedIn: Tarik Chouika',
    idtxt: 'This conversation\'s Chat ID: {id}',
    unknown: 'I did not understand that command 🤔\nType /help to see what I can do, or just send your message — it will reach Tarik.',
    fwdLabel: 'New message from a bot visitor',
    reqLabel: 'New website request',
    site: '🌐 Website',
    wa: '💬 WhatsApp',
    mail: '✉️ Email',
  },
};

const LANG_NAMES = {
  ar: 'العربية', en: 'English', fr: 'Français', es: 'Español',
  it: 'Italiano', de: 'Deutsch', nl: 'Nederlands', pt: 'Português',
};
const TYPE_LABELS = {
  ar: { inq: 'استفسار', con: 'استشارة', book: 'حجز موعد' },
  fr: { inq: 'Demande d’information', con: 'Consultation', book: 'Rendez-vous' },
  en: { inq: 'Inquiry', con: 'Consultation', book: 'Booking' },
};

/* ---------------- helpers ---------------- */
function esc(s) {
  return String(s == null ? '' : s)
    .replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
}
function json(obj, status, origin) {
  const h = { 'Content-Type': 'application/json; charset=utf-8' };
  if (origin && SITE_ORIGIN_RE.test(origin)) {
    h['Access-Control-Allow-Origin'] = origin;
    h['Vary'] = 'Origin';
  }
  return new Response(JSON.stringify(obj), { status: status || 200, headers: h });
}
async function tg(method, body) {
  try {
    const r = await fetch(API + '/' + method, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(body),
    });
    return await r.json();
  } catch (e) {
    return { ok: false, error: String(e) };
  }
}
async function send(chatId, text, buttons) {
  const body = { chat_id: chatId, text: text };
  if (buttons) { body.reply_markup = { inline_keyboard: buttons }; }
  return tg('sendMessage', body);
}
function mainButtons(L) {
  return [[
    { text: T[L].site, url: SITE },
    { text: T[L].wa, url: WA },
  ], [
    { text: T[L].mail, url: MAIL },
  ]];
}
function pickLang(from, text) {
  if (/[\u0600-\u06FF]/.test(text || '')) { return 'ar'; }
  const lc = String((from && from.language_code) || '').slice(0, 2).toLowerCase();
  if (lc === 'ar') { return 'ar'; }
  if (lc === 'fr') { return 'fr'; }
  return 'en';
}

/* ---------------- simple per-isolate rate limiter ---------------- */
const hits = new Map();
function rateLimited(ip) {
  const now = Date.now();
  const WINDOW = 10 * 60 * 1000;
  const MAX = 5;
  let arr = (hits.get(ip) || []).filter((t) => now - t < WINDOW);
  if (arr.length >= MAX) { hits.set(ip, arr); return true; }
  arr.push(now);
  hits.set(ip, arr);
  if (hits.size > 5000) {
    for (const [k, v] of hits) {
      if (!v.some((t) => now - t < WINDOW)) { hits.delete(k); }
    }
  }
  return false;
}

/* ---------------- webhook ---------------- */
async function handleWebhook(request) {
  if (request.headers.get('X-Telegram-Bot-Api-Secret-Token') !== WEBHOOK_SECRET) {
    return new Response('unauthorized', { status: 401 });
  }
  let update;
  try { update = await request.json(); } catch (e) { return new Response('ok'); }
  try {
    const m = update.message;
    if (m && m.text) {
      const from = m.from || {};
      const isOwner = String(from.id) === String(OWNER_ID);
      const L = pickLang(from, m.text);
      const text = String(m.text).trim();
      const cmd = text.split(/[\s@]+/)[0].toLowerCase();

      if (cmd === '/start') {
        await send(m.chat.id, T[L].welcome.replace('{name}', from.first_name || ''), mainButtons(L));
      } else if (cmd === '/help' || cmd === '/aide') {
        await send(m.chat.id, T[L].help);
      } else if (cmd === '/id') {
        await send(m.chat.id, T[L].idtxt.replace('{id}', String(m.chat.id)));
      } else if (cmd === '/links') {
        await send(m.chat.id, T[L].links, mainButtons(L));
      } else if (cmd.indexOf('/') === 0) {
        await send(m.chat.id, T[L].unknown);
      } else if (isOwner) {
        await send(m.chat.id, T[L].owner);
      } else {
        const head =
          '📨 <b>' + T[L].fwdLabel + '</b>\n' +
          '👤 <b>' + esc((from.first_name || '') + ' ' + (from.last_name || '')) + '</b>' +
          (from.username ? ' · @' + esc(from.username) : '') +
          ' · <code>' + String(from.id) + '</code>\n\n💬 ' + esc(text);
        await tg('sendMessage', {
          chat_id: OWNER_ID, text: head, parse_mode: 'HTML',
          disable_web_page_preview: true,
        });
        await send(m.chat.id, T[L].ack.replace('{name}', from.first_name || ''), mainButtons(L));
      }
    }
  } catch (e) { /* never fail the webhook — Telegram would retry forever */ }
  return new Response('ok');
}

/* ---------------- website notify gateway ---------------- */
async function handleNotify(request) {
  const origin = request.headers.get('Origin') || '';
  if (!SITE_ORIGIN_RE.test(origin)) {
    return json({ ok: false, error: 'origin_not_allowed' }, 403, origin);
  }
  let b;
  try { b = await request.json(); } catch (e) { return json({ ok: false, error: 'bad_json' }, 400, origin); }

  const v = (x, n) => String(x == null ? '' : x).trim().slice(0, n);
  const type = v(b.type, 8);
  const name = v(b.name, 80);
  const contact = v(b.contact, 120);
  const details = v(b.details, 1500);
  const when = v(b.when, 120);
  const lang = v(b.lang, 2).toLowerCase();
  const page = v(b.page, 200);

  if (type !== 'inq' && type !== 'con' && type !== 'book') {
    return json({ ok: false, error: 'invalid_type' }, 422, origin);
  }
  if (!name || !contact || !details) {
    return json({ ok: false, error: 'missing_fields' }, 422, origin);
  }
  const ip = request.headers.get('CF-Connecting-IP') || 'unknown';
  if (rateLimited(ip)) {
    return json({ ok: false, error: 'rate_limited' }, 429, origin);
  }

  const L = T[lang] ? lang : 'en';
  const lines = [
    '🟢 <b>' + T[L].reqLabel + '</b>',
    '🌐 ' + esc(LANG_NAMES[lang] || lang) + ' · ' + esc(page),
    '📌 <b>' + (L === 'ar' ? 'النوع' : L === 'fr' ? 'Type' : 'Type') + ':</b> ' + TYPE_LABELS[L][type],
    '👤 <b>' + (L === 'ar' ? 'الاسم' : L === 'fr' ? 'Nom' : 'Name') + ':</b> ' + esc(name),
    '📞 <b>' + (L === 'ar' ? 'التواصل' : L === 'fr' ? 'Contact' : 'Contact') + ':</b> ' + esc(contact),
    '📝 <b>' + (L === 'ar' ? 'التفاصيل' : L === 'fr' ? 'Détails' : 'Details') + ':</b> ' + esc(details),
  ];
  if (type === 'book' && when) {
    lines.push('🗓 <b>' + (L === 'ar' ? 'الموعد المقترح' : L === 'fr' ? 'Rendez-vous souhaité' : 'Preferred time') + ':</b> ' + esc(when));
  }
  lines.push('— ' + (L === 'ar' ? 'مساعد موقع طارق شويكة' : L === 'fr' ? 'Assistant du site de Tarik Chouika' : 'Tarik Chouika website assistant'));

  const r = await tg('sendMessage', {
    chat_id: OWNER_ID,
    text: lines.join('\n'),
    parse_mode: 'HTML',
    disable_web_page_preview: true,
  });
  if (r && r.ok) { return json({ ok: true }, 200, origin); }
  return json({ ok: false, error: 'send_failed' }, 502, origin);
}

/* ---------------- router ---------------- */
export default {
  async fetch(request) {
    const url = new URL(request.url);

    if (request.method === 'OPTIONS' && url.pathname === '/notify') {
      const origin = request.headers.get('Origin') || '';
      const h = {
        'Access-Control-Allow-Methods': 'POST, OPTIONS',
        'Access-Control-Allow-Headers': 'Content-Type',
        'Access-Control-Max-Age': '86400',
        'Vary': 'Origin',
      };
      if (SITE_ORIGIN_RE.test(origin)) { h['Access-Control-Allow-Origin'] = origin; }
      return new Response(null, { status: 204, headers: h });
    }
    if (request.method === 'POST' && url.pathname === '/notify') { return handleNotify(request); }
    if (request.method === 'POST' && url.pathname === '/webhook') { return handleWebhook(request); }
    if (request.method === 'GET' && (url.pathname === '/healthz' || url.pathname === '/')) {
      return new Response(JSON.stringify({ ok: true, bot: 'tarikchouika_bot', service: 'tarik-bot' }),
        { status: 200, headers: { 'Content-Type': 'application/json; charset=utf-8' } });
    }
    return new Response('Not found', { status: 404 });
  },
};
