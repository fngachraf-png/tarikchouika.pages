#!/usr/bin/env python3
"""Build CMDP project pages (8 languages) from epdp skeletons, add homepage
cards, fix pagers, update project counts, and extend the sitemap."""
import os, re, sys

sys.path.insert(0, '/home/z/my-project/scripts')
from inject_shots import UI  # reuse gallery UI translations

SITE = '/home/z/my-project/site'

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

C = {}  # CMDP content per language

C['ar'] = dict(
 meta='منصة CMDP الرقمية لإدارة التعاونيات المغربية: لوحة قيادة، الأعضاء والحصص، الجمع العام، المالية، سجل الوثائق، والامتثال للقانون 112.12 — بتصميم مغربي عصري.',
 field='منصة رقمية لإدارة التعاونيات',
 lead='منصة مغربية شاملة ترقمن تدبير التعاونيات: الأعضاء والجمعات العامة والمجالس والمالية والوثائق — مع تتبّع الجهات الوصية والامتثال للقانون 112.12، بروح زليجية مغربية عصرية.',
 about='CMDP منصة رقمية لإدارة التعاونيات بالمغرب صُممت حول الواقع اليومي للتعاونية: ثماني وحدات مترابطة تغطي لوحة القيادة بمؤشرات ورسوم فورية، وبطاقات التعاونيات مع التسجيل بالسجل المحلي وبطاقة ODCO، وسجل المنخرطين والحصص والمناصب، والجمعات العامة ومحاضرها واجتماعات المجلس، والمداخيل والمصاريف والتقارير المالية الجاهزة، وسجل وثائق مؤرشف زمنياً مع تنبيهات انتهاء الصلاحية، وتتبّع التفاعلات مع ODCO والضرائب وCNSS، ومكتبة قانونية تجمع القانون 112.12 والمراسيم والمبادئ — كل ذلك بواجهة عربية RTL وتصميم مغربي عصري بروح الزليج والقوس المغربي.',
 value_lead='CMDP يحوّل تدبير التعاونية من أوراق متفرقة إلى نظام واحد واضح:',
 values=[('لوحة قيادة بصيرة واحدة', 'مؤشرات ورسوم بيانية فورية تعرض سلامة التعاونية: مداخيل الموسم، مواعيد الجمع العام، وتنبيهات الوثائق — في نظرة واحدة.'),
   ('امتثال قانوني مدموج', 'المكتبة القانونية تضم القانون 112.12 والمراسيم والمبادئ، وتربط كل إجراء بمادته — فتبقى التعاونية دائماً في الجانب الصحيح من القانون.'),
   ('علاقة منضبطة مع الجهات الوصية', 'تتبّع التفاعلات مع ODCO والضرائب وCNSS في سجل واحد: ماذا قُدّم، ومتى، وما تبقّى — بلا مواعيد ضائعة.'),
   ('ذاكرة وثائق لا تنسى', 'سجل مؤرشف زمنياً لكل الوثائق مع تنبيهات انتهاء الصلاحية — انتهاء التسجيل أو التجديد لا يفاجئك أبداً.')],
 effort='التحدي الأكبر كان ترجمة النصوص القانونية الجافة إلى تجربة استخدام واضحة: بنيت ثماني وحدات مترابطة بمنطق السنة التعاونية — من التأسيس إلى الجمع العام السنوي — وحرصت على أن تعمل كل وحدة وحدها ومع الأخريات. كما ضبطت الأرقام الوطنية المرجعية (65,315 تعاونية نشيطة، أزيد من 788,000 منخرط، 34% نساء، 40,033 تعاونية فلاحية) لتضع تدبير كل تعاونية في صورتها الوطنية الحقيقية.',
 stats=[('الوحدات المترابطة', '8 وحدات'), ('الإطار القانوني', 'قانون 112.12'), ('لغة الواجهة', 'عربية RTL بالكامل')],
 chips_build=['واجهة ساكنة (Cloudflare Pages)', 'قاعدة بيانات محلية (SQLite)', 'تصميم مغربي عصري (زليج وقوس)', 'رسوم بيانية للوحة القيادة', 'تنبيهات انتهاء الصلاحية', 'واجهة عربية RTL أصيلة', 'بنية 8 وحدات مترابطة'],
 chips_ops=['Cloudflare Pages للتشغيل والنشر', 'قاعدة بيانات محلية خفيفة (SQLite)', 'تصميم متجاوب مع كل الشاشات', 'مؤشرات ورسوم فورية للوحة القيادة', 'مكتبة قانونية قابلة للتوسيع'],
 tools=[('الواجهة الساكنة', 'صفحات خفيفة تُقدَّم من شبكة Cloudflare العالمية: فتح سريع في المغرب وخارجه، وتحديث فوري مع كل نسخة جديدة — دون خوادم باهظة.'),
   ('قاعدة البيانات المحلية (SQLite)', 'محرّك بيانات صغير يعمل دون خادم: يخزّن التعاونيات والأعضاء والعمليات في ملف واحد — مثالي لحساسية بيانات التعاونيات.'),
   ('التصميم المغربي العصري', 'روح الزليج والقوس المغربي في واجهة رقمية: هوية بصرية محلية بلغة عصرية تميّز المنصة عن القوالب الجاهزة.'),
   ('لوحة القيادة والرسوم البيانية', 'مؤشرات فورية ورسوم تُظهر مداخيل الموسم ونسبة النمو وموعد الجمع العام — القرار مبني على رقم لا على انطباع.'),
   ('بنية الوحدات الثماني', 'كل وظيفة (الأعضاء، المالية، الوثائق...) وحدة مستقلة تعمل وحدها وتتكامل مع البقية — التطوير يتقدم دون كسر الكل.'),
   ('مكتبة القانون 112.12', 'النصوص القانونية والمراسيم منظمة ومرتبطة بالإجراءات — من التأسيس بخمسة أعضاء إلى الجمع العام السنوي العادي.'),
   ('تنبيهات انتهاء الصلاحية', 'الوثائق التي تنتهي (تسجيل، تجديد...) تُنبِّه قبل موعدها — التعاونية لا تُفاجأ بورقة منتهية عند الحاجة.'),
   ('الواجهة العربية RTL أصيلة', 'صُممت من اليمين إلى اليسار منذ السطر الأول، لا ترجمة معكوسة — تجربة طبيعية للمستخدم المغربي.')],
 features=['ثماني وحدات مترابطة تغطي دورة حياة التعاونية كاملة', 'لوحة قيادة بمؤشرات ورسوم بيانية فورية', 'سجل المنخرطين والحصص ومناصب المجلس والاشتراكات', 'مالية شاملة: مداخيل ومصاريف وتقارير جاهزة', 'سجل وثائق مؤرشف زمنياً مع تنبيهات انتهاء الصلاحية', 'تتبّع التفاعلات مع ODCO والضرائب وCNSS ومكتبة القانون 112.12'],
 costs=dict(self='0 درهم — بُنيت ضمن منظومة مجانية كاملة.',
   pro='25,000 – 70,000 درهم تقريباً لمنصة إدارة بهذا الحجم والامتثال القانوني.',
   now='0 درهم شهرياً ضمن الباقة المجانية.',
   scale='نطاق خاص (100 – 150 درهم سنوياً)، مع استضافة بيانات محمية عند الانتقال للاستخدام الفعلي متعدد التعاونيات.'),
 learned='علّمتني CMDP أن أنقل «البيروقراطية» من عدو إلى مادة تصميم: القانون 112.12 ليس عقبة بل خريطة وظيفية جاهزة. تعلمت أن أقرأ النص التنظيمي وأستخرج منه تدفقات العمل — من نصاب الجمع العام إلى آجال التجديد — ثم أحوّلها إلى شاشات بسيطة. كما تعمّق فهمي بأن الرقمنة في المغرب تنجح حين تحترم السياق المحلي: لغة، وهوية بصرية، وواقع التعاونيات.',
 tag='رقمنة التعاونيات المغربية',
 card_desc='منصة شاملة لإدارة التعاونيات وفق القانون 112.12: لوحة قيادة، الأعضاء والحصص، الجمع العام، المالية، وسجل الوثائق — مع تتبّع الجهات الوصية (ODCO والضرائب وCNSS) بتصميم مغربي عصري.')

