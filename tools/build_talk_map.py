#!/usr/bin/env python3
"""Build the interactive talk map from ``_talks/*.md`` without geocoding.

Talks with a real host location are plotted normally, including seminars that
were delivered online for a named institution (for example ITMP or NTNU).
Only events whose location is literally ``Online`` are collected in a clearly
labelled virtual marker in the Atlantic; this keeps them visible without
inventing a geographical location.

Physical markers are placed in a Leaflet.markercluster group. Markers remain individually visible at the initial world view. Only markers at the
same (or effectively identical) coordinates are grouped, and clicking such a city
group spiderfies the individual talks immediately.

Dependencies:
    pip install pyyaml

Run from the repository root:
    python tools/build_talk_map.py
"""

from __future__ import annotations

import html
import json
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parents[1]
TALKS_DIR = ROOT / "_talks"
COORDS_FILE = ROOT / "_data" / "talk_locations.yml"
OUTPUT = ROOT / "talkmap" / "talks_map.html"

COLOURS = {
    "Invited talk": "#8b1a1a",
    "Invited seminar": "#2c6077",
    "Contributed talk": "#263945",
    "Discussion session": "#666c70",
}
ONLINE_COLOUR = "#a96f16"
# A visual anchor only, deliberately placed over the Atlantic. It is not meant
# to imply a geographical location for virtual events.
ONLINE_HUB = (18.0, -31.0)


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


def links_for(data: dict[str, Any]) -> str:
    links = []
    for key, label in (
        ("event_url", "event"),
        ("video_url", "video"),
        ("slides_url", "slides"),
    ):
        if data.get(key):
            url = html.escape(str(data[key]), quote=True)
            links.append(
                f'<a href="{url}" target="_blank" rel="noopener noreferrer">[{label}]</a>'
            )
    return " ".join(links)


