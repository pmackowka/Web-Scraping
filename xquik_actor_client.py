"""Bezpieczny klient opcjonalnych Actorów Xquik na Apify."""

import os
import re
from decimal import Decimal, InvalidOperation
from urllib.parse import urlparse

from apify_client import ApifyClient
from dotenv import load_dotenv

XQUIK_TWEET_ACTOR = "xquik/x-tweet-scraper"
XQUIK_FOLLOWER_ACTOR = "xquik/x-follower-scraper"

TWEET_MODES = (
    "legacy",
    "tweet",
    "tweets",
    "search",
    "profileTweets",
    "profileReplies",
    "profileMedia",
    "profileLikes",
    "listTweets",
    "article",
    "replies",
    "quotes",
    "thread",
    "retweeters",
    "favoriters",
)

FOLLOWER_RELATIONS = (
    "followers",
    "following",
    "verified_followers",
    "list_members",
    "list_followers",
    "community_members",
)

TWEET_TARGET_FIELDS = {
    "tweet": "tweetIds",
    "tweets": "tweetIds",
    "search": "searchTerms",
    "profileTweets": "twitterHandles",
    "profileReplies": "twitterHandles",
    "profileMedia": "twitterHandles",
    "profileLikes": "twitterHandles",
    "listTweets": "listIds",
    "article": "articleTweetIds",
    "replies": "replyTweetIds",
    "quotes": "quoteTweetIds",
    "thread": "threadTweetIds",
    "retweeters": "retweeterTweetIds",
    "favoriters": "favoriterTweetIds",
}

X_HOSTS = {
    "x.com",
    "www.x.com",
    "twitter.com",
    "www.twitter.com",
    "mobile.twitter.com",
}

HANDLE_PATTERN = re.compile(r"^@?[A-Za-z0-9_]{1,15}$")


class XquikActorError(RuntimeError):
    """Błąd walidacji lub uruchomienia Actora Xquik."""


def run_xquik_tweets(
    actor_input,
    *,
    max_items,
    max_total_charge_usd,
    approved=False,
    client=None,
):
    """Uruchamia Xquik X Tweet Scraper z limitami po stronie Apify."""
    return _run_xquik_actor(
        XQUIK_TWEET_ACTOR,
        actor_input,
        max_items=max_items,
        max_total_charge_usd=max_total_charge_usd,
        approved=approved,
        client=client,
    )


def run_xquik_followers(
    actor_input,
    *,
    max_items,
    max_total_charge_usd,
    approved=False,
    client=None,
):
    """Uruchamia Xquik X Follower Scraper z limitami po stronie Apify."""
    return _run_xquik_actor(
        XQUIK_FOLLOWER_ACTOR,
        actor_input,
        max_items=max_items,
        max_total_charge_usd=max_total_charge_usd,
        approved=approved,
        client=client,
    )


def build_tweet_input(
    mode,
    targets,
    *,
    max_items,
    max_items_per_target=None,
    query_type="Latest",
    output_variant="rich",
    output_preset="nested",
    field_style="camelCase",
):
    """Buduje wejście dla każdego natywnego trybu X Tweet Scraper."""
    if mode not in TWEET_MODES:
        raise XquikActorError(f"Nieobsługiwany tryb: {mode}")
    _validate_positive_integer(max_items, "max_items")
    _validate_positive_integer(
        max_items_per_target,
        "max_items_per_target",
        optional=True,
    )
    _validate_targets(targets)

    actor_input = {
        "mode": mode,
        "maxItems": max_items,
        "queryType": query_type,
        "outputVariant": output_variant,
        "outputPreset": output_preset,
        "fieldStyle": field_style,
    }
    if max_items_per_target is not None:
        actor_input["maxItemsPerTarget"] = max_items_per_target

    urls, plain_targets = _split_urls(targets)
    if urls:
        actor_input["startUrls"] = urls

    if mode == "legacy":
        if plain_targets:
            actor_input["searchTerms"] = plain_targets
    else:
        target_field = TWEET_TARGET_FIELDS[mode]
        if plain_targets:
            _validate_tweet_targets(mode, plain_targets)
            actor_input[target_field] = plain_targets

    if not urls and not plain_targets:
        raise XquikActorError("Podaj co najmniej jeden cel.")
    return actor_input


def build_follower_input(
    relations,
    targets,
    *,
    max_items,
    max_items_per_target=None,
    output_mode="compact",
    dedupe_mode="none",
    overlap_mode=False,
):
    """Buduje wejście dla wszystkich natywnych relacji X Follower Scraper."""
    _validate_positive_integer(max_items, "max_items")
    _validate_positive_integer(
        max_items_per_target,
        "max_items_per_target",
        optional=True,
    )
    _validate_targets(targets)

    if not relations:
        raise XquikActorError("Podaj co najmniej jedną relację.")
    invalid_relations = [
        relation
        for relation in relations
        if relation not in FOLLOWER_RELATIONS
    ]
    if invalid_relations:
        raise XquikActorError(
            f"Nieobsługiwane relacje: {', '.join(invalid_relations)}"
        )

    actor_input = {
        "maxItems": max_items,
        "outputMode": output_mode,
        "dedupeMode": dedupe_mode,
        "overlapMode": overlap_mode,
        "includeTargetMetadata": True,
    }
    if len(relations) == 1:
        actor_input["relation"] = relations[0]
    else:
        actor_input["relations"] = relations
    if max_items_per_target is not None:
        actor_input["maxItemsPerTarget"] = max_items_per_target

    urls, plain_targets = _split_urls(targets)
    if urls:
        actor_input["startUrls"] = urls
    if plain_targets:
        _assign_follower_targets(actor_input, relations, plain_targets)
    return actor_input


