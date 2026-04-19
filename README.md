# Web Scraping

Projekt do scrapowania danych z X (Twitter) używając Apify API.

## Wymagania

```bash
pip install -r requirements.txt
```

## Konfiguracja

1. Skopiuj plik konfiguracyjny:
```bash
cp config.example.env .env
```

2. Dodaj swój API token z https://console.apify.com/settings

## Użycie

```bash
# Aktywuj środowisko
source venv/bin/activate  # lub venv\Scripts\activate na Windows

# Uruchom scraper
python scrape.py -q "OpenCode" -m 20 -t Top
```

### Parametry:
- `-q` --query: hasło wyszukiwania (domyślnie: OpenCode)
- `-m` --max: liczba tweetów (domyślnie: 20)
- `-t` --type: Top lub Latest (domyślnie: Top)

## Wyniki

Wyniki zapisują się w folderze `output/`:
```
output/tweets-2026-04-18.md
```

## Uruchomienie z Open Code

Gdy potrzebujesz pobrać tweety, powiedz:
- "Pobierz tweety o OpenCode z X"
- lub "/scraper"

Skrypt automatycznie pobiera tweety dla OpenCode i CloudCode i zapisuje w `output/`.