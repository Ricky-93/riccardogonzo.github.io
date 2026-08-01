#!/usr/bin/env python3
"""Rebuild talkmap/talks_map.html from the _talks collection.

The map follows the original website design: one large coloured marker per
location, with every presentation at that location listed in one readable
popup. Fully online series are assigned to their original organising base.
"""
from __future__ import annotations
import datetime as dt
import html
import json
from pathlib import Path
from typing import Any
import yaml

ROOT = Path(__file__).resolve().parents[1]
TALKS = ROOT / "_talks"
COORDS = ROOT / "_data" / "talk_locations.yml"
OUTPUT = ROOT / "talkmap" / "talks_map.html"
COLORS = {"Invited talk":"darkred","Invited seminar":"blue","Contributed talk":"darkblue","Discussion session":"gray"}
PRIORITY = {"Invited talk":4,"Invited seminar":3,"Contributed talk":2,"Discussion session":1}
ONLINE_BASE = {
    "Worldline Seminars": "Plymouth, UK",
    "Physics in Intense Fields, PIF22": "Plymouth, UK",
    "Amplitudes Lounge Seminar": "Padova, Italy",
    "GRAMPA seminar series": "Edinburgh, UK",
}

def read_front_matter(path: Path) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8")
    _, raw, _ = text.split("---", 2)
    return yaml.safe_load(raw)

def display_date(value: Any) -> str:
    if isinstance(value, (dt.date, dt.datetime)):
        return value.strftime("%B %Y")
    try:
        return dt.date.fromisoformat(str(value)[:10]).strftime("%B %Y")
    except ValueError:
        return str(value)

def video_link(data: dict[str, Any]) -> str:
    url = data.get("video_url")
    if not url:
        return ""
    return f'<a href="{html.escape(str(url), quote=True)}" target="_blank" rel="noopener noreferrer">[video]</a>'

def page(payload: str) -> str:
    template = (ROOT / "tools" / "talk_map_template.html").read_text(encoding="utf-8")
    return template.replace("__PAYLOAD__", payload)

def main() -> None:
    coordinates = yaml.safe_load(COORDS.read_text(encoding="utf-8")) or {}
    groups: dict[str, list[dict[str, Any]]] = {}
    skipped: list[str] = []
    for path in sorted(TALKS.glob("*.md")):
        d = read_front_matter(path)
        location = str(d.get("location", ""))
        if location.casefold() == "online":
            location = ONLINE_BASE.get(str(d.get("venue", "")), "")
        if not location or location not in coordinates:
            skipped.append(f"{path.name}: no coordinates for {location!r}")
            continue
        event = {
            "title": str(d["title"]), "type": str(d["type"]),
            "venue": str(d["venue"]), "date": display_date(d["date"]),
            "date_sort": str(d["date"]), "location": location,
            "video": video_link(d),
        }
        groups.setdefault(location, []).append(event)
    markers = []
    for location, events in groups.items():
        events.sort(key=lambda e: e["date_sort"], reverse=True)
        dominant = max(events, key=lambda e: PRIORITY.get(e["type"], 0))["type"]
        lat, lon = coordinates[location]
        markers.append({"location": location, "lat": lat, "lon": lon, "colour": COLORS.get(dominant, "cadetblue"), "events": events})
    markers.sort(key=lambda x: x["location"])
    OUTPUT.write_text(page(json.dumps(markers, ensure_ascii=False)), encoding="utf-8")
    for item in skipped:
        print(item)
    print(f"Wrote {OUTPUT} with {len(markers)} location markers and {sum(len(m['events']) for m in markers)} presentations.")

if __name__ == "__main__":
    main()
