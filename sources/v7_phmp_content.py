# -*- coding: utf-8 -*-
"""v7: PHMP (phmp.pages.dev — pharmacy management platform) content, 8 languages.
Structure mirrors the existing project entries exactly (card / page / v4 / tools)."""

PHMP = {
    'ar': {
        'card': {
            'name': 'PHMP',
            'tag': 'منصة إدارة الصيدليات',
            'desc': 'منصة احترافية لإدارة الصيدليات: نقطة بيع ومخزون ووصفات وتقارير، مع واجهة للزبون لطلب الأدوية من صيدليته مع خيار التوصيل.',
        },
        'page': {
            'about': 'PHMP منصة مزدوجة الأطراف لإدارة الصيدليات. الواجهة العامة تخاطب الزبون: يختار صيدليته من الصيدليات المتوفرة في منطقته، يتصفح الأدوية وطلبها مع خيار التوصيل، بلا استمارات معقدة. وواجهة الإدارة تخاطب المالك والصيادلة: نقطة بيع سريعة بمسح الباركود، تتبع المخزون، تسجيل الوصفات، تقارير ولوحات رسوم بيانية للمبيعات والعمليات، إدارة صيدليات متعددة بمصفوفة صلاحيات دقيقة، سجلات تدقيق لكل عملية حساسة، ومراجع قانونية مغربية رسمية لقطاع الأدوية والصيدلة مدمجة داخل المنصة مع إمكانية فتح النص الأصلي.',
            'tech': ['React (واجهة تفاعلية)', 'Vite (بناء سريع)', 'لوحات رسوم بيانية', 'قاعدة بيانات الأدوية', 'مسح الباركود', 'خدمات خلفية (Cloudflare Workers)', 'جلسات دخول موقعة', 'Cloudflare Pages'],
            'features': ['واجهة زبون لاختيار الصيدلية وطلب الأدوية مع التوصيل', 'نقطة بيع سريعة بمسح الباركود', 'تتبع المخزون وتسجيل الوصفات', 'تقارير ولوحات رسوم بيانية للمبيعات والعمليات', 'إدارة صيدليات متعددة بصلاحيات وسجلات تدقيق', 'مراجع قانونية مغربية لقطاع الأدوية داخل المنصة'],
            'learned': 'علّمني هذا المشروع أن البرمجيات في القطاع الصحي تحمل مسؤولية مضاعفة: خطأ في سعر دواء أو تفاعل دوائي ليس كخطأ في متجر عادي. تعلمت بناء منصة تخدم طرفين مختلفين — زبون يريد الطلب بسهولة، وصيدلي يريد السرعة والدقة — وأن أوازن بينهما في نظام واحد، وأن الامتثال للوائح المغربية الرسمية ليس قيداً بل أساس الثقة في أي منصة تلمس صحة الناس.',
        },
        'v4': {
            'value_intro': 'PHMP يرقمن الصيدلية من الاستقبال إلى التقرير:',
            'values': [
                ('منصة بطرفين في نظام واحد', 'الزبون يطلب دواءه من صيدليته ببضع نقرات مع خيار التوصيل، والصيدلي يستقبل الطلب على نفس النظام ويجهزه — دورة كاملة بلا ورق.'),
                ('الباركود بدل الكتابة اليدوية', 'مسح الباركود يقلّص أخطاء الإدخال ويسرّع نقطة البيع — دقة لا غنى عنها في التعامل مع الأدوية.'),
                ('امتثال مغربي حقيقي', 'المراجع القانونية واللوائح المنظمة لقطاع الأدوية والصيدلة بالمغرب مدمجة داخل المنصة مع فتح النص الأصلي — لا اجتهاد خارج القانون.'),
                ('قرارات مبنية على أرقام', 'لوحات رسوم بيانية تلخص المبيعات والعمليات والمخزون، فتعرف الصيدلية ما يُباع وما ينقص قبل أن ينفد.'),
            ],
            'effort': 'بنيتُ المنصة على وجهين: واجهة الزبون البسيطة — اختيار الصيدلية والطلب والتوصيل — وواجهة الإدارة العميقة: نقطة بيع، مخزون، وصفات، تقارير، صيدليات متعددة، مصفوفة صلاحيات وسجلات تدقيق. الجزء الأصعب لم يكن الشاشات بل فهم عمل الصيدلية الحقيقي: كيف يُسجَّل البيع، متى يُخصم من المخزون، وكيف تُحفظ الحقوق واللوائح — مع قاعدة بيانات الأدوية والمراجع القانونية الرسمية.',
            'effort_stats': [('الأطراف المخدومة', 'زبون + مالك + صيادلة'), ('وحدات الإدارة', 'نقطة بيع ومخزون ووصفات وتقارير'), ('المرجعية', 'لوائح قطاع الأدوية بالمغرب')],
            'ops': ['React + Vite — واجهة سريعة تُبنى وتُحدَّث بسرعة', 'خدمات خلفية عبر Cloudflare Workers', 'جلسات دخول موقعة وصلاحيات مفحوصة', 'سجلات تدقيق للعمليات الحساسة', 'Cloudflare Pages للتشغيل'],
            'cost_self': '0 درهم — بُنيت على منظومة مجانية (استضافة وخدمات خلفية) بمساعدة أدوات الذكاء الاصطناعي في التطوير.',
            'cost_market': '60,000 – 180,000 درهم تقريباً لنظام إدارة صيدليات بهذا العمق: نقطة بيع ومخزون ووصفات وتقارير وامتثال قانوني.',
            'cost_now': '0 درهم شهرياً ضمن الباقة المجانية.',
            'cost_scale': 'خادم وقاعدة بيانات دائمان عند انتشار الاستخدام في صيدليات متعددة: تقديرياً 200 – 700 درهم شهرياً.',
        },
        'tools': [
            ('React', 'مكتبة من ميتا لبناء الواجهات التفاعلية: تقسّم الشاشة إلى مكونات صغيرة قابلة لإعادة الاستخدام — زر، بطاقة، جدول — فيصبح نظام كبير كمنصة الصيدلية منظماً وقابلاً للصيانة، كغرف مرتبة في بيت واحد.'),
            ('Vite', 'أداة البناء الحديثة التي تجمع المشروع وتُحدّث المعاينة في أجزاء من الثانية بدل دقائق الانتظار — كأنها مطبخ مجهز يجهّز الطلب فور وصوله؛ لهذا صارت المعيار العملي لمشاريع React.'),
            ('لوحات الرسوم البيانية', 'مكتبات رسوم تحوّل الأرقام إلى مخططات بصرية — أعمدة وخطوط ودوائر — فيرى الصيدلي حركة المبيعات والمخزون بنظرة واحدة بدل تتبع جداول طويلة.'),
            ('قاعدة بيانات الأدوية', 'قائمة منظمة للأدوية بأسمائها وأشكالها وتصنيفها، تعمل كذاكرة موثوقة للمنصة: بحث سريع، معلومات دقيقة، وتحديث مركزي يصل إلى كل الشاشات دفعة واحدة.'),
            ('مسح الباركود', 'قراءة الخطوط السوداء المطبوعة على علبة كل دواء: مسحة واحدة بالقارئ تسجّل البيع وتخصم من المخزون تلقائياً — لا كتابة يدوية ولا أخطاء أرقام.'),
            ('جلسات الدخول الموقعة (JWT)', 'بطاقة دخول رقمية موقعة تصدرها المنصة بعد التحقق من الحساب وتُفحص مع كل طلب — فلا يصل إلى بيانات الصيدلية إلا من يملك الحق، مثل شارة موظف لا تُنسخ.'),
            ('Cloudflare Workers (الخدمات الخلفية)', 'خدمات صغيرة تعمل على شبكة كلاودفلير العالمية قرب المستخدم: تستقبل طلبات الدخول والبيانات وتعالجها دون خادم تقليدي — سرعة وتوافر عاليان بتكلفة قريبة من الصفر.'),
            ('واجهة عربية RTL وخط Cairo', 'المنصة مبنية أصلاً بالعربية من اليمين إلى اليسار بخط Cairo الواضح — ليست ترجمة ملحقة بل تصميم عربي من الأساس، وهذا يظهر في كل زر وكل جدول.'),
        ],
    },

    'en': {
        'card': {
            'name': 'PHMP',
            'tag': 'Pharmacy management platform',
            'desc': 'A professional pharmacy management platform: point of sale, inventory, prescriptions and reports, plus a customer side to order medicines from a nearby pharmacy with delivery.',
        },
        'page': {
            'about': 'PHMP is a two-sided pharmacy management platform. The public side speaks to the customer: pick a pharmacy in your area, browse medicines and order them with home delivery — no complicated forms. The admin side speaks to the owner and pharmacists: a fast barcode point of sale, inventory tracking, prescription records, sales and operations dashboards, multi-pharmacy management with a fine-grained permissions matrix, audit logs for every sensitive action, and official Moroccan legal references for the pharmaceutical sector built into the platform, with links to the original texts.',
            'tech': ['React (interactive UI)', 'Vite (fast build tool)', 'Chart dashboards', 'Medicines database', 'Barcode scanning', 'Backend services (Cloudflare Workers)', 'Signed login sessions', 'Cloudflare Pages'],
            'features': ['Customer side to pick a pharmacy and order medicines with delivery', 'Fast point of sale with barcode scanning', 'Inventory tracking and prescription records', 'Sales and operations dashboards with charts', 'Multi-pharmacy management, permissions and audit logs', 'Moroccan pharmaceutical legal references inside the platform'],
            'learned': 'This project taught me that software in healthcare carries double responsibility: a mistake in a medicine\'s price or interaction is not like a mistake in an ordinary shop. I learned to build a platform serving two very different sides — a customer who wants effortless ordering and a pharmacist who needs speed and accuracy — and to balance both in one system, and that compliance with official Moroccan regulations is not a constraint but the very foundation of trust in any platform that touches people\'s health.',
        },
        'v4': {
            'value_intro': 'PHMP digitizes the pharmacy from the counter to the report:',
            'values': [
                ('A two-sided platform in one system', 'The customer orders medicine from their pharmacy in a few taps with delivery, and the pharmacist receives the order on the same system and prepares it — a complete paperless cycle.'),
                ('Barcodes instead of handwriting', 'Barcode scanning cuts entry errors and speeds up the point of sale — the accuracy you cannot do without when handling medicines.'),
                ('Real Moroccan compliance', 'The legal references and regulations governing Morocco\'s pharmaceutical sector are built into the platform with links to the original texts — no guesswork outside the law.'),
                ('Decisions driven by numbers', 'Chart dashboards summarize sales, operations and inventory, so the pharmacy knows what sells and what runs low before it runs out.'),
            ],
            'effort': 'I built the platform on two faces: the simple customer side — choosing a pharmacy, ordering, delivery — and the deep admin side: point of sale, inventory, prescriptions, reports, multiple pharmacies, a permissions matrix and audit logs. The hardest part was not the screens but understanding how a real pharmacy works: how a sale is recorded, when stock is deducted, and how rights and regulations are preserved — together with a medicines database and the official legal references.',
            'effort_stats': [('Sides served', 'customer + owner + pharmacists'), ('Admin modules', 'POS, inventory, prescriptions, reports'), ('Reference', 'Moroccan pharmaceutical regulations')],
            'ops': ['React + Vite — a fast UI that builds and updates quickly', 'Backend services on Cloudflare Workers', 'Signed sessions and server-checked permissions', 'Audit logs for sensitive operations', 'Cloudflare Pages for hosting'],
            'cost_self': '0 MAD — built on a free stack (hosting and backend services) with AI-assisted development.',
            'cost_market': 'Approximately 60,000 – 180,000 MAD for a pharmacy management system of this depth: POS, inventory, prescriptions, reports and legal compliance.',
            'cost_now': '0 MAD per month on the free tier.',
            'cost_scale': 'A dedicated server and database as usage spreads across multiple pharmacies: an estimated 200 – 700 MAD per month.',
        },
        'tools': [
            ('React', 'A Meta library for building interactive interfaces: it splits the screen into small reusable components — a button, a card, a table — so a large system like a pharmacy platform stays organized and maintainable, like tidy rooms in one house.'),
            ('Vite', 'The modern build tool that bundles the project and refreshes the preview in fractions of a second instead of minutes of waiting — like a fully equipped kitchen that prepares the order the moment it arrives; that is why it became the practical standard for React projects.'),
            ('Chart dashboards', 'Charting libraries turn numbers into visual plots — bars, lines and circles — so the pharmacist reads sales and stock movement at a glance instead of scanning long tables.'),
            ('Medicines database', 'An organized catalogue of medicines with their names, forms and classifications: a trusted memory for the platform — fast search, accurate information, and one central update reaching every screen at once.'),
            ('Barcode scanning', 'Reading the black bars printed on every medicine box: one scan records the sale and deducts the stock automatically — no manual typing, no number errors.'),
            ('Signed sessions (JWT)', 'A signed digital pass issued after the account is verified and checked with every request — only those with the right reach the pharmacy\'s data, like a staff badge that cannot be copied.'),
            ('Cloudflare Workers (backend services)', 'Small services running on Cloudflare\'s global network close to the user: they receive login and data requests and process them without a traditional server — high speed and availability at near-zero cost.'),
            ('Arabic RTL interface and Cairo font', 'The platform is natively Arabic, right-to-left, with the clear Cairo typeface — not a bolted-on translation but an Arabic design from the ground up, visible in every button and every table.'),
        ],
    },

    'fr': {
        'card': {
            'name': 'PHMP',
            'tag': 'Plateforme de gestion de pharmacie',
            'desc': 'Une plateforme professionnelle de gestion de pharmacies : caisse, stock, ordonnances et rapports, plus une interface client pour commander ses médicaments avec livraison.',
        },
        'page': {
            'about': 'PHMP est une plateforme de gestion de pharmacies à double face. Le côté public s\'adresse au client : choisir sa pharmacie parmi celles disponibles dans sa zone, parcourir les médicaments et les commander avec livraison — sans formulaires compliqués. Le côté administration s\'adresse au propriétaire et aux pharmaciens : une caisse rapide par lecture de codes-barres, le suivi du stock, l\'enregistrement des ordonnances, des rapports et tableaux de bord graphiques des ventes et opérations, la gestion de plusieurs pharmacies avec une matrice de permissions fine, des journaux d\'audit pour chaque action sensible, et les références juridiques marocaines officielles du secteur pharmaceutique intégrées dans la plateforme, avec accès aux textes originaux.',
            'tech': ['React (interface interactive)', 'Vite (construction rapide)', 'Tableaux de bord graphiques', 'Base de données des médicaments', 'Lecture de codes-barres', 'Services back-end (Cloudflare Workers)', 'Sessions de connexion signées', 'Cloudflare Pages'],
            'features': ['Interface client pour choisir sa pharmacie et commander avec livraison', 'Caisse rapide par lecture de codes-barres', 'Suivi du stock et enregistrement des ordonnances', 'Rapports et tableaux de bord graphiques des ventes et opérations', 'Gestion multi-pharmacies, permissions et journaux d\'audit', 'Références juridiques marocaines du secteur pharmaceutique intégrées'],
            'learned': 'Ce projet m\'a appris qu\'un logiciel dans la santé porte une responsabilité doublée : une erreur sur le prix ou l\'interaction d\'un médicament n\'est pas une erreur de boutique ordinaire. J\'ai appris à construire une plateforme servant deux publics très différents — un client qui veut commander sans effort et un pharmacien qui exige vitesse et précision — et à les équilibrer dans un seul système ; et que la conformité aux règlements marocains officiels n\'est pas une contrainte mais le fondement même de la confiance dans toute plateforme qui touche à la santé des gens.',
        },
        'v4': {
            'value_intro': 'PHMP numérise la pharmacie du comptoir au rapport :',
            'values': [
                ('Une plateforme à double face dans un seul système', 'Le client commande ses médicaments en quelques touches avec livraison, et le pharmacien reçoit la commande dans le même système et la prépare — un cycle complet sans papier.'),
                ('Le code-barres plutôt que l\'écriture manuelle', 'La lecture du code-barres réduit les erreurs de saisie et accélère la caisse — la précision indispensable quand on manipule des médicaments.'),
                ('Une conformité marocaine réelle', 'Les références juridiques et règlements du secteur pharmaceutique marocain sont intégrés à la plateforme avec accès aux textes originaux — pas d\'improvisation hors la loi.'),
                ('Des décisions fondées sur les chiffres', 'Des tableaux de bord graphiques résument ventes, opérations et stock : la pharmacie sait ce qui se vend et ce qui manque avant la rupture.'),
            ],
            'effort': 'J\'ai construit la plateforme sur deux faces : le côté client simple — choisir la pharmacie, commander, se faire livrer — et le côté administration profond : caisse, stock, ordonnances, rapports, pharmacies multiples, matrice de permissions et journaux d\'audit. Le plus difficile n\'a pas été les écrans mais de comprendre le fonctionnement réel d\'une pharmacie : comment une vente s\'enregistre, quand le stock se déduit, et comment les droits et règlements se préservent — avec une base de données des médicaments et les références juridiques officielles.',
            'effort_stats': [('Publics servis', 'client + propriétaire + pharmaciens'), ('Modules d\'administration', 'caisse, stock, ordonnances, rapports'), ('Référence', 'règlements pharmaceutiques marocains')],
            'ops': ['React + Vite — une interface rapide à construire et à mettre à jour', 'Services back-end sur Cloudflare Workers', 'Sessions signées et permissions vérifiées', 'Journaux d\'audit des opérations sensibles', 'Cloudflare Pages pour l\'hébergement'],
            'cost_self': '0 MAD — construite sur une pile gratuite (hébergement et services back-end) avec un développement assisté par l\'IA.',
            'cost_market': 'Environ 60 000 – 180 000 MAD pour un système de gestion de pharmacie de cette profondeur : caisse, stock, ordonnances, rapports et conformité juridique.',
            'cost_now': '0 MAD par mois sur l\'offre gratuite.',
            'cost_scale': 'Un serveur et une base de données dédiés quand l\'usage s\'étend à plusieurs pharmacies : environ 200 – 700 MAD par mois.',
        },
        'tools': [
            ('React', 'Une bibliothèque de Meta pour construire des interfaces interactives : elle découpe l\'écran en petits composants réutilisables — un bouton, une carte, un tableau — pour qu\'un grand système comme une plateforme de pharmacie reste organisé et maintenable, comme des pièces rangées dans une même maison.'),
            ('Vite', 'L\'outil de construction moderne qui assemble le projet et rafraîchit l\'aperçu en une fraction de seconde au lieu de minutes d\'attente — comme une cuisine équipée qui prépare la commande dès qu\'elle arrive ; c\'est pourquoi il est devenu le standard pratique des projets React.'),
            ('Tableaux de bord graphiques', 'Des bibliothèques de graphiques transforment les chiffres en visuels — barres, courbes et cercles — pour que le pharmacien lise ventes et stock d\'un seul regard au lieu de parcourir de longs tableaux.'),
            ('Base de données des médicaments', 'Un catalogue organisé des médicaments avec leurs noms, formes et classifications : une mémoire fiable pour la plateforme — recherche rapide, informations précises, et une mise à jour centrale qui atteint tous les écrans d\'un coup.'),
            ('Lecture de codes-barres', 'Lire les barres noires imprimées sur chaque boîte de médicament : un seul scan enregistre la vente et déduit le stock automatiquement — pas de saisie manuelle, pas d\'erreurs de chiffres.'),
            ('Sessions signées (JWT)', 'Un laissez-passer numérique signé, délivré après vérification du compte et contrôlé à chaque requête — seuls ceux qui en ont le droit accèdent aux données de la pharmacie, comme un badge de personnel infalsifiable.'),
            ('Cloudflare Workers (services back-end)', 'De petits services exécutés sur le réseau mondial de Cloudflare, près de l\'utilisateur : ils reçoivent les requêtes de connexion et de données et les traitent sans serveur traditionnel — vitesse et disponibilité élevées à un coût quasi nul.'),
            ('Interface arabe RTL et police Cairo', 'La plateforme est arabe de conception, de droite à gauche, avec la police Cairo claire — pas une traduction plaquée mais un design arabe dès la base, visible dans chaque bouton et chaque tableau.'),
        ],
    },

    'es': {
        'card': {
            'name': 'PHMP',
            'tag': 'Plataforma de gestión de farmacias',
            'desc': 'Una plataforma profesional de gestión de farmacias: punto de venta, inventario, recetas e informes, más una interfaz de cliente para pedir medicamentos con entrega a domicilio.',
        },
        'page': {
            'about': 'PHMP es una plataforma de gestión de farmacias de doble cara. El lado público habla al cliente: elegir su farmacia entre las disponibles en su zona, explorar los medicamentos y pedirlos con entrega a domicilio, sin formularios complicados. El lado de administración habla al propietario y a los farmacéuticos: un punto de venta rápido con lectura de códigos de barras, seguimiento de inventario, registro de recetas, informes y paneles gráficos de ventas y operaciones, gestión de varias farmacias con una matriz de permisos precisa, registros de auditoría de cada acción sensible y referencias legales marroquíes oficiales del sector farmacéutico integradas en la plataforma, con acceso a los textos originales.',
            'tech': ['React (interfaz interactiva)', 'Vite (construcción rápida)', 'Paneles gráficos', 'Base de datos de medicamentos', 'Lectura de códigos de barras', 'Servicios back-end (Cloudflare Workers)', 'Sesiones de acceso firmadas', 'Cloudflare Pages'],
            'features': ['Interfaz de cliente para elegir farmacia y pedir medicamentos con entrega', 'Punto de venta rápido con lectura de códigos de barras', 'Seguimiento de inventario y registro de recetas', 'Informes y paneles gráficos de ventas y operaciones', 'Gestión multifarmacia con permisos y registros de auditoría', 'Referencias legales marroquíes del sector farmacéutico integradas'],
            'learned': 'Este proyecto me enseñó que el software sanitario lleva doble responsabilidad: un error en el precio o la interacción de un medicamento no es como un error en una tienda corriente. Aprendí a construir una plataforma que sirve a dos públicos muy distintos — un cliente que quiere pedir sin esfuerzo y un farmacéutico que necesita velocidad y precisión — y a equilibrarlos en un solo sistema; y que cumplir la normativa marroquí oficial no es una carga sino la base misma de la confianza en cualquier plataforma que toca la salud de las personas.',
        },
        'v4': {
            'value_intro': 'PHMP digitaliza la farmacia del mostrador al informe:',
            'values': [
                ('Una plataforma de doble cara en un solo sistema', 'El cliente pide sus medicamentos en unos toques con entrega, y el farmacéutico recibe el pedido en el mismo sistema y lo prepara — un ciclo completo sin papel.'),
                ('Códigos de barras en vez de escritura manual', 'La lectura del código de barras reduce los errores de tecleo y agiliza el punto de venta — la precisión imprescindible al manejar medicamentos.'),
                ('Cumplimiento marroquí real', 'Las referencias legales y reglamentos del sector farmacéutico marroquí están integrados en la plataforma con acceso a los textos originales — sin improvisaciones fuera de la ley.'),
                ('Decisiones basadas en números', 'Los paneles gráficos resumen ventas, operaciones e inventario: la farmacia sabe qué se vende y qué falta antes de agotarse.'),
            ],
            'effort': 'Construí la plataforma en dos caras: el lado cliente sencillo — elegir farmacia, pedir, entrega — y el lado de administración profundo: punto de venta, inventario, recetas, informes, varias farmacias, matriz de permisos y registros de auditoría. Lo más difícil no fueron las pantallas sino entender el funcionamiento real de una farmacia: cómo se registra una venta, cuándo se descuenta el stock y cómo se preservan los derechos y los reglamentos — junto con una base de datos de medicamentos y las referencias legales oficiales.',
            'effort_stats': [('Públicos atendidos', 'cliente + propietario + farmacéuticos'), ('Módulos de administración', 'TPV, inventario, recetas, informes'), ('Referencia', 'reglamentos farmacéuticos marroquíes')],
            'ops': ['React + Vite — una interfaz rápida de construir y actualizar', 'Servicios back-end en Cloudflare Workers', 'Sesiones firmadas y permisos verificados', 'Registros de auditoría de operaciones sensibles', 'Cloudflare Pages como alojamiento'],
            'cost_self': '0 MAD — construida con una pila gratuita (alojamiento y servicios back-end) y desarrollo asistido por IA.',
            'cost_market': 'Aproximadamente 60 000 – 180 000 MAD por un sistema de gestión de farmacias de esta profundidad: TPV, inventario, recetas, informes y cumplimiento legal.',
            'cost_now': '0 MAD al mes en el plan gratuito.',
            'cost_scale': 'Un servidor y base de datos dedicados cuando el uso se extienda a varias farmacias: entre 200 y 700 MAD al mes estimados.',
        },
        'tools': [
            ('React', 'Una biblioteca de Meta para construir interfaces interactivas: divide la pantalla en pequeños componentes reutilizables — un botón, una tarjeta, una tabla — para que un sistema grande como una plataforma de farmacias se mantenga ordenado y mantenible, como habitaciones ordenadas en una misma casa.'),
            ('Vite', 'La herramienta de construcción moderna que ensambla el proyecto y refresca la vista previa en fracciones de segundo en vez de minutos de espera — como una cocina equipada que prepara el pedido en cuanto llega; por eso se ha vuelto el estándar práctico de los proyectos React.'),
            ('Paneles gráficos', 'Bibliotecas de gráficos convierten los números en imágenes visuales — barras, líneas y círculos — para que el farmacéutico lea ventas y existencias de un vistazo en vez de recorrer tablas largas.'),
            ('Base de datos de medicamentos', 'Un catálogo organizado de medicamentos con sus nombres, formas y clasificaciones: una memoria fiable para la plataforma — búsqueda rápida, información precisa y una actualización central que llega a todas las pantallas a la vez.'),
            ('Lectura de códigos de barras', 'Leer las barras negras impresas en cada caja de medicamento: una sola pasada registra la venta y descuenta el stock automáticamente — sin tecleo manual ni errores de cifras.'),
            ('Sesiones firmadas (JWT)', 'Un pase digital firmado que se emite tras verificar la cuenta y se comprueba en cada petición — solo quien tiene derecho accede a los datos de la farmacia, como una credencial de empleado imposible de copiar.'),
            ('Cloudflare Workers (servicios back-end)', 'Pequeños servicios que corren en la red global de Cloudflare cerca del usuario: reciben las peticiones de acceso y datos y las procesan sin servidor tradicional — alta velocidad y disponibilidad a coste casi nulo.'),
            ('Interfaz árabe RTL y tipografía Cairo', 'La plataforma es árabe de origen, de derecha a izquierda, con la tipografía Cairo clara — no una traducción añadida sino un diseño árabe desde la base, visible en cada botón y cada tabla.'),
        ],
    },

    'it': {
        'card': {
            'name': 'PHMP',
            'tag': 'Piattaforma di gestione farmacie',
            'desc': 'Una piattaforma professionale per la gestione delle farmacie: cassa, inventario, ricette e report, più un lato cliente per ordinare farmaci dalla farmacia vicina con consegna a domicilio.',
        },
        'page': {
            'about': 'PHMP è una piattaforma di gestione farmacie a doppio lato. Il lato pubblico parla al cliente: scegliere la propria farmacia tra quelle disponibili nella zona, sfogliare i farmaci e ordinarli con consegna a domicilio, senza moduli complicati. Il lato amministrazione parla al titolare e ai farmacisti: una cassa veloce con lettura dei codici a barre, tracciamento dell\'inventario, registro delle ricette, report e dashboard grafiche di vendite e operazioni, gestione di più farmacie con una matrice di permessi precisa, registri di audit per ogni azione sensibile e i riferimenti legali marocchini ufficiali del settore farmaceutico integrati nella piattaforma, con accesso ai testi originali.',
            'tech': ['React (interfaccia interattiva)', 'Vite (build veloce)', 'Dashboard grafiche', 'Database dei farmaci', 'Lettura codici a barre', 'Servizi back-end (Cloudflare Workers)', 'Sessioni di accesso firmate', 'Cloudflare Pages'],
            'features': ['Lato cliente per scegliere la farmacia e ordinare farmaci con consegna', 'Cassa veloce con lettura dei codici a barre', 'Tracciamento inventario e registro ricette', 'Report e dashboard grafiche di vendite e operazioni', 'Gestione multifarmacia con permessi e registri di audit', 'Riferimenti legali marocchini del settore farmaceutico integrati'],
            'learned': 'Questo progetto mi ha insegnato che il software sanitario porta una responsabilità doppia: un errore nel prezzo o nell\'interazione di un farmaco non è come un errore in un negozio qualunque. Ho imparato a costruire una piattaforma che serve due pubblici molto diversi — un cliente che vuole ordinare senza sforzo e un farmacista che ha bisogno di velocità e precisione — e a bilanciarli in un unico sistema; e che la conformità ai regolamenti marocchini ufficiali non è un vincolo ma il fondamento stesso della fiducia in qualsiasi piattaforma che tocca la salute delle persone.',
        },
        'v4': {
            'value_intro': 'PHMP digitalizza la farmacia dal bancone al report:',
            'values': [
                ('Una piattaforma a doppio lato in un solo sistema', 'Il cliente ordina i farmaci in pochi tocchi con consegna, e il farmacista riceve l\'ordine nello stesso sistema e lo prepara — un ciclo completo senza carta.'),
                ('Codici a barre invece della scrittura a mano', 'La lettura del codice a barre riduce gli errori di digitazione e accelera la cassa — la precisione indispensabile quando si maneggiano farmaci.'),
                ('Conformità marocchina reale', 'I riferimenti legali e i regolamenti del settore farmaceutico marocchino sono integrati nella piattaforma con accesso ai testi originali — niente improvvisazioni fuori dalla legge.'),
                ('Decisioni basate sui numeri', 'Le dashboard grafiche riassumono vendite, operazioni e inventario: la farmacia sa cosa si vende e cosa manca prima che finisca.'),
            ],
            'effort': 'Ho costruito la piattaforma su due fronti: il lato cliente semplice — scegliere la farmacia, ordinare, farsi consegnare — e il lato amministrazione profondo: cassa, inventario, ricette, report, più farmacie, matrice di permessi e registri di audit. La parte più difficile non sono state le schermate ma capire come funziona una farmacia vera: come si registra una vendita, quando si scorpora lo stock e come si preservano i diritti e i regolamenti — insieme a un database dei farmaci e ai riferimenti legali ufficiali.',
            'effort_stats': [('Pubblici serviti', 'cliente + titolare + farmacisti'), ('Moduli di amministrazione', 'cassa, inventario, ricette, report'), ('Riferimento', 'regolamenti farmaceutici marocchini')],
            'ops': ['React + Vite — un\'interfaccia veloce da costruire e aggiornare', 'Servizi back-end su Cloudflare Workers', 'Sessioni firmate e permessi verificati', 'Registri di audit per le operazioni sensibili', 'Cloudflare Pages per l\'hosting'],
            'cost_self': '0 MAD — costruita con uno stack gratuito (hosting e servizi back-end) e sviluppo assistito dall\'IA.',
            'cost_market': 'Circa 60.000 – 180.000 MAD per un sistema di gestione farmacie di questa profondità: cassa, inventario, ricette, report e conformità legale.',
            'cost_now': '0 MAD al mese con il piano gratuito.',
            'cost_scale': 'Un server e un database dedicati quando l\'uso si estende a più farmacie: stimati 200 – 700 MAD al mese.',
        },
        'tools': [
            ('React', 'Una libreria di Meta per costruire interfacce interattive: divide lo schermo in piccoli componenti riutilizzabili — un pulsante, una card, una tabella — così un sistema grande come una piattaforma farmacie resta ordinato e manutenibile, come camere in ordine in una sola casa.'),
            ('Vite', 'Lo strumento di build moderno che assembla il progetto e aggiorna l\'anteprima in frazioni di secondo invece di minuti d\'attesa — come una cucina attrezzata che prepara l\'ordine appena arriva; per questo è diventato lo standard pratico dei progetti React.'),
            ('Dashboard grafiche', 'Librerie di grafici trasformano i numeri in visualizzazioni — barre, linee e cerchi — così il farmacista legge vendite e scorte a colpo d\'occhio invece di scorrere tabelle lunghe.'),
            ('Database dei farmaci', 'Un catalogo organizzato dei farmaci con nomi, forme e classificazioni: una memoria affidabile per la piattaforma — ricerca veloce, informazioni precise e un aggiornamento centrale che arriva a tutte le schermate in una volta.'),
            ('Lettura codici a barre', 'Leggere le barre nere stampate su ogni scatola di farmaco: una sola scansione registra la vendita e scorpora lo stock automaticamente — niente digitazione manuale, niente errori di cifre.'),
            ('Sessioni firmate (JWT)', 'Un lasciapassare digitale firmato, emesso dopo la verifica dell\'account e controllato a ogni richiesta — solo chi ne ha diritto accede ai dati della farmacia, come un badge dipendente non copiabile.'),
            ('Cloudflare Workers (servizi back-end)', 'Piccoli servizi eseguiti sulla rete globale di Cloudflare vicino all\'utente: ricevono le richieste di accesso e dati e le elaborano senza un server tradizionale — alta velocità e disponibilità a costo quasi zero.'),
            ('Interfaccia araba RTL e font Cairo', 'La piattaforma è araba per progetto, da destra a sinistra, con il font Cairo chiaro — non una traduzione appiccicata ma un design arabo fin dalle basi, visibile in ogni pulsante e ogni tabella.'),
        ],
    },

    'de': {
        'card': {
            'name': 'PHMP',
            'tag': 'Apotheken-Managementplattform',
            'desc': 'Eine professionelle Plattform für das Apothekenmanagement: Kasse, Lager, Rezepte und Berichte, dazu eine Kundenansicht, um Medikamente aus der Nähe-Apotheke mit Lieferung zu bestellen.',
        },
        'page': {
            'about': 'PHMP ist eine zweiseitige Plattform für das Apothekenmanagement. Die öffentliche Seite spricht den Kunden an: Apotheke in der Umgebung wählen, Medikamente durchstöbern und mit Lieferung bestellen — ohne komplizierte Formulare. Die Verwaltungsseite spricht den Eigentümer und die Apotheker an: eine schnelle Kasse mit Barcode-Scanning, Lagerverfolgung, Rezepterfassung, Berichte und grafische Dashboards für Verkäufe und Abläufe, Verwaltung mehrerer Apotheken mit feiner Rechte-Matrix, Audit-Protokolle für jede sensible Aktion sowie offizielle marokkanische Rechtsquellen des Pharmasektors, direkt in die Plattform eingebettet und mit Zugriff auf die Originaltexte.',
            'tech': ['React (interaktive Oberfläche)', 'Vite (schnelles Build-Tool)', 'Grafische Dashboards', 'Medikamenten-Datenbank', 'Barcode-Scanning', 'Backend-Dienste (Cloudflare Workers)', 'Signierte Anmeldesitzungen', 'Cloudflare Pages'],
            'features': ['Kundenansicht: Apotheke wählen und Medikamente mit Lieferung bestellen', 'Schnelle Kasse mit Barcode-Scanning', 'Lagerverfolgung und Rezepterfassung', 'Berichte und grafische Dashboards für Verkäufe und Abläufe', 'Mehrere Apotheken verwalten: Rechte und Audit-Protokolle', 'Marokkanische Rechtsquellen des Pharmasektors in der Plattform'],
            'learned': 'Dieses Projekt hat mir gezeigt, dass Software im Gesundheitswesen doppelte Verantwortung trägt: Ein Fehler beim Preis oder bei der Wechselwirkung eines Medikaments ist nicht wie ein Fehler in einem gewöhnlichen Laden. Ich habe gelernt, eine Plattform für zwei sehr verschiedene Seiten zu bauen — eine Kundin, die mühelos bestellen will, und einen Apotheker, der Geschwindigkeit und Präzision braucht — und beide in einem System auszubalancieren; und dass die Einhaltung der offiziellen marokkanischen Vorschriften keine Last ist, sondern das Fundament des Vertrauens in jede Plattform, die die Gesundheit der Menschen berührt.',
        },
        'v4': {
            'value_intro': 'PHMP digitalisiert die Apotheke vom Tresen bis zum Bericht:',
            'values': [
                ('Eine zweiseitige Plattform in einem System', 'Die Kundin bestellt Medikamente mit wenigen Tipps samt Lieferung, und der Apotheker erhält die Bestellung im selben System und bereitet sie vor — ein vollständiger Kreislauf ohne Papier.'),
                ('Barcode statt Handschrift', 'Das Barcode-Scanning reduziert Eingabefehler und beschleunigt die Kasse — die Genauigkeit, die beim Umgang mit Medikamenten unverzichtbar ist.'),
                ('Echte marokkanische Compliance', 'Die Rechtsquellen und Vorschriften des marokkanischen Pharmasektors sind in die Plattform eingebettet, mit Zugriff auf die Originaltexte — kein Raten außerhalb des Gesetzes.'),
                ('Entscheidungen auf Basis von Zahlen', 'Grafische Dashboards fassen Verkäufe, Abläufe und Lager zusammen: Die Apotheke weiß, was sich verkauft und was fehlt, bevor es ausgeht.'),
            ],
            'effort': 'Ich habe die Plattform auf zwei Seiten gebaut: die einfache Kundenseite — Apotheke wählen, bestellen, liefern lassen — und die tiefe Verwaltungsseite: Kasse, Lager, Rezepte, Berichte, mehrere Apotheken, eine Rechte-Matrix und Audit-Protokolle. Das Schwierigste waren nicht die Bildschirme, sondern das Verständnis einer echten Apotheke: wie ein Verkauf erfasst wird, wann das Lager abgebucht wird und wie Rechte und Vorschriften gewahrt bleiben — zusammen mit einer Medikamenten-Datenbank und den offiziellen Rechtsquellen.',
            'effort_stats': [('Bediente Seiten', 'Kunde + Eigentümer + Apotheker'), ('Verwaltungsmodule', 'Kasse, Lager, Rezepte, Berichte'), ('Referenz', 'marokkanische Arzneimittelvorschriften')],
            'ops': ['React + Vite — eine schnelle Oberfläche, die sich rasch bauen und aktualisieren lässt', 'Backend-Dienste auf Cloudflare Workers', 'Signierte Sitzungen und serverseitig geprüfte Rechte', 'Audit-Protokolle für sensible Vorgänge', 'Cloudflare Pages als Hosting'],
            'cost_self': '0 MAD — gebaut auf einem kostenlosen Stack (Hosting und Backend-Dienste) mit KI-gestützter Entwicklung.',
            'cost_market': 'Etwa 60.000 – 180.000 MAD für ein Apothekenverwaltungssystem dieser Tiefe: Kasse, Lager, Rezepte, Berichte und rechtliche Konformität.',
            'cost_now': '0 MAD pro Monat im Free-Tarif.',
            'cost_scale': 'Ein eigener Server und eine Datenbank, sobald die Nutzung auf mehrere Apotheken wächst: geschätzt 200 – 700 MAD pro Monat.',
        },
        'tools': [
            ('React', 'Eine Meta-Bibliothek für interaktive Oberflächen: Sie zerlegt den Bildschirm in kleine wiederverwendbare Bausteine — ein Knopf, eine Karte, eine Tabelle — damit ein großes System wie eine Apothekenplattform organisiert und wartbar bleibt, wie aufgeräumte Zimmer in einem Haus.'),
            ('Vite', 'Das moderne Build-Tool, das das Projekt bündelt und die Vorschau in Sekundenbruchteilen statt in Minuten Wartezeit aktualisiert — wie eine ausgestattete Küche, die die Bestellung zubereitet, sobald sie ankommt; deshalb ist es der praktische Standard für React-Projekte geworden.'),
            ('Grafische Dashboards', 'Diagramm-Bibliotheken verwandeln Zahlen in visuelle Darstellungen — Balken, Linien und Kreise —, sodass der Apotheker Verkäufe und Lager auf einen Blick liest statt lange Tabellen zu durchforsten.'),
            ('Medikamenten-Datenbank', 'Ein organisiertes Verzeichnis der Medikamente mit Namen, Formen und Klassifikationen: ein verlässliches Gedächtnis der Plattform — schnelle Suche, genaue Informationen und ein zentrales Update, das alle Bildschirme gleichzeitig erreicht.'),
            ('Barcode-Scanning', 'Die schwarzen Balken auf jeder Medikamentenschachtel lesen: Ein einziger Scan erfasst den Verkauf und bucht das Lager automatisch ab — kein manuelles Tippen, keine Zahlendreher.'),
            ('Signierte Sitzungen (JWT)', 'Ein digitaler, signierter Ausweis, der nach der Kontoprüfung ausgestellt und bei jeder Anfrage kontrolliert wird — nur wer berechtigt ist, kommt an die Daten der Apotheke, wie ein Mitarbeiterbadge, das sich nicht kopieren lässt.'),
            ('Cloudflare Workers (Backend-Dienste)', 'Kleine Dienste, die auf Cloudflares globalem Netz nahe beim Nutzer laufen: Sie empfangen Anmelde- und Datenanfragen und verarbeiten sie ohne klassischen Server — hohe Geschwindigkeit und Verfügbarkeit zu nahezu null Kosten.'),
            ('Arabische RTL-Oberfläche und Cairo-Schrift', 'Die Plattlikation ist von Grund auf arabisch, von rechts nach links, mit der klaren Cairo-Schrift — keine nachträglich angeklebte Übersetzung, sondern ein arabisches Design von der Basis her, sichtbar in jedem Knopf und jeder Tabelle.'),
        ],
    },

    'nl': {
        'card': {
            'name': 'PHMP',
            'tag': 'Apotheekbeheerplatform',
            'desc': 'Een professioneel platform voor apotheekbeheer: kassa, voorraad, recepten en rapporten, plus een klantenkant om medicijnen te bestellen bij een apotheek in de buurt, met levering.',
        },
        'page': {
            'about': 'PHMP is een tweezijdig platform voor apotheekbeheer. De openbare kant spreekt de klant aan: kies je apotheek uit de beschikbare apotheken in je regio, bekijk de medicijnen en bestel ze met levering aan huis — zonder ingewikkelde formulieren. De beheerkant spreekt de eigenaar en apothekers aan: een snelle kassa met barcode-scanning, voorraadopvolging, registratie van recepten, rapporten en grafische dashboards van verkopen en activiteiten, beheer van meerdere apotheken met een fijnmazige rechtenmatrix, auditlogboeken voor elke gevoelige handeling, en de officiële Marokkaanse wettelijke referenties van de farmasector, ingebouwd in het platform, met toegang tot de originele teksten.',
            'tech': ['React (interactieve interface)', 'Vite (snelle build)', 'Grafische dashboards', 'Medicijndatabase', 'Barcode-scanning', 'Back-enddiensten (Cloudflare Workers)', 'Ondertekende sessies', 'Cloudflare Pages'],
            'features': ['Klantenkant om een apotheek te kiezen en medicijnen te bestellen met levering', 'Snelle kassa met barcode-scanning', 'Voorraadopvolging en receptregistratie', 'Rapporten en grafische dashboards van verkopen en activiteiten', 'Beheer van meerdere apotheken met rechten en auditlogboeken', 'Marokkaanse wettelijke referenties van de farmasector in het platform'],
            'learned': 'Dit project leerde me dat software in de gezondheidszorg dubbele verantwoordelijkheid draagt: een fout in de prijs of wisselwerking van een medicijn is niet hetzelfde als een fout in een gewone winkel. Ik leerde een platform bouwen dat twee heel verschillende kanten bedient — een klant die moeiteloos wil bestellen en een apotheker die snelheid en precisie nodig heeft — en beide in balans te houden binnen één systeem; en dat naleving van de officiële Marokkaanse regelgeving geen beperking is maar het fundament van vertrouwen in elk platform dat de gezondheid van mensen raakt.',
        },
        'v4': {
            'value_intro': 'PHMP digitaliseert de apotheek, van de toonbank tot het rapport:',
            'values': [
                ('Een tweezijdig platform in één systeem', 'De klant bestelt medicijnen in een paar tikken met levering, en de apotheker ontvangt de bestelling in hetzelfde systeem en bereidt ze voor — een volledige cyclus zonder papier.'),
                ('Barcodes in plaats van handschrift', 'Barcode-scanning vermindert invoerfouten en versnelt de kassa — de nauwkeurigheid die onmisbaar is bij het werken met medicijnen.'),
                ('Echte Marokkaanse naleving', 'De wettelijke referenties en regelgeving van de Marokkaanse farmasector zijn in het platform ingebouwd, met toegang tot de originele teksten — geen giswerk buiten de wet.'),
                ('Beslissingen gebaseerd op cijfers', 'Grafische dashboards vatten verkopen, activiteiten en voorraad samen: de apotheek weet wat verkoopt en wat ontbreekt, vóór het op is.'),
            ],
            'effort': 'Ik bouwde het platform op twee gezichten: de eenvoudige klantenkant — apotheek kiezen, bestellen, laten leveren — en de diepe beheerkant: kassa, voorraad, recepten, rapporten, meerdere apotheken, een rechtenmatrix en auditlogboeken. Het moeilijkste waren niet de schermen, maar het begrijpen van hoe een echte apotheek werkt: hoe een verkoop wordt geregistreerd, wanneer de voorraad wordt afgeboekt en hoe rechten en regels bewaard blijven — samen met een medicijndatabase en de officiële wettelijke referenties.',
            'effort_stats': [('Bediende kanten', 'klant + eigenaar + apothekers'), ('Beheermodules', 'kassa, voorraad, recepten, rapporten'), ('Referentie', 'Marokkaanse farmaregelgeving')],
            'ops': ['React + Vite — een snelle interface die vlot bouwt en actualiseert', 'Back-enddiensten op Cloudflare Workers', 'Ondertekende sessies en gecontroleerde rechten', 'Auditlogboeken voor gevoelige handelingen', 'Cloudflare Pages als hosting'],
            'cost_self': '0 MAD — gebouwd op een gratis stack (hosting en back-enddiensten) met AI-ondersteunde ontwikkeling.',
            'cost_market': 'Ongeveer 60.000 – 180.000 MAD voor een apotheekbeheersysteem van deze diepgang: kassa, voorraad, recepten, rapporten en wettelijke naleving.',
            'cost_now': '0 MAD per maand in het gratis pakket.',
            'cost_scale': 'Een eigen server en database zodra het gebruik zich over meerdere apotheken uitbreidt: geschat 200 – 700 MAD per maand.',
        },
        'tools': [
            ('React', 'Een Meta-bibliotheek voor interactieve interfaces: ze verdeelt het scherm in kleine herbruikbare onderdelen — een knop, een kaart, een tabel — zodat een groot systeem als een apotheekplatform georganiseerd en onderhoudbaar blijft, als opgeruimde kamers in één huis.'),
            ('Vite', 'De moderne build-tool die het project bundelt en de voorverversing in een fractie van een seconde actualiseert in plaats van minuten wachten — als een voluitgeruste keuken die de bestelling bereidt zodra ze binnenkomt; daarom is het de praktische standaard voor React-projecten.'),
            ('Grafische dashboards', 'Grafiekbibliotheken zetten cijfers om in visuele voorstellingen — balken, lijnen en cirkels — zodat de apotheker verkopen en voorraad in één oogopslag leest in plaats van lange tabellen door te spitten.'),
            ('Medicijndatabase', 'Een georganiseerde catalogus van medicijnen met namen, vormen en classificaties: een betrouwbaar geheugen voor het platform — snel zoeken, nauwkeurige informatie en één centrale update die alle schermen tegelijk bereikt.'),
            ('Barcode-scanning', 'De zwarte streepjes lezen die op elke medicijnverpakking staan: één scan registreert de verkoop en boekt de voorraad automatisch af — geen handmatig typen, geen cijferfouten.'),
            ('Ondertekende sessies (JWT)', 'Een digitaal, ondertekend toegangsbewijs dat na verificatie van het account wordt uitgegeven en bij elk verzoek wordt gecontroleerd — alleen wie het recht heeft, komt bij de gegevens van de apotheek, zoals een personeelsbadge die niet te kopiëren is.'),
            ('Cloudflare Workers (back-enddiensten)', 'Kleine diensten die op Cloudflares wereldwijde netwerk dicht bij de gebruiker draaien: ze ontvangen inlog- en gegevensverzoeken en verwerken die zonder traditionele server — hoge snelheid en beschikbaarheid tegen vrijwel geen kosten.'),
            ('Arabische RTL-interface en Cairo-lettertype', 'Het platform is van oorsprong Arabisch, van rechts naar links, met het heldere Cairo-lettertype — geen achteraf geplakte vertaling maar een Arabisch ontwerp vanaf de basis, zichtbaar in elke knop en elke tabel.'),
        ],
    },

    'pt': {
        'card': {
            'name': 'PHMP',
            'tag': 'Plataforma de gestão de farmácias',
            'desc': 'Uma plataforma profissional de gestão de farmácias: ponto de venda, inventário, receitas e relatórios, mais um lado cliente para encomendar medicamentos da farmácia da zona, com entrega.',
        },
        'page': {
            'about': 'A PHMP é uma plataforma de gestão de farmácias de dois lados. O lado público fala com o cliente: escolher a sua farmácia entre as disponíveis na sua zona, navegar pelos medicamentos e encomendá-los com entrega ao domicílio — sem formulários complicados. O lado de administração fala com o proprietário e os farmacêuticos: um ponto de venda rápido com leitura de códigos de barras, acompanhamento do inventário, registo de receitas, relatórios e painéis gráficos de vendas e operações, gestão de várias farmácias com uma matriz de permissões fina, registos de auditoria para cada ação sensível e as referências legais marroquinas oficiais do setor farmacêutico integradas na plataforma, com acesso aos textos originais.',
            'tech': ['React (interface interativa)', 'Vite (compilação rápida)', 'Painéis gráficos', 'Base de dados de medicamentos', 'Leitura de códigos de barras', 'Serviços back-end (Cloudflare Workers)', 'Sessões de entrada assinadas', 'Cloudflare Pages'],
            'features': ['Lado cliente para escolher a farmácia e encomendar medicamentos com entrega', 'Ponto de venda rápido com leitura de códigos de barras', 'Acompanhamento de inventário e registo de receitas', 'Relatórios e painéis gráficos de vendas e operações', 'Gestão multi-farmácia com permissões e registos de auditoria', 'Referências legais marroquinas do setor farmacêutico na plataforma'],
            'learned': 'Este projeto ensinou-me que o software na saúde traz responsabilidade dobrada: um erro no preço ou na interação de um medicamento não é como um erro numa loja comum. Aprendi a construir uma plataforma que serve dois públicos muito diferentes — um cliente que quer encomendar sem esforço e um farmacêutico que precisa de velocidade e precisão — e a equilibrá-los num só sistema; e que a conformidade com os regulamentos marroquinos oficiais não é uma restrição mas o próprio fundamento da confiança em qualquer plataforma que toca a saúde das pessoas.',
        },
        'v4': {
            'value_intro': 'A PHMP digitaliza a farmácia do balcão ao relatório:',
            'values': [
                ('Uma plataforma de dois lados num só sistema', 'O cliente encomenda os medicamentos em poucos toques com entrega, e o farmacêutico recebe a encomenda no mesmo sistema e prepara-a — um ciclo completo sem papel.'),
                ('Códigos de barras em vez de escrita à mão', 'A leitura do código de barras reduz os erros de introdução e acelera o ponto de venda — a precisão indispensável quando se manuseiam medicamentos.'),
                ('Conformidade marroquina real', 'As referências legais e regulamentos do setor farmacêutico marroquino estão integrados na plataforma, com acesso aos textos originais — sem palpites fora da lei.'),
                ('Decisões baseadas em números', 'Os painéis gráficos resumem vendas, operações e inventário: a farmácia sabe o que se vende e o que falta antes de esgotar.'),
            ],
            'effort': 'Construí a plataforma em duas faces: o lado cliente simples — escolher a farmácia, encomendar, receber em casa — e o lado de administração profundo: ponto de venda, inventário, receitas, relatórios, várias farmácias, uma matriz de permissões e registos de auditoria. A parte mais difícil não foram os ecrãs, mas compreender como funciona uma farmácia real: como se registra uma venda, quando se desconta o stock e como se preservam os direitos e os regulamentos — junto com uma base de dados de medicamentos e as referências legais oficiais.',
            'effort_stats': [('Lados servidos', 'cliente + proprietário + farmacêuticos'), ('Módulos de administração', 'PDV, inventário, receitas, relatórios'), ('Referência', 'regulamentos farmacêuticos marroquinos')],
            'ops': ['React + Vite — uma interface rápida de compilar e atualizar', 'Serviços back-end no Cloudflare Workers', 'Sessões assinadas e permissões verificadas', 'Registos de auditoria das operações sensíveis', 'Cloudflare Pages como alojamento'],
            'cost_self': '0 MAD — construída numa pilha gratuita (alojamento e serviços back-end) com desenvolvimento assistido por IA.',
            'cost_market': 'Aproximadamente 60 000 – 180 000 MAD por um sistema de gestão de farmácias desta profundidade: PDV, inventário, receitas, relatórios e conformidade legal.',
            'cost_now': '0 MAD por mês no plano gratuito.',
            'cost_scale': 'Um servidor e uma base de dados dedicados quando a utilização se estende a várias farmácias: estimados 200 – 700 MAD por mês.',
        },
        'tools': [
            ('React', 'Uma biblioteca da Meta para construir interfaces interativas: divide o ecrã em pequenos componentes reutilizáveis — um botão, um cartão, uma tabela — para que um sistema grande como uma plataforma de farmácias se mantenha organizado e sustentável, como quartos arrumados numa só casa.'),
            ('Vite', 'A ferramenta de compilação moderna que agrupa o projeto e atualiza a pré-visualização em frações de segundo em vez de minutos de espera — como uma cozinha equipada que prepara o pedido assim que chega; por isso tornou-se o padrão prático dos projetos React.'),
            ('Painéis gráficos', 'Bibliotecas de gráficos transformam os números em visualizações — barras, linhas e círculos — para que o farmacêutico leia vendas e stock num relance em vez de percorrer tabelas longas.'),
            ('Base de dados de medicamentos', 'Um catálogo organizado de medicamentos com nomes, formas e classificações: uma memória fiável para a plataforma — pesquisa rápida, informação precisa e uma atualização central que chega a todos os ecrãs de uma vez.'),
            ('Leitura de códigos de barras', 'Ler as barras pretas impressas em cada caixa de medicamento: uma única leitura registra a venda e desconta o stock automaticamente — sem escrita manual, sem erros de números.'),
            ('Sessões assinadas (JWT)', 'Um passe digital assinado, emitido após a verificação da conta e conferido em cada pedido — só quem tem direito chega aos dados da farmácia, como um crachá de funcionário que não se copia.'),
            ('Cloudflare Workers (serviços back-end)', 'Pequenos serviços que correm na rede global da Cloudflare perto do utilizador: recebem os pedidos de entrada e de dados e processam-nos sem um servidor tradicional — alta velocidade e disponibilidade a custo quase zero.'),
            ('Interface árabe RTL e tipo de letra Cairo', 'A plataforma é árabe de origem, da direita para a esquerda, com o tipo de letra Cairo claro — não é uma tradução acrescentada mas um desenho árabe desde a base, visível em cada botão e cada tabela.'),
        ],
    },
}

