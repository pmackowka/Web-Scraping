#!/usr/bin/env python3
"""
Web Scraper - pobiera tweety z X (Twitter) używając Apify API.
"""

import os
import sys
import json
import argparse
from datetime import datetime, timedelta
from pathlib import Path

try:
    from apify_client import ApifyClient
    from dotenv import load_dotenv
except ImportError:
    print("❌ Brak zależności. Aktywuj venv i zainstaluj pakiety:")
    print("   source venv/bin/activate && pip install -r requirements.txt")
    sys.exit(1)

load_dotenv()

ACTOR_ID = "kaitoeasyapi/twitter-x-data-tweet-scraper-pay-per-result-cheapest"
OUTPUT_DIR = Path(__file__).parent / "output"
RAW_DIR = OUTPUT_DIR / "raw"
RAW_DIR.mkdir(parents=True, exist_ok=True)
SEEN_TWEETS_FILE = Path(__file__).parent / "seen_tweets.json"

# Domyślne frazy — źródło prawdy opisane w .claude/CLAUDE.md ("Parametry kanoniczne")
DEFAULT_KEYWORDS = ["Claude Code", "Codex", "n8n"]

# Odrzuca tweety spoza kontekstu IT. Porównanie case-insensitive.
# "disclosure" celowo usunięte — łapało security-tweety o responsible disclosure.
EXCLUDE_WORDS = [
    "ufo",
    "extraterrestrial",
    "alien",
    "aliens",
    "area 51",
    "redstone arsenal",
]

# Odrzuca zakamuflowaną reklamę (engagement bait) — wzorzec "wrzuć komentarz,
# wyślę Ci szablon/skilla" typowy dla marketerów na X. Dosłowne frazy, jak
# EXCLUDE_WORDS — łapie tylko najbardziej oczywiste przypadki, parafrazy
# przechodzą dalej i muszą zostać złapane ręcznie w kroku 3 (patrz SKILL.md).
AD_BAIT_PHRASES = [
    "comment and i'll send",
    "comment below and i'll",
    "drop a comment and i'll",
    "reply and i'll send",
    "dm me and i'll send",
    "dm me for the",
    "dm me the word",
    "i'll dm you the",
    "i'll send you the",
    "comment \"guide\"",
    "comment 'guide'",
    "comment \"template\"",
    "comment 'template'",
    "link in bio",
    "worth bookmarking",
    "bookmark this before",
]


def get_api_token():
    """Pobiera API token z zmiennej środowiskowej lub pliku .env"""
    token = os.getenv("APIFY_API_TOKEN")
    if token:
        return token

    env_file = Path(__file__).parent / ".env"
    if env_file.exists():
        load_dotenv(env_file)
        token = os.getenv("APIFY_API_TOKEN")
        if token:
            return token

    print("❌ Brak API token!")
    print("   1. Wejdź na https://console.apify.com/settings")
    print("   2. Skopiuj token z sekcji 'API tokens'")
    print("   3. Wklej do pliku .env jako APIFY_API_TOKEN=...")
    sys.exit(1)


def load_seen_tweets():
    """Wczytuje listę ID tweetów, które już widzieliśmy"""
    if SEEN_TWEETS_FILE.exists():
        try:
            return set(json.loads(SEEN_TWEETS_FILE.read_text(encoding="utf-8")))
        except Exception:
            return set()
    return set()


def save_seen_tweets(seen_ids):
    """Zapisuje listę ID tweetów do pliku"""
    try:
        SEEN_TWEETS_FILE.write_text(json.dumps(list(seen_ids)), encoding="utf-8")
    except Exception as e:
        print(f"⚠️ Nie udało się zapisać seen_tweets.json: {e}")


def scrape_tweets(query, max_items=20, query_type="Top"):
    """Pobiera tweety dla danego zapytania"""
    client = ApifyClient(token=get_api_token())

    input_data = {
        "twitterContent": query,
        "maxItems": max_items,
        "queryType": query_type,
        "lang": "en",
        "include:nativeretweets": True
    }

    print(f"🔍 Szukam: '{query}' ({max_items} tweetów, {query_type})...")

    try:
        run = client.actor(ACTOR_ID).call(run_input=input_data)

        if not run or not run.get("defaultDatasetId"):
            print(f"⚠️  Brak wyników dla: {query}")
            return []

        items = list(client.dataset(run.get("defaultDatasetId")).iterate_items())

        if not items:
            print(f"⚠️  Brak wyników w datasecie dla: {query}")
            return []

        print(f"✅ Pobrano {len(items)} tweetów dla: {query}")
        return items

    except Exception as e:
        print(f"❌ Błąd podczas pobierania '{query}': {e}")
        return []


