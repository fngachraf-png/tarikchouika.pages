# v9 — CMDP project + live screenshots gallery (2026-11-05)

Content of this version:
- `capture_shots.py` — Playwright capture of 10 project sites (desktop hero 1440x900@2x,
  desktop content, tablet 768x1024@2x, mobile 390x844@3x), downscaled + optimized to /img/shots/.
- `fix_shots.py` — repair pass (natsup/natsuptc mobile needed no-scroll strategy; phmp d2 = login modal).
- `recapture_d2.py` — d2 re-captured as 1000x1000 squares so the trio-row cover-crop never cuts text.
- `build_css_js.py` — appends gallery + device-frame + lightbox CSS, shots-lightbox JS, bumps v8->v9.
- `inject_shots.py` — injects the "project in pictures" section + lightbox markup into project pages (8 langs).
- `build_cmdp.py` — builds the 8 CMDP pages from epdp skeletons with full localized content.
- `update_site.py` — homepage cards, pager fixes, project counts 7/8 -> 9, sitemap.
- `qa_local.py` — measurement QA: 3 viewports, overflow, image loading, lightbox, gallery layout.

All screenshots are real captures from the live project sites, validated statistically
(pixel variance) and visually (VLM review). No credentials in any file.