C['en'] = dict(
 meta='CMDP digital platform for Moroccan cooperatives: dashboard, members and shares, general assembly, finances, document registry and Law 112.12 compliance — in a modern Moroccan design.',
 field='Digital platform for cooperative management',
 lead='A comprehensive Moroccan platform that digitizes cooperative governance — members, general assemblies, boards, finances and documents — with supervisory-authority tracking and Law 112.12 compliance, in a modern zellige-inspired design.',
 about='CMDP is a digital platform for managing Moroccan cooperatives, designed around the daily reality of a cooperative: eight interconnected units covering a dashboard with instant indicators and charts, cooperative cards with local-registry registration and the ODCO card, a members-and-shares registry with board positions, general assemblies with minutes and board meetings, income, expenses and ready financial reports, a time-stamped document registry with expiry alerts, tracking of interactions with ODCO, taxes and CNSS, and a legal library gathering Law 112.12, its decrees and principles — all in a fully Arabic RTL interface with a modern Moroccan design rooted in zellige and the Moroccan arch.',
 value_lead='CMDP turns cooperative governance from scattered papers into one clear system:',
 values=[('A dashboard with one clear view', 'Instant indicators and charts show the cooperative\u2019s health: season income, general-assembly dates and document alerts — all at a glance.'),
   ('Compliance built in', 'The legal library holds Law 112.12, its decrees and principles, linking every action to its article — so the cooperative always stays on the right side of the law.'),
   ('Disciplined relations with authorities', 'Track interactions with ODCO, taxes and CNSS in one log: what was filed, when, and what remains — no lost deadlines.'),
   ('A memory that never forgets', 'A time-stamped registry of every document with expiry alerts — a lapsed registration or renewal never takes you by surprise.')],
 effort='The biggest challenge was translating dry legal texts into a clear user experience: I built eight interconnected units following the rhythm of the cooperative year — from founding to the annual general assembly — making sure each unit works alone and with the others. I also set the national reference figures (65,315 active cooperatives, over 788,000 members, 34% women, 40,033 agricultural cooperatives) to place each cooperative\u2019s management within its true national picture.',
 stats=[('Interconnected units', '8 units'), ('Legal framework', 'Law 112.12'), ('Interface language', 'Fully Arabic RTL')],
 chips_build=['Static frontend (Cloudflare Pages)', 'Local database (SQLite)', 'Modern Moroccan design (zellige & arch)', 'Dashboard charts', 'Expiry alerts', 'Native Arabic RTL interface', '8-unit modular structure'],
 chips_ops=['Cloudflare Pages for hosting and deploys', 'Lightweight local database (SQLite)', 'Responsive on every screen', 'Instant dashboard indicators and charts', 'Extensible legal library'],
 tools=[('Static frontend', 'Light pages served from Cloudflare\u2019s global network: fast loading in Morocco and beyond, with instant updates on every new release — no expensive servers.'),
   ('Local SQLite database', 'A tiny serverless data engine that stores cooperatives, members and transactions in a single file — ideal given the sensitivity of cooperative data.'),
   ('Modern Moroccan design', 'The spirit of zellige and the Moroccan arch in a digital interface: a local visual identity in a contemporary language that sets the platform apart from generic templates.'),
   ('Dashboard & charts', 'Instant indicators and charts showing season income, growth rate and assembly dates — decisions based on numbers, not impressions.'),
   ('Eight-unit architecture', 'Every function (members, finance, documents...) is a standalone unit that works alone and integrates with the rest — development moves forward without breaking the whole.'),
   ('Law 112.12 library', 'Legal texts and decrees organized and linked to actions — from founding with five members to the ordinary annual general assembly.'),
   ('Expiry alerts', 'Documents that expire (registration, renewal...) alert you ahead of time — the cooperative is never surprised by an expired paper when it matters.'),
   ('Native Arabic RTL', 'Designed right-to-left from the very first line, not a mirrored translation — a natural experience for the Moroccan user.')],
 features=['Eight interconnected units covering the full cooperative lifecycle', 'Dashboard with instant indicators and charts', 'Registry of members, shares, board positions and subscriptions', 'Complete finances: income, expenses and ready reports', 'Time-stamped document registry with expiry alerts', 'Interaction tracking with ODCO, taxes and CNSS plus the Law 112.12 library'],
 costs=dict(self='0 MAD — built on an entirely free stack.',
   pro='Roughly 25,000–70,000 MAD for a management platform of this scope and legal compliance.',
   now='0 MAD per month on the free tier.',
   scale='A custom domain (100–150 MAD/year), plus secured data hosting when moving to real multi-cooperative use.'),
 learned='CMDP taught me to turn \u201cbureaucracy\u201d from an enemy into design material: Law 112.12 is not an obstacle but a ready-made functional map. I learned to read regulatory text and extract the workflows — from assembly quorum to renewal deadlines — then turn them into simple screens. It also deepened my conviction that digitalization in Morocco succeeds when it respects local context: language, visual identity and the real world of cooperatives.',
 tag='Digitizing Moroccan cooperatives',
 card_desc='A comprehensive platform for managing cooperatives under Law 112.12: dashboard, members & shares, general assembly, finances and a document registry — with supervisory-authority tracking (ODCO, taxes, CNSS) in a modern Moroccan design.')

