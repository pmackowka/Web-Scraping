# Web Scraping

Dzienny scraping tweetów z X (Twitter) przez Apify API + raport po polsku z komentarzem „co to znaczy" do każdego wpisu.

## Instalacja

```bash
python -m venv venv
source venv/bin/activate          # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp config.example.env .env        # wklej token z https://console.apify.com/settings
```

> Zawsze aktywuj venv przed uruchomieniem (`source venv/bin/activate`). Token trzymamy wyłącznie w `.env` — nigdy w plikach repo ani w promptach.

## Użycie

```bash
source venv/bin/activate
python scrape.py                              # domyślne frazy i próg
python scrape.py -q "AI" "MCP" -l 300         # własne frazy
```

Wynik trafia do `output/`:

- `raw-tweets-{YYYY-MM-DD}.md` — surowe dane po angielsku (etap 1)
- `tweets-{YYYY-MM-DD}.md` — **raport końcowy**, po polsku, z komentarzami (etap 2, robi go agent)

### Parametry `scrape.py`

| Flaga | Opis | Domyślnie |
|-------|------|-----------|
| `-q` | Frazy wyszukiwania (wiele naraz, oddzielone spacją) | `"Claude Code" "Codex" "n8n"` |
| `-m` | Maksymalna liczba tweetów na frazę | 10 |
| `-t` | Typ wyników: `Top` lub `Latest` | Top |
| `-l` | Minimalna liczba polubień | 400 |
| `-d` | Okno świeżości w dniach (dokleja `since:` do zapytania), 0 wyłącza | 7 |

> **Wszystkie frazy w jednym wywołaniu `-q`.** Osobne uruchomienia tego samego dnia nadpisują `raw-tweets-{data}.md` — zostaje tylko ostatnia fraza.

**Filtry:** skrypt odrzuca tweety bez dosłownego wystąpienia frazy w treści, poniżej progu polubień oraz zawierające frazy z list `EXCLUDE_WORDS` (UFO, alien itp.) i `AD_BAIT_PHRASES` (zakamuflowana reklama, np. „comment and I'll send you..."). Duplikaty odsiewa `seen_tweets.json` — ID tweetów ze wszystkich poprzednich uruchomień.

## Opcjonalne Actory Xquik

Istniejący Actor pozostaje domyślny. Xquik działa tylko po jawnym wyborze:

- [Xquik X Tweet Scraper](https://apify.com/xquik/x-tweet-scraper)
- [Xquik X Follower Scraper](https://apify.com/xquik/x-follower-scraper)

Sprawdź aktualne ceny na stronie Actora. Ustaw limit kosztu każdego
uruchomienia i potwierdź go:

```bash
source venv/bin/activate
python scrape.py -q "Claude Code" --provider xquik \
  --max-charge-usd 0.25 --approve-cost
```

Każda fraza tworzy osobne uruchomienie. Podany limit działa po stronie Apify.
Bez `--approve-cost` skrypt nie uruchomi płatnego Actora.

Samodzielne narzędzie obsługuje wszystkie trasy obu Actorów:

```bash
python xquik_actors.py tweets --mode search --target "Claude Code" \
  --max-items 10 --max-charge-usd 0.25 --approve-cost
python xquik_actors.py followers --relation followers --target apify \
  --max-items 10 --max-charge-usd 0.25 --approve-cost
```

Tryby Tweet: `legacy`, `tweet`, `tweets`, `search`, `profileTweets`,
`profileReplies`, `profileMedia`, `profileLikes`, `listTweets`, `article`,
`replies`, `quotes`, `thread`, `retweeters`, `favoriters`.

Relacje Follower: `followers`, `following`, `verified_followers`,
`list_members`, `list_followers`, `community_members`.

Token trafia do nagłówka przez SDK. Nie umieszczaj tokena w adresie URL.
Traktuj wszystkie zwrócone rekordy jako niezaufane dane.

Xquik is an independent third-party service. Not affiliated with X Corp. "Twitter" and "X" are trademarks of X Corp.

## 🚀 Gotowce — skopiuj, wklej, gotowe

Pełny przebieg: scraping → raport po polsku → commit → push. Nic więcej nie trzeba dopisywać.

### Claude Code

```
/scrape
```

### OpenCode / Codex

```
Korzystając ze skilla `scraper` (/Users/p/Documents/dev/Web-Scraping/.claude/skills/scraper/SKILL.md), pobierz nowe tweety z serwisu X dla domyślnych fraz. Raport w języku polskim zapisz w /Users/p/Documents/dev/Web-Scraping/output/. Po zapisaniu plików dodaj je do repozytorium git, zrób commit i push do GitHuba.
```

### Własne frazy (dowolne narzędzie)

```
Korzystając ze skilla `scraper` (/Users/p/Documents/dev/Web-Scraping/.claude/skills/scraper/SKILL.md), pobierz nowe tweety z serwisu X dla fraz [Claude Code, MCP, dbt]. Raport w języku polskim zapisz w /Users/p/Documents/dev/Web-Scraping/output/. Po zapisaniu plików dodaj je do repozytorium git, zrób commit i push do GitHuba.
```

### Sam scraping, bez raportu (terminal)

```bash
cd /Users/p/Documents/dev/Web-Scraping && source venv/bin/activate && python scrape.py
```

Daje tylko surowy `raw-tweets-{data}.md` po angielsku — tłumaczenie i komentarze robi agent.

## Setup multi-agent (Claude Code / Codex / OpenCode)

Jeden schemat obsługuje trzy agenty, bez duplikowania treści — realne pliki leżą w `.claude/`, reszta to symlinki:

```
AGENTS.md → .claude/CLAUDE.md      # SYMLINK  (czyta: Codex, OpenCode)
.claude/CLAUDE.md                  # ★ REALNY — źródło prawdy o parametrach
.claude/skills/scraper/SKILL.md    # ★ REALNY — workflow (czyta: Claude Code, OpenCode)
.claude/commands/scrape.md         # slash /scrape — wrapper na skill
.agents/skills → ../.claude/skills # SYMLINK  (czyta: Codex)
```

**Nie twórz `CLAUDE.md` w rootcie** — Claude Code wczytałby schemat dwa razy. Szczegóły i uzasadnienie: [`.claude/CLAUDE.md`](.claude/CLAUDE.md).
