#!/usr/bin/env python3
"""Build the talk map in the original website style.

The map uses the original full-size, unclustered coloured pins. Talks with a
named host location are shown at that location, including seminars delivered
online for ITMP, NTNU, etc. Records whose location is literally ``Online`` are
collected under one orange pin. Only explicit ``video_url`` links are shown.

Dependencies:
    pip install pyyaml

Run from the repository root:
    python tools/build_talk_map.py
"""

from __future__ import annotations

import datetime as dt
import html
import json
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parents[1]
TALKS_DIR = ROOT / "_talks"
COORDS_FILE = ROOT / "_data" / "talk_locations.yml"
OUTPUT = ROOT / "talkmap" / "talks_map.html"

MARKER_COLOURS = {
    "Invited talk": "darkred",
    "Invited seminar": "blue",
    "Contributed talk": "darkblue",
    "Discussion session": "gray",
}
ONLINE_HUB = (24.0, -29.0)


def front_matter(path: Path) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        raise ValueError(f"{path}: missing YAML front matter")
    _, raw, _ = text.split("---", 2)
    data = yaml.safe_load(raw) or {}
    required = {"title", "type", "venue", "date", "location"}
    missing = required - data.keys()
    if missing:
        raise ValueError(f"{path}: missing {sorted(missing)}")
    return data


def display_date(value: Any) -> str:
    if isinstance(value, (dt.date, dt.datetime)):
        return value.strftime("%B %Y")
    text = str(value)
    try:
        return dt.date.fromisoformat(text[:10]).strftime("%B %Y")
    except ValueError:
        return text


def video_link(data: dict[str, Any]) -> str:
    if not data.get("video_url"):
        return ""
    url = html.escape(str(data["video_url"]), quote=True)
    return f'<a href="{url}" target="_blank" rel="noopener noreferrer">[video]</a>'


def event_payload(data: dict[str, Any]) -> dict[str, Any]:
    event_type = str(data["type"])
    location = str(data["location"])
    return {
        "title": str(data["title"]),
        "type": event_type,
        "venue": str(data["venue"]),
        "date": display_date(data["date"]),
        "date_sort": str(data["date"]),
        "location": location,
        "video": video_link(data),
        "marker_colour": MARKER_COLOURS.get(event_type, "cadetblue"),
        "online": location.casefold() == "online",
    }


def make_page(markers: list[dict[str, Any]], online_only: list[dict[str, Any]]) -> str:
    payload = json.dumps(markers, ensure_ascii=False)
    online_payload = json.dumps(online_only, ensure_ascii=False)
    return r'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