C['fr'] = dict(
 meta='CMDP, plateforme numérique de gestion des coopératives marocaines : tableau de bord, membres et parts, assemblée générale, finances, registre des documents et conformité à la loi 112.12 — dans un design marocain moderne.',
 field='Plateforme numérique de gestion des coopératives',
 lead='Une plateforme marocaine complète qui numérise la gouvernance des coopératives — membres, assemblées générales, conseils, finances et documents — avec suivi des autorités de tutelle et conformité à la loi 112.12, dans un design moderne inspiré du zellige.',
 about='CMDP est une plateforme numérique de gestion des coopératives au Maroc, conçue autour du quotidien réel d\u2019une coopérative : huit unités interconnectées couvrant un tableau de bord avec indicateurs et graphiques instantanés, les cartes de coopératives avec inscription au registre local et carte ODCO, le registre des adhérents, parts et postes du conseil, les assemblées générales avec leurs procès-verbaux et réunions du conseil, recettes, dépenses et rapports financiers prêts à l\u2019emploi, un registre de documents horodaté avec alertes d\u2019expiration, le suivi des interactions avec l\u2019ODCO, les impôts et la CNSS, et une bibliothèque juridique réunissant la loi 112.12, ses décrets et principes — le tout dans une interface 100 % arabe RTL au design marocain moderne, entre esprit du zellige et arche marocaine.',
 value_lead='CMDP transforme la gouvernance d\u2019une coopérative, de papiers dispersés en un système clair :',
 values=[('Un tableau de bord, une vision nette', 'Des indicateurs et graphiques instantanés montrent la santé de la coopérative : recettes de la saison, dates d\u2019assemblée générale, alertes documentaires — tout d\u2019un coup d\u2019œil.'),
   ('La conformité intégrée', 'La bibliothèque juridique réunit la loi 112.12, ses décrets et principes, et relie chaque démarche à son article — la coopérative reste toujours du bon côté de la loi.'),
   ('Des rapports disciplinés avec les autorités', 'Suivez les interactions avec l\u2019ODCO, les impôts et la CNSS dans un registre unique : ce qui a été déposé, quand, et ce qui reste — plus d\u2019échéances perdues.'),
   ('Une mémoire qui n\u2019oublie pas', 'Un registre horodaté de tous les documents avec alertes d\u2019expiration — une inscription ou un renouvellement lapsé ne vous surprendra jamais.')],
 effort='Le plus grand défi : traduire des textes juridiques arides en une expérience claire. J\u2019ai construit huit unités interconnectées au rythme de l\u2019année coopérative — de la fondation à l\u2019assemblée générale annuelle — en veillant à ce que chacune fonctionne seule et avec les autres. J\u2019ai également intégré les chiffres nationaux de référence (65 315 coopératives actives, plus de 788 000 adhérents, 34 % de femmes, 40 033 coopératives agricoles) pour replacer la gestion de chaque coopérative dans sa vraie image nationale.',
 stats=[('Unités interconnectées', '8 unités'), ('Cadre juridique', 'Loi 112.12'), ('Langue de l\u2019interface', 'Arabe RTL à 100 %')],
 chips_build=['Front-end statique (Cloudflare Pages)', 'Base de données locale (SQLite)', 'Design marocain moderne (zellige et arche)', 'Graphiques du tableau de bord', 'Alertes d\u2019expiration', 'Interface arabe RTL native', 'Structure modulaire en 8 unités'],
 chips_ops=['Cloudflare Pages pour l\u2019hébergement et les déploiements', 'Base locale légère (SQLite)', 'Responsive sur tous les écrans', 'Indicateurs et graphiques instantanés', 'Bibliothèque juridique extensible'],
 tools=[('Front-end statique', 'Des pages légères servies depuis le réseau mondial de Cloudflare : ouverture rapide au Maroc comme ailleurs, mise à jour immédiate à chaque version — sans serveurs coûteux.'),
   ('Base SQLite locale', 'Un petit moteur de données sans serveur qui stocke coopératives, membres et opérations dans un seul fichier — idéal vu la sensibilité des données des coopératives.'),
   ('Design marocain moderne', 'L\u2019esprit du zellige et de l\u2019arche marocaine dans une interface numérique : une identité visuelle locale au langage contemporain, loin des modèles génériques.'),
   ('Tableau de bord et graphiques', 'Indicateurs instantanés et graphiques montrant recettes de la saison, taux de croissance et date d\u2019assemblée — des décisions basées sur le chiffre, pas sur l\u2019impression.'),
   ('Architecture en huit unités', 'Chaque fonction (membres, finances, documents...) est une unité autonome qui fonctionne seule et s\u2019intègre au reste — le développement avance sans tout casser.'),
   ('Bibliothèque de la loi 112.12', 'Textes juridiques et décrets organisés et reliés aux démarches — de la fondation à cinq membres à l\u2019assemblée générale ordinaire annuelle.'),
   ('Alertes d\u2019expiration', 'Les documents qui expirent (inscription, renouvellement...) alertent en amont — la coopérative n\u2019est jamais surprise par un papier périmé au mauvais moment.'),
   ('Arabe RTL natif', 'Conçue de droite à gauche dès la première ligne, pas une traduction inversée — une expérience naturelle pour l\u2019utilisateur marocain.')],
 features=['Huit unités interconnectées couvrant tout le cycle de vie de la coopérative', 'Tableau de bord avec indicateurs et graphiques instantanés', 'Registre des adhérents, parts, postes du conseil et cotisations', 'Finances complètes : recettes, dépenses et rapports prêts à l\u2019emploi', 'Registre de documents horodaté avec alertes d\u2019expiration', 'Suivi des interactions avec l\u2019ODCO, les impôts et la CNSS, et bibliothèque de la loi 112.12'],
 costs=dict(self='0 DH — construite sur une pile entièrement gratuite.',
   pro='Environ 25 000 à 70 000 DH pour une plateforme de gestion de cette ampleur et de cette conformité juridique.',
   now='0 DH par mois dans le cadre de l\u2019offre gratuite.',
   scale='Un domaine propre (100–150 DH/an), plus un hébergement de données sécurisé lors du passage à un usage réel multi-coopératives.'),
 learned='CMDP m\u2019a appris à transformer la « bureaucratie » d\u2019ennemie en matière de conception : la loi 112.12 n\u2019est pas un obstacle mais une carte fonctionnelle prête à l\u2019emploi. J\u2019ai appris à lire un texte réglementaire et à en extraire les flux de travail — du quorum d\u2019assemblée aux échéances de renouvellement — puis à les transformer en écrans simples. J\u2019ai aussi approfondi ma conviction que la numérisation au Maroc réussit quand elle respecte le contexte local : langue, identité visuelle et réalité des coopératives.',
 tag='Numériser les coopératives marocaines',
 card_desc='Une plateforme complète de gestion des coopératives conformément à la loi 112.12 : tableau de bord, membres et parts, assemblée générale, finances et registre des documents — avec suivi des autorités de tutelle (ODCO, impôts, CNSS) dans un design marocain moderne.')