def filter_tweets(items, keyword, min_likes=20, exclude_words=None):
    """Filtruje tweety zawierające keyword i mające min_likes polubień"""
    filtered = []
    keyword_lower = keyword.lower()

    for item in items:
        text = item.get("text", "")
        text_lower = text.lower()
        like_count = item.get("likeCount", 0)

        if keyword_lower in text_lower and like_count >= min_likes:
            if exclude_words and any(excl in text_lower for excl in exclude_words):
                continue
            filtered.append(item)

    print(f"📝 Przefiltrowano: {len(filtered)}/{len(items)} tweetów spełnia kryteria (słowo: '{keyword}', min. {min_likes} ❤️)")
    return filtered


def format_to_markdown(items, keyword):
    """Konwertuje tweety do formatu Markdown"""
    if not items:
        return f"## {keyword}\n\nBrak tweetów do wyświetlenia.\n"

    md = f"## {keyword}\n\n"
    md += f"*Pobrano: {datetime.now().strftime('%Y-%m-%d %H:%M')}*\n\n"

    for item in items:
        author = item.get("author", {})
        username = author.get("userName", "unknown")
        name = author.get("name", username)
        text = item.get("text", "")
        created_at = item.get("createdAt", "")
        like_count = item.get("likeCount", 0)
        retweet_count = item.get("retweetCount", 0)
        view_count = item.get("viewCount", 0)
        url = item.get("url", "")

        md += f"### @{username}\n"
        md += f"**{name}** | "
        md += f"Data: {created_at} | "
        md += f"❤️ Polubienia: {like_count} | "
        md += f"🔁 {retweet_count} | "
        md += f"👁 {view_count}\n\n"
        md += f"{text}\n\n"
        if url:
            md += f"[Link do tweeta]({url})\n"
        md += "\n---\n\n"

    return md


def save_to_file(content, filepath):
    """Zapisuje treść do pliku pod podaną ścieżką"""
    filepath.write_text(content, encoding="utf-8")
    print(f"💾 Zapisano: {filepath}")
    return filepath


def main():
    parser = argparse.ArgumentParser(description="Pobieranie tweetów z X")
    parser.add_argument("-q", "--query", nargs="+", default=DEFAULT_KEYWORDS,
                      help=f"Hasła wyszukiwania, wiele naraz (default: {' '.join(DEFAULT_KEYWORDS)})")
    parser.add_argument("-m", "--max", type=int, default=10, help="Maksymalna liczba tweetów na frazę (default: 10)")
    parser.add_argument("-t", "--type", default="Top", choices=["Top", "Latest"],
                      help="Typ wyszukiwania (default: Top)")
    parser.add_argument("-l", "--likes", type=int, default=400, help="Minimalna liczba polubień (default: 400)")
    parser.add_argument("-d", "--days", type=int, default=7,
                      help="Okno świeżości w dniach — dokleja 'since:' do zapytania, 0 wyłącza (default: 7)")

    args = parser.parse_args()

    keywords = args.query

    all_markdown = "# Web Scraping - X Tweets\n\n"
    all_markdown += f"*Data pobrania: {datetime.now().strftime('%Y-%m-%d %H:%M')}*\n\n"

    seen_ids = load_seen_tweets()
    new_seen_ids = set()
    total_new = 0

    # Filtr świeżości: tryb Top bez daty zwraca stare viralowe tweety (płatne per result)
    since_clause = ""
    if args.days > 0:
        since_date = (datetime.now() - timedelta(days=args.days)).strftime("%Y-%m-%d")
        since_clause = f" since:{since_date}"

    for keyword in keywords:
        items = scrape_tweets(f"{keyword}{since_clause}", args.max, args.type)
        filtered = filter_tweets(items, keyword, args.likes, EXCLUDE_WORDS + AD_BAIT_PHRASES)

        # Deduplikacja — tweet bez ID/URL przechodzi, ale nie trafia do seen
        unique_items = []
        for item in filtered:
            tweet_id = item.get("id") or item.get("url")
            if tweet_id in seen_ids or tweet_id in new_seen_ids:
                continue
            unique_items.append(item)
            if tweet_id:
                new_seen_ids.add(tweet_id)

        total_new += len(unique_items)
        markdown = format_to_markdown(unique_items, keyword)
        all_markdown += markdown

    if total_new == 0:
        print("\nℹ️ Nie znaleziono żadnych nowych tweetów.")
        # Opcjonalnie: można przerwać zapisywanie pustego pliku, 
        # ale zostawmy to użytkownikowi do decyzji.
        
    filename = f"{datetime.now().strftime('%Y-%m-%d')}.md"
    filepath = RAW_DIR / filename
    save_to_file(all_markdown, filepath)

    # Zapisujemy nowe ID do pliku na przyszłość
    save_seen_tweets(seen_ids.union(new_seen_ids))

    print(f"\n✅ Gotowe! Pobrano unikalnych: {total_new}. Wynik w: {filepath}")


if __name__ == "__main__":
    main()