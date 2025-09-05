---
layout: archive
title: "My work"
permalink: /my-work/
author_profile: true
redirect_from:
  - /resume
---

{% include base_path %}

Publications
======
  <ul>{% for post in site.publications reversed %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>