<script src="https://cdn.jsdelivr.net/npm/leaflet@1.9.3/dist/leaflet.js"></script>
<script src="https://code.jquery.com/jquery-3.7.1.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/Leaflet.awesome-markers/2.0.2/leaflet.awesome-markers.js"></script>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/leaflet@1.9.3/dist/leaflet.css">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/Leaflet.awesome-markers/2.0.2/leaflet.awesome-markers.css">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@fortawesome/fontawesome-free@6.2.0/css/all.min.css">
<style>
html,body,#map{width:100%;height:100%;margin:0;padding:0}
.leaflet-container{font-size:1rem}
.awesome-marker{filter:drop-shadow(0 1px 1px rgba(0,0,0,.28))}
.talk-popup{font:17px/1.38 Avenir,"Helvetica Neue",Arial,sans-serif;min-width:270px}
.talk-popup b{font-size:1.05em}
.talk-popup i{display:inline-block;margin:.18em 0}
.talk-popup a{color:#006699;font-weight:600}
.online-list{margin:.45em 0 0 1.15em;padding:0}
.online-list li{margin:0 0 .7em}
.map-legend{background:rgba(255,255,255,.96);padding:8px 10px;border-radius:4px;box-shadow:0 1px 5px rgba(0,0,0,.3);font:12px/1.4 Avenir,"Helvetica Neue",Arial,sans-serif;color:#333}
.map-legend div{margin:3px 0;white-space:nowrap}
.legend-dot{display:inline-block;width:10px;height:10px;margin-right:7px;border-radius:50%;vertical-align:-1px;border:1px solid rgba(0,0,0,.18)}
</style>
</head>
<body>
<div id="map"></div>
<script>
const markers = __PAYLOAD__;
const onlineOnly = __ONLINE_PAYLOAD__;
const map = L.map("map", {
  center: [40.0, 40.0],
  zoom: 3,
  zoomControl: true,
  scrollWheelZoom: true,
  preferCanvas: false
});
L.tileLayer("https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png", {
  minZoom: 0,
  maxZoom: 20,
  maxNativeZoom: 20,
  subdomains: "abcd",
  attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors &copy; <a href="https://carto.com/attributions">CARTO</a>'
}).addTo(map);

function markerIcon(colour) {
  return L.AwesomeMarkers.icon({
    markerColor: colour,
    iconColor: "white",
    icon: "circle",
    prefix: "fa",
    extraClasses: "fa-rotate-0"
  });
}
function videoLine(item) {
  return item.video ? `<br>${item.video}` : "";
}
function popupHtml(item) {
  return `<div class="talk-popup"><b>${item.venue}</b>, ${item.location}<br>` +
         `<i>${item.title}</i><br>${item.date} (${item.type.toLowerCase()})${videoLine(item)}</div>`;
}
for (const item of markers) {
  L.marker([item.lat, item.lon], {
    icon: markerIcon(item.marker_colour),
    riseOnHover: true,
    title: item.title
  }).addTo(map).bindPopup(popupHtml(item), {
    maxWidth: 430,
    minWidth: 285,
    maxHeight: 280
  });
}
if (onlineOnly.length) {
  const items = onlineOnly.map(item =>
    `<li><b>${item.venue}</b><br><i>${item.title}</i><br>${item.date} (${item.type.toLowerCase()})${videoLine(item)}</li>`
  ).join("");
  L.marker([24.0, -29.0], {
    icon: markerIcon("orange"),
    riseOnHover: true,
    title: "Online presentations"
  }).addTo(map).bindPopup(
    `<div class="talk-popup"><b>Online presentations</b><ul class="online-list">${items}</ul></div>`,
    {maxWidth: 450, minWidth: 310, maxHeight: 300}
  );
}
const legend = L.control({position: "bottomright"});
legend.onAdd = function() {
  const div = L.DomUtil.create("div", "map-legend");
  div.innerHTML =
    '<div><span class="legend-dot" style="background:#a71919"></span>Invited talk</div>' +
    '<div><span class="legend-dot" style="background:#2a81cb"></span>Invited seminar</div>' +
    '<div><span class="legend-dot" style="background:#0067a3"></span>Contributed talk</div>' +
    '<div><span class="legend-dot" style="background:#575757"></span>Discussion session</div>' +
    '<div><span class="legend-dot" style="background:#f69730"></span>Online presentations</div>';
  L.DomEvent.disableClickPropagation(div);
  return div;
};
legend.addTo(map);
</script>
</body>
</html>
'''.replace("__PAYLOAD__", payload).replace("__ONLINE_PAYLOAD__", online_payload)


def main() -> None:
    coords = yaml.safe_load(COORDS_FILE.read_text(encoding="utf-8")) or {}
    markers: list[dict[str, Any]] = []
    online_only: list[dict[str, Any]] = []
    skipped: list[str] = []

    for path in sorted(TALKS_DIR.glob("*.md")):
        item = event_payload(front_matter(path))
        if item["online"]:
            online_only.append(item)
            continue
        location = item["location"]
        if location not in coords:
            skipped.append(f"{path.name}: no coordinates for {location!r}")
            continue
        item["lat"], item["lon"] = coords[location]
        markers.append(item)

    online_only.sort(key=lambda item: item["date_sort"], reverse=True)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(make_page(markers, online_only), encoding="utf-8")

    if skipped:
        print("\n".join(skipped))
    print(f"Wrote {OUTPUT} with {len(markers)} geographic markers and {len(online_only)} online records.")


if __name__ == "__main__":
    main()
