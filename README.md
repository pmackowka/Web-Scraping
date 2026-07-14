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
| `-l` | Minimalna liczba polubień | 500 |

> **Wszystkie frazy w jednym wywołaniu `-q`.** Osobne uruchomienia tego samego dnia nadpisują `raw-tweets-{data}.md` — zostaje tylko ostatnia fraza.

**Filtry:** skrypt odrzuca tweety bez dosłownego wystąpienia frazy w treści, poniżej progu polubień oraz zawierające frazy z listy `EXCLUDE_WORDS` (UFO, alien itp.). Duplikaty odsiewa `seen_tweets.json` — ID tweetów ze wszystkich poprzednich uruchomień.

## Jak uruchomić raport (etap 2)

| Narzędzie | Jak |
|-----------|-----|
| **Claude Code** | `/scrape` (albo poproś o użycie skilla `scraper`) |
| **OpenCode** | „Korzystając ze skilla `scraper`, pobierz nowe tweety i zapisz raport w `output/`. Potem commit i push." |
| **Codex** | To samo — skille widzi przez `.agents/skills` |
| **Terminal** | `python scrape.py` daje tylko surowy plik; tłumaczenie i komentarze robi agent |

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
