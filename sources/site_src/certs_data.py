# -*- coding: utf-8 -*-
"""Language-neutral data for the 13 certificates + 4 digital projects."""

# (img, field, issuer_key, year, month, day, credential_id, drive_file_id)
CERTS = [
    ('c01', 'marketing', 'google_en', 2021, 3, 31, '2YQ Q7H DY9', '1vMuqC5qmBTjrW6w1eJzXta1a9DvaMCzu'),
    ('c02', 'marketing', 'google_ar', 2021, 4, 5, 'W6G 9GJ VNJ', '1CSFIpEjZFzcEz-lohuIZN--Cix02fAVK'),
    ('c03', 'ai', 'huawei', 2026, 5, 19, 'ICT20260519000075', '157u_HHFZ5zjTtalp0lqrn9FEFdI1e9ep'),
    ('c04', 'civic', 'portal', 2026, 5, 11, '', '16vvanzIqMqLpTtbdripkPx-LXnTBrutC'),
    ('c05', 'civic', 'portal', 2026, 5, 12, '', '1zjQVDH1eoAdAZasAS8Aobf1K85zZ0pwB'),
    ('c06', 'civic', 'portal', 2026, 5, 15, '', '131oY8Irv1b52lgllNkJOSFMqV0yD7Aru'),
    ('c07', 'ai', 'hp', 2026, 5, 20, 'de90c5ca-0aec-420e-a45e-2ee4c54a3d95', '1kNRgSUqSaQrFH_Hx1JlIfIxpgzrF3bYr'),
    ('c08', 'biz', 'hp', 2026, 5, 21, 'c76722f4-9169-474f-83e8-d93859654c2d', '1IvbA562tZfexM4Op75Hmp0SCjRHNKrKx'),
    ('c09', 'ai', 'hp', 2026, 5, 22, 'd2ac4794-2648-4482-8638-770aea13df94', '1EcmCHYloQEIdm7eFLEqw6-A6rfO1fTmK'),
    ('c10', 'biz', 'hp', 2026, 5, 25, '3f368344-f7a1-494a-abb5-8175edee5557', '1fZiENBUZeyvNQMWiJgukvIuCiC-mSNuv'),
    ('c11', 'web', 'hp', 2026, 7, 1, '8bcaf75d-3310-4ee7-8bf5-4e4d5e1cab24', '18AKBs8Fn94L1p93EuD9LHLbKUesb1G1c'),
    ('c12', 'biz', 'hp', 2026, 10, 13, 'bf38e3fc-9cc4-40cc-894b-4acf2dba020b', '1KYYLcm4uhoW49uf9M-Hb3WR7jA1-sR7y'),
    ('c13', 'ai', 'hp', 2026, 10, 13, '5338a6e7-8c2f-4755-85a2-8e77fb1901c0', '1k3Px92loI-fjMp5UdR2zQDK9v7tnKbcS'),
]

# SEO-friendly URL slugs (one detail page per certificate)
SLUGS = {
    'c01': 'digital-marketing-english',
    'c02': 'digital-marketing-arabic',
    'c03': 'overview-of-ai',
    'c04': 'participatory-democracy',
    'c05': 'associations-legal-framework',
    'c06': 'community-communication',
    'c07': 'ai-for-business-professionals',
    'c08': 'effective-leadership',
    'c09': 'ai-for-beginners',
    'c10': 'professional-communication',
    'c11': 'effective-websites',
    'c12': 'email-for-work',
    'c13': 'strategic-planning-in-the-ai-era',
}

# filter order (translation keys in t_*.py: fields dict)
FIELDS = ['all', 'ai', 'biz', 'civic', 'marketing', 'web']

# English credential names for JSON-LD (canonical reference)
CERTS_EN = {
    'c01': 'Fundamentals of Digital Marketing (English)',
    'c02': 'Fundamentals of Digital Marketing (Arabic)',
    'c03': 'Overview of AI',
    'c04': 'Participatory Democracy Training Module',
    'c05': 'Legal Framework for Establishing Associations Training Module',
    'c06': 'Community Communication Training Module',
    'c07': 'AI for Business Professionals',
    'c08': 'Effective Leadership',
    'c09': 'AI for Beginners',
    'c10': 'Professional Communication for Career Growth',
    'c11': 'Effective Websites',
    'c12': 'Email for Work',
    'c13': 'Strategic Planning in the AI Era',
}

# (key, image, url) — names/descriptions live in translations
PROJECTS = [
    ('natsuptc', '/img/pj-natsuptc.jpg', 'https://natsuptc.pages.dev'),
    ('syda', '/img/pj-syda.jpg', 'https://syda.pages.dev'),
    ('dtsg', '/img/pj-dtsg.jpg', 'https://dtsg.pages.dev'),
    ('hrmp', '/img/pj-hrmp.jpg', 'https://hrmp.pages.dev'),
]
