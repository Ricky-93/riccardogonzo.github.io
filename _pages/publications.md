---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

Here you can explore my research papers, with links to the journal, arXiv version and a short abstract for each work. My complete publication record is also available on [INSPIRE--HEP](https://inspirehep.net/authors/1812058?ui-citation-summary=true).

## Collaboration network

Each node represents a co-author, preprint or journal article. Click on a node for more information.

<iframe src="/collab_net/network.html" height="300" width="100%" style="border: none"></iframe>

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
