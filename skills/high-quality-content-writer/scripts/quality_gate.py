#!/usr/bin/env python3
"""Deterministic content quality gate for high-quality-content-writer.

Combines:
- tropes.fyi-style pattern scoring from slop_score.py
- slop-check quote/article criteria
- a c8c-style evaluator JSON contract: score, reason, fix_instructions, criteria
"""

from __future__ import annotations

import argparse
import json
import re
from typing import Any

import slop_score


EN_AI_PATTERNS = (
    "essentially",
    "it's important to note",
    "in conclusion",
    "at the end of the day",
    "a myriad of",
    "navigate the landscape",
    "unlock the potential",
    "in today's fast-paced world",
    "game-changer",
    "deep dive",
    "leverage",
    "synergy",
    "holistic approach",
)

RU_AI_PATTERNS = (
    "в конечном итоге",
    "стоит отметить",
    "важно понимать",
    "ключевой момент",
    "безусловно",
    "в целом и общем",
    "не лишним будет",
    "нельзя не отметить",
    "это позволяет",
    "данный подход",
)

BUZZWORDS = (
    "innovative",
    "cutting-edge",
    "revolutionary",
    "empower",
    "transform",
    "seamless",
    "robust",
    "game-changing",
    "next-generation",
    "best-in-class",
    "holistic",
    "paradigm",
    "ecosystem",
    "scalable",
    "actionable",
    "streamline",
    "disruptive",
    "world-class",
)


def words(text: str) -> list[str]:
    return re.findall(r"\b[\w']+\b", text, flags=re.UNICODE)


def sentences(text: str) -> list[str]:
    return [s.strip() for s in re.split(r"(?<=[.!?])\s+", text) if s.strip()]


def paragraphs(text: str) -> list[str]:
    return [p.strip() for p in re.split(r"\n\s*\n+", text) if p.strip()]


def count_patterns(text: str, patterns: tuple[str, ...]) -> int:
    lower = text.lower()
    return sum(lower.count(p.lower()) for p in patterns)


def count_regex(text: str, pattern: str) -> int:
    return len(re.findall(pattern, text, flags=re.IGNORECASE | re.MULTILINE))


def has_first_person(text: str) -> bool:
    return bool(re.search(r"\b(I|me|my|mine|we|our|ours|я|меня|мой|мы|наш)\b", text, re.IGNORECASE))


def count_specifics(text: str) -> int:
    number_count = count_regex(text, r"\b\d+(?:[.,]\d+)?%?\b")
    date_count = count_regex(text, r"\b(?:20\d{2}|19\d{2}|Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\b")
    link_count = count_regex(text, r"https?://|www\.")
    codeish_count = count_regex(text, r"`[^`]+`|\b[A-Z][A-Za-z0-9]+(?:\.[A-Za-z0-9_]+|\(\))")
    proper_count = count_regex(text, r"\b[A-Z][a-z]+(?:\s+[A-Z][a-z]+){0,2}\b")
    return number_count + date_count + link_count + codeish_count + proper_count


def info_density(text: str) -> float:
    wc = max(len(words(text)), 1)
    return count_specifics(text) / wc * 1000


def verdict_from_article_score(score: int) -> tuple[str, float]:
    if score <= 20:
        return "clean", 1.0
    if score <= 35:
        return "good", 1.0
    if score <= 50:
        return "acceptable", 0.7
    if score <= 70:
        return "probable_slop", 0.3
    return "obvious_slop", 0.1


def verdict_from_quote_score(score: int) -> tuple[str, float]:
    if score <= 10:
        return "clean", 1.0
    if score <= 18:
        return "good", 1.0
    if score <= 25:
        return "acceptable", 0.7
    return "probable_slop", 0.3


def points_from_density(density: float) -> int:
    if density >= 15:
        return 0
    if density >= 10:
        return 1
    if density >= 5:
        return 2
    if density >= 2:
        return 3
    return 4


def clamp(value: int, low: int, high: int) -> int:
    return max(low, min(high, value))


