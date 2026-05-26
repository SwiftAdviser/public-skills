#!/usr/bin/env python3
"""Score URLs or text files for AI-writing trope density.

URL mode first calls the observed public tropes.fyi AI Vetter server action.
If that cannot return a score, the script falls back to local extraction and
local regex-style scoring.
"""

from __future__ import annotations

import argparse
import html
import json
import re
import sys
import urllib.error
import urllib.request
from dataclasses import dataclass
from html.parser import HTMLParser
from typing import Any


ACTION_ID = "404078c1891780d50bb636ae78e61eacced061b793"
VETTER_URL = "https://tropes.fyi/vetter"


@dataclass(frozen=True)
class TropeRule:
    trope_id: str
    name: str
    category: str
    patterns: tuple[str, ...]


RULES: tuple[TropeRule, ...] = (
    TropeRule(
        "quietly-magic-adverbs",
        '"Quietly" and Other Magic Adverbs',
        "word-choice",
        (
            r"\bquietly\b",
            r"\bquiet intelligence\b",
            r"\bdeeply\b",
            r"\bfundamentally\b",
            r"\bremarkably\b",
            r"\barguably\b",
        ),
    ),
    TropeRule(
        "delve",
        '"Delve" and Friends',
        "word-choice",
        (
            r"\bdelv(?:e|es|ed|ing)\b",
            r"\bcertainly\b",
            r"\butili[sz](?:e|es|ed|ing|ation)\b",
            r"\bleverage(?:s|d|ing)?\b",
            r"\brobust\b",
            r"\bstreamline(?:s|d|ing)?\b",
            r"\bharness(?:es|ed|ing)?\b",
        ),
    ),
    TropeRule(
        "tapestry-landscape",
        '"Tapestry" and "Landscape"',
        "word-choice",
        (
            r"\btapestry\b",
            r"\blandscape\b",
            r"\bparadigm\b",
            r"\bsynergy\b",
            r"\becosystem(?:s)?\b",
            r"\bframework(?:s)?\b",
        ),
    ),
    TropeRule(
        "serves-as",
        'The "Serves As" Dodge',
        "word-choice",
        (
            r"\bserves as\b",
            r"\bstands as\b",
            r"\bmarks (?:a|an|the)?\b",
            r"\brepresents (?:a|an|the)?\b",
        ),
    ),
    TropeRule(
        "negative-parallelism",
        "Negative Parallelism",
        "sentence-structure",
        (
            r"\bit'?s not [^.?!;:]{1,120}[.!?]\s+it'?s [^.?!]{1,120}",
            r"\bnot because [^,.;!?]{1,140},?\s+but because\b",
            r"\b(?:isn'?t|aren'?t|wasn'?t|weren'?t) [^.?!]{1,100}[.!?]\s+(?:it|they|this|that|the question)\s+(?:is|are|was|were)\b",
            r"\btreat [^.?!]{1,120}\bas [^.?!]{1,120},\s*not [^.?!]{1,80}",
            r"\s--\s*not\b",
            r"\s-\s*not\b",
            r"\s—\s*not\b",
        ),
    ),
    TropeRule(
        "not-x-not-y-just-z",
        '"Not X. Not Y. Just Z."',
        "sentence-structure",
        (
            r"\bnot [^.?!]{1,80}[.!?]\s+not [^.?!]{1,80}[.!?]\s+(?:just |but |only |a |an |the )?[^.?!]{1,120}",
            r"\bnot [^,.;!?]{1,80},\s+not [^,.;!?]{1,80},\s+but\b",
        ),
    ),
    TropeRule(
        "the-x-a-y",
        '"The X? A Y."',
        "sentence-structure",
        (
            r"\bthe [A-Za-z][^?]{1,60}\?\s+(?:a|an|the|this|that|it|nobody|nothing|everything|[A-Z])[^\n.?!]{1,120}",
            r"\b(?:worst|best|scary|funny|hard|weird) part\?\s+[^\n.?!]{1,120}",
        ),
    ),
    TropeRule(
        "tricolon-abuse",
        "Tricolon Abuse",
        "sentence-structure",
        (
            r"\b\w+(?:ing|ion|ity|ment|ance|ence|ship|ers?|ors?)\b,\s+\b\w+(?:ing|ion|ity|ment|ance|ence|ship|ers?|ors?)\b,\s+(?:and\s+)?\b\w+(?:ing|ion|ity|ment|ance|ence|ship|ers?|ors?)\b",
            r"\b[A-Z][^.?!;]{5,80};\s+[A-Z][^.?!;]{5,80};\s+[A-Z][^.?!;]{5,80}",
        ),
    ),
    TropeRule(
        "worth-noting",
        '"It\'s Worth Noting"',
        "sentence-structure",
        (
            r"\bit'?s worth noting\b",
            r"\bit bears mentioning\b",
            r"\bimportantly\b",
            r"\binterestingly\b",
            r"\bnotably\b",
        ),
    ),
    TropeRule(
        "superficial-analyses",
        "Superficial Analyses",
        "sentence-structure",
        (
            r"\bhighlighting (?:its|the|their)\b[^.?!]{1,140}",
            r"\breflecting broader\b[^.?!]{1,140}",
            r"\bcontributing to\b[^.?!]{1,140}",
            r"\bunderscoring (?:its|the|their)\b[^.?!]{1,140}",
            r"\bshaping (?:its|the|their)\b[^.?!]{1,140}",
        ),
    ),
    TropeRule(
        "false-ranges",
        "False Ranges",
        "sentence-structure",
        (
            r"\bfrom [^.\n]{3,80} to [^.\n]{3,80}(?: to [^.\n]{3,80})?",
        ),
    ),
    TropeRule(
        "short-punchy-fragments",
        "Short Punchy Fragments",
        "paragraph-structure",
        (
            r"(?:^|\n)(?:[A-Z][A-Za-z']{0,14}(?: [A-Za-z']{1,14}){0,3}\.){3,}",
            r"\b[A-Z][a-z]+ [a-z]+\.\s+[A-Z][a-z]+\.\s+[A-Z][a-z]+\.",
        ),
    ),
    TropeRule(
        "listicle-trench-coat",
        "Listicle in a Trench Coat",
        "paragraph-structure",
        (
            r"\bthe first\b[^.?!]{1,220}\bthe second\b",
            r"\bthe second\b[^.?!]{1,220}\bthe third\b",
            r"\bthe third\b[^.?!]{1,220}\bthe fourth\b",
            r"\bfirst takeaway\b|\bsecond takeaway\b|\bthird takeaway\b|\bfourth takeaway\b",
        ),
    ),
    TropeRule(
        "heres-the-kicker",
        '"Here\'s the Kicker"',
        "tone",
        (
            r"\bhere'?s the kicker\b",
            r"\bhere'?s the thing\b",
            r"\bhere'?s where it gets interesting\b",
            r"\bhere'?s what most people miss\b",
            r"\bhere'?s the starting point\b",
            r"\bhere'?s the deal\b",
            r"\bhere'?s the catch\b",
        ),
    ),
    TropeRule(
        "think-of-it-as",
        '"Think of It As..."',
        "tone",
        (
            r"\bthink of it as\b",
            r"\bthink of it like\b",
            r"\bit'?s like\b",
        ),
    ),
    TropeRule(
        "imagine-a-world",
        '"Imagine a World Where..."',
        "tone",
        (
            r"\bimagine a world where\b",
            r"\bin that world\b",
            r"\bimagine (?:if|that|every|a)\b",
        ),
    ),
    TropeRule(
        "false-vulnerability",
        "False Vulnerability",
        "tone",
        (
            r"\band yes\b",
            r"\bsince we'?re being honest\b",
            r"\bthis is not a rant\b",
            r"\bto be clear\b",
        ),
    ),
    TropeRule(
        "truth-is-simple",
        '"The Truth Is Simple"',
        "tone",
        (
            r"\bthe reality is (?:simple|simpler|clear|obvious)\b",
            r"\bthe truth is (?:simple|simpler|clear|obvious)\b",
            r"\bhistory is (?:clear|unambiguous)\b",
            r"\bthe real (?:story|issue|reason|point) is\b",
            r"\bnone of (?:this|these|them) is the real\b",
        ),
    ),
    TropeRule(
        "grandiose-stakes",
        "Grandiose Stakes Inflation",
        "tone",
        (
            r"\bfundamentally reshape\b",
            r"\bdefine the next era\b",
            r"\bnext era of\b",
            r"\bsomething entirely new\b",
            r"\bchange everything\b",
            r"\bthe future of\b",
        ),
    ),
    TropeRule(
        "lets-break-down",
        '"Let\'s Break This Down"',
        "tone",
        (
            r"\blet'?s break (?:this|it) down\b",
            r"\blet'?s unpack\b",
            r"\blet'?s explore\b",
            r"\blet'?s dive in\b",
            r"\blet'?s delve\b",
        ),
    ),
    TropeRule(
        "vague-attributions",
        "Vague Attributions",
        "tone",
        (
            r"\bexperts (?:argue|say|suggest|believe|warn)\b",
            r"\bindustry reports suggest\b",
            r"\bobservers (?:have )?(?:cited|argue|say|suggest)\b",
            r"\bseveral publications\b",
            r"\bmany experts\b",
        ),
    ),
    TropeRule(
        "invented-concept-labels",
        "Invented Concept Labels",
        "tone",
        (
            r"\b[a-z][a-z-]+ (?:paradox|trap|creep|divide|vacuum|inversion|matrix|layer|engine|loop|gap|flywheel)\b",
        ),
    ),
    TropeRule(
        "em-dash-addiction",
        "Em-Dash Addiction",
        "formatting",
        (
            r"—",
            r"\s--\s",
        ),
    ),
    TropeRule(
        "bold-first-bullets",
        "Bold-First Bullets",
        "formatting",
        (
            r"(?m)^\s*[-*]\s+\*\*[^*\n]{1,80}\*\*:",
            r"(?m)^\s*\d+\.\s+\*\*[^*\n]{1,80}\*\*:",
        ),
    ),
    TropeRule(
        "unicode-decoration",
        "Unicode Decoration",
        "formatting",
        (
            r"→|⇒|↔|•|“|”|‘|’",
        ),
    ),
    TropeRule(
        "fractal-summaries",
        "Fractal Summaries",
        "composition",
        (
            r"\bin this section\b",
            r"\bas we'?ve seen\b",
            r"\band so we return to where we began\b",
            r"\bwhat we'?ve covered\b",
        ),
    ),
    TropeRule(
        "historical-analogy-stacking",
        "Historical Analogy Stacking",
        "composition",
        (
            r"\bApple didn'?t build\b[^.?!]{1,220}\bFacebook didn'?t build\b",
            r"\bEvery major technological shift\b[^.?!]{1,220}\bweb\b[^.?!]{1,220}\bmobile\b[^.?!]{1,220}\bcloud\b",
            r"\bTake [A-Z][A-Za-z0-9]+[^.?!]{1,180}\bconsider [A-Z][A-Za-z0-9]+",
        ),
    ),
    TropeRule(
        "signposted-conclusion",
        "The Signposted Conclusion",
        "composition",
        (
            r"\bin conclusion\b",
            r"\bto sum up\b",
            r"\bin summary\b",
        ),
    ),
    TropeRule(
        "despite-its-challenges",
        '"Despite Its Challenges..."',
        "composition",
        (
            r"\bdespite (?:its|their|these) [^.?!]{0,80}challenges\b",
            r"\bfaces challenges\b[^.?!]{1,220}\bdespite (?:these|those|its|their) challenges\b",
        ),
    ),
)