def event_payload(path: Path, data: dict[str, Any]) -> dict[str, Any]:
    venue = str(data["venue"])
    location = str(data["location"])
    # A named host city always receives a normal marker, even when the seminar
    # itself was delivered online. This rule also applies automatically to any
    # future institution-hosted online seminar.
    is_locationless_online = location.casefold() == "online"
    return {
        "title": str(data["title"]),
        "type": str(data["type"]),
        "venue": venue,
        "date": str(data["date"]),
        "location": location,
        "url": f"/talks/{path.stem}/",
        "links": links_for(data),
        "colour": COLOURS.get(str(data["type"]), "#666c70"),
        "online": is_locationless_online,
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

    # Newest first in the aggregate online popup.
    online_only.sort(key=lambda item: item["date"], reverse=True)

    payload = json.dumps(markers, ensure_ascii=False)
    online_payload = json.dumps(online_only, ensure_ascii=False)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(
        """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css">
<link rel="stylesheet" href="https://unpkg.com/leaflet.markercluster@1.5.3/dist/MarkerCluster.css">
<style>
html,body,#map{height:100%;margin:0}
.leaflet-popup-content{line-height:1.35;max-height:330px;overflow:auto}
.map-legend{background:rgba(255,255,255,.94);padding:8px 10px;border-radius:4px;box-shadow:0 1px 5px rgba(0,0,0,.28);font:12px/1.35 Arial,sans-serif;color:#263945}
.map-legend div{margin:2px 0;white-space:nowrap}
.legend-dot{display:inline-block;width:9px;height:9px;border-radius:50%;margin-right:6px;vertical-align:baseline}
.online-dot{background:#a96f16;border:2px solid #a96f16;box-sizing:border-box}
.online-hub{background:#a96f16;color:#fff;border:2px solid #fff;border-radius:50%;box-shadow:0 1px 5px rgba(0,0,0,.35);display:flex;align-items:center;justify-content:center;width:32px;height:32px;font:bold 11px/1 Arial,sans-serif;text-align:center}
.online-label{background:rgba(255,255,255,.92);border:1px solid #d7c29a;border-radius:3px;color:#7a4d0d;font:bold 11px/1.2 Arial,sans-serif;padding:2px 5px;box-shadow:none}
.online-list{margin:.45em 0 0 1.15em;padding:0}
.online-list li{margin:0 0 .55em 0}
.map-note{color:#666c70;font-size:11px}
/* Custom cluster icons matching the website palette. */
.talk-cluster{background:transparent;border:0}
.talk-cluster div{display:flex;align-items:center;justify-content:center;border:2px solid rgba(255,255,255,.95);border-radius:50%;background:rgba(38,57,69,.92);color:#fff;box-shadow:0 1px 6px rgba(0,0,0,.36);font:bold 12px/1 Arial,sans-serif}
.talk-cluster-small div{width:32px;height:32px}
.talk-cluster-medium div{width:38px;height:38px;font-size:12.5px}
.talk-cluster-large div{width:44px;height:44px;font-size:13px}
</style>
</head>
<body>
<div id="map"></div>
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
<script src="https://unpkg.com/leaflet.markercluster@1.5.3/dist/leaflet.markercluster.js"></script>
<script>
const markers = __PAYLOAD__;
const onlineOnly = __ONLINE_PAYLOAD__;
const onlineHub = [18.0, -31.0];
const map = L.map("map", {
  scrollWheelZoom: false,
  zoomSnap: 0.25,
  zoomDelta: 0.5
}).setView([25, 5], 2.25);
L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
  maxZoom: 18,
  attribution: "&copy; OpenStreetMap contributors"
}).addTo(map);

function eventLinks(item) {
  return item.links ? `<br>${item.links}` : "";
}

function clusterIcon(cluster) {
  const count = cluster.getChildCount();
  const sizeClass = count < 10 ? "small" : (count < 25 ? "medium" : "large");
  const diameter = sizeClass === "small" ? 32 : (sizeClass === "medium" ? 38 : 44);
  return L.divIcon({
    html: `<div><span>${count}</span></div>`,
    className: `talk-cluster talk-cluster-${sizeClass}`,
    iconSize: L.point(diameter, diameter)
  });
}

const talkClusters = L.markerClusterGroup({
  showCoverageOnHover: false,
  spiderfyOnMaxZoom: true,
  zoomToBoundsOnClick: false,
  removeOutsideVisibleBounds: true,
  maxClusterRadius: 2,
  spiderfyDistanceMultiplier: 1.45,
  spiderLegPolylineOptions: {weight: 1.4, color: "#666c70", opacity: 0.65},
  iconCreateFunction: clusterIcon
});

const bounds = [];
for (const item of markers) {
  const style = {radius: 6, color: item.colour, weight: 2, fillColor: item.colour, fillOpacity: 0.85};
  const marker = L.circleMarker([item.lat, item.lon], style);
  const content = `<strong><a href="${item.url}">${item.title}</a></strong><br>` +
    `${item.type} · ${item.venue}<br>${item.date} · ${item.location}${eventLinks(item)}`;
  marker.bindPopup(content);
  talkClusters.addLayer(marker);
  bounds.push([item.lat, item.lon]);
}
map.addLayer(talkClusters);
// A grouped city opens immediately into its individual talks instead of
// zooming into a large regional cluster.
talkClusters.on("clusterclick", function(event) {
  event.layer.spiderfy();
});

if (onlineOnly.length) {
  const icon = L.divIcon({
    className: "",
    html: `<div class="online-hub">Online<br>${onlineOnly.length}</div>`,
    iconSize: [32, 32],
    iconAnchor: [16, 16]
  });
  const onlineMarker = L.marker(onlineHub, {icon}).addTo(map);
  const items = onlineOnly.map(item =>
    `<li><strong><a href="${item.url}">${item.title}</a></strong><br>` +
    `${item.type} · ${item.venue}<br>${item.date}${eventLinks(item)}</li>`
  ).join("");
  onlineMarker.bindPopup(
    `<strong>Online presentations (${onlineOnly.length})</strong><br>` +
    `<span class="map-note">Virtual marker; not a geographic location.</span>` +
    `<ul class="online-list">${items}</ul>`,
    {maxWidth: 390}
  );
  bounds.push(onlineHub);
}

L.control.scale({imperial: false}).addTo(map);

const legend = L.control({position: "bottomright"});
legend.onAdd = function() {
  const div = L.DomUtil.create("div", "map-legend");
  div.innerHTML =
    `<div><span class="legend-dot" style="background:#8b1a1a"></span>Invited talk</div>` +
    `<div><span class="legend-dot" style="background:#2c6077"></span>Invited seminar</div>` +
    `<div><span class="legend-dot" style="background:#263945"></span>Contributed talk</div>` +
    `<div><span class="legend-dot" style="background:#666c70"></span>Discussion session</div>` +
    `<div><span class="legend-dot online-dot"></span>Locationless online events</div>`;
  return div;
};
legend.addTo(map);
</script>
</body>
</html>
""".replace("__PAYLOAD__", payload).replace("__ONLINE_PAYLOAD__", online_payload),
        encoding="utf-8",
    )

    if skipped:
        print("\n".join(skipped))
    represented = len(markers) + len(online_only)
    print(
        f"Wrote {OUTPUT} with {len(markers)} geolocated records shown individually except for "
        f"same-location spiderfy groups, and one online marker representing "
        f"{len(online_only)} locationless events ({represented} records represented)."
    )


if __name__ == "__main__":
    main()