def quote_slop_score(text: str) -> tuple[int, list[str], dict[str, int]]:
    wc = len(words(text))
    spec = count_specifics(text)
    pattern_count = count_patterns(text, EN_AI_PATTERNS) + count_patterns(text, RU_AI_PATTERNS)
    first_person = has_first_person(text)
    density = info_density(text)

    scores: dict[str, int] = {}
    scores["zero_position"] = 5 if not first_person and spec < 2 else 2 if spec < 2 else 0
    scores["no_life_dirt"] = 6 if spec == 0 else 3 if spec < 3 else 0
    scores["no_verifiability"] = 4 if spec == 0 else 2 if spec < 2 else 0
    scores["fake_confidence"] = clamp(count_regex(text, r"\b(always|never|must|undoubtedly|certainly|безусловно)\b") * 2, 0, 4)
    scores["lexical_repetition"] = clamp(pattern_count, 0, 3)
    scores["too_clean_logic"] = 3 if not re.search(r"\b(but|although|however|except|unless|но|однако)\b", text, re.IGNORECASE) and wc > 35 else 0
    scores["weak_causality"] = 4 if count_regex(text, r"\bbecause\b|\bso that\b|\btherefore\b|\bпоэтому\b") == 0 and wc > 35 else 1 if wc > 35 else 0
    scores["no_personal_stake"] = 5 if not first_person else 0
    first_hand_bonus = -5 if re.search(r"\b(I tried|I built|my project|my experience|когда я делал|я пробовал)\b", text, re.IGNORECASE) else 0
    scores["first_hand_bonus"] = first_hand_bonus
    scores["info_density"] = points_from_density(density)

    indicators = [key for key, value in scores.items() if value > 0]
    if first_hand_bonus < 0:
        indicators.append("first_hand_bonus")
    total = sum(scores.values())
    return total, indicators, scores


