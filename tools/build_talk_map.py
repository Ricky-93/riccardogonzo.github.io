#!/usr/bin/env python3
"""Build the interactive talk map from ``_talks/*.md`` without geocoding.

Talks with a named host location are shown at that location, even when they
were delivered online (for example ITMP or NTNU). Only records whose location
is literally ``Online`` are collected under a separate virtual pin in the
Atlantic. Full-size Leaflet pins are used, as on the original website. Talks
at identical or nearby coordinates can be separated by clicking the pin.

Only video links explicitly stored as ``video_url`` are shown.

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
PANE_NAMES = {
    "Invited talk": "invitedTalks",
    "Invited seminar": "invitedSeminars",
    "Contributed talk": "contributedTalks",
    "Discussion session": "discussionSessions",
}
ONLINE_MARKER_COLOUR = "orange"
ONLINE_HUB = (18.0, -31.0)  # visual anchor only, not a geographic claim


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


def event_payload(path: Path, data: dict[str, Any]) -> dict[str, Any]:
    event_type = str(data["type"])
    location = str(data["location"])
    return {
        "title": str(data["title"]),
        "type": event_type,
        "venue": str(data["venue"]),
        "date": display_date(data["date"]),
        "date_sort": str(data["date"]),
        "location": location,
        "url": f"/talks/{path.stem}/",
        "video": video_link(data),
        "marker_colour": MARKER_COLOURS.get(event_type, "cadetblue"),
        "pane": PANE_NAMES.get(event_type, "otherTalks"),
        "online": location.casefold() == "online",
    }


def main() -> None:
    coords = yaml.safe_load(COORDS_FILE.read_text(encoding="utf-8")) or {}
    markers: list[dict[str, Any]] = []
    online_only: list[dict[str, Any]] = []
    skipped: list[str] = []

    for path in sorted(TALKS_DIR.glob("*.md")):
        data = front_matter(path)
        item = event_payload(path, data)
        location = item["location"]

        if item["online"]:
            online_only.append(item)
            continue

        if location not in coords:
            skipped.append(f"{path.name}: no coordinates for {location!r}")
            continue

        item["lat"] = coords[location][0]
        item["lon"] = coords[location][1]
        markers.append(item)

    online_only.sort(key=lambda item: item["date_sort"], reverse=True)
    payload = json.dumps(markers, ensure_ascii=False)
    online_payload = json.dumps(online_only, ensure_ascii=False)

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    page = r'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/Leaflet.awesome-markers/2.0.0/leaflet.awesome-markers.css">
<link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.0.0/css/bootstrap-glyphicons.css">
<style>
html,body,#map{height:100%;margin:0}
.leaflet-popup-content{line-height:1.4;max-height:330px;overflow:auto;font-family:Arial,sans-serif}
.leaflet-popup-content a{color:#2c6077}
.map-legend{background:rgba(255,255,255,.95);padding:8px 10px;border-radius:4px;box-shadow:0 1px 5px rgba(0,0,0,.28);font:12px/1.4 Arial,sans-serif;color:#263945}
.map-legend div{margin:3px 0;white-space:nowrap}
.legend-pin{display:inline-block;width:10px;height:15px;margin:0 7px 0 2px;border-radius:8px 8px 8px 0;transform:rotate(-45deg);vertical-align:-3px;box-shadow:0 0 0 1px rgba(0,0,0,.12)}
.legend-pin span{display:block;width:4px;height:4px;margin:3px;background:#fff;border-radius:50%}
.online-list{margin:.5em 0 0 1.15em;padding:0}
.online-list li{margin:0 0 .6em}
.map-note{color:#666c70;font-size:11px}
/* Keep the original, highly visible full-size pin appearance. */
.awesome-marker{filter:drop-shadow(0 1px 1px rgba(0,0,0,.28))}
</style>
</head>
<body>
<div id="map"></div>
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/Leaflet.awesome-markers/2.0.0/leaflet.awesome-markers.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/OverlappingMarkerSpiderfier-Leaflet/0.2.6/oms.min.js"></script>
<script>
const markers = __PAYLOAD__;
const onlineOnly = __ONLINE_PAYLOAD__;
const onlineHub = [18.0, -31.0];

const map = L.map("map", {
  center: [25, 5],
  zoom: 2,
  scrollWheelZoom: false,
  zoomControl: true,
  preferCanvas: false
});

L.tileLayer("https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png", {
  maxZoom: 20,
  subdomains: "abcd",
  attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors &copy; <a href="https://carto.com/attributions">CARTO</a>'
}).addTo(map);

map.createPane("discussionSessions").style.zIndex = 620;
map.createPane("contributedTalks").style.zIndex = 630;
map.createPane("invitedSeminars").style.zIndex = 640;
map.createPane("invitedTalks").style.zIndex = 650;
map.createPane("otherTalks").style.zIndex = 610;

const oms = new OverlappingMarkerSpiderfier(map, {
  keepSpiderfied: true,
  nearbyDistance: 28,
  circleSpiralSwitchover: 8,
  legWeight: 1.6
});

function markerIcon(markerColour) {
  return L.AwesomeMarkers.icon({
    markerColor: markerColour,
    iconColor: "white",
    icon: "info-sign",
    prefix: "glyphicon"
  });
}

function externalVideo(item) {
  return item.video ? `<br>${item.video}` : "";
}

for (const item of markers) {
  const marker = L.marker([item.lat, item.lon], {
    icon: markerIcon(item.marker_colour),
    pane: item.pane,
    riseOnHover: true,
    title: item.title
  }).addTo(map);
  marker.bindPopup(
    `<strong><a href="${item.url}">${item.title}</a></strong><br>` +
    `${item.venue}<br>${item.date} · ${item.type}<br>${item.location}${externalVideo(item)}`,
    {maxWidth: 350}
  );
  oms.addMarker(marker);
}

oms.addListener("click", function(marker) {
  marker.openPopup();
});

if (onlineOnly.length) {
  const onlineMarker = L.marker(onlineHub, {
    icon: markerIcon("orange"),
    riseOnHover: true,
    title: "Online presentations"
  }).addTo(map);
  const items = onlineOnly.map(item =>
    `<li><strong><a href="${item.url}">${item.title}</a></strong><br>` +
    `${item.venue}<br>${item.date} · ${item.type}${externalVideo(item)}</li>`
  ).join("");
  onlineMarker.bindPopup(
    `<strong>Online presentations (${onlineOnly.length})</strong><br>` +
    `<span class="map-note">Virtual marker; not a geographic location.</span>` +
    `<ul class="online-list">${items}</ul>`,
    {maxWidth: 390}
  );
}

L.control.scale({imperial: false}).addTo(map);

const legend = L.control({position: "bottomright"});
legend.onAdd = function() {
  const div = L.DomUtil.create("div", "map-legend");
  div.innerHTML =
    `<div><span class="legend-pin" style="background:#a71919"><span></span></span>Invited talk</div>` +
    `<div><span class="legend-pin" style="background:#2a81cb"><span></span></span>Invited seminar</div>` +
    `<div><span class="legend-pin" style="background:#0067a3"><span></span></span>Contributed talk</div>` +
    `<div><span class="legend-pin" style="background:#575757"><span></span></span>Discussion session</div>` +
    `<div><span class="legend-pin" style="background:#f69730"><span></span></span>Online presentations</div>`;
  return div;
};
legend.addTo(map);
</script>
</body>
</html>
'''.replace("__PAYLOAD__", payload).replace("__ONLINE_PAYLOAD__", online_payload)

    OUTPUT.write_text(page, encoding="utf-8")

    if skipped:
        print("\n".join(skipped))
    represented = len(markers) + len(online_only)
    print(
        f"Wrote {OUTPUT} with {len(markers)} full-size geographic pins and one online pin "
        f"representing {len(online_only)} locationless events ({represented} records represented)."
    )


if __name__ == "__main__":
    main()
