# AGENTS.md

## Data bieżąca

Przed rozpoczęciem pracy sprawdź aktualną datę:
```bash
date +%Y-%m-%d
```
Wszystkie pliki wyjściowe używają formatu `raw-tweets-{YYYY-MM-DD}.md` / `tweets-{YYYY-MM-DD}.md`. Data w nazwie pliku musi zgadzać się z dzisiejszą datą — w przeciwnym razie skrypt utworzy plik z inną datą niż agent odczyta.

## Uruchamianie

Zawsze aktywuj venv przed pracą:

```bash
source venv/bin/activate
```

Skrypt `scrape.py` auto-instaluje brakujące pakiety (apify-client, python-dotenv), ale venv musi być aktywny.

## Wymagana konfiguracja

Plik `.env` z `APIFY_API_TOKEN` jest wymagany. Szablon: `config.example.env`. Bez tokena skrypt kończy pracę z błędem.

## Dwuetapowy pipeline wyników

1. **`scrape.py`** → `output/raw-tweets-{YYYY-MM-DD}.md` — surowe dane po angielsku
2. **Skill OpenCode** (`.opencode/skills/scraper/SKILL.md`) → `output/tweets-{YYYY-MM-DD}.md` — tłumaczenie + komentarze po polsku

Skill to autorytatywny opis workflow — czytaj go przed generowaniem raportu.

## Język — POLSKI

Wszystkie pliki `tweets-*.md` muszą być po polsku (poza nazwami własnymi i datami). Sekcja "Co to znaczy" musi mieć **5-6 pełnych zdań**. To najczęstszy błąd agentów.

## Flagi CLI `scrape.py`

- `-q` przyjmuje **wiele** słów kluczowych oddzielonych spacją — podawaj wszystkie w jednym wywołaniu, nie uruchamiaj skryptu osobno dla każdego słowa (tworzyłoby duplikaty pliku wyjściowego)
- `-l` — minimalna liczba polubień (domyślnie 20); w skillu ustawione 100
- `-t` — `Top` lub `Latest`

## Deduplikacja

`seen_tweets.json` przechowuje ID tweetów z poprzednich uruchomień. Uwaga: `.gitignore` blokuje `*.json`, ale `seen_tweets.json` jest tracked — nie dodawaj innych plików JSON do repo.

## Słowa wykluczające

`EXCLUDE_WORDS` w `scrape.py` (linia 36) to lista fraz, które odrzucają tweety spoza kontekstu IT. Jeśli pojawią się nowe fałszywe pozytywy (np. o UFO dla frazy "Antigravity"), dodaj frazę do tej listy. Porównanie jest case-insensitive.

## Auto-push do remote

Po utworzeniu plików w `output/` **zawsze**:
1. Dodaj wszystkie zmienione/nowe pliki do gita (`git add -A`)
2. Zrób commit z opisem zmian
3. Wypchnij do remote (`git push`)

Użytkownik czyta raporty z poziomu aplikacji Git na telefonie, więc push musi być wykonany za każdym razem. Dotyczy to też zmian w `AGENTS.md`, `SKILL.md`, `README.md` i `scrape.py` — najpierw wprowadź zmiany, potem commit + push.

## Czego nie ma

Brak testów, lintowania, formatowania, typechecka i CI. Nie próbuj uruchamiać `pytest`, `ruff`, `black` itp.