C['es'] = dict(
 meta='CMDP, plataforma digital de gestión de cooperativas marroquíes: panel de control, socios y participaciones, asamblea general, finanzas, registro de documentos y cumplimiento de la ley 112.12 — con un diseño marroquí moderno.',
 field='Plataforma digital de gestión de cooperativas',
 lead='Una plataforma marroquí integral que digitaliza la gobernanza de las cooperativas — socios, asambleas generales, consejos, finanzas y documentos — con seguimiento de las autoridades supervisoras y cumplimiento de la ley 112.12, en un diseño moderno inspirado en el zellige.',
 about='CMDP es una plataforma digital para gestionar cooperativas marroquíes, diseñada en torno a la realidad diaria de una cooperativa: ocho unidades interconectadas que cubren un panel de control con indicadores y gráficos instantáneos, fichas de cooperativas con inscripción en el registro local y tarjeta ODCO, registro de socios, participaciones y cargos del consejo, asambleas generales con actas y reuniones del consejo, ingresos, gastos e informes financieros listos, un registro de documentos sellado en el tiempo con alertas de caducidad, seguimiento de las interacciones con ODCO, impuestos y CNSS, y una biblioteca legal que reúne la ley 112.12, sus decretos y principios — todo en una interfaz 100 % árabe RTL con un diseño marroquí moderno de espíritu zellige y arco marroquí.',
 value_lead='CMDP convierte la gobernanza de una cooperativa, de papeles dispersos a un sistema claro:',
 values=[('Un panel, una visión nítida', 'Indicadores y gráficos instantáneos muestran la salud de la cooperativa: ingresos de la temporada, fechas de asamblea y alertas de documentos — de un solo vistazo.'),
   ('Cumplimiento integrado', 'La biblioteca legal reúne la ley 112.12, sus decretos y principios, y vincula cada trámite con su artículo — la cooperativa siempre queda del lado correcto de la ley.'),
   ('Relación disciplinada con las autoridades', 'Sigue las interacciones con ODCO, impuestos y CNSS en un solo registro: qué se presentó, cuándo y qué falta — sin plazos perdidos.'),
   ('Una memoria que no olvida', 'Un registro sellado en el tiempo de cada documento con alertas de caducidad — un registro o renovación vencida nunca te tomará por sorpresa.')],
 effort='El mayor reto fue traducir textos legales áridos en una experiencia clara: construí ocho unidades interconectadas siguiendo el ritmo del año cooperativo — de la fundación a la asamblea general anual — asegurando que cada unidad funcione sola y con las demás. También fijé las cifras nacionales de referencia (65.315 cooperativas activas, más de 788.000 socios, 34 % mujeres, 40.033 cooperativas agrícolas) para situar la gestión de cada cooperativa en su verdadero panorama nacional.',
 stats=[('Unidades interconectadas', '8 unidades'), ('Marco legal', 'Ley 112.12'), ('Idioma de la interfaz', 'Árabe RTL al 100 %')],
 chips_build=['Front-end estático (Cloudflare Pages)', 'Base de datos local (SQLite)', 'Diseño marroquí moderno (zellige y arco)', 'Gráficos del panel', 'Alertas de caducidad', 'Interfaz árabe RTL nativa', 'Estructura modular de 8 unidades'],
 chips_ops=['Cloudflare Pages para alojamiento y despliegues', 'Base local ligera (SQLite)', 'Responsive en todas las pantallas', 'Indicadores y gráficos instantáneos', 'Biblioteca legal ampliable'],
 tools=[('Front-end estático', 'Páginas ligeras servidas desde la red global de Cloudflare: apertura rápida en Marruecos y fuera, actualización inmediata en cada versión — sin servidores costosos.'),
   ('Base de datos SQLite local', 'Un pequeño motor de datos sin servidor que guarda cooperativas, socios y operaciones en un solo archivo — ideal para la sensibilidad de los datos cooperativos.'),
   ('Diseño marroquí moderno', 'El espíritu del zellige y del arco marroquí en una interfaz digital: identidad visual local con lenguaje contemporáneo que distingue la plataforma de las plantillas genéricas.'),
   ('Panel y gráficos', 'Indicadores instantáneos y gráficos que muestran ingresos de la temporada, tasa de crecimiento y fecha de la asamblea — decisiones basadas en números, no en impresiones.'),
   ('Arquitectura de ocho unidades', 'Cada función (socios, finanzas, documentos...) es una unidad autónoma que funciona sola y se integra con el resto — el desarrollo avanza sin romper el conjunto.'),
   ('Biblioteca de la ley 112.12', 'Textos legales y decretos organizados y vinculados a los trámites — desde la fundación con cinco socios hasta la asamblea general ordinaria anual.'),
   ('Alertas de caducidad', 'Los documentos que caducan (inscripción, renovación...) avisan con antelación — la cooperativa nunca se sorprende con un papel vencido cuando importa.'),
   ('Árabe RTL nativo', 'Diseñada de derecha a izquierda desde la primera línea, no una traducción invertida — una experiencia natural para el usuario marroquí.')],
 features=['Ocho unidades interconectadas que cubren todo el ciclo de vida de la cooperativa', 'Panel de control con indicadores y gráficos instantáneos', 'Registro de socios, participaciones, cargos del consejo y cuotas', 'Finanzas completas: ingresos, gastos e informes listos', 'Registro de documentos sellado en el tiempo con alertas de caducidad', 'Seguimiento de interacciones con ODCO, impuestos y CNSS más la biblioteca de la ley 112.12'],
 costs=dict(self='0 MAD — construida sobre un ecosistema totalmente gratuito.',
   pro='Aprox. 25.000–70.000 MAD por una plataforma de gestión de este alcance y cumplimiento legal.',
   now='0 MAD al mes en el plan gratuito.',
   scale='Dominio propio (100–150 MAD/año) y alojamiento de datos protegido al pasar al uso real multi-cooperativo.'),
 learned='CMDP me enseñó a convertir la «burocracia» de enemiga en material de diseño: la ley 112.12 no es un obstáculo sino un mapa funcional listo para usar. Aprendí a leer el texto normativo y extraer los flujos de trabajo — del quórum de la asamblea a los plazos de renovación — y convertirlos en pantallas simples. También profundicé mi convicción de que la digitalización en Marruecos tiene éxito cuando respeta el contexto local: idioma, identidad visual y realidad de las cooperativas.',
 tag='Digitalizar las cooperativas marroquíes',
 card_desc='Una plataforma integral de gestión de cooperativas conforme a la ley 112.12: panel de control, socios y participaciones, asamblea general, finanzas y registro de documentos — con seguimiento de autoridades (ODCO, impuestos, CNSS) en un diseño marroquí moderno.')

C['it'] = dict(
 meta='CMDP, piattaforma digitale per la gestione delle cooperative marocchine: dashboard, soci e quote, assemblea generale, finanze, registro documenti e conformità alla legge 112.12 — in un design marocchino moderno.',
 field='Piattaforma digitale per la gestione delle cooperative',
 lead='Una piattaforma marocchina completa che digitalizza la governance delle cooperative — soci, assemblee generali, consigli, finanze e documenti — con tracciamento delle autorità di vigilanza e conformità alla legge 112.12, in un design moderno ispirato allo zellige.',
 about='CMDP è una piattaforma digitale per la gestione delle cooperative marocchine, disegnata attorno alla realtà quotidiana di una cooperativa: otto unità interconnesse che coprono una dashboard con indicatori e grafici istantanei, le schede delle cooperative con iscrizione al registro locale e tessera ODCO, il registro degli iscritti, quote e cariche del consiglio, le assemblee generali con verbali e riunioni del consiglio, entrate, uscite e report finanziari pronti, un registro documenti con data certa e avvisi di scadenza, il tracciamento delle interazioni con ODCO, imposte e CNSS, e una biblioteca giuridica che raccoglie la legge 112.12, i suoi decreti e principi — tutto in un\u2019interfaccia araba RTL al 100 % con un design marocchino moderno tra spirito di zellige e arco marocchino.',
 value_lead='CMDP trasforma la governance di una cooperativa da carte sparse a un sistema chiaro:',
 values=[('Una dashboard, una visione netta', 'Indicatori e grafici istantanei mostrano la salute della cooperativa: entrate di stagione, date dell\u2019assemblea e avvisi sui documenti — tutto a colpo d\u2019occhio.'),
   ('Conformità integrata', 'La biblioteca giuridica raccoglie la legge 112.12, i decreti e i principi, collegando ogni pratica al suo articolo — la cooperativa resta sempre dal lato giusto della legge.'),
   ('Rapporti disciplinati con le autorità', 'Traccia le interazioni con ODCO, imposte e CNSS in un unico registro: cosa è stato presentato, quando e cosa resta — nessuna scadenza persa.'),
   ('Una memoria che non dimentica', 'Un registro con data certa di ogni documento con avvisi di scadenza — un\u2019iscrizione o un rinnovo scaduto non ti coglierà mai di sorpresa.')],
 effort='La sfida più grande è stata tradurre testi giuridici aridi in un\u2019esperienza chiara: ho costruito otto unità interconnesse seguendo il ritmo dell\u2019anno cooperativo — dalla fondazione all\u2019assemblea generale annuale — assicurando che ogni unità funzioni da sola e con le altre. Ho anche inserito i numeri nazionali di riferimento (65.315 cooperative attive, oltre 788.000 iscritti, 34 % donne, 40.033 cooperative agricole) per collocare la gestione di ogni cooperativa nel suo vero quadro nazionale.',
 stats=[('Unità interconnesse', '8 unità'), ('Quadro giuridico', 'Legge 112.12'), ('Lingua dell\u2019interfaccia', 'Arabo RTL al 100 %')],
 chips_build=['Front-end statico (Cloudflare Pages)', 'Database locale (SQLite)', 'Design marocchino moderno (zellige e arco)', 'Grafici della dashboard', 'Avvisi di scadenza', 'Interfaccia araba RTL nativa', 'Struttura modulare a 8 unità'],
 chips_ops=['Cloudflare Pages per hosting e deploy', 'Database locale leggero (SQLite)', 'Responsive su ogni schermo', 'Indicatori e grafici istantanei', 'Biblioteca giuridica estendibile'],
 tools=[('Front-end statico', 'Pagine leggere servite dalla rete globale di Cloudflare: apertura rapida in Marocco e fuori, aggiornamento immediato a ogni versione — senza server costosi.'),
   ('Database SQLite locale', 'Un piccolo motore dati senza server che archivia cooperative, soci e operazioni in un solo file — ideale per la sensibilità dei dati cooperativi.'),
   ('Design marocchino moderno', 'Lo spirito dello zellige e dell\u2019arco marocchino in un\u2019interfaccia digitale: identità visiva locale con linguaggio contemporaneo che distingue la piattaforma dai template generici.'),
   ('Dashboard e grafici', 'Indicatori istantanei e grafici che mostrano entrate di stagione, tasso di crescita e data dell\u2019assemblea — decisioni basate sui numeri, non sulle impressioni.'),
   ('Architettura a otto unità', 'Ogni funzione (soci, finanze, documenti...) è un\u2019unità autonoma che funziona da sola e si integra con il resto — lo sviluppo avanza senza rompere il tutto.'),
   ('Biblioteca della legge 112.12', 'Testi giuridici e decreti organizzati e collegati alle pratiche — dalla fondazione con cinque soci all\u2019assemblea generale ordinaria annuale.'),
   ('Avvisi di scadenza', 'I documenti che scadono (iscrizione, rinnovo...) avvisano in anticipo — la cooperativa non si trova mai sorpresa da un documento scaduto al momento giusto.'),
   ('Arabo RTL nativo', 'Disegnata da destra a sinistra dalla prima riga, non una traduzione invertita — un\u2019esperienza naturale per l\u2019utente marocchino.')],
 features=['Otto unità interconnesse che coprono l\u2019intero ciclo di vita della cooperativa', 'Dashboard con indicatori e grafici istantanei', 'Registro di iscritti, quote, cariche del consiglio e quote associative', 'Finanze complete: entrate, uscite e report pronti', 'Registro documenti con data certa e avvisi di scadenza', 'Tracciamento delle interazioni con ODCO, imposte e CNSS più la biblioteca della legge 112.12'],
 costs=dict(self='0 MAD — costruita su uno stack completamente gratuito.',
   pro='Circa 25.000–70.000 MAD per una piattaforma gestionale di questa portata e conformità legale.',
   now='0 MAD al mese con il piano gratuito.',
   scale='Dominio dedicato (100–150 MAD/anno) e hosting dati protetto al passaggio all\u2019uso reale multi-cooperativa.'),
 learned='CMDP mi ha insegnato a trasformare la «burocrazia» da nemica a materia di design: la legge 112.12 non è un ostacolo ma una mappa funzionale pronta all\u2019uso. Ho imparato a leggere il testo normativo ed estrarne i flussi di lavoro — dal quorum dell\u2019assemblea alle scadenze di rinnovo — per poi tradurli in schermate semplici. Ha anche rafforzato la mia convinzione che la digitalizzazione in Marocco riesce quando rispetta il contesto locale: lingua, identità visiva e realtà delle cooperative.',
 tag='Digitalizzare le cooperative marocchine',
 card_desc='Una piattaforma completa per la gestione delle cooperative ai sensi della legge 112.12: dashboard, soci e quote, assemblea generale, finanze e registro documenti — con tracciamento delle autorità (ODCO, imposte, CNSS) in un design marocchino moderno.')