# ---------- count fixes: six -> seven (pj_sub, desc meta, chatbot texts) ----------
COUNT_FIX = {
    'ar': [
        ('ستة مشاريع حيّة بنيتها', 'سبعة مشاريع حيّة بنيتها'),
        ('وستة مشاريع رقمية حيّة', 'وسبعة مشاريع رقمية حيّة'),
        ('(6 مشاريع حية)', '(7 مشاريع حية)'),
        ('ستة مشاريع رقمية حية بناها طارق', 'سبعة مشاريع رقمية حية بناها طارق'),
    ],
    'en': [
        ('Six live projects I built', 'Seven live projects I built'),
        ('and six live digital projects', 'and seven live digital projects'),
        ('six live digital projects', 'seven live digital projects'),
        ('(6 live projects)', '(7 live projects)'),
        ('Six live digital projects Tarik built', 'Seven live digital projects Tarik built'),
    ],
    'fr': [
        ("Six projets en ligne que j'ai réalisés", "Sept projets en ligne que j'ai réalisés"),
        ('six projets numériques', 'sept projets numériques'),
        ('Six projets numériques en ligne', 'Sept projets numériques en ligne'),
        ('(6 projets en ligne)', '(7 projets en ligne)'),
    ],
    'es': [
        ('Seis proyectos en línea que construí', 'Siete proyectos en línea que construí'),
        ('seis proyectos digitales', 'siete proyectos digitales'),
        ('Seis proyectos digitales en línea', 'Siete proyectos digitales en línea'),
        ('(6 proyectos en línea)', '(7 proyectos en línea)'),
    ],
    'it': [
        ('Sei progetti online realizzati', 'Sette progetti online realizzati'),
        ('sei progetti digitali', 'sette progetti digitali'),
        ('Sei progetti digitali online', 'Sette progetti digitali online'),
        ('(6 progetti online)', '(7 progetti online)'),
    ],
    'de': [
        ('Sechs Live-Projekte, die ich', 'Sieben Live-Projekte, die ich'),
        ('sechs digitale Projekte', 'sieben digitale Projekte'),
        ('Sechs digitale Live-Projekte', 'Sieben digitale Live-Projekte'),
        ('(6 Live-Projekte)', '(7 Live-Projekte)'),
    ],
    'nl': [
        ('Zes live projecten die ik', 'Zeven live projecten die ik'),
        ('zes digitale projecten', 'zeven digitale projecten'),
        ('Zes digitale liveprojecten', 'Zeven digitale liveprojecten'),
        ('(6 live projecten)', '(7 live projecten)'),
    ],
    'pt': [
        ('Seis projetos online que construí', 'Sete projetos online que construí'),
        ('seis projetos digitais', 'sete projetos digitais'),
        ('Seis projetos digitais online', 'Sete projetos digitais online'),
        ('(6 projetos online)', '(7 projetos online)'),
    ],
}

