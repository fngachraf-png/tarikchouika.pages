#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""EPDP project content for all 8 languages (v8).
Structure per language: card / page / v4 / tools."""

EPDP = {}

# ================================ ARABIC ================================
EPDP['ar'] = {
    'card': {
        'name': 'EPDP — كاتبك الرقمي',
        'tag': 'منصة الوثائق الإدارية المغربية',
        'desc': 'منصة مجانية تجمع أكثر من 1180 نموذجاً ووثيقة إدارية مغربية رسمية بالعربية والفرنسية — من طلبات CNSS والضرائب إلى العقود والوكالات — مع دليل البوابات الرسمية ومساعد ذكي يجيب من مصادر موثقة.',
    },
    'page': {
        'about': 'EPDP — «كاتبك الرقمي» — منصة مغربية ترقمن خدمات الكاتب العمومي: مكتبة من أكثر من 1180 نموذجاً ووثيقة إدارية رسمية بالعربية والفرنسية — طلبات موجهة للإدارات، شكايات، عقود كراء وبيع، وكالات، تصاريح بالشرف، سير ذاتية — منظمة في 19 فئة إدارية تغطي الضمان الاجتماعي والضرائب والعقود وغيرها. إلى جانب المكتبة: دليل شامل لبوابات أكثر من 38 جهة رسمية مغربية، ومساعد ذكي يجيب من مصادر موثقة بدون هلوسة، ومساعد يملأ وثيقتك ببياناتك ويحررها بشكل احترافي — كل ذلك مجاناً بالكامل ودون تسجيل.',
        'tech': ['Next.js (إطار عمل حديث)', 'React (واجهة تفاعلية)', 'خطا Cairo وNoto Kufi Arabic', 'تصميم عربي أصلي RTL', 'تخزين محلي للتفضيلات', 'بنية وثائق في 19 فئة', 'مساعد ذكي مقيد بالمصادر', 'Cloudflare Pages (الاستضافة)'],
        'features': [
            'مكتبة تضم أكثر من 1180 نموذجاً ووثيقة إدارية رسمية بالعربية والفرنسية',
            '19 فئة إدارية: من الضرائب والضمان الاجتماعي إلى العقود والشكايات',
            'دليل موثق لأكثر من 38 جهة رسمية مغربية مع الروابط المباشرة',
            'مساعد ذكي يجيب من مصادر رسمية موثقة — بدون معلومات مخترعة',
            'ملء الوثائق آلياً ببياناتك مع تحرير احترافي جاهز للطباعة',
            'مجاني بالكامل، بدون تسجيل، وبواجهة في 7 لغات',
        ],
        'learned': 'علّمني EPDP أن قيمة المنتج الرقمي تُقاس بمقدار الوقت الذي يوفره على الناس: كل دقيقة يختصرها المواطن في البحث عن وثيقته هي المكسب الحقيقي. وتعلمت الانضباط في المعلومة — حين تتعامل مع وثائق رسمية لا مجال للتقريب: كل نموذج يجب أن يطابق مصدره، وإلا فقدت المنصة معناها. كما تعلمت تصميم تجربة ثنائية اللغة (عربية/فرنسية) تحترم طريقة عمل الإدارة المغربية وتبسّطها للمواطن.',
    },
    'v4': {
        'value_intro': 'EPDP يختصر على المواطن المغربي طريق الوثيقة الإدارية:',
        'values': [
            ('مكتبة وطنية في رابط واحد', 'أكثر من 1180 نموذجاً رسمياً في مكان واحد بدل التنقيب بين المواقع والشبابيك: من طلب الضمان الاجتماعي إلى عقد كراء جاهز بالعربية والفرنسية.'),
            ('خريطة البوابات الرسمية', 'دليل مرتب لأكثر من 38 جهة رسمية (ضرائب، ضمان اجتماعي، عدل، جماعات...) مع الرابط المباشر لكل واحدة — الوصول الصحيح من المحاولة الأولى.'),
            ('أجوبة من مصادر موثقة لا من الخيال', 'المساعد الذكي مضبوط على المصادر الرسمية فقط: إن لم توجد الإجابة فيها يقول ذلك بوضوح — ثقة تُبنى على الدقة.'),
            ('وثيقتك جاهزة في دقائق', 'أدخل بياناتك مرة واحدة فيتولى المساعد ملء النموذج وتحريره — تنزّله مطبوعاً بشكل لائق جاهزاً للتوقيع والإيداع.'),
        ],
        'effort': 'أكبر عمل في EPDP ليس الشاشات بل المضمون: جمع وتدقيق أكثر من 1180 وثيقة ونموذج من مصادرها الرسمية، وتصنيفها في 19 فئة بمنطق يفهمه المواطن لا الإدارة، مع الحرص على النسختين العربية والفرنسية لكل وثيقة. فوق ذلك بنيت المنصة نفسها: بحث سريع، وتبديل لغات محفوظ، ومساعد ذكي مقيد بمصادر رسمية حتى لا يخترع جواباً — لأن الثقة في منصة كهذه أهم من كثرة الميزات.',
        'effort_stats': [('الوثائق والنماذج', 'أكثر من 1180'), ('الفئات الإدارية', '19 فئة'), ('الجهات الرسمية المرجعية', 'أكثر من 38')],
        'ops': [
            'Next.js — بنية حديثة سريعة وسهلة التطوير',
            'خطوط عربية احترافية (Cairo وNoto Kufi)',
            'تخزين محلي لتفضيلات المستخدم دون تسجيل',
            'مساعد ذكي مقيد بالمصادر الرسمية',
            'Cloudflare Pages للتشغيل والنشر',
        ],
        'cost_self': '0 درهم — بُنيت على منظومة مجانية (استضافة ونشر) بمساعدة أدوات الذكاء الاصطناعي في التطوير والتجميع.',
        'cost_market': 'منصة وثائق إدارية بهذا الحجم (مكتبة موثقة + دليل جهات + مساعد ذكي): تقديرياً 80,000 – 250,000 درهم عند تطويرها تجارياً.',
        'cost_now': '0 درهم شهرياً ضمن الباقة المجانية.',
        'cost_scale': 'عند النمو الواسع (بحث أسرع وقاعدة بيانات وخدمات خلفية): تقديرياً 200 – 800 درهم شهرياً.',
    },
    'tools': [
        ('Next.js', 'إطار عمل حديث مبني فوق React: يُنتج صفحات سريعة التحميل وسهلة الفهرسة في محركات البحث، ويُحدّث الجزء المتغير فقط دون إعادة تحميل الصفحة كاملة.'),
        ('React', 'مكتبة ميتا لواجهات المستخدم: تقسّم الصفحة إلى مكونات صغيرة قابلة لإعادة الاستخدام — زر، بطاقة، قائمة — فيبقى الموقع متسقاً وسهل التطوير.'),
        ('خطا Cairo وNoto Kufi Arabic', 'خطان عربيان احترافيان مصممان للشاشات: حروف واضحة في كل الأحجام، تمنح النصوص الإدارية هيبة وسهولة قراءة.'),
        ('التصميم العربي أولاً (RTL)', 'المنصة مصممة أصلاً من اليمين إلى اليسار ثم تُضاف اللغات الأخرى — ليست ترجمة معكوسة بل تصميم عربي صحيح منذ البداية.'),
        ('التخزين المحلي (localStorage)', 'ذاكرة صغيرة داخل متصفحك تحفظ اختيارك للغة والإعدادات: تعود فتجد المنصة كما تركتها، دون حساب ودون تسجيل.'),
        ('تنظيم الوثائق في 19 فئة', 'كل وثيقة مصنفة (ضرائب، ضمان اجتماعي، عقود، شكايات...) فتجد ما تبحث عنه في نقرتين بدل التنقيب في مئات الملفات.'),
        ('المساعد الذكي المقيد بالمصادر', 'مساعد يجيب حصراً من وثائق ومصادر رسمية مضبوطة سلفاً: إن لم توجد الإجابة في المصدر يقول ذلك بصراحة بدل اختراع جواب — هذا هو العلاج العملي للهلوسة.'),
        ('Cloudflare Pages', 'خدمة الاستضافة العالمية التي تقدّم المنصة من نقاط قريبة من المستخدم في كل الدول: فتح سريع في المغرب وخارجه، مع شهادة أمان وتحديث فوري عند كل نسخة جديدة.'),
    ],
}

# ================================ ENGLISH ================================
EPDP['en'] = {
    'card': {
        'name': 'EPDP — Your Digital Scribe',
        'tag': 'Moroccan administrative documents platform',
        'desc': 'A free platform gathering 1,180+ official Moroccan administrative forms and documents in Arabic and French — from CNSS and tax requests to contracts and proxies — with an official-portals guide and a smart assistant answering from verified sources.',
    },
    'page': {
        'about': 'EPDP — “Your Digital Scribe” — is a Moroccan platform that digitizes the services of the traditional public scribe: a library of more than 1,180 official administrative forms and documents in Arabic and French — requests addressed to administrations, complaints, rental and sale contracts, proxies, honor declarations, CVs — organized into 19 administrative categories covering social security, taxes, contracts and more. Alongside the library: a comprehensive guide to the portals of 38+ official Moroccan entities, a smart assistant that answers from verified sources without hallucination, and an assistant that fills your document with your data and formats it professionally — all completely free and without registration.',
        'tech': ['Next.js (modern framework)', 'React (interactive interface)', 'Cairo + Noto Kufi Arabic fonts', 'Native Arabic-first RTL design', 'Local preferences storage', '19-category document architecture', 'Source-restricted smart assistant', 'Cloudflare Pages (hosting)'],
        'features': [
            'Library of 1,180+ official administrative forms in Arabic and French',
            '19 administrative categories: from taxes and social security to contracts and complaints',
            'Verified guide to 38+ official Moroccan entities with direct links',
            'Smart assistant answering from verified official sources — no invented information',
            'Automatic document filling with your data, professionally formatted for printing',
            'Completely free, no registration, interface in 7 languages',
        ],
        'learned': "EPDP taught me that a digital product's value is measured by the time it saves people: every minute a citizen saves looking for a document is the real gain. I learned discipline with information — when you handle official documents there is no room for approximation: every form must match its source, or the platform loses its meaning. I also learned to design a bilingual (Arabic/French) experience that respects how the Moroccan administration works while simplifying it for the citizen.",
    },
    'v4': {
        'value_intro': 'EPDP shortens the citizen\u2019s path to administrative documents:',
        'values': [
            ('A national library in one link', 'More than 1,180 official forms in one place instead of digging through websites and counters: from a social-security request to a ready rental contract, in Arabic and French.'),
            ('A map of official portals', 'An organized guide to 38+ official entities (taxes, social security, justice, municipalities...) with the direct link to each one — the right door on the first try.'),
            ('Answers from verified sources, not imagination', 'The smart assistant is restricted to official sources only: if the answer is not there, it says so clearly — trust built on accuracy.'),
            ('Your document ready in minutes', 'Enter your data once and the assistant fills the form and formats it — you download it properly printed, ready to sign and submit.'),
        ],
        'effort': 'The biggest work in EPDP was not the screens but the content: collecting and verifying more than 1,180 forms and documents from their official sources, classifying them into 19 categories with logic a citizen understands rather than an administration, and carefully maintaining both the Arabic and French versions of every document. On top of that I built the platform itself: fast search, persistent language switching, and a smart assistant restricted to official sources so it never invents an answer — because trust matters more here than feature count.',
        'effort_stats': [('Documents and forms', 'More than 1,180'), ('Administrative categories', '19 categories'), ('Official reference entities', 'More than 38')],
        'ops': [
            'Next.js — a fast, modern, maintainable architecture',
            'Professional Arabic fonts (Cairo and Noto Kufi)',
            'Local storage of user preferences without registration',
            'Smart assistant restricted to official sources',
            'Cloudflare Pages for hosting and deployment',
        ],
        'cost_self': '0 dirhams — built on a free ecosystem (hosting and deployment) with the help of AI tools in development and compilation.',
        'cost_market': 'An administrative-documents platform of this scale (verified library + entities guide + smart assistant): roughly 80,000 – 250,000 dirhams if developed commercially.',
        'cost_now': '0 dirhams per month on the free plan.',
        'cost_scale': 'At wide adoption (faster search, database and backend services): an estimated 200 – 800 dirhams per month.',
    },
    'tools': [
        ('Next.js', 'A modern framework built on top of React: it produces fast-loading pages that search engines index easily, and updates only the part that changes instead of reloading the whole page.'),
        ('React', "Meta's interface library: it splits the page into small reusable components — a button, a card, a list — so the site stays consistent and easy to develop."),
        ('Cairo and Noto Kufi Arabic fonts', 'Two professional Arabic typefaces designed for screens: clear letters at every size, giving administrative texts dignity and readability.'),
        ('Arabic-first design (RTL)', 'The platform is designed right-to-left from the start, then other languages are added — not a reversed translation but a properly Arabic design.'),
        ('Local storage (localStorage)', 'A small memory inside your browser that remembers your language and preferences: you come back and find the platform as you left it — no account, no registration.'),
        ('Documents organized into 19 categories', 'Every document is classified (taxes, social security, contracts, complaints...) so you find what you need in two clicks instead of digging through hundreds of files.'),
        ('The source-restricted smart assistant', 'An assistant that answers exclusively from officially verified documents and sources chosen in advance: if the answer is not there, it says so honestly instead of inventing one — the practical cure for hallucination.'),
        ('Cloudflare Pages', 'The global hosting service that serves the platform from points close to users in every country: fast loading in Morocco and abroad, with security certificates and instant updates on every new release.'),
    ],
}

# ================================ FRENCH ================================
EPDP['fr'] = {
    'card': {
        'name': 'EPDP — Votre scribe numérique',
        'tag': 'Plateforme de documents administratifs marocains',
        'desc': 'Une plateforme gratuite réunissant plus de 1 180 formulaires et documents administratifs marocains officiels en arabe et en français — de la CNSS aux impôts, contrats et procurations — avec un guide des portails officiels et un assistant intelligent qui répond à partir de sources vérifiées.',
    },
    'page': {
        'about': 'EPDP — « Votre scribe numérique » — est une plateforme marocaine qui numérise les services du scribe public traditionnel : une bibliothèque de plus de 1 180 formulaires et documents administratifs officiels en arabe et en français — demandes adressées aux administrations, réclamations, contrats de location et de vente, procurations, déclarations sur l\u2019honneur, CV — organisés en 19 catégories administratives couvrant la sécurité sociale, les impôts, les contrats et plus. À côté de la bibliothèque : un guide complet des portails de plus de 38 entités officielles marocaines, un assistant intelligent qui répond à partir de sources vérifiées sans hallucination, et un assistant qui remplit votre document avec vos données et le met en forme professionnellement — le tout entièrement gratuitement et sans inscription.',
        'tech': ['Next.js (framework moderne)', 'React (interface interactive)', 'Polices Cairo + Noto Kufi Arabic', 'Conception arabe d\u2019abord (RTL)', 'Stockage local des préférences', 'Architecture documentaire en 19 catégories', 'Assistant intelligent restreint aux sources', 'Cloudflare Pages (hébergement)'],
        'features': [
            'Bibliothèque de plus de 1 180 formulaires administratifs officiels en arabe et en français',
            '19 catégories administratives : des impôts et de la sécurité sociale aux contrats et réclamations',
            'Guide vérifié de plus de 38 entités officielles marocaines avec liens directs',
            'Assistant intelligent répondant à partir de sources officielles vérifiées — sans information inventée',
            'Remplissage automatique des documents avec vos données, mise en forme professionnelle prête à imprimer',
            'Entièrement gratuit, sans inscription, interface en 7 langues',
        ],
        'learned': 'EPDP m\u2019a appris que la valeur d\u2019un produit numérique se mesure au temps qu\u2019il fait gagner aux gens : chaque minute que le citoyen économise en cherchant son document est le vrai gain. J\u2019ai appris la rigueur de l\u2019information — face à des documents officiels, aucun approximatif n\u2019est permis : chaque formulaire doit correspondre à sa source, sinon la plateforme perd son sens. J\u2019ai aussi appris à concevoir une expérience bilingue (arabe/français) qui respecte le fonctionnement de l\u2019administration marocaine tout en le simplifiant pour le citoyen.',
    },
    'v4': {
        'value_intro': 'EPDP raccourcit le chemin du citoyen vers le document administratif :',
        'values': [
            ('Une bibliothèque nationale en un seul lien', 'Plus de 1 180 formulaires officiels au même endroit, au lieu de fouiller sites et guichets : d\u2019une demande de sécurité sociale à un contrat de location prêt à l\u2019emploi, en arabe et en français.'),
            ('Une carte des portails officiels', 'Un guide ordonné de plus de 38 entités officielles (impôts, sécurité sociale, justice, communes...) avec le lien direct de chacune — la bonne porte dès le premier essai.'),
            ('Des réponses de sources vérifiées, pas d\u2019imaginaire', 'L\u2019assistant intelligent est limité aux sources officielles : si la réponse ne s\u2019y trouve pas, il le dit clairement — une confiance bâtie sur la précision.'),
            ('Votre document prêt en quelques minutes', 'Saisissez vos données une fois : l\u2019assistant remplit le formulaire et le met en forme — vous le téléchargez proprement imprimé, prêt à signer et à déposer.'),
        ],
        'effort': 'Le plus gros travail dans EPDP n\u2019est pas les écrans mais le contenu : collecter et vérifier plus de 1 180 formulaires et documents auprès de leurs sources officielles, les classer en 19 catégories avec une logique que le citoyen comprend — pas l\u2019administration — et veiller aux versions arabe et française de chaque document. Par-dessus cela, j\u2019ai bâti la plateforme elle-même : recherche rapide, changement de langue mémorisé, et un assistant intelligent restreint aux sources officielles pour qu\u2019il n\u2019invente jamais de réponse — car ici la confiance compte plus que le nombre de fonctions.',
        'effort_stats': [('Documents et formulaires', 'Plus de 1 180'), ('Catégories administratives', '19 catégories'), ('Entités officielles de référence', 'Plus de 38')],
        'ops': [
            'Next.js — une architecture moderne, rapide et maintenable',
            'Polices arabes professionnelles (Cairo et Noto Kufi)',
            'Stockage local des préférences sans inscription',
            'Assistant intelligent restreint aux sources officielles',
            'Cloudflare Pages pour l\u2019hébergement et le déploiement',
        ],
        'cost_self': '0 dirham — construite sur un écosystème gratuit (hébergement et déploiement) avec l\u2019aide d\u2019outils d\u2019IA pour le développement et la compilation.',
        'cost_market': 'Une plateforme de documents administratifs de cette ampleur (bibliothèque vérifiée + guide des entités + assistant intelligent) : environ 80 000 – 250 000 dirhams en développement commercial.',
        'cost_now': '0 dirham par mois sur l\u2019offre gratuite.',
        'cost_scale': 'En cas de large adoption (recherche plus rapide, base de données et services backend) : environ 200 – 800 dirhams par mois.',
    },
    'tools': [
        ('Next.js', 'Un framework moderne construit sur React : il produit des pages à chargement rapide, faciles à indexer par les moteurs de recherche, et ne met à jour que la partie qui change au lieu de recharger toute la page.'),
        ('React', 'La bibliothèque d\u2019interfaces de Meta : elle découpe la page en petits composants réutilisables — un bouton, une carte, une liste — pour un site cohérent et facile à faire évoluer.'),
        ('Polices Cairo et Noto Kufi Arabic', 'Deux polices arabes professionnelles conçues pour les écrans : des lettres nettes à toutes les tailles, qui donnent aux textes administratives tenue et lisibilité.'),
        ('Conception arabe d\u2019abord (RTL)', 'La plateforme est conçue de droite à gauche dès le départ, puis les autres langues s\u2019ajoutent — pas une traduction inversée, mais un vrai design arabe.'),
        ('Stockage local (localStorage)', 'Une petite mémoire dans votre navigateur qui retient votre langue et vos réglages : vous revenez et retrouvez la plateforme telle que vous l\u2019avez laissée — sans compte ni inscription.'),
        ('Documents organisés en 19 catégories', 'Chaque document est classé (impôts, sécurité sociale, contrats, réclamations...) : vous trouvez ce qu\u2019il vous faut en deux clics au lieu de fouiller des centaines de fichiers.'),
        ('L\u2019assistant restreint aux sources', 'Un assistant qui répond exclusivement à partir de documents et sources officiels préalablement vérifiés : si la réponse ne s\u2019y trouve pas, il le dit franchement au lieu d\u2019en inventer une — le remède pratique aux hallucinations.'),
        ('Cloudflare Pages', 'Le service d\u2019hébergement mondial qui sert la plateforme depuis des points proches des utilisateurs dans tous les pays : chargement rapide au Maroc comme ailleurs, avec certificats de sécurité et mises à jour instantanées.'),
    ],
}

# ================================ SPANISH ================================
EPDP['es'] = {
    'card': {
        'name': 'EPDP — Tu escriba digital',
        'tag': 'Plataforma de documentos administrativos marroquíes',
        'desc': 'Plataforma gratuita que reúne más de 1.180 formularios y documentos administrativos marroquíes oficiales en árabe y francés — de la CNSS y los impuestos a los contratos y poderes — con una guía de portales oficiales y un asistente inteligente que responde desde fuentes verificadas.',
    },
    'page': {
        'about': 'EPDP — «Tu escriba digital» — es una plataforma marroquí que digitaliza los servicios del escriba público tradicional: una biblioteca de más de 1.180 formularios y documentos administrativos oficiales en árabe y francés — solicitudes dirigidas a las administraciones, reclamaciones, contratos de alquiler y venta, poderes, declaraciones juradas, currículums — organizados en 19 categorías administrativas que cubren la seguridad social, los impuestos, los contratos y más. Junto a la biblioteca: una guía completa de los portales de más de 38 entidades oficiales marroquíes, un asistente inteligente que responde desde fuentes verificadas sin alucinaciones, y un asistente que rellena tu documento con tus datos y lo formatea profesionalmente — todo completamente gratis y sin registro.',
        'tech': ['Next.js (framework moderno)', 'React (interfaz interactiva)', 'Fuentes Cairo + Noto Kufi Arabic', 'Diseño árabe nativo (RTL)', 'Almacenamiento local de preferencias', 'Arquitectura documental en 19 categorías', 'Asistente inteligente restringido a fuentes', 'Cloudflare Pages (alojamiento)'],
        'features': [
            'Biblioteca con más de 1.180 formularios administrativos oficiales en árabe y francés',
            '19 categorías administrativas: de impuestos y seguridad social a contratos y reclamaciones',
            'Guía verificada de más de 38 entidades oficiales marroquíes con enlaces directos',
            'Asistente inteligente que responde desde fuentes oficiales verificadas — sin información inventada',
            'Rellenado automático de documentos con tus datos, con formato profesional listo para imprimir',
            'Totalmente gratis, sin registro, interfaz en 7 idiomas',
        ],
        'learned': 'EPDP me enseñó que el valor de un producto digital se mide por el tiempo que ahorra a la gente: cada minuto que el ciudadano ahorra buscando su documento es la verdadera ganancia. Aprendí la disciplina de la información: cuando manejas documentos oficiales no hay lugar para la aproximación; cada formulario debe coincidir con su fuente, o la plataforma pierde su sentido. También aprendí a diseñar una experiencia bilingüe (árabe/francés) que respeta el funcionamiento de la administración marroquí y lo simplifica para el ciudadano.',
    },
    'v4': {
        'value_intro': 'EPDP acorta el camino del ciudadano hacia el documento administrativo:',
        'values': [
            ('Una biblioteca nacional en un solo enlace', 'Más de 1.180 formularios oficiales en un solo lugar en vez de buscar entre webs y ventanillas: desde una solicitud de seguridad social hasta un contrato de alquiler listo, en árabe y francés.'),
            ('Un mapa de los portales oficiales', 'Guía ordenada de más de 38 entidades oficiales (impuestos, seguridad social, justicia, municipios...) con el enlace directo de cada una — la puerta correcta al primer intento.'),
            ('Respuestas de fuentes verificadas, no de la imaginación', 'El asistente inteligente está restringido solo a fuentes oficiales: si la respuesta no está ahí, lo dice con claridad — confianza construida sobre precisión.'),
            ('Tu documento listo en minutos', 'Introduce tus datos una vez y el asistente rellena el formulario y lo formatea — lo descargas bien impreso, listo para firmar y presentar.'),
        ],
        'effort': 'El mayor trabajo en EPDP no fueron las pantallas sino el contenido: recopilar y verificar más de 1.180 formularios y documentos de sus fuentes oficiales, clasificarlos en 19 categorías con una lógica que entienda el ciudadano y no la administración, y cuidar las versiones árabe y francesa de cada documento. Encima de eso construí la plataforma en sí: búsqueda rápida, cambio de idioma persistente y un asistente inteligente restringido a fuentes oficiales para que nunca invente una respuesta — porque aquí la confianza importa más que la cantidad de funciones.',
        'effort_stats': [('Documentos y formularios', 'Más de 1.180'), ('Categorías administrativas', '19 categorías'), ('Entidades oficiales de referencia', 'Más de 38')],
        'ops': [
            'Next.js — una arquitectura moderna, rápida y mantenible',
            'Fuentes árabes profesionales (Cairo y Noto Kufi)',
            'Almacenamiento local de preferencias sin registro',
            'Asistente inteligente restringido a fuentes oficiales',
            'Cloudflare Pages para el alojamiento y despliegue',
        ],
        'cost_self': '0 dírhams — construida sobre un ecosistema gratuito (alojamiento y despliegue) con ayuda de herramientas de IA en el desarrollo y la recopilación.',
        'cost_market': 'Una plataforma de documentos administrativos de esta escala (biblioteca verificada + guía de entidades + asistente inteligente): aproximadamente 80.000 – 250.000 dírhams en desarrollo comercial.',
        'cost_now': '0 dírhams al mes en el plan gratuito.',
        'cost_scale': 'Con amplia adopción (búsqueda más rápida, base de datos y servicios backend): unos 200 – 800 dírhams al mes.',
    },
    'tools': [
        ('Next.js', 'Un framework moderno construido sobre React: produce páginas de carga rápida, fáciles de indexar por los buscadores, y actualiza solo la parte que cambia en vez de recargar toda la página.'),
        ('React', 'La biblioteca de interfaces de Meta: divide la página en componentes pequeños reutilizables — un botón, una tarjeta, una lista — para un sitio coherente y fácil de desarrollar.'),
        ('Fuentes Cairo y Noto Kufi Arabic', 'Dos tipografías árabes profesionales diseñadas para pantallas: letras nítidas en todos los tamaños, que dan a los textos administrativos solidez y legibilidad.'),
        ('Diseño árabe nativo (RTL)', 'La plataforma está diseñada de derecha a izquierda desde el inicio y luego se añaden los demás idiomas — no es una traducción invertida sino un diseño árabe correcto.'),
        ('Almacenamiento local (localStorage)', 'Una pequeña memoria dentro de tu navegador que recuerda tu idioma y preferencias: vuelves y encuentras la plataforma como la dejaste — sin cuenta ni registro.'),
        ('Documentos organizados en 19 categorías', 'Cada documento está clasificado (impuestos, seguridad social, contratos, reclamaciones...) para encontrar lo que buscas en dos clics en vez de revolver cientos de archivos.'),
        ('El asistente restringido a fuentes', 'Un asistente que responde exclusivamente a partir de documentos y fuentes oficiales verificadas de antemano: si la respuesta no está, lo dice con honestidad en vez de inventarla — el remedio práctico contra las alucinaciones.'),
        ('Cloudflare Pages', 'El servicio de alojamiento global que sirve la plataforma desde puntos cercanos al usuario en todos los países: carga rápida en Marruecos y fuera, con certificados de seguridad y actualizaciones instantáneas.'),
    ],
}

# ================================ ITALIAN ================================
EPDP['it'] = {
    'card': {
        'name': 'EPDP — Il tuo scrivano digitale',
        'tag': 'Piattaforma di documenti amministrativi marocchini',
        'desc': 'Piattaforma gratuita che raccoglie oltre 1.180 moduli e documenti amministrativi marocchini ufficiali in arabo e francese — da CNSS e tasse a contratti e procure — con guida ai portali ufficiali e un assistente intelligente che risponde da fonti verificate.',
    },
    'page': {
        'about': 'EPDP — «Il tuo scrivano digitale» — è una piattaforma marocchina che digitalizza i servizi dello scrivano pubblico tradizionale: una biblioteca di oltre 1.180 moduli e documenti amministrativi ufficiali in arabo e francese — richieste alle amministrazioni, reclami, contratti di locazione e vendita, procure, dichiarazioni giurate, curriculum — organizzati in 19 categorie amministrative che coprono previdenza sociale, tasse, contratti e altro. Accanto alla biblioteca: una guida completa ai portali di oltre 38 enti ufficiali marocchini, un assistente intelligente che risponde da fonti verificate senza allucinazioni, e un assistente che compila il tuo documento con i tuoi dati e lo formatta professionalmente — il tutto completamente gratis e senza registrazione.',
        'tech': ['Next.js (framework moderno)', 'React (interfaccia interattiva)', 'Font Cairo + Noto Kufi Arabic', 'Design arabo nativo (RTL)', 'Archiviazione locale delle preferenze', 'Architettura documentale in 19 categorie', 'Assistente intelligente vincolato alle fonti', 'Cloudflare Pages (hosting)'],
        'features': [
            'Biblioteca con oltre 1.180 moduli amministrativi ufficiali in arabo e francese',
            '19 categorie amministrative: da tasse e previdenza a contratti e reclami',
            'Guida verificata di oltre 38 enti ufficiali marocchini con link diretti',
            'Assistente intelligente che risponde da fonti ufficiali verificate — senza informazioni inventate',
            'Compilazione automatica dei documenti con i tuoi dati, formattazione professionale pronta per la stampa',
            'Completamente gratuito, senza registrazione, interfaccia in 7 lingue',
        ],
        'learned': 'EPDP mi ha insegnato che il valore di un prodotto digitale si misura dal tempo che fa risparmiare alle persone: ogni minuto che il cittadino rispara cercando il suo documento è il vero guadagno. Ho imparato la disciplina dell\u2019informazione: con documenti ufficiali non c\u2019è spazio per l\u2019approssimazione, ogni modulo deve corrispondere alla sua fonte o la piattaforma perde senso. Ho anche imparato a progettare un\u2019esperienza bilingue (arabo/francese) che rispetta il funzionamento dell\u2019amministrazione marocchina e la semplifica per il cittadino.',
    },
    'v4': {
        'value_intro': 'EPDP accorcia il percorso del cittadino verso il documento amministrativo:',
        'values': [
            ('Una biblioteca nazionale in un solo link', 'Oltre 1.180 moduli ufficiali in un unico posto invece di frugare tra siti e sportelli: da una richiesta di previdenza sociale a un contratto d\u2019affitto pronto, in arabo e francese.'),
            ('Una mappa dei portali ufficiali', 'Guida ordinata di oltre 38 enti ufficiali (tasse, previdenza, giustizia, comuni...) con il link diretto di ciascuno — la porta giusta al primo tentativo.'),
            ('Risposte da fonti verificate, non dall\u2019immaginazione', 'L\u2019assistente intelligente è vincolato alle sole fonti ufficiali: se la risposta non c\u2019è, lo dichiara chiaramente — fiducia costruita sulla precisione.'),
            ('Il tuo documento pronto in pochi minuti', 'Inserisci i tuoi dati una volta e l\u2019assistente compila il modulo e lo formatta — lo scarichi stampato con cura, pronto da firmare e presentare.'),
        ],
        'effort': 'Il lavoro più grande in EPDP non sono state le schermate ma i contenuti: raccogliere e verificare oltre 1.180 moduli e documenti dalle loro fonti ufficiali, classificarli in 19 categorie con una logica che capisca il cittadino e non l\u2019amministrazione, e curare le versioni araba e francese di ogni documento. Sopra a questo ho costruito la piattaforma stessa: ricerca veloce, cambio lingua memorizzato e un assistente intelligente vincolato alle fonti ufficiali perché non inventi mai una risposta — qui la fiducia conta più del numero di funzioni.',
        'effort_stats': [('Documenti e moduli', 'Oltre 1.180'), ('Categorie amministrative', '19 categorie'), ('Enti ufficiali di riferimento', 'Oltre 38')],
        'ops': [
            'Next.js — un\u2019architettura moderna, rapida e manutenibile',
            'Font arabe professionali (Cairo e Noto Kufi)',
            'Archiviazione locale delle preferenze senza registrazione',
            'Assistente intelligente vincolato alle fonti ufficiali',
            'Cloudflare Pages per hosting e pubblicazione',
        ],
        'cost_self': '0 dirham — costruita su un ecosistema gratuito (hosting e pubblicazione) con l\u2019aiuto di strumenti IA nello sviluppo e nella raccolta.',
        'cost_market': 'Una piattaforma di documenti amministrativi di questa scala (biblioteca verificata + guida agli enti + assistente intelligente): indicativamente 80.000 – 250.000 dirham nello sviluppo commerciale.',
        'cost_now': '0 dirham al mese sul piano gratuito.',
        'cost_scale': 'Con un\u2019adozione ampia (ricerca più veloce, database e servizi backend): circa 200 – 800 dirham al mese.',
    },
    'tools': [
        ('Next.js', 'Un framework moderno costruito su React: produce pagine a caricamento rapido, facili da indicizzare nei motori di ricerca, e aggiorna solo la parte che cambia invece di ricaricare tutta la pagina.'),
        ('React', 'La libreria di interfacce di Meta: divide la pagina in piccoli componenti riutilizzabili — un pulsante, una scheda, una lista — per un sito coerente e facile da sviluppare.'),
        ('Font Cairo e Noto Kufi Arabic', 'Due tipografie arabe professionali pensate per gli schermi: lettere nitide a ogni dimensione, che danno ai testi amministrativi solidità e leggibilità.'),
        ('Design arabo nativo (RTL)', 'La piattaforma è progettata da destra a sinistra fin dall\u2019inizio e poi si aggiungono le altre lingue — non una traduzione invertita ma un vero design arabo.'),
        ('Archiviazione locale (localStorage)', 'Una piccola memoria nel tuo browser che ricorda lingua e preferenze: torni e ritrovi la piattaforma come l\u2019hai lasciata — senza account né registrazione.'),
        ('Documenti organizzati in 19 categorie', 'Ogni documento è classificato (tasse, previdenza, contratti, reclami...) così trovi ciò che ti serve in due clic invece di cercare tra centinaia di file.'),
        ('L\u2019assistente vincolato alle fonti', 'Un assistente che risponde esclusivamente da documenti e fonti ufficiali verificate in anticipo: se la risposta non c\u2019è, lo dice con onestà invece di inventarla — il rimedio pratico contro le allucinazioni.'),
        ('Cloudflare Pages', 'Il servizio di hosting globale che serve la piattaforma da punti vicini agli utenti in ogni paese: apertura rapida in Marocco e fuori, con certificati di sicurezza e aggiornamenti istantanei.'),
    ],
}

# ================================ GERMAN ================================
EPDP['de'] = {
    'card': {
        'name': 'EPDP — Dein digitaler Schreiber',
        'tag': 'Plattform für marokkanische Verwaltungsdokumente',
        'desc': 'Eine kostenlose Plattform mit über 1.180 offiziellen marokkanischen Verwaltungsformularen und -dokumenten auf Arabisch und Französisch — von CNSS und Steuern bis zu Verträgen und Vollmachten — mit Leitfaden zu offiziellen Portalen und einem KI-Assistenten, der aus geprüften Quellen antwortet.',
    },
    'page': {
        'about': 'EPDP — „Dein digitaler Schreiber“ — ist eine marokkanische Plattform, die die Dienste des klassischen öffentlichen Schreibers digitalisiert: eine Bibliothek mit über 1.180 offiziellen Verwaltungsformularen und -dokumenten auf Arabisch und Französisch — Anträge an Behörden, Beschwerden, Miet- und Kaufverträge, Vollmachten, Ehrenerklärungen, Lebensläufe — geordnet in 19 Verwaltungskategorien von Sozialversicherung über Steuern bis zu Verträgen. Dazu: ein umfassender Leitfaden zu den Portalen von über 38 offiziellen marokkanischen Stellen, ein KI-Assistent, der aus geprüften Quellen ohne Halluzination antwortet, und ein Assistent, der dein Dokument mit deinen Daten ausfüllt und professionell formatiert — alles völlig kostenlos und ohne Registrierung.',
        'tech': ['Next.js (modernes Framework)', 'React (interaktive Oberfläche)', 'Schriften Cairo + Noto Kufi Arabic', 'Arabisch-first-Design (RTL)', 'Lokale Speicherung der Einstellungen', 'Dokumentarchitektur in 19 Kategorien', 'Quellengebundener KI-Assistent', 'Cloudflare Pages (Hosting)'],
        'features': [
            'Bibliothek mit über 1.180 offiziellen Verwaltungsformularen auf Arabisch und Französisch',
            '19 Verwaltungskategorien: von Steuern und Sozialversicherung bis zu Verträgen und Beschwerden',
            'Geprüfter Leitfaden zu über 38 offiziellen marokkanischen Stellen mit direkten Links',
            'KI-Assistent, der aus geprüften offiziellen Quellen antwortet — ohne erfundene Informationen',
            'Automatisches Ausfüllen der Dokumente mit deinen Daten, professionell formatiert und druckfertig',
            'Vollständig kostenlos, ohne Registrierung, Oberfläche in 7 Sprachen',
        ],
        'learned': 'EPDP hat mir gezeigt: Der Wert eines digitalen Produkts bemisst sich nach der Zeit, die es den Menschen spart — jede Minute, die ein Bürger bei der Suche nach seinem Dokument spart, ist der echte Gewinn. Ich habe Disziplin im Umgang mit Informationen gelernt: Bei offiziellen Dokumenten gibt es kein „ungefähr“ — jedes Formular muss exakt seiner Quelle entsprechen, sonst verliert die Plattform ihren Sinn. Außerdem lernte ich, ein zweisprachiges Erlebnis (Arabisch/Französisch) zu gestalten, das die Arbeitsweise der marokkanischen Verwaltung respektiert und sie für den Bürger vereinfacht.',
    },
    'v4': {
        'value_intro': 'EPDP verkürzt den Weg des Bürgers zum Verwaltungsdokument:',
        'values': [
            ('Eine nationale Bibliothek in einem Link', 'Über 1.180 offizielle Formulare an einem Ort statt endloser Suche auf Websites und an Schaltern: vom Sozialversicherungsantrag bis zum fertigen Mietvertrag, auf Arabisch und Französisch.'),
            ('Eine Landkarte der offiziellen Portale', 'Ein geordneter Leitfaden zu über 38 offiziellen Stellen (Steuern, Sozialversicherung, Justiz, Gemeinden...) mit direktem Link zu jeder — die richtige Tür beim ersten Versuch.'),
            ('Antworten aus geprüften Quellen, nicht aus der Phantasie', 'Der KI-Assistent ist ausschließlich auf offizielle Quellen beschränkt: Wenn die Antwort dort nicht steht, sagt er das klar — Vertrauen auf Grundlage von Genauigkeit.'),
            ('Dein Dokument in Minuten fertig', 'Gib deine Daten einmal ein, der Assistent füllt das Formular aus und formatiert es — du lädst es sauber ausgedruckt herunter, bereit zum Unterschreiben und Einreichen.'),
        ],
        'effort': 'Die größte Arbeit in EPDP waren nicht die Bildschirmseiten, sondern der Inhalt: über 1.180 Formulare und Dokumente aus ihren offiziellen Quellen sammeln und prüfen, sie in 19 Kategorien mit einer Logik ordnen, die der Bürger versteht — nicht die Verwaltung — und bei jedem Dokument die arabische und die französische Fassung pflegen. Darüber hinaus baute ich die Plattform selbst: schnelle Suche, gespeicherter Sprachwechsel und ein KI-Assistent, der an offizielle Quellen gebunden ist, damit er nie eine Antwort erfindet — denn hier zählt Vertrauen mehr als Funktionsfülle.',
        'effort_stats': [('Dokumente und Formulare', 'Über 1.180'), ('Verwaltungskategorien', '19 Kategorien'), ('Offizielle Referenzstellen', 'Über 38')],
        'ops': [
            'Next.js — eine moderne, schnelle, wartbare Architektur',
            'Professionelle arabische Schriften (Cairo und Noto Kufi)',
            'Lokale Speicherung der Einstellungen ohne Registrierung',
            'KI-Assistent gebunden an offizielle Quellen',
            'Cloudflare Pages für Hosting und Deployment',
        ],
        'cost_self': '0 Dirham — gebaut auf einem kostenlosen Ökosystem (Hosting und Deployment) mit Hilfe von KI-Werkzeugen bei Entwicklung und Zusammenstellung.',
        'cost_market': 'Eine Verwaltungsdokument-Plattform dieses Umfangs (geprüfte Bibliothek + Stellenleitfaden + KI-Assistent): etwa 80.000 – 250.000 Dirham bei kommerzieller Entwicklung.',
        'cost_now': '0 Dirham pro Monat im Free-Tarif.',
        'cost_scale': 'Bei breiter Nutzung (schnellere Suche, Datenbank und Backend-Dienste): geschätzt 200 – 800 Dirham pro Monat.',
    },
    'tools': [
        ('Next.js', 'Ein modernes Framework auf Basis von React: Es erzeugt schnell ladende Seiten, die Suchmaschinen leicht indexieren, und aktualisiert nur den geänderten Teil statt die ganze Seite neu zu laden.'),
        ('React', 'Die UI-Bibliothek von Meta: Sie zerlegt die Seite in kleine wiederverwendbare Bausteine — Button, Karte, Liste — so bleibt die Seite einheitlich und leicht weiterzuentwickeln.'),
        ('Schriften Cairo und Noto Kufi Arabic', 'Zwei professionelle arabische Schriften, gebaut für Bildschirme: klare Buchstaben in jeder Größe — sie geben Verwaltungstexten Würde und Lesbarkeit.'),
        ('Arabisch-first-Design (RTL)', 'Die Plattform ist von Anfang an von rechts nach links entworfen, die anderen Sprachen kamen danach — keine spiegelverkehrt übersetzte, sondern eine echt arabische Gestaltung.'),
        ('Lokaler Speicher (localStorage)', 'Ein kleines Gedächtnis in deinem Browser, das Sprache und Einstellungen merkt: Du kommst zurück und findest alles so, wie du es verlassen hast — ohne Konto, ohne Registrierung.'),
        ('Dokumente in 19 Kategorien geordnet', 'Jedes Dokument ist einsortiert (Steuern, Sozialversicherung, Verträge, Beschwerden...) — du findest, was du suchst, mit zwei Klicks statt hunderte Dateien zu durchwühlen.'),
        ('Der quellengebundene Assistent', 'Ein Assistent, der ausschließlich aus vorab geprüften offiziellen Dokumenten und Quellen antwortet: Wenn die Antwort dort nicht steht, sagt er es ehrlich, statt eine zu erfinden — das praktische Gegenmittel gegen Halluzination.'),
        ('Cloudflare Pages', 'Der weltweite Hosting-Dienst, der die Plattform von Punkten in der Nähe der Nutzer in allen Ländern ausliefert: schnelles Laden in Marokko und anderswo, mit Sicherheitszertifikaten und Sofort-Updates bei jeder neuen Version.'),
    ],
}

# ================================ DUTCH ================================
EPDP['nl'] = {
    'card': {
        'name': 'EPDP — Jouw digitale griffier',
        'tag': 'Platform voor Marokkaanse administratieve documenten',
        'desc': 'Een gratis platform met meer dan 1.180 officiële Marokkaanse administratieve formulieren en documenten in het Arabisch en Frans — van CNSS en belastingen tot contracten en volmachten — met een gids voor officiële portalen en een slimme assistent die antwoordt uit gecontroleerde bronnen.',
    },
    'page': {
        'about': 'EPDP — «Jouw digitale griffier» — is een Marokkaans platform dat de diensten van de traditionele openbare griffier digitaliseert: een bibliotheek met meer dan 1.180 officiële administratieve formulieren en documenten in het Arabisch en Frans — verzoeken aan diensten, klachten, huur- en koopcontracten, volmachten, eerlijke verklaringen, cv\u2019s — georganiseerd in 19 administratieve categorieën die sociale zekerheid, belastingen, contracten en meer dekken. Daarnaast: een volledige gids van de portalen van 38+ officiële Marokkaanse instanties, een slimme assistent die antwoordt uit gecontroleerde bronnen zonder hallucinatie, en een assistent die jouw document invult met jouw gegevens en het professioneel opmaakt — alles volledig gratis en zonder registratie.',
        'tech': ['Next.js (modern framework)', 'React (interactieve interface)', 'Lettertypes Cairo + Noto Kufi Arabic', 'Arabisch-eerst ontwerp (RTL)', 'Lokale opslag van voorkeuren', 'Documentarchitectuur in 19 categorieën', 'Brongebonden slimme assistent', 'Cloudflare Pages (hosting)'],
        'features': [
            'Bibliotheek met meer dan 1.180 officiële administratieve formulieren in het Arabisch en Frans',
            '19 administratieve categorieën: van belastingen en sociale zekerheid tot contracten en klachten',
            'Gecontroleerde gids van 38+ officiële Marokkaanse instanties met directe links',
            'Slimme assistent die antwoordt uit gecontroleerde officiële bronnen — zonder verzonnen informatie',
            'Automatisch invullen van documenten met jouw gegevens, professioneel opgemaakt en klaar om te printen',
            'Volledig gratis, zonder registratie, interface in 7 talen',
        ],
        'learned': 'EPDP leerde me dat de waarde van een digitaal product wordt afgemeten aan de tijd die het mensen bespaart: elke minuut die een burger uitspaart bij het zoeken naar zijn document is de echte winst. Ik leerde discipline in informatie — bij officiële documenten is geen benadering toegestaan: elk formulier moet exact overeenkomen met zijn bron, anders verliest het platform zijn zin. Ook leerde ik een tweetalige (Arabisch/Franse) ervaring ontwerpen die de werkwijze van de Marokkaanse administratie respecteert en ze voor de burger vereenvoudigt.',
    },
    'v4': {
        'value_intro': 'EPDP verkort de weg van de burger naar het administratieve document:',
        'values': [
            ('Een nationale bibliotheek in één link', 'Meer dan 1.180 officiële formulieren op één plek in plaats van spitten door websites en loketten: van een sociaal-zekerheidsverzoek tot een klaar huurcontract, in het Arabisch en Frans.'),
            ('Een kaart van de officiële portalen', 'Een geordende gids van 38+ officiële instanties (belastingen, sociale zekerheid, justitie, gemeenten...) met de directe link van elk — de juiste deur bij de eerste poging.'),
            ('Antwoorden uit gecontroleerde bronnen, niet uit verbeelding', 'De slimme assistent is uitsluitend gebonden aan officiële bronnen: staat het antwoord er niet, dan zegt hij dat helder — vertrouwen gebouwd op nauwkeurigheid.'),
            ('Jouw document klaar in enkele minuten', 'Vul je gegevens één keer in en de assistent vult het formulier in en maakt het op — je downloadt het netjes geprint, klaar om te ondertekenen en in te dienen.'),
        ],
        'effort': 'Het grootste werk in EPDP waren niet de schermen maar de inhoud: meer dan 1.180 formulieren en documenten uit hun officiële bronnen verzamelen en controleren, ze indelen in 19 categorieën met een logica die de burger begrijpt — niet de administratie — en bij elk document de Arabische én Franse versie verzorgen. Daarbovenop bouwde ik het platform zelf: snel zoeken, bewaarde taalkeuze en een slimme assistent gebonden aan officiële bronnen zodat hij nooit een antwoord verzint — want hier weegt vertrouwen zwaarder dan het aantal functies.',
        'effort_stats': [('Documenten en formulieren', 'Meer dan 1.180'), ('Administratieve categorieën', '19 categorieën'), ('Officiële referentie-instanties', 'Meer dan 38')],
        'ops': [
            'Next.js — een moderne, snelle, onderhoudbare architectuur',
            'Professionele Arabische lettertypes (Cairo en Noto Kufi)',
            'Lokale opslag van voorkeuren zonder registratie',
            'Slimme assistent gebonden aan officiële bronnen',
            'Cloudflare Pages voor hosting en uitrol',
        ],
        'cost_self': '0 dirham — gebouwd op een gratis ecosysteem (hosting en uitrol) met hulp van AI-tools bij ontwikkeling en samenstelling.',
        'cost_market': 'Een platform voor administratieve documenten van deze schaal (gecontroleerde bibliotheek + instantiegids + slimme assistent): grofweg 80.000 – 250.000 dirham bij commerciële ontwikkeling.',
        'cost_now': '0 dirham per maand op het gratis pakket.',
        'cost_scale': 'Bij brede adoptie (sneller zoeken, database en backend-diensten): geschat 200 – 800 dirham per maand.',
    },
    'tools': [
        ('Next.js', 'Een modern framework bovenop React: het levert snel ladende pagina\u2019s die zoekmachines makkelijk indexeren, en werkt alleen het gewijzigde deel bij in plaats van de hele pagina te herladen.'),
        ('React', 'De interfacebibliotheek van Meta: ze splitst de pagina in kleine herbruikbare onderdelen — een knop, een kaart, een lijst — zodat de site consistent blijft en makkelijk te bouwen is.'),
        ('Lettertypes Cairo en Noto Kufi Arabic', 'Twee professionele Arabische lettertypes, ontworpen voor schermen: heldere letters in elke grootte, wat administratieve teksten waardigheid en leesbaarheid geeft.'),
        ('Arabisch-eerst ontwerp (RTL)', 'Het platform is vanaf het begin van rechts naar links ontworpen; de andere talen kwamen daarna — geen gespiegelde vertaling maar een echt Arabisch ontwerp.'),
        ('Lokale opslag (localStorage)', 'Een klein geheugen in je browser dat je taal en voorkeuren onthoudt: je komt terug en vindt het platform zoals je het achterliet — zonder account, zonder registratie.'),
        ('Documenten georganiseerd in 19 categorieën', 'Elk document is ingedeeld (belastingen, sociale zekerheid, contracten, klachten...) zodat je vindt wat je zoekt in twee klikken in plaats van honderden bestanden door te spitten.'),
        ('De brongebonden assistent', 'Een assistent die uitsluitend antwoordt uit vooraf gecontroleerde officiële documenten en bronnen: staat het antwoord er niet, dan zegt hij dat eerlijk in plaats van er een te verzinnen — het praktische middel tegen hallucinatie.'),
        ('Cloudflare Pages', 'De wereldwijde hostingdienst die het platform levert vanaf punten dicht bij de gebruiker in elk land: snel laden in Marokko en daarbuiten, met beveiligingscertificaten en directe updates bij elke nieuwe versie.'),
    ],
}

# =============================== PORTUGUESE ===============================
EPDP['pt'] = {
    'card': {
        'name': 'EPDP — O teu escriba digital',
        'tag': 'Plataforma de documentos administrativos marroquinos',
        'desc': 'Plataforma gratuita que reúne mais de 1.180 formulários e documentos administrativos marroquinos oficiais em árabe e francês — da CNSS e impostos a contratos e procurações — com um guia dos portais oficiais e um assistente inteligente que responde a partir de fontes verificadas.',
    },
    'page': {
        'about': 'EPDP — «O teu escriba digital» — é uma plataforma marroquina que digitaliza os serviços do escriba público tradicional: uma biblioteca com mais de 1.180 formulários e documentos administrativos oficiais em árabe e francês — pedidos dirigidos às administrações, reclamações, contratos de arrendamento e compra e venda, procurações, declarações sob palavra de honra, currículos — organizados em 19 categorias administrativas que abrangem segurança social, impostos, contratos e mais. Ao lado da biblioteca: um guia completo dos portais de mais de 38 entidades oficiais marroquinas, um assistente inteligente que responde a partir de fontes verificadas sem alucinação, e um assistente que preenche o teu documento com os teus dados e o formata profissionalmente — tudo totalmente grátis e sem registo.',
        'tech': ['Next.js (framework moderno)', 'React (interface interativa)', 'Fontes Cairo + Noto Kufi Arabic', 'Design árabe nativo (RTL)', 'Armazenamento local de preferências', 'Arquitetura documental em 19 categorias', 'Assistente inteligente restrito às fontes', 'Cloudflare Pages (alojamento)'],
        'features': [
            'Biblioteca com mais de 1.180 formulários administrativos oficiais em árabe e francês',
            '19 categorias administrativas: de impostos e segurança social a contratos e reclamações',
            'Guia verificado de mais de 38 entidades oficiais marroquinas com ligações diretas',
            'Assistente inteligente que responde a partir de fontes oficiais verificadas — sem informação inventada',
            'Preenchimento automático dos documentos com os teus dados, formatação profissional pronta a imprimir',
            'Totalmente gratuito, sem registo, interface em 7 línguas',
        ],
        'learned': 'A EPDP ensinou-me que o valor de um produto digital mede-se pelo tempo que poupa às pessoas: cada minuto que o cidadão poupa à procura do seu documento é o ganho real. Aprendi a disciplina da informação — ao lidar com documentos oficiais não há espaço para aproximações: cada formulário tem de corresponder à sua fonte, senão a plataforma perde o sentido. Aprendi também a desenhar uma experiência bilingue (árabe/francês) que respeita o funcionamento da administração marroquina e o simplifica para o cidadão.',
    },
    'v4': {
        'value_intro': 'A EPDP encurta o caminho do cidadão até ao documento administrativo:',
        'values': [
            ('Uma biblioteca nacional num só link', 'Mais de 1.180 formulários oficiais num único sítio em vez de vasculhar sites e balcões: de um pedido de segurança social a um contrato de arrendamento pronto, em árabe e francês.'),
            ('Um mapa dos portais oficiais', 'Um guia ordenado de mais de 38 entidades oficiais (impostos, segurança social, justiça, municípios...) com a ligação direta de cada uma — a porta certa à primeira tentativa.'),
            ('Respostas de fontes verificadas, não da imaginação', 'O assistente inteligente está restrito apenas a fontes oficiais: se a resposta não lá está, ele diz-o com clareza — confiança construída sobre precisão.'),
            ('O teu documento pronto em minutos', 'Introduz os teus dados uma vez e o assistente preenche o formulário e formata-o — descarregas-lo bem impresso, pronto para assinar e entregar.'),
        ],
        'effort': 'O maior trabalho na EPDP não foram os ecrãs mas o conteúdo: recolher e verificar mais de 1.180 formulários e documentos junto das suas fontes oficiais, classificá-los em 19 categorias com uma lógica que o cidadão entende — não a administração — e cuidar das versões árabe e francesa de cada documento. Por cima disso construí a própria plataforma: pesquisa rápida, mudança de língua memorizada e um assistente inteligente restrito a fontes oficiais para que nunca invente uma resposta — porque aqui a confiança pesa mais do que a quantidade de funções.',
        'effort_stats': [('Documentos e formulários', 'Mais de 1.180'), ('Categorias administrativas', '19 categorias'), ('Entidades oficiais de referência', 'Mais de 38')],
        'ops': [
            'Next.js — uma arquitetura moderna, rápida e manutenível',
            'Fontes árabes profissionais (Cairo e Noto Kufi)',
            'Armazenamento local de preferências sem registo',
            'Assistente inteligente restrito às fontes oficiais',
            'Cloudflare Pages para alojamento e implantação',
        ],
        'cost_self': '0 dirhams — construída sobre um ecossistema gratuito (alojamento e implantação) com a ajuda de ferramentas de IA no desenvolvimento e compilação.',
        'cost_market': 'Uma plataforma de documentos administrativos desta escala (biblioteca verificada + guia de entidades + assistente inteligente): aproximadamente 80.000 – 250.000 dirhams em desenvolvimento comercial.',
        'cost_now': '0 dirhams por mês no plano gratuito.',
        'cost_scale': 'Com ampla adoção (pesquisa mais rápida, base de dados e serviços de backend): cerca de 200 – 800 dirhams por mês.',
    },
    'tools': [
        ('Next.js', 'Uma framework moderna construída sobre React: produz páginas de carregamento rápido, fáceis de indexar pelos motores de busca, e atualiza apenas a parte que muda em vez de recarregar a página toda.'),
        ('React', 'A biblioteca de interfaces da Meta: divide a página em componentes pequenos e reutilizáveis — um botão, um cartão, uma lista — para um site coerente e fácil de desenvolver.'),
        ('Fontes Cairo e Noto Kufi Arabic', 'Duas fontes árabes profissionais desenhadas para ecrãs: letras nítidas em todos os tamanhos, que dão aos textos administrativos solidez e legibilidade.'),
        ('Design árabe nativo (RTL)', 'A plataforma foi desenhada de direita para a esquerda desde o início, e só depois se acrescentaram as outras línguas — não é uma tradução invertida, é um verdadeiro design árabe.'),
        ('Armazenamento local (localStorage)', 'Uma pequena memória dentro do teu navegador que guarda a tua língua e preferências: voltas e encontras a plataforma como a deixaste — sem conta e sem registo.'),
        ('Documentos organizados em 19 categorias', 'Cada documento está classificado (impostos, segurança social, contratos, reclamações...) para encontrares o que procuras em dois cliques em vez de vasculhares centenas de ficheiros.'),
        ('O assistente restrito às fontes', 'Um assistente que responde exclusivamente a partir de documentos e fontes oficiais verificadas previamente: se a resposta não existe, ele diz-o com honestidade em vez de a inventar — o remédio prático contra a alucinação.'),
        ('Cloudflare Pages', 'O serviço de alojamento global que serve a plataforma a partir de pontos próximos dos utilizadores em todos os países: abertura rápida em Marrocos e fora dele, com certificados de segurança e atualizações instantâneas.'),
    ],
}