def article_slop_score(text: str) -> tuple[int, list[str], dict[str, int]]:
    wc = len(words(text))
    paras = paragraphs(text)
    sents = sentences(text)
    spec = count_specifics(text)
    density = info_density(text)
    first_person = has_first_person(text)
    pattern_count = count_patterns(text, EN_AI_PATTERNS) + count_patterns(text, RU_AI_PATTERNS)
    buzzword_count = count_patterns(text, BUZZWORDS)
    link_count = count_regex(text, r"https?://|www\.")
    list_count = count_regex(text, r"(?m)^\s*(?:[-*]|\d+\.)\s+")
    heading_count = count_regex(text, r"(?m)^#{1,4}\s+")
    codeish = count_regex(text, r"```|`[^`]+`")
    contradiction_count = count_regex(text, r"\b(but|although|however|except|unless|tradeoff|caveat|но|однако)\b")
    cta_count = count_regex(text, r"\b(sign up|book a demo|buy now|start today|subscribe|join now)\b")

    scores: dict[str, int] = {}
    scores["zero_author_position"] = 6 if not first_person and spec < 4 else 3 if not first_person else 0
    scores["too_even_tone"] = 4 if count_regex(text, r"!|\?|I |we |lol|damn|wrong|mistake") == 0 and wc > 250 else 2 if wc > 250 else 0
    scores["no_personal_accountability"] = 4 if not first_person else 2 if count_regex(text, r"\bI\b|\bmy\b|\bwe\b|\bour\b") < 2 else 0
    scores["clone_paragraphs"] = 5 if len(paras) >= 4 and max((len(p) for p in paras), default=0) - min((len(p) for p in paras), default=0) < 180 else 2 if len(paras) >= 4 else 0
    scores["lists_for_lists_sake"] = 4 if list_count >= 8 else 2 if list_count >= 4 else 0
    scores["unnatural_completeness"] = 5 if heading_count >= 6 and wc < 1800 else 3 if heading_count >= 4 else 0
    scores["generic_without_specifics"] = 6 if spec < 3 and wc > 150 else 3 if spec < 8 and wc > 400 else 0
    scores["no_verifiability"] = 7 if spec < 2 and link_count == 0 else 4 if spec < 5 and link_count == 0 else 0
    scores["no_life_dirt"] = 5 if count_regex(text, r"\bbroke|stuck|failed|surprise|bug|mistake|blocked|слом|застрял|ошибка\b") == 0 and wc > 250 else 0
    scores["no_edge_cases"] = 5 if contradiction_count == 0 and wc > 300 else 3 if contradiction_count < 2 and wc > 700 else 0
    scores["links_for_show"] = 5 if link_count > 0 and count_regex(text, r"wikipedia|general|guide|overview") else 0
    scores["fake_confidence"] = clamp(count_regex(text, r"\b(always|never|must|undoubtedly|certainly|clearly|obviously|безусловно)\b") * 2, 0, 5)
    scores["implausible_examples"] = 5 if count_regex(text, r"\b\d{2,4}%\b") and link_count == 0 else 0
    scores["weak_cause_effect"] = 6 if count_regex(text, r"\bbecause\b|\btherefore\b|\bso that\b|\bled to\b|\bresulted in\b|\bпоэтому\b") == 0 and wc > 350 else 3 if wc > 350 else 0
    scores["lexical_repetition"] = clamp(pattern_count + buzzword_count // 2, 0, 4)
    scores["pseudo_metaphors"] = clamp(count_regex(text, r"\blike a\b|\bthink of it as\b|\borchestra|bridge|highway|engine\b"), 0, 3)
    scores["bad_terminology"] = clamp(buzzword_count, 0, 5)
    scores["sharp_depth_jumps"] = 2 if count_regex(text, r"\bbasically\b|\bsimply\b") and codeish else 0
    scores["too_clean_logic"] = 4 if contradiction_count == 0 and wc > 300 else 2 if contradiction_count < 2 and wc > 800 else 0
    scores["sterile_conclusions"] = 4 if count_regex(text, r"\bin conclusion\b|\bto sum up\b|\bin summary\b|\bbest practices\b") else 0
    scores["promotional_intent"] = clamp(cta_count * 4, 0, 8)
    scores["source_attribution"] = -3 if link_count >= 2 else 7 if count_regex(text, r"\baccording to\b|\bresearch shows\b|\bexperts\b") and link_count == 0 else 0
    scores["first_hand_experience"] = -7 if count_regex(text, r"\bI built\b|\bI tried\b|\bmy project\b|\bwe shipped\b") else 0 if first_person else 3
    scores["information_density"] = points_from_density(density) + (1 if codeish == 0 and re.search(r"\bAPI|code|repo|PR|commit|deploy\b", text) else 0)

    indicators = [key for key, value in scores.items() if value > 0]
    if any(value < 0 for value in scores.values()):
        indicators.extend([key for key, value in scores.items() if value < 0])
    total = sum(scores.values())
    return total, indicators, scores


def criterion_score_from_penalty(penalty: int, max_penalty: int) -> int:
    if max_penalty <= 0:
        return 10
    return clamp(round(10 - (penalty / max_penalty) * 9), 1, 10)


def build_fix_instructions(
    *,
    trope_result: dict[str, Any],
    slop_scores: dict[str, int],
    indicators: list[str],
    content_type: str,
) -> str:
    fixes: list[str] = []
    detections = trope_result["result"].get("detections", [])
    for detection in detections[:5]:
        fixes.append(
            f"Remove or rewrite {detection['tropeName']} ({detection['matchCount']} matches); replace with direct, specific wording."
        )
    if any(k in indicators for k in ("generic_without_specifics", "no_verifiability", "no_life_dirt", "info_density", "information_density")):
        fixes.append("Add concrete facts: names, numbers, dates, versions, implementation details, or examples from the source.")
    if any(k in indicators for k in ("weak_cause_effect", "weak_causality")):
        fixes.append("Strengthen causality: show A -> B -> C instead of saying the point is important.")
    if any(k in indicators for k in ("zero_author_position", "zero_position")):
        fixes.append("Commit to a position; delete generic overview sentences that say nothing testable.")
    if any(k in indicators for k in ("fake_confidence", "too_clean_logic", "no_edge_cases")):
        fixes.append("Add context, limits, exceptions, or tradeoffs where the current draft overclaims.")
    if any(k in indicators for k in ("bad_terminology", "lexical_repetition")):
        fixes.append("Replace buzzwords and repeated AI lexicon with plain nouns and verbs.")
    if content_type == "quote" and "no_personal_stake" in indicators:
        fixes.append("If this is meant to be a customer voice, use first-hand detail or mark it as summary instead of a quote.")
    return " ".join(fixes) if fixes else "No major fixes required; keep the current specificity and voice."


def evaluate(text: str, *, content_type: str = "auto", title: str = "Candidate") -> dict[str, Any]:
    wc = len(words(text))
    sent_count = len(sentences(text))
    inferred_type = "quote" if (content_type == "auto" and (wc <= 160 or sent_count <= 5)) else "article"
    if content_type in {"quote", "article"}:
        inferred_type = content_type

    trope_result = slop_score.local_score(text, title=title)
    trope_score = trope_result["result"]["score"]
    trope_verdict = trope_result["result"]["verdict"]

    if inferred_type == "quote":
        slop_total, indicators, slop_scores = quote_slop_score(text)
        slop_verdict, weight_modifier = verdict_from_quote_score(slop_total)
        slop_max = 38
    else:
        slop_total, indicators, slop_scores = article_slop_score(text)
        slop_verdict, weight_modifier = verdict_from_article_score(slop_total)
        slop_max = 126

    slop_risk_score = criterion_score_from_penalty(slop_total, slop_max)
    trope_quality_score = criterion_score_from_penalty(trope_score, 100)
    specificity_score = criterion_score_from_penalty(
        slop_scores.get("generic_without_specifics", 0)
        + slop_scores.get("no_verifiability", 0)
        + slop_scores.get("no_life_dirt", 0)
        + slop_scores.get("info_density", 0)
        + slop_scores.get("information_density", 0),
        24,
    )
    causality_score = criterion_score_from_penalty(
        slop_scores.get("weak_cause_effect", 0) + slop_scores.get("weak_causality", 0),
        8,
    )
    voice_score = criterion_score_from_penalty(
        slop_scores.get("zero_author_position", 0)
        + slop_scores.get("zero_position", 0)
        + slop_scores.get("too_even_tone", 0)
        + slop_scores.get("no_personal_accountability", 0),
        19,
    )
    brief_adherence_score = 9 if wc >= 20 else 5

    criteria = [
        {"id": "slop_risk", "score": slop_risk_score},
        {"id": "trope_risk", "score": trope_quality_score},
        {"id": "specificity", "score": specificity_score},
        {"id": "causality", "score": causality_score},
        {"id": "voice", "score": voice_score},
        {"id": "brief_adherence_proxy", "score": brief_adherence_score},
    ]
    score = round(sum(c["score"] for c in criteria) / len(criteria), 1)
    passed = (
        score >= 8
        and trope_score <= 25
        and slop_verdict in {"clean", "good"}
    )
    reason = (
        f"{inferred_type} scored {score}/10; trope verdict {trope_verdict} ({trope_score}), "
        f"slop-check verdict {slop_verdict} ({slop_total})."
    )
    fix_instructions = build_fix_instructions(
        trope_result=trope_result,
        slop_scores=slop_scores,
        indicators=indicators,
        content_type=inferred_type,
    )

    return {
        "success": True,
        "passed": passed,
        "score": score,
        "threshold": 8,
        "reason": reason,
        "fix_instructions": "" if passed else fix_instructions,
        "criteria": criteria,
        "content_type": inferred_type,
        "slop_metrics": {
            "score": slop_total,
            "max_score": slop_max,
            "verdict": slop_verdict,
            "indicators": indicators,
            "weight_modifier": weight_modifier,
            "criteria_scores": slop_scores,
        },
        "trope_metrics": trope_result["result"],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Evaluate content against quality and slop gates.")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--file")
    group.add_argument("--text")
    parser.add_argument("--type", choices=["auto", "quote", "article"], default="auto")
    parser.add_argument("--pretty", action="store_true")
    args = parser.parse_args()

    if args.file:
        with open(args.file, "r", encoding="utf-8") as fh:
            text = fh.read()
        title = args.file
    else:
        text = args.text
        title = "Inline text"

    result = evaluate(text, content_type=args.type, title=title)
    print(json.dumps(result, ensure_ascii=False, indent=2 if args.pretty else None))
    return 0 if result["passed"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