C['de'] = dict(
 meta='CMDP – digitale Plattform für marokkanische Genossenschaften: Dashboard, Mitglieder und Anteile, Generalversammlung, Finanzen, Dokumentenregister und Einhaltung von Gesetz 112.12 — in modernem marokkanischem Design.',
 field='Digitale Plattform für Genossenschaftsverwaltung',
 lead='Eine umfassende marokkanische Plattform, die die Verwaltung von Genossenschaften digitalisiert — Mitglieder, Generalversammlungen, Vorstände, Finanzen und Dokumente — mit Verfolgung der Aufsichtsbehörden und Einhaltung von Gesetz 112.12, in modernem Zellige-inspiriertem Design.',
 about='CMDP ist eine digitale Plattform zur Verwaltung marokkanischer Genossenschaften, konzipiert um den Alltag einer Genossenschaft: acht verbundene Einheiten, die ein Dashboard mit sofortigen Kennzahlen und Diagrammen, Genossenschaftskarten mit Eintragung im lokalen Register und ODCO-Karte, das Register der Mitglieder, Anteile und Vorstandspositionen, Generalversammlungen mit Protokollen und Vorstandssitzungen, Einnahmen, Ausgaben und fertige Finanzberichte, ein zeitgestempeltes Dokumentenregister mit Ablauferinnerungen, die Verfolgung der Kontakte mit ODCO, Steuern und CNSS sowie eine Rechtsbibliothek mit Gesetz 112.12, seinen Erlassen und Grundsätzen abdecken — alles in einer komplett arabischen RTL-Oberfläche mit modernem marokkanischem Design aus Zellige-Geist und marokkanischem Bogen.',
 value_lead='CMDP verwandelt die Genossenschaftsverwaltung von verstreuten Papieren in ein klares System:',
 values=[('Ein Dashboard, ein klarer Blick', 'Sofortige Kennzahlen und Diagramme zeigen die Gesundheit der Genossenschaft: Saisonumsätze, Termin der Generalversammlung, Dokumenten-Erinnerungen — alles auf einen Blick.'),
   ('Eingebaute Rechtssicherheit', 'Die Rechtsbibliothek versammelt Gesetz 112.12, seine Erlasse und Grundsätze und verknüpft jeden Schritt mit seinem Artikel — die Genossenschaft bleibt immer auf der richtigen Seite des Gesetzes.'),
   ('Disziplinierte Behördenkontakte', 'Verfolgung der Kontakte mit ODCO, Steuern und CNSS in einem Register: was eingereicht wurde, wann und was bleibt — keine verlorenen Fristen.'),
   ('Ein Gedächtnis, das nichts vergisst', 'Ein zeitgestempeltes Register aller Dokumente mit Ablauferinnerungen — eine abgelaufene Eintragung oder Erneuerung überrascht Sie nie.')],
 effort='Die größte Herausforderung war, trockene Gesetzestexte in ein klares Nutzungserlebnis zu übersetzen: Ich baute acht verbundene Einheiten im Rhythmus des Genossenschaftsjahres — von der Gründung bis zur jährlichen Generalversammlung — und sorgte dafür, dass jede Einheit allein und mit den anderen funktioniert. Zudem verankerte ich die nationalen Referenzzahlen (65.315 aktive Genossenschaften, über 788.000 Mitglieder, 34 % Frauen, 40.033 Landwirtschaftsgenossenschaften), um die Verwaltung jeder Genossenschaft in ihr wahres nationales Bild zu stellen.',
 stats=[('Verbundene Einheiten', '8 Einheiten'), ('Rechtsrahmen', 'Gesetz 112.12'), ('Sprache der Oberfläche', 'Vollständig Arabisch RTL')],
 chips_build=['Statisches Front-end (Cloudflare Pages)', 'Lokale Datenbank (SQLite)', 'Modernes marokkanisches Design (Zellige und Bogen)', 'Dashboard-Diagramme', 'Ablauferinnerungen', 'Native arabische RTL-Oberfläche', 'Modulare 8-Einheiten-Struktur'],
 chips_ops=['Cloudflare Pages für Hosting und Deployment', 'Leichte lokale Datenbank (SQLite)', 'Responsiv auf jedem Bildschirm', 'Sofortige Kennzahlen und Diagramme', 'Erweiterbare Rechtsbibliothek'],
 tools=[('Statisches Front-end', 'Leichte Seiten aus Cloudflares globalem Netzwerk: schnelles Laden in Marokko und darüber hinaus, sofortige Updates bei jeder Version — ohne teure Server.'),
   ('Lokale SQLite-Datenbank', 'Eine kleine serverlose Daten-Engine, die Genossenschaften, Mitglieder und Vorgänge in einer einzigen Datei speichert — ideal bei der Sensibilität von Genossenschaftsdaten.'),
   ('Modernes marokkanisches Design', 'Der Geist von Zellige und marokkanischem Bogen in einer digitalen Oberfläche: lokale visuelle Identität in zeitgemäßer Sprache, abgesetzt von generischen Vorlagen.'),
   ('Dashboard und Diagramme', 'Sofortige Kennzahlen und Diagramme zu Saisonumsätzen, Wachstumsrate und Versammlungstermin — Entscheidungen auf Basis von Zahlen, nicht von Eindrücken.'),
   ('Acht-Einheiten-Architektur', 'Jede Funktion (Mitglieder, Finanzen, Dokumente...) ist eine eigenständige Einheit, die allein und im Verbund funktioniert — die Entwicklung geht voran, ohne das Ganze zu brechen.'),
   ('Gesetz-112.12-Bibliothek', 'Rechtstexte und Erlasse, geordnet und mit den Schritten verknüpft — von der Gründung mit fünf Mitgliedern bis zur ordentlichen Jahresversammlung.'),
   ('Ablauferinnerungen', 'Ablaufende Dokumente (Eintragung, Erneuerung...) erinnern vorab — die Genossenschaft wird nie von einem abgelaufenen Papier überrascht, wenn es darauf ankommt.'),
   ('Natives Arabisch RTL', 'Von der ersten Zeile an von rechts nach links gestaltet, keine gespiegelte Übersetzung — ein natürliches Erlebnis für marokkanische Nutzer.')],
 features=['Acht verbundene Einheiten für den gesamten Lebenszyklus der Genossenschaft', 'Dashboard mit sofortigen Kennzahlen und Diagrammen', 'Register der Mitglieder, Anteile, Vorstandspositionen und Beiträge', 'Vollständige Finanzen: Einnahmen, Ausgaben und fertige Berichte', 'Zeitgestempeltes Dokumentenregister mit Ablauferinnerungen', 'Verfolgung der Kontakte mit ODCO, Steuern und CNSS plus Gesetz-112.12-Bibliothek'],
 costs=dict(self='0 MAD — auf einem vollständig kostenlosen Stack aufgebaut.',
   pro='Etwa 25.000–70.000 MAD für eine Verwaltungsplattform dieses Umfangs mit Rechtskonformität.',
   now='0 MAD pro Monat im Free-Tarif.',
   scale='Eigene Domain (100–150 MAD/Jahr) sowie geschütztes Daten-Hosting beim Übergang zum realen Multi-Kooperativen-Betrieb.'),
 learned='CMDP lehrte mich, „Bürokratie“ vom Feind zum Gestaltungsmaterial zu machen: Gesetz 112.12 ist kein Hindernis, sondern eine fertige funktionale Landkarte. Ich lernte, Verordnungstexte zu lesen und die Arbeitsabläufe herauszuziehen — vom Versammlungsquorum bis zu Erneuerungsfristen — und sie in einfache Bildschirme zu übersetzen. Es vertiefte auch meine Überzeugung: Digitalisierung in Marokko gelingt, wenn sie den lokalen Kontext respektiert — Sprache, visuelle Identität und die Realität der Genossenschaften.',
 tag='Marokkanische Genossenschaften digitalisieren',
 card_desc='Eine umfassende Plattform zur Genossenschaftsverwaltung gemäß Gesetz 112.12: Dashboard, Mitglieder und Anteile, Generalversammlung, Finanzen und Dokumentenregister — mit Verfolgung der Aufsichtsbehörden (ODCO, Steuern, CNSS) in modernem marokkanischem Design.')

