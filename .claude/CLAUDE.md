# CLAUDE.md

Dzienny scraping tweetów z X (Apify) + raport po polsku. Ten plik jest jedynym źródłem prawdy o parametrach uruchomienia.

## Kto co czyta (setup multi-agent)

```
Web-Scraping/
├── AGENTS.md → .claude/CLAUDE.md      # SYMLINK  (czyta: Codex, OpenCode)
├── .claude/
│   ├── CLAUDE.md                      # ★ REALNY — ten plik
│   ├── skills/scraper/SKILL.md        # ★ REALNY  (czyta: Claude Code, OpenCode)
│   └── commands/scrape.md             # slash /scrape — cienki wrapper na skill
└── .agents/
    └── skills → ../.claude/skills     # SYMLINK  (czyta: Codex)
```

Reguła: `.claude/` = pliki realne, `AGENTS.md` i `.agents/` = same wskaźniki. Edycja `.claude/CLAUDE.md` natychmiast zmienia `AGENTS.md` — to ten sam i-node, nie ma czego synchronizować.

> **NIE twórz `CLAUDE.md` w rootcie repo.** Claude Code wczytałby schemat dwa razy (root + `.claude/`). Uwaga na `/init`. Kontrola: `ls CLAUDE.md` musi zwracać „No such file".

Uwaga: konfiguracja (uprawnienia, MCP) **nie jest** współdzielona między narzędziami — symlinki obejmują tylko instrukcje i skille.

## Parametry kanoniczne

Trzy frazy, jedno wywołanie, próg 500 polubień:

```bash
cd /Users/p/Documents/dev/Web-Scraping && source venv/bin/activate && \
  python scrape.py -q "Claude Code" "Codex" "n8n" -m 10 -t Top -l 500
```

To są też domyślne wartości w `scrape.py` — samo `python scrape.py` daje ten sam efekt. Jeśli zmieniasz frazy lub próg, zmień je **tutaj i w `scrape.py`**; skill i komenda odsyłają do tego pliku, nie powtarzają wartości.

| Flaga | Znaczenie | Domyślnie |
|-------|-----------|-----------|
| `-q` | Frazy (wiele naraz, oddzielone spacją) | `"Claude Code" "Codex" "n8n"` |
| `-m` | Maks. tweetów na frazę | 10 |
| `-t` | `Top` lub `Latest` | Top |
| `-l` | Minimalna liczba polubień | 500 |

> **Wszystkie frazy w jednym wywołaniu `-q`.** Osobne uruchomienia tego samego dnia nadpisują `raw-tweets-{data}.md` — zostanie tylko ostatnia fraza.

## Data bieżąca

Sprawdź przed startem: `date +%Y-%m-%d`. Nazwy plików (`raw-tweets-{YYYY-MM-DD}.md`, `tweets-{YYYY-MM-DD}.md`) muszą używać dzisiejszej daty — inaczej agent czyta inny plik, niż skrypt zapisał.

## Środowisko

`source venv/bin/activate` przed każdą pracą. Wymagany `.env` z `APIFY_API_TOKEN` (szablon: `config.example.env`) — bez tokena skrypt kończy się błędem. Token trzymamy wyłącznie w `.env`; nigdy nie wklejaj go do plików w repo ani do promptów.

## Dwuetapowy pipeline

1. `scrape.py` → `output/raw-tweets-{data}.md` — surowe dane po angielsku
2. Skill `scraper` (`.claude/skills/scraper/SKILL.md`) → `output/tweets-{data}.md` — tłumaczenie + komentarze po polsku

**Skill jest autorytatywnym opisem workflow — przeczytaj go przed generowaniem raportu.**

## Język — POLSKI

Wszystkie pliki `tweets-*.md` po polsku (poza nazwami własnymi i datami systemowymi). Sekcja „Co to znaczy" musi mieć **5-6 pełnych zdań**. To najczęstszy błąd agentów.

**Zero znaków CJK w polskim tekście.** Modele wstawiają chińskie słowa w środek zdania (`潜在nie`, `warto密切关注`, `czy数据分析`) — znaleziono to w 10 raportach i naprawiono 2026-07-14. Sprawdź przed commitem:

```bash
grep -P '[\x{4e00}-\x{9fff}]' output/tweets-$(date +%F).md   # musi nic nie zwrócić
```

## Deduplikacja i filtry

- `seen_tweets.json` przechowuje ID tweetów z poprzednich uruchomień. `.gitignore` blokuje `*.json`, ale ten plik jest tracked — nie dodawaj innych JSON-ów do repo.
- `filter_tweets` wymaga **dosłownego** wystąpienia frazy w treści tweeta (case-insensitive) — świadoma decyzja: zero fałszywych pozytywów kosztem części trafień.
- `EXCLUDE_WORDS` w `scrape.py` odrzuca tweety spoza IT. Nowy fałszywy pozytyw → dopisz frazę do listy.

## Auto-push do remote

Po utworzeniu plików w `output/` **zawsze**: `git add -A`, commit z opisem, `git push`. Użytkownik czyta raporty z aplikacji Git na telefonie — bez pusha raport dla niego nie istnieje. Dotyczy też zmian w tym pliku, `SKILL.md`, `README.md` i `scrape.py`.

## Czego nie ma

Brak testów, lintowania, formatowania, typechecka i CI. Nie próbuj uruchamiać `pytest`, `ruff`, `black` itp.
