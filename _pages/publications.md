---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

I have 22 papers, including 20 published in renowned journals such as *Journal of High Energy Physics*, *Physical Review D* and *Physical Review Letters*, with over 1100 citations and an h-index of 16 according to INSPIRE--HEP (July 2026).

[INSPIRE--HEP](https://inspirehep.net/authors/1812058?ui-citation-summary=true){: .btn .btn--primary}
[ORCID](https://orcid.org/0000-0001-7285-6295){: .btn}
[Google Scholar](https://scholar.google.com/citations?user=TDT1fI0AAAAJ&hl=en){: .btn}

## Collaboration network

Each node represents a co-author, preprint or journal article. Click on a node for more information.

<iframe src="/collab_net/network.html" title="Interactive publication and collaboration network" loading="lazy" height="340" width="100%" style="border:0;"></iframe>

{% assign publications = site.publications | sort: "date" | reverse %}

## Preprints

{% for post in publications %}
  {% unless post.paperurl %}
    {% include archive-single-publication.html %}
  {% endunless %}
{% endfor %}

## Peer-reviewed publications

{% for post in publications %}
  {% if post.paperurl %}
    {% include archive-single-publication.html %}
  {% endif %}
{% endfor %}