class TextExtractor(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.skip_depth = 0
        self.parts: list[str] = []
        self.title_parts: list[str] = []
        self.in_title = False

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag in {"script", "style", "noscript", "svg"}:
            self.skip_depth += 1
        if tag == "title":
            self.in_title = True
        if tag in {"p", "div", "section", "article", "br", "li", "h1", "h2", "h3"}:
            self.parts.append("\n")

    def handle_endtag(self, tag: str) -> None:
        if tag in {"script", "style", "noscript", "svg"} and self.skip_depth:
            self.skip_depth -= 1
        if tag == "title":
            self.in_title = False
        if tag in {"p", "div", "section", "article", "li", "h1", "h2", "h3"}:
            self.parts.append("\n")

    def handle_data(self, data: str) -> None:
        if self.skip_depth:
            return
        if self.in_title:
            self.title_parts.append(data)
        self.parts.append(data)

    @property
    def text(self) -> str:
        return normalize_text(" ".join(self.parts))

    @property
    def title(self) -> str:
        return normalize_text(" ".join(self.title_parts))


def normalize_text(text: str) -> str:
    text = html.unescape(text)
    text = re.sub(r"[ \t\r\f\v]+", " ", text)
    text = re.sub(r"\n\s*\n+", "\n\n", text)
    return text.strip()


def word_count(text: str) -> int:
    return len(re.findall(r"\b[\w']+\b", text))


def excerpt(text: str, start: int, end: int, radius: int = 75) -> str:
    left = max(0, start - radius)
    right = min(len(text), end + radius)
    snip = normalize_text(text[left:right])
    return snip


def call_vetter_api(url: str, timeout: int = 30) -> dict[str, Any]:
    body = json.dumps([url]).encode("utf-8")
    req = urllib.request.Request(
        VETTER_URL,
        data=body,
        method="POST",
        headers={
            "Next-Action": ACTION_ID,
            "Content-Type": "text/plain;charset=UTF-8",
            "User-Agent": "high-quality-content-writer/1.0",
        },
    )
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        raw = resp.read().decode("utf-8", errors="replace")
    parsed = parse_next_action_response(raw)
    if not parsed:
        raise RuntimeError("Could not parse Vetter API response")
    parsed.setdefault("mode", "tropes.fyi-api")
    return parsed


def parse_next_action_response(raw: str) -> dict[str, Any] | None:
    candidates: list[dict[str, Any]] = []
    for line in raw.splitlines():
        match = re.match(r"^\d+:(.*)$", line.strip())
        if not match:
            continue
        payload = match.group(1)
        try:
            value = json.loads(payload)
        except json.JSONDecodeError:
            continue
        if isinstance(value, dict) and "success" in value:
            candidates.append(value)
    return candidates[-1] if candidates else None


def jina_reader_url(url: str) -> str:
    return f"https://r.jina.ai/http://{url}"


def fetch_jina_markdown(url: str, timeout: int = 30) -> tuple[str, str]:
    req = urllib.request.Request(
        jina_reader_url(url),
        headers={"User-Agent": "high-quality-content-writer/1.0"},
    )
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        raw = resp.read().decode("utf-8", errors="replace")
    if not raw.strip() or "Failed to fetch" in raw[:500] or "upstream connect error" in raw[:500].lower():
        raise RuntimeError("Jina Reader returned no usable markdown")
    title_match = re.search(r"^Title:\s*(.+)$", raw, flags=re.MULTILINE)
    title = title_match.group(1).strip() if title_match else url
    return title, normalize_text(raw)


def fetch_url_text(url: str, timeout: int = 30) -> tuple[str, str]:
    try:
        return fetch_jina_markdown(url, timeout=timeout)
    except Exception:
        pass
    req = urllib.request.Request(url, headers={"User-Agent": "high-quality-content-writer/1.0"})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        raw = resp.read().decode("utf-8", errors="replace")
    parser = TextExtractor()
    parser.feed(raw)
    return parser.title or url, parser.text


def local_score(text: str, *, url: str | None = None, title: str | None = None) -> dict[str, Any]:
    detections: list[dict[str, Any]] = []
    for rule in RULES:
        matches = []
        count = 0
        for pattern in rule.patterns:
            for match in re.finditer(pattern, text, flags=re.IGNORECASE | re.MULTILINE):
                count += 1
                if len(matches) < 12:
                    matches.append(
                        {
                            "tropeId": rule.trope_id,
                            "excerpt": excerpt(text, match.start(), match.end()),
                            "position": match.start(),
                        }
                    )
        if count:
            detections.append(
                {
                    "tropeId": rule.trope_id,
                    "tropeName": rule.name,
                    "category": rule.category,
                    "matchCount": count,
                    "matches": matches,
                }
            )

    add_custom_detections(text, detections)
    detections.sort(key=lambda d: (-d["matchCount"], d["tropeName"]))

    wc = word_count(text)
    trope_count = len(detections)
    total_matches = sum(d["matchCount"] for d in detections)
    density = (total_matches / max(wc, 1)) * 1000
    score = min(100, round((total_matches * 3.5) + (trope_count * 4) + (density * 2.5)))
    detection_counts = {d["tropeId"]: d["matchCount"] for d in detections}
    if detection_counts.get("short-punchy-fragments", 0) >= 5:
        score = max(score, 85)
        if detection_counts.get("negative-parallelism", 0) > 0:
            score = 100
    verdict, color = verdict_for_score(score)
    return {
        "success": True,
        "mode": "local",
        "result": {
            "url": url or "",
            "title": title or "Local text",
            "score": score,
            "verdict": verdict,
            "verdictColor": color,
            "tropeCount": trope_count,
            "totalMatches": total_matches,
            "wordCount": wc,
            "detections": detections,
        },
    }


def add_custom_detections(text: str, detections: list[dict[str, Any]]) -> None:
    existing_ids = {d["tropeId"] for d in detections}
    short_fragments = find_short_punchy_fragments(text)
    if short_fragments and "short-punchy-fragments" not in existing_ids:
        capped_fragments = short_fragments[:5]
        detections.append(
            {
                "tropeId": "short-punchy-fragments",
                "tropeName": "Short Punchy Fragments",
                "category": "paragraph-structure",
                "matchCount": len(capped_fragments),
                "matches": [
                    {
                        "tropeId": "short-punchy-fragments",
                        "excerpt": item["excerpt"],
                        "position": item["position"],
                    }
                    for item in capped_fragments
                ],
            }
        )

    sentences = re.findall(r"[^.!?\n][^.!?\n]{5,220}[.!?]", text)
    opener_positions: dict[str, list[tuple[int, str]]] = {}
    for sentence in sentences:
        clean = normalize_text(sentence)
        words = re.findall(r"\b[A-Za-z']+\b", clean)
        if len(words) < 4:
            continue
        opener = " ".join(words[:2]).lower()
        if opener in {"it is", "this is", "there is", "there are"}:
            continue
        pos = text.find(sentence)
        opener_positions.setdefault(opener, []).append((pos, clean))
    repeated_openers = [
        item for item in opener_positions.values() if len(item) >= 3
    ]
    if repeated_openers:
        matches = []
        count = 0
        for group in repeated_openers:
            for pos, sentence in group[:4]:
                count += 1
                if len(matches) < 12:
                    matches.append(
                        {
                            "tropeId": "anaphora-abuse",
                            "excerpt": excerpt(text, max(pos, 0), max(pos, 0) + len(sentence)),
                            "position": max(pos, 0),
                        }
                    )
        detections.append(
            {
                "tropeId": "anaphora-abuse",
                "tropeName": "Anaphora Abuse",
                "category": "sentence-structure",
                "matchCount": count,
                "matches": matches,
            }
        )

    normalized_sentences: dict[str, tuple[int, str]] = {}
    duplicate_matches = []
    for sentence in sentences:
        clean = normalize_text(sentence)
        key = re.sub(r"\W+", " ", clean.lower()).strip()
        if len(key.split()) < 8:
            continue
        pos = text.find(sentence)
        if key in normalized_sentences:
            duplicate_matches.append((max(pos, 0), clean))
        else:
            normalized_sentences[key] = (max(pos, 0), clean)
    if duplicate_matches:
        detections.append(
            {
                "tropeId": "content-duplication",
                "tropeName": "Content Duplication",
                "category": "composition",
                "matchCount": len(duplicate_matches),
                "matches": [
                    {
                        "tropeId": "content-duplication",
                        "excerpt": excerpt(text, pos, pos + len(sentence)),
                        "position": pos,
                    }
                    for pos, sentence in duplicate_matches[:12]
                ],
            }
        )

    metaphor_terms = ("ecosystem", "wall", "door", "primitive", "flywheel", "engine")
    metaphor_matches = []
    for term in metaphor_terms:
        positions = [m.start() for m in re.finditer(rf"\b{re.escape(term)}s?\b", text, re.IGNORECASE)]
        if len(positions) >= 6:
            metaphor_matches.extend((pos, term) for pos in positions[:6])
    if metaphor_matches:
        detections.append(
            {
                "tropeId": "dead-metaphor",
                "tropeName": "The Dead Metaphor",
                "category": "composition",
                "matchCount": len(metaphor_matches),
                "matches": [
                    {
                        "tropeId": "dead-metaphor",
                        "excerpt": excerpt(text, pos, pos + len(term)),
                        "position": pos,
                    }
                    for pos, term in metaphor_matches[:12]
                ],
            }
        )


def find_short_punchy_fragments(text: str) -> list[dict[str, Any]]:
    fragments: list[dict[str, Any]] = []
    for line_match in re.finditer(r"(?m)^(.+?)$", text):
        raw = line_match.group(1).strip()
        if not raw:
            continue
        cleaned = re.sub(r"^#{1,6}\s+", "", raw)
        cleaned = re.sub(r"^\s*(?:[-*]|\d+[.)])\s+", "", cleaned)
        cleaned = re.sub(r"\[[^\]]+\]\([^)]+\)", "", cleaned).strip()
        if not cleaned or cleaned.startswith("Title:") or cleaned.startswith("URL Source:"):
            continue
        parts = [p.strip() for p in re.split(r"(?<=[.!?])\s+", cleaned) if p.strip()]
        for part in parts:
            word_len = len(re.findall(r"\b[\w']+\b", part))
            if 1 <= word_len <= 5 and re.search(r"[.!?]$", part):
                fragments.append({"excerpt": part, "position": line_match.start(1)})
    return fragments if len(fragments) >= 4 else []


def verdict_for_score(score: int) -> tuple[str, str]:
    if score < 15:
        return "Human", "text-green-700"
    if score < 35:
        return "AI-assisted", "text-lime-700"
    if score < 55:
        return "Suspicious", "text-orange-600"
    if score < 75:
        return "Barely Legible", "text-red-600"
    return "Pure AI Slop", "text-red-700"


def main() -> int:
    parser = argparse.ArgumentParser(description="Score text or URL for AI-writing tropes.")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--url")
    group.add_argument("--file")
    group.add_argument("--text")
    parser.add_argument("--local-only", action="store_true", help="Do not call the public tropes.fyi API for URLs.")
    parser.add_argument("--pretty", action="store_true", help="Pretty-print JSON.")
    args = parser.parse_args()

    result: dict[str, Any]
    if args.url:
        if not args.local_only:
            try:
                result = call_vetter_api(args.url)
                if result.get("success"):
                    print(json.dumps(result, ensure_ascii=False, indent=2 if args.pretty else None))
                    return 0
            except (RuntimeError, urllib.error.URLError, TimeoutError) as exc:
                api_error = str(exc)
            else:
                api_error = result.get("error") or "API returned no score"
        else:
            api_error = "Skipped API because --local-only was set"
        try:
            title, text = fetch_url_text(args.url)
            result = local_score(text, url=args.url, title=title)
            result["apiFallbackReason"] = api_error
        except Exception as exc:  # noqa: BLE001 - CLI should report any extraction failure.
            result = {"success": False, "error": f"{api_error}; local fallback failed: {exc}", "mode": "failed"}
    elif args.file:
        with open(args.file, "r", encoding="utf-8") as fh:
            result = local_score(fh.read(), title=args.file)
    else:
        result = local_score(args.text, title="Inline text")

    print(json.dumps(result, ensure_ascii=False, indent=2 if args.pretty else None))
    return 0 if result.get("success") else 1


if __name__ == "__main__":
    raise SystemExit(main())
