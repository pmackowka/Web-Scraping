---
name: scraper
description: Scrapuje tweety z X (Twitter) przez Apify i generuje dzienny raport po polsku w output/tweets/{data}.md. Używaj, gdy użytkownik prosi o pobranie tweetów, scraping X, nowe tweety lub dzienny raport.
---

# scraper

> [!IMPORTANT]
> **RAPORT MUSI BYĆ W CAŁOŚCI PO POLSKU.** Sekcja „Co to znaczy" musi mieć **3-4 pełne zdania** — bez sztucznego dopychania objętości. To najczęstszy błąd agentów.

Autorytatywny opis workflow. Parametry uruchomienia (frazy, próg polubień) są zdefiniowane w `.claude/CLAUDE.md` → sekcja „Parametry kanoniczne" i zaszyte jako domyślne w `scrape.py`. **Nie powtarzaj ich tutaj — wołaj skrypt bez flag.**

## Krok 1: Data i konfiguracja

```bash
date +%Y-%m-%d
```

Sprawdź, czy istnieje `.env` z `APIFY_API_TOKEN` (szablon: `config.example.env`). Brak tokena → poproś użytkownika, nie zgaduj.

## Krok 2: Scraping (TYLKO RAZ, wszystkie frazy naraz)

Domyślne frazy i próg polubień:

```bash
cd /Users/p/Documents/dev/Web-Scraping && source venv/bin/activate && python scrape.py
```

Jeśli użytkownik podał własne frazy — wszystkie w jednym `-q`:

```bash
cd /Users/p/Documents/dev/Web-Scraping && source venv/bin/activate && python scrape.py -q "fraza A" "fraza B"
```

> Nigdy nie uruchamiaj skryptu osobno dla każdej frazy — każde wywołanie nadpisuje `output/raw/{data}.md` i zostaje tylko ostatnia fraza.

Wynik: `output/raw/{YYYY-MM-DD}.md` (surowe dane po angielsku).

## Krok 3: Raport po polsku

Przeczytaj `output/raw/{YYYY-MM-DD}.md` (data z kroku 1) i **utwórz nowy plik** `output/tweets/{YYYY-MM-DD}.md`:

```markdown
# Web Scraping - X Tweets

*Data pobrania: YYYY-MM-DD HH:MM*

## Podsumowanie

[3-4 zdania o tym, co ciekawego dzieje się w trendach — po polsku.]

---

## [Fraza]

*Pobrano: YYYY-MM-DD HH:MM*

### @użytkownik
**Nazwa** | Data: [data oryg.] | ❤️ Polubienia: [n] | 🔁 [n] | 👁 [n]

[Treść tweeta przetłumaczona w całości na polski]

> **Co to znaczy:** [3-4 PEŁNE ZDANIA o praktycznym znaczeniu wpisu dla programisty — co z tego wynika i jak wykorzystać narzędzie w codziennej pracy. Bez ogólników i bez naciągania długości: jeśli tweet to luźny komentarz albo żart bez realnej treści, napisz krótko, zamiast dopychać zdaniami-wypełniaczami.]

[Link do tweeta](URL)

---
```

### Zasady

- **Język**: cały plik po polsku, poza nazwami własnymi i datami systemowymi.
- **Zero znaków CJK**: żadnych chińskich/japońskich znaków w polskim tekście. Modele potrafią wstawić `潜在`, `因为`, `数据分析` w środek zdania — to nawracający błąd, wykryty w 10 raportach. Wyjątek: nazwy własne (np. japoński nick autora tweeta). Kontrola przed commitem:
  ```bash
  grep -P '[\x{4e00}-\x{9fff}]' output/tweets/$(date +%F).md
  ```
- **Weryfikacja treści**: mimo filtrów w skrypcie (`EXCLUDE_WORDS`, `AD_BAIT_PHRASES`) sprawdź każdy tweet ręcznie:
  - cokolwiek ewidentnie spoza IT (UFO, ezoteryka, pseudonauka) pomiń w raporcie.
  - **Zakamuflowana reklama**: pomiń tweety, które łączą wyssane z palca/niepotwierdzone statystyki z wezwaniem do akcji typu „skomentuj X, a wyślę Ci szablon/skilla/przewodnika", „DM po dostęp", „link w bio". Regex w skrypcie łapie tylko dosłowne frazy — marketerzy parafrazują, więc oceniaj po wzorcu (teza brzmi jak lead magnet, nie jak realny insight), nie tylko po słowach kluczowych.
- **Jeden plik końcowy**: `output/tweets/{YYYY-MM-DD}.md`, nie twórz wielu raportów.
- **Deduplikacja**: robi ją skrypt (`seen_tweets.json`) — nie filtruj ręcznie.

## Krok 4: Commit i push

Push jest obowiązkowy — użytkownik czyta raporty z aplikacji Git na telefonie.

```bash
cd /Users/p/Documents/dev/Web-Scraping && git add -A && \
  git commit -m "tweets YYYY-MM-DD: <3-5 słów o głównych trendach>" && git push
```

## Krok 5: Podsumowanie w czacie

Po pushu pokaż użytkownikowi krótkie podsumowanie: ile tweetów, jakie trendy, ścieżka do raportu.