C['nl'] = dict(
 meta='CMDP, digitaal platform voor Marokkaanse coöperaties: dashboard, leden en aandelen, algemene vergadering, financiën, documentenregister en naleving van wet 112.12 — in een modern Marokkaans ontwerp.',
 field='Digitaal platform voor coöperatiebeheer',
 lead='Een volledig Marokkaans platform dat het beheer van coöperaties digitaliseert — leden, algemene vergaderingen, besturen, financiën en documenten — met tracking van toezichthouders en naleving van wet 112.12, in een modern zellige-geïnspireerd ontwerp.',
 about='CMDP is een digitaal platform voor het beheer van Marokkaanse coöperaties, ontworpen rond de dagelijkse realiteit van een coöperatie: acht verbonden eenheden die een dashboard met directe indicatoren en grafieken, coöperatiekaarten met inschrijving in het lokale register en ODCO-kaart, het register van leden, aandelen en bestuursfuncties, algemene vergaderingen met notulen en bestuursvergaderingen, inkomsten, uitgaven en kant-en-klare financiële rapporten, een tijdstempel-documentenregister met vervalherinneringen, de tracking van contacten met ODCO, belastingen en CNSS, en een juridische bibliotheek met wet 112.12, de decreten en principes dekken — allemaal in een volledig Arabische RTL-interface met een modern Marokkaans ontwerp, tussen zellige-geest en Marokkaanse boog.',
 value_lead='CMDP verandert coöperatiebeheer van verspreide papieren in één helder systeem:',
 values=[('Eén dashboard, één heldere blik', 'Directe indicatoren en grafieken tonen de gezondheid van de coöperatie: seizoensinkomsten, data van de algemene vergadering, documentherinneringen — alles in één oogopslag.'),
   ('Ingebouwde regelgeving', 'De juridische bibliotheek bundelt wet 112.12, de decreten en principes, en koppelt elke stap aan zijn artikel — de coöperatie blijft altijd aan de juiste kant van de wet.'),
   ('Gedisciplineerd contact met autoriteiten', 'Volg de contacten met ODCO, belastingen en CNSS in één register: wat is ingediend, wanneer en wat resteert — geen verloren deadlines.'),
   ('Een geheugen dat niets vergeet', 'Een tijdstempel-register van elk document met vervalherinneringen — een verlopen inschrijving of vernieuwing verrast je nooit meer.')],
 effort='De grootste uitdaging was droge wetteksten vertalen naar een heldere gebruikerservaring: ik bouwde acht verbonden eenheden volgens het ritme van het coöperatiejaar — van oprichting tot de jaarlijkse algemene vergadering — en zorgde dat elke eenheid alleen én met de anderen werkt. Ik verankerde ook de nationale referentiecijfers (65.315 actieve coöperaties, meer dan 788.000 leden, 34 % vrouwen, 40.033 landbouwcoöperaties) om het beheer van elke coöperatie in zijn echte nationale beeld te plaatsen.',
 stats=[('Verbonden eenheden', '8 eenheden'), ('Juridisch kader', 'Wet 112.12'), ('Interfacetaal', 'Volledig Arabisch RTL')],
 chips_build=['Statische front-end (Cloudflare Pages)', 'Lokale database (SQLite)', 'Modern Marokkaans ontwerp (zellige en boog)', 'Dashboardgrafieken', 'Vervalherinneringen', 'Natuurlijke Arabische RTL-interface', 'Modulaire structuur van 8 eenheden'],
 chips_ops=['Cloudflare Pages voor hosting en deploys', 'Lichtgewicht lokale database (SQLite)', 'Responsief op elk scherm', 'Directe indicatoren en grafieken', 'Uitbreidbare juridische bibliotheek'],
 tools=[('Statische front-end', 'Lichte pagina\u2019s vanaf Cloudflares wereldwijde netwerk: snel laden in Marokko en erbuiten, directe updates bij elke versie — zonder dure servers.'),
   ('Lokale SQLite-database', 'Een kleine serverloze data-engine die coöperaties, leden en transacties in één bestand opslaat — ideaal gezien de gevoeligheid van coöperatiedata.'),
   ('Modern Marokkaans ontwerp', 'De geest van zellige en de Marokkaanse boog in een digitale interface: lokale visuele identiteit in eigentijdse taal, onderscheiden van generieke templates.'),
   ('Dashboard en grafieken', 'Directe indicatoren en grafieken over seizoensinkomsten, groeipercentage en vergaderdatum — beslissingen op basis van cijfers, niet van indrukken.'),
   ('Architectuur van acht eenheden', 'Elke functie (leden, financiën, documenten...) is een zelfstandige eenheid die alleen en in verbintenis werkt — de ontwikkeling gaat vooruit zonder het geheel te breken.'),
   ('Bibliotheek van wet 112.12', 'Wetteksten en decreten, geordend en gekoppeld aan stappen — van oprichting met vijf leden tot de jaarlijkse algemene vergadering.'),
   ('Vervalherinneringen', 'Documenten die vervallen (inschrijving, vernieuwing...) waarschuwen vooraf — de coöperatie wordt nooit verrast door een verlopen papier op het verkeerde moment.'),
   ('Natuurlijk Arabisch RTL', 'Van rechts naar links ontworpen vanaf de eerste regel, geen gespiegelde vertaling — een natuurlijke ervaring voor de Marokkaanse gebruiker.')],
 features=['Acht verbonden eenheden die de volledige levenscyclus van de coöperatie dekken', 'Dashboard met directe indicatoren en grafieken', 'Register van leden, aandelen, bestuursfuncties en lidmaatschapsbijdragen', 'Volledige financiën: inkomsten, uitgaven en kant-en-klare rapporten', 'Tijdstempel-documentenregister met vervalherinneringen', 'Tracking van contacten met ODCO, belastingen en CNSS plus de bibliotheek van wet 112.12'],
 costs=dict(self='0 MAD — gebouwd op een volledig gratis stack.',
   pro='Ongeveer 25.000–70.000 MAD voor een beheerplatform van deze omvang en juridische naleving.',
   now='0 MAD per maand via het gratis pakket.',
   scale='Eigen domein (100–150 MAD per jaar), plus beveiligde datahosting bij de overstap naar echt gebruik door meerdere coöperaties.'),
 learned='CMDP leerde me \u201ebureaucratie\u201d van vijand tot ontwerpmateriaal te maken: wet 112.12 is geen obstakel maar een kant-en-klare functionele kaart. Ik leerde regelgeving lezen en de werkstromen eruit halen — van quorum op de vergadering tot vernieuwingstermijnen — en ze om te zetten in eenvoudige schermen. Het verdiepte ook mijn overtuiging dat digitalisering in Marokko slaagt wanneer ze de lokale context respecteert: taal, visuele identiteit en de realiteit van coöperaties.',
 tag='Marokkaanse coöperaties digitaliseren',
 card_desc='Een volledig platform voor coöperatiebeheer volgens wet 112.12: dashboard, leden en aandelen, algemene vergadering, financiën en documentenregister — met tracking van toezichthouders (ODCO, belastingen, CNSS) in een modern Marokkaans ontwerp.')