# ---------- chatbot a_projects: PHMP bullet inserted before the closing sentence ----------
A_PROJECTS_BULLET = {
    'ar': '• <a href="https://phmp.pages.dev" target="_blank" rel="noopener">PHMP</a> — منصة إدارة الصيدليات: نقطة بيع ومخزون ووصفات وتقارير<br>',
    'en': '• <a href="https://phmp.pages.dev" target="_blank" rel="noopener">PHMP</a> — pharmacy management platform: POS, inventory, prescriptions and reports<br>',
    'fr': '• <a href="https://phmp.pages.dev" target="_blank" rel="noopener">PHMP</a> — plateforme de gestion de pharmacie : caisse, stock, ordonnances et rapports<br>',
    'es': '• <a href="https://phmp.pages.dev" target="_blank" rel="noopener">PHMP</a> — plataforma de gestión de farmacias: TPV, inventario, recetas e informes<br>',
    'it': '• <a href="https://phmp.pages.dev" target="_blank" rel="noopener">PHMP</a> — piattaforma di gestione farmacie: cassa, inventario, ricette e report<br>',
    'de': '• <a href="https://phmp.pages.dev" target="_blank" rel="noopener">PHMP</a> — Apotheken-Managementplattform: Kasse, Lager, Rezepte und Berichte<br>',
    'nl': '• <a href="https://phmp.pages.dev" target="_blank" rel="noopener">PHMP</a> — apotheekbeheerplatform: kassa, voorraad, recepten en rapporten<br>',
    'pt': '• <a href="https://phmp.pages.dev" target="_blank" rel="noopener">PHMP</a> — plataforma de gestão de farmácias: PDV, inventário, receitas e relatórios<br>',
}
A_PROJECTS_TAIL_MARK = {
    'ar': 'التفاصيل الكاملة', 'en': 'Full details', 'fr': 'Détails complets',
    'es': 'Detalles completos', 'it': 'Dettagli completi', 'de': 'Alle Details',
    'nl': 'Volledige details', 'pt': 'Detalhes completos',
}

# ---------- chatbot keywords: add PHMP terms ----------
KW_ADD = {
    'ar': ['phmp', 'صيدلية', 'صيدليات', 'أدوية', 'دواء'],
    'en': ['phmp', 'pharmacy'],
    'fr': ['phmp', 'pharmacie'],
    'es': ['phmp', 'farmacia'],
    'it': ['phmp', 'farmacia'],
    'de': ['phmp', 'apotheke'],
    'nl': ['phmp', 'apotheek'],
    'pt': ['phmp', 'farmácia'],
}
