#!/usr/bin/env python3
"""CLI dla opcjonalnych Actorów Xquik na Apify."""

import argparse
import json
import sys
from pathlib import Path

from xquik_actor_client import (
    FOLLOWER_RELATIONS,
    TWEET_MODES,
    XquikActorError,
    build_follower_input,
    build_tweet_input,
    run_xquik_followers,
    run_xquik_tweets,
)


def _write_results(items, output_path):
    payload = json.dumps(items, ensure_ascii=False, indent=2)
    if output_path:
        path = Path(output_path)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(payload + "\n", encoding="utf-8")
        print(f"Zapisano {len(items)} rekordów: {path}")
    else:
        print(payload)


def _build_parser():
    parser = argparse.ArgumentParser(
        description="Opcjonalne, ograniczone uruchomienia Actorów Xquik."
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    tweets = subparsers.add_parser("tweets", help="X Tweet Scraper")
    tweets.add_argument("--mode", choices=TWEET_MODES, required=True)
    tweets.add_argument("--target", nargs="+", required=True)
    tweets.add_argument("--max-items", type=int, required=True)
    tweets.add_argument("--max-items-per-target", type=int)
    tweets.add_argument(
        "--query-type",
        choices=("Latest", "Top", "Latest + Top"),
        default="Latest",
    )
    tweets.add_argument(
        "--output-variant",
        choices=("legacy", "rich", "raw"),
        default="rich",
    )
    tweets.add_argument(
        "--output-preset",
        choices=("nested", "flat"),
        default="nested",
    )
    tweets.add_argument(
        "--field-style",
        choices=("legacy", "camelCase", "snake_case"),
        default="camelCase",
    )

    followers = subparsers.add_parser("followers", help="X Follower Scraper")
    followers.add_argument(
        "--relation",
        choices=FOLLOWER_RELATIONS,
        nargs="+",
        required=True,
    )
    followers.add_argument("--target", nargs="+", required=True)
    followers.add_argument("--max-items", type=int, required=True)
    followers.add_argument("--max-items-per-target", type=int)
    followers.add_argument(
        "--output-mode",
        choices=("compact", "full", "raw"),
        default="compact",
    )
    followers.add_argument(
        "--dedupe-mode",
        choices=("none", "first", "merge"),
        default="none",
    )
    followers.add_argument("--overlap-mode", action="store_true")

    for subparser in (tweets, followers):
        subparser.add_argument(
            "--max-charge-usd",
            type=float,
            required=True,
        )
        subparser.add_argument(
            "--approve-cost",
            action="store_true",
            help="Potwierdź dopiero po zgodzie użytkownika.",
        )
        subparser.add_argument("--output")
    return parser


def main():
    args = _build_parser().parse_args()
    try:
        if args.command == "tweets":
            actor_input = build_tweet_input(
                args.mode,
                args.target,
                max_items=args.max_items,
                max_items_per_target=args.max_items_per_target,
                query_type=args.query_type,
                output_variant=args.output_variant,
                output_preset=args.output_preset,
                field_style=args.field_style,
            )
            items = run_xquik_tweets(
                actor_input,
                max_items=args.max_items,
                max_total_charge_usd=args.max_charge_usd,
                approved=args.approve_cost,
            )
        else:
            actor_input = build_follower_input(
                args.relation,
                args.target,
                max_items=args.max_items,
                max_items_per_target=args.max_items_per_target,
                output_mode=args.output_mode,
                dedupe_mode=args.dedupe_mode,
                overlap_mode=args.overlap_mode,
            )
            items = run_xquik_followers(
                actor_input,
                max_items=args.max_items,
                max_total_charge_usd=args.max_charge_usd,
                approved=args.approve_cost,
            )
        _write_results(items, args.output)
    except XquikActorError as error:
        print(f"❌ {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