C['pt'] = dict(
 meta='CMDP, plataforma digital de gestão de cooperativas marroquinas: painel de controlo, membros e quotas, assembleia geral, finanças, registo de documentos e conformidade com a lei 112.12 — num design marroquino moderno.',
 field='Plataforma digital de gestão de cooperativas',
 lead='Uma plataforma marroquina completa que digitaliza a governação das cooperativas — membros, assembleias gerais, direções, finanças e documentos — com acompanhamento das autoridades de supervisão e conformidade com a lei 112.12, num design moderno inspirado no zellige.',
 about='CMDP é uma plataforma digital para gerir cooperativas marroquinas, desenhada em torno da realidade diária de uma cooperativa: oito unidades interligadas que cobrem um painel de controlo com indicadores e gráficos instantâneos, fichas de cooperativas com registo local e cartão ODCO, o registo de membros, quotas e cargos da direção, assembleias gerais com atas e reuniões da direção, receitas, despesas e relatórios financeiros prontos, um registo de documentos com data certa e alertas de validade, o acompanhamento das interações com ODCO, impostos e CNSS, e uma biblioteca jurídica que reúne a lei 112.12, os seus decretos e princípios — tudo numa interface árabe RTL a 100 % com um design marroquino moderno entre o espírito do zellige e o arco marroquino.',
 value_lead='CMDP transforma a governação de uma cooperativa, de papéis dispersos num sistema claro:',
 values=[('Um painel, uma visão nítida', 'Indicadores e gráficos instantâneos mostram a saúde da cooperativa: receitas da época, datas da assembleia e alertas de documentos — tudo num relance.'),
   ('Conformidade integrada', 'A biblioteca jurídica reúne a lei 112.12, os decretos e princípios, ligando cada passo ao seu artigo — a cooperativa fica sempre do lado certo da lei.'),
   ('Relação disciplinada com as autoridades', 'Acompanhe as interações com ODCO, impostos e CNSS num só registo: o que foi entregue, quando, e o que falta — sem prazos perdidos.'),
   ('Uma memória que não esquece', 'Um registo com data certa de todos os documentos com alertas de validade — um registo ou renovação expirado nunca o surpreende.')],
 effort='O maior desafio foi traduzir textos legais áridos numa experiência clara: construí oito unidades interligadas ao ritmo do ano cooperativo — da fundação à assembleia geral anual — garantindo que cada unidade funciona sozinha e com as outras. Fixei também os números nacionais de referência (65.315 cooperativas ativas, mais de 788.000 membros, 34 % mulheres, 40.033 cooperativas agrícolas) para situar a gestão de cada cooperativa no seu verdadeiro quadro nacional.',
 stats=[('Unidades interligadas', '8 unidades'), ('Enquadramento legal', 'Lei 112.12'), ('Idioma da interface', 'Árabe RTL a 100 %')],
 chips_build=['Front-end estático (Cloudflare Pages)', 'Base de dados local (SQLite)', 'Design marroquino moderno (zellige e arco)', 'Gráficos do painel', 'Alertas de validade', 'Interface árabe RTL nativa', 'Estrutura modular de 8 unidades'],
 chips_ops=['Cloudflare Pages para alojamento e deploys', 'Base local leve (SQLite)', 'Responsivo em todos os ecrãs', 'Indicadores e gráficos instantâneos', 'Biblioteca jurídica expansível'],
 tools=[('Front-end estático', 'Páginas leves servidas pela rede global da Cloudflare: abertura rápida em Marrocos e além, atualização imediata em cada versão — sem servidores caros.'),
   ('Base SQLite local', 'Um pequeno motor de dados sem servidor que guarda cooperativas, membros e operações num único ficheiro — ideal para a sensibilidade dos dados das cooperativas.'),
   ('Design marroquino moderno', 'O espírito do zellige e do arco marroquino numa interface digital: identidade visual local em linguagem contemporânea, distinta dos templates genéricos.'),
   ('Painel e gráficos', 'Indicadores instantâneos e gráficos que mostram receitas da época, taxa de crescimento e data da assembleia — decisões baseadas em números, não em impressões.'),
   ('Arquitetura de oito unidades', 'Cada função (membros, finanças, documentos...) é uma unidade autónoma que funciona sozinha e se integra com as restantes — o desenvolvimento avança sem partir o todo.'),
   ('Biblioteca da lei 112.12', 'Textos legais e decretos organizados e ligados aos passos — da fundação com cinco membros à assembleia geral ordinária anual.'),
   ('Alertas de validade', 'Os documentos que expiram (registo, renovação...) avisam com antecedência — a cooperativa nunca é surpreendida por um papel caducado na hora certa.'),
   ('Árabe RTL nativo', 'Desenhada da direita para a esquerda desde a primeira linha, não uma tradução invertida — uma experiência natural para o utilizador marroquino.')],
 features=['Oito unidades interligadas que cobrem todo o ciclo de vida da cooperativa', 'Painel de controlo com indicadores e gráficos instantâneos', 'Registo de membros, quotas, cargos da direção e quotizações', 'Finanças completas: receitas, despesas e relatórios prontos', 'Registo de documentos com data certa e alertas de validade', 'Acompanhamento das interações com ODCO, impostos e CNSS mais a biblioteca da lei 112.12'],
 costs=dict(self='0 MAD — construída numa infraestrutura totalmente gratuita.',
   pro='Aprox. 25.000–70.000 MAD por uma plataforma de gestão desta dimensão e conformidade legal.',
   now='0 MAD por mês no plano gratuito.',
   scale='Domínio próprio (100–150 MAD/ano) e alojamento de dados protegido na passagem ao uso real multi-cooperativo.'),
 learned='CMDP ensinou-me a transformar a «burocracia» de inimiga em material de design: a lei 112.12 não é um obstáculo, é um mapa funcional pronto a usar. Aprendi a ler o texto normativo e a extrair os fluxos de trabalho — do quórum da assembleia aos prazos de renovação — e a transformá-los em ecrãs simples. Aprofundou também a minha convicção de que a digitalização em Marrocos tem sucesso quando respeita o contexto local: língua, identidade visual e a realidade das cooperativas.',
 tag='Digitalizar as cooperativas marroquinas',
 card_desc='Uma plataforma completa de gestão de cooperativas conforme a lei 112.12: painel, membros e quotas, assembleia geral, finanças e registo de documentos — com acompanhamento das autoridades (ODCO, impostos, CNSS) num design marroquino moderno.')