def _run_xquik_actor(
    actor_id,
    actor_input,
    *,
    max_items,
    max_total_charge_usd,
    approved,
    client,
):
    _validate_positive_integer(max_items, "max_items")
    if isinstance(max_total_charge_usd, bool):
        raise XquikActorError(
            "max_total_charge_usd musi być dodatnią, skończoną liczbą."
        )
    try:
        charge_limit = Decimal(str(max_total_charge_usd))
    except (InvalidOperation, TypeError, ValueError):
        raise XquikActorError(
            "max_total_charge_usd musi być dodatnią, skończoną liczbą."
        ) from None
    if not charge_limit.is_finite() or charge_limit <= 0:
        raise XquikActorError(
            "max_total_charge_usd musi być dodatnią, skończoną liczbą."
        )
    if approved is not True:
        raise XquikActorError(
            "Płatne uruchomienie niezatwierdzone. Dodaj --approve-cost "
            "dopiero po zgodzie użytkownika."
        )

    bounded_input = dict(actor_input)
    bounded_input["maxItems"] = max_items
    apify_client = client or ApifyClient(token=_get_api_token())
    run = apify_client.actor(actor_id).call(
        run_input=bounded_input,
        max_items=max_items,
        max_total_charge_usd=charge_limit,
    )

    if not run:
        raise XquikActorError("Apify nie zwróciło danych uruchomienia.")
    if run.get("status") != "SUCCEEDED":
        raise XquikActorError(
            f"Actor {actor_id} zakończył się statusem {run.get('status')}."
        )

    dataset_id = run.get("defaultDatasetId")
    if not dataset_id:
        raise XquikActorError("Uruchomienie nie zwróciło identyfikatora datasetu.")

    result = apify_client.dataset(dataset_id).list_items(limit=max_items)
    return list(result.items)


def _get_api_token():
    token = os.getenv("APIFY_API_TOKEN")
    if token:
        return token

    load_dotenv()
    token = os.getenv("APIFY_API_TOKEN")
    if not token:
        raise XquikActorError(
            "Brak APIFY_API_TOKEN. Ustaw token w środowisku lub pliku .env."
        )
    return token


def _validate_positive_integer(value, name, optional=False):
    if optional and value is None:
        return
    if (
        not isinstance(value, int)
        or isinstance(value, bool)
        or value <= 0
    ):
        raise XquikActorError(f"{name} musi być dodatnią liczbą całkowitą.")


def _validate_targets(targets):
    if not targets or any(
        not isinstance(target, str) or not target.strip()
        for target in targets
    ):
        raise XquikActorError("Cele muszą być niepustą listą tekstów.")


def _split_urls(targets):
    urls = []
    plain_targets = []
    for target in targets:
        target = target.strip()
        if target.lower().startswith(("http://", "https://")):
            _validate_x_url(target)
            urls.append(target)
        else:
            plain_targets.append(target)
    return urls, plain_targets


def _validate_x_url(value):
    parsed = urlparse(value)
    if (
        parsed.scheme not in {"http", "https"}
        or parsed.hostname not in X_HOSTS
        or parsed.username
        or parsed.password
    ):
        raise XquikActorError(
            "Nieobsługiwany URL. Użyj adresu x.com lub twitter.com."
        )


def _validate_tweet_targets(mode, targets):
    if mode.startswith("profile"):
        invalid = [target for target in targets if not HANDLE_PATTERN.fullmatch(target)]
        if invalid:
            raise XquikActorError(
                f"Niepoprawne uchwyty X: {', '.join(invalid)}"
            )
    elif mode != "search":
        invalid = [target for target in targets if not target.isdigit()]
        if invalid:
            raise XquikActorError(
                f"Ten tryb wymaga numerycznych ID: {', '.join(invalid)}"
            )


def _assign_follower_targets(actor_input, relations, targets):
    relation_groups = {
        "profile": {"followers", "following", "verified_followers"},
        "list": {"list_members", "list_followers"},
        "community": {"community_members"},
    }
    groups = {
        group
        for group, group_relations in relation_groups.items()
        if any(relation in group_relations for relation in relations)
    }
    if len(groups) != 1:
        raise XquikActorError(
            "Relacje z różnych typów celu wymagają osobnych uruchomień."
        )

    group = groups.pop()
    if group == "profile":
        invalid = [target for target in targets if not HANDLE_PATTERN.fullmatch(target)]
        if invalid:
            raise XquikActorError(
                f"Niepoprawne uchwyty X: {', '.join(invalid)}"
            )
        actor_input["twitterHandles"] = targets
    elif group == "list":
        _require_numeric_ids(targets)
        actor_input["listIds"] = targets
    else:
        _require_numeric_ids(targets)
        actor_input["communityIds"] = targets


def _require_numeric_ids(targets):
    invalid = [target for target in targets if not target.isdigit()]
    if invalid:
        raise XquikActorError(
            f"Relacja wymaga numerycznych ID: {', '.join(invalid)}"
        )
