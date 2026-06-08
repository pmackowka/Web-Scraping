# Web Scraping

Projekt do scrapowania danych z X (Twitter) używając Apify API.

## Wymagania

### 1. Utwórz środowisko wirtualne

```bash
# macOS / Linux:
python -m venv venv

# Windows:
python -m venv venv
```

### 2. Aktywuj środowisko wirtualne

```bash
# macOS / Linux:
source venv/bin/activate

# Windows (PowerShell):
venv\Scripts\Activate

# Windows (CMD):
venv\Scripts\activate.bat
```

### 3. Zainstaluj zależności

```bash
pip install -r requirements.txt
```

> **Uwaga:** Zawsze aktywuj venv przed uruchomieniem projektu (`source venv/bin/activate`). Środowisko wirtualne izoluje zależności tego projektu od innych.

## Konfiguracja

1. Skopiuj plik konfiguracyjny:
```bash
cp config.example.env .env
```

2. Dodaj swój API token z https://console.apify.com/settings

## Użycie

```bash
# Najpierw aktywuj środowisko:
source venv/bin/activate

# Uruchom skrypt:
python scrape.py -q "OpenCode" "Claude Code" -m 5 -t Top
```

### Parametry:
- `-q` --query: hasło wyszukiwania (domyślnie: OpenCode)
- `-m` --max: liczba tweetów na frazę (domyślnie: 5)
- `-t` --type: Top lub Latest (domyślnie: Top)
- `-l` --likes: minimalna liczba polubień (domyślnie: 200)

> **Filtrowanie wykluczające:** Skrypt automatycznie odrzuca tweety zawierające frazy z listy `EXCLUDE_WORDS` (np. UFO, alien). Aby dodać nowe, edytuj stałą w `scrape.py:36`.

## Wyniki

Wyniki zapisują się w folderze `output/`:
- `output/raw-tweets-{YYYY-MM-DD}.md`: Surowe dane (angielski/oryginalny).
- `output/tweets-{YYYY-MM-DD}.md`: **Ostateczny raport** (przetłumaczony na polski, z komentarzami).

## Ręczne uruchomienie

### Z Claude Code (polecenie `/scrape`)

Wpisz `/scrape` w Claude Code — polecenie jest zdefiniowane w `.claude/commands/scrape.md`.

### Z OpenCode (skill)

Polecenie dla agenta nr 1:
```
Korzystając ze Skilla z '/Users/p/Documents/dev/Web-Scraping/.opencode/skills/scraper/SKILL.md', pobierz nowe tweety z serwisu X dla fraz [Claude Code, OpenRouter, Codex, Antigravity]. Wynikowy plik markdown zapisz w '/Users/p/Documents/dev/Web-Scraping/output/'. Po zapisaniu plików, dodaj nowe pliki Markdown do repozytorium git, zrób commit i push do GitHuba.
```

Polecenie dla agenta nr 2:
```
Korzystając ze Skilla z '/Users/p/Documents/dev/Web-Scraping/.opencode/skills/scraper/SKILL.md', pobierz nowe tweety z serwisu X dla fraz [OpenCode, Claude Code, OpenRouter, OpenAI Codex, Antigravity, @warpdotdev, @stape_io, n8n]. Wynikowy plik markdown zapisz w '/Users/p/Documents/dev/Web-Scraping/output/'. Po zapisaniu plików, dodaj nowe pliki Markdown do repozytorium git, zrób commit i push do GitHuba.
```

### Z terminala (bash)

```bash
cd /Users/p/Documents/dev/Web-Scraping && source venv/bin/activate && python scrape.py -q "OpenCode" "Claude Code" "OpenRouter" "OpenAI Codex" "Antigravity" "@warpdotdev" "@stape_io" "n8n" -m 10 -t Top -l 200
```

### Parametry `scrape.py`:

| Flaga | Opis | Domyślnie |
|-------|------|-----------|
| `-q` | Frazy wyszukiwania (wiele naraz, oddzielone spacją) | OpenCode |
| `-m` | Maksymalna liczba tweetów na frazę | 5 |
| `-t` | Typ wyników: `Top` lub `Latest` | Top |
| `-l` | Minimalna liczba polubień | 20 |

> **Ważne:** Zawsze podawaj wszystkie frazy w jednym wywołaniu `-q`. Uruchamianie skryptu osobno dla każdej frazy tworzy duplikaty pliku wyjściowego.