# ---------------------------------------------------------------- build pages

def sub_p_after(html, anchor, new_p):
    """replace first <p>...</p> after anchor"""
    i = html.find(anchor)
    assert i >= 0, anchor
    m = re.compile(r'<p>(.*?)</p>', re.S).search(html, i)
    assert m, 'p after ' + anchor
    return html[:m.start(1)] + new_p + html[m.end(1):]

def build_page(lang):
    src = f'{SITE}/projects/epdp/index.html' if lang == 'ar' else f'{SITE}/{lang}/projects/epdp/index.html'
    html = open(src, encoding='utf-8').read()
    c = C[lang]
    name_new, name_old = CMDP_NAME[lang], EPDP_NAME[lang]

    # 1. project name everywhere (title, h1, crumbs, alts, json-ld, aria)
    html = html.replace(name_old, name_new)
    # 2. paths & assets
    html = html.replace('/projects/epdp/', '/projects/cmdp/')
    html = html.replace('epdp.pages.dev', 'cmdp.pages.dev')
    html = html.replace('pj-epdp.jpg', 'pj-cmdp.jpg')
    html = html.replace('/img/shots/epdp-', '/img/shots/cmdp-')
    # 3. meta descriptions + json-ld
    html = re.sub(r'(<meta name="description" content=")[^"]*(")', lambda m: m.group(1) + c['meta'] + m.group(2), html)
    html = re.sub(r'(<meta property="og:description" content=")[^"]*(")', lambda m: m.group(1) + c['meta'] + m.group(2), html)
    html = re.sub(r'("description": ")(.*?)(",\s*"url")', lambda m: m.group(1) + c['about'] + m.group(3), html, flags=re.S)
    html = re.sub(r'("about": ")(.*?)("})', lambda m: m.group(1) + c['field'] + m.group(3), html, flags=re.S)
    # 4. hero zone
    html = re.sub(r'(<span class="cert-field">).*?(</span>)', lambda m: m.group(1) + c['field'] + m.group(2), html, flags=re.S)
    html = re.sub(r'(<p class="page-lead reveal">).*?(</p>)', lambda m: m.group(1) + c['lead'] + m.group(2), html, flags=re.S)
    # 5. content sections
    html = sub_p_after(html, 'id="pp-about"', c['about'])
    html = sub_p_after(html, 'id="pp-learned"', c['learned'])
    html = sub_p_after(html, 'id="pp-effort"', c['effort'])
    # value lead
    html = re.sub(r'(id="pp-value">.*?<p class="dsec-lead">).*?(</p>)',
                  lambda m: m.group(1) + c['value_lead'] + m.group(2), html, flags=re.S)
    # value grid articles
    vals = '\n'.join(f'<article class="value-card card reveal">\n<h3>{t}</h3>\n<p>{p}</p>\n</article>' for t, p in c['values'])
    html = re.sub(r'(class="value-grid">).*?(</div>\s*</section>)',
                  lambda m: m.group(1) + '\n' + vals + '\n        ' + m.group(2), html, flags=re.S)
    # effort stats
    stats = '\n'.join(f'<div><dt>{dt}</dt><dd>{dd}</dd></div>' for dt, dd in c['stats'])
    html = re.sub(r'(class="effort-stats">).*?(</dl>)',
                  lambda m: m.group(1) + '\n' + stats + '\n        ' + m.group(2), html, flags=re.S)
    # chips (build then ops)
    html = re.sub(r'(id="pp-tech">.*?class="chips reveal">).*?(</ul>)',
                  lambda m: m.group(1) + '\n' + '\n'.join(f'<li class="chip">{x}</li>' for x in c['chips_build']) + '\n        ' + m.group(2),
                  html, flags=re.S)
    html = re.sub(r'(class="chips ops reveal">).*?(</ul>)',
                  lambda m: m.group(1) + '\n' + '\n'.join(f'<li class="chip">{x}</li>' for x in c['chips_ops']) + '\n        ' + m.group(2),
                  html, flags=re.S)
    # tools grid
    tools = '\n'.join(f'<article class="tool-card reveal">\n<h3>{t}</h3>\n<p>{p}</p>\n</article>' for t, p in c['tools'])
    html = re.sub(r'(class="tools-grid">).*?(</div>\s*</section>)',
                  lambda m: m.group(1) + '\n' + tools + '\n        ' + m.group(2), html, flags=re.S)
    # features list (keep check icon svg)
    CHK = '<svg class="ic" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg>'
    feats = '\n'.join(f'<li>{CHK}<span>{x}</span></li>' for x in c['features'])
    html = re.sub(r'(class="feature-list reveal">).*?(</ul>)',
                  lambda m: m.group(1) + '\n' + feats + '\n        ' + m.group(2), html, flags=re.S)
    # costs: replace the four cost-v values in order
    vals4 = [c['costs']['self'], c['costs']['pro'], c['costs']['now'], c['costs']['scale']]
    it = iter(vals4)
    html = re.sub(r'(<span class="cost-v">)[^<]*(</span>)', lambda m: m.group(1) + next(it) + m.group(2), html)
    assert all(v in html for v in vals4), 'cost values missing ' + lang
    # 6. pager prev: phmp -> epdp
    html = re.sub(r'(pager-card prev" href=")/projects/phdp/(")', r'\1/projects/epdp/\2', html)
    html = re.sub(r'(pager-card prev"[\s\S]*?<span class="ttl">)PHMP(</span>)', r'\1EPDP\2', html)

    dst = f'{SITE}/projects/cmdp/index.html' if lang == 'ar' else f'{SITE}/{lang}/projects/cmdp/index.html'
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    open(dst, 'w', encoding='utf-8').write(html)
    return dst

made = [build_page(l) for l in ['ar', 'en', 'fr', 'es', 'it', 'de', 'nl', 'pt']]
print('CMDP pages built:', len(made))
for m in made:
    print('  ', m)
