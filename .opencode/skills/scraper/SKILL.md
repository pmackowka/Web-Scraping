# scraper

Scrapuje tweety z X (Twitter) używając Apify API i zapisuje wyniki do Markdown.

## Uruchomienie

Gdy użytkownik poprosi o pobranie tweetów z X, wykonaj następujące kroki:

### Krok 1: Sprawdź konfigurację

Sprawdź czy istnieje plik `.env` w projekcie `/Users/p/Documents/dev/Web-Scraping/`:

```
cat /Users/p/Documents/dev/Web-Scraping/.env
```

Jeśli plik nie istnieje lub nie zawiera `APIFY_API_TOKEN`:
1. Poproś użytkownika o token z https://console.apify.com/settings
2. Utwórz plik `.env` z tokenem

### Krok 2: Uruchom skrypt

```
cd /Users/p/Documents/dev/Web-Scraping && python scrape.py -q "OpenCode" -m 20 -t Top
```

**Opcjonalne parametry:**
- `-q` --query: hasło wyszukiwania (domyślnie: OpenCode)
- `-m` --max: maksymalna liczba tweetów (domyślnie: 20)
- `-t` --type: typ wyszukiwania - Top lub Latest (domyślnie: Top)

**Przykładowe wywołania:**
```
# Tylko OpenCode
python scrape.py -q "OpenCode"

# OpenCode + CloudCode
python scrape.py -q "OpenCode"

# Tylko CloudCode
python scrape.py -q "CloudCode"

# Inne hasło
python scrape.py -q "Cursor" -m 50 -t Latest
```

### Krok 3: Pobierz wyniki

Wynik zapisuje się w:
```
/Users/p/Documents/dev/Web-Scraping/output/tweets-{YYYY-MM-DD}.md
```

Otwórz plik i pokaż użytkownikowi W JĘZYKU POLSKIM:
- Podsumowanie (najważniejsze tematy z tweetów) w języku polskim.
- Listę tweetów z treściami przetłumaczonymi w całości na język polski. Oprócz samego tłumaczenia, **dla każdego tweeta musisz dopisać krótki kontekst/opis**, używając przedrostka:
`Co to znaczy: `
W 2-3 zdaniach wyjaśnij praktyczne znaczenie każdego wpisu - co ta informacja oznacza dla mnie i jak mogę wykorzystać omawiane narzędzia, rozwiązania lub triki w codziennej pracy programistycznej używając OpenCode lub CloudCode. Same suche przetłumaczenie to za mało.

> [!IMPORTANT]
> Zanim pokażesz wyniki użytkownikowi, bezwzględnie musisz:
> 1. Przetłumaczyć w pliku Markdown wszystkie tweety na język polski.
> 2. Dodać dla każdego tweeta sekcję "Co to znaczy: " z merytorycznym i jasnym komentarzem co on oznacza w praktyce z perspektywy korzystania z OpenCode i CloudCode!

## Przykładowe uruchomienie

Użytkownik mówi:
- "Pobierz tweety o OpenCode z X"
- "Znajdź najnowsze wpisy o CloudCode na Twitterze"
- "Ściągnij tweety o CLI agents"
- "/scraper"

## Uwagi

- Jeśli API token nie jest dostępny, poinformuj użytkownika, że musi go podać
- Skrypt automatycznie szuka OpenCode i CloudCode razem
- Maksymalnie 20 tweetów do pobrania (domyślnie)
- Jeśli actor zwróci błąd, pokaż użytkownikowi komunikat błędu