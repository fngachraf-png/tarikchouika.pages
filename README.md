# tarikchouika.pages.dev — Tarik Chouika personal website

Source of the multilingual (AR/EN/FR/ES/IT/DE/NL/PT + RTL) personal website
deployed on Cloudflare Pages at **https://tarikchouika.pages.dev**.

## Security architecture (2026-11 update)

The Telegram bot backend runs as a Cloudflare Worker (`tarik-bot`) and reads
its secrets from **environment bindings** — never from code:

| Binding        | Type         | Purpose                                  |
|----------------|--------------|------------------------------------------|
| `BOT_TOKEN`    | secret_text  | Telegram bot token                       |
| `WEBHOOK_SECRET` | secret_text | Shared secret with Telegram `setWebhook` |
| `OWNER_ID`     | plain_text   | Owner Telegram chat id                   |

> History of this repository was reset on 2026-11-03: a Telegram bot token
> had been accidentally committed and publicly exposed (detected by
> GitGuardian). The token was removed from all code and rotated, and the git
> history was rewritten. **Never commit tokens** — use the Cloudflare
> dashboard (Workers & Pages → tarik-bot → Settings → Variables) to manage
> secrets.

## Layout

- `/` — Arabic homepage (default), `/en`, `/fr`, … — localized pages
- `certs/` — certificate pages (13) · `projects/` — project pages (7)
- `js/` `css/` — chatbot, i18n, theme, styles
- `sources/` — build scripts and the Cloudflare Worker source
