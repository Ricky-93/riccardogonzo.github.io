---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

Over the years, I have had the privilege of working with some amazing people on several interesting problems in gravitational physics. Below is a list of my publications. Links to the journal and arXiv versions, together with a short abstract, are provided for each paper. My complete publication record is also available on [INSPIRE--HEP](https://inspirehep.net/authors/1812058?ui-citation-summary=true).

## Collaboration network

The network below shows the people I have worked with and the papers that came from these collaborations. Click on a person or paper for more information.

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
