---
layout: single
title: "My work"
permalink: /my-work/
author_profile: true
redirect_from:
  - /resume
---

{% if author.googlescholar %}
  You can also find my articles on <u><a href="{{author.googlescholar}}">my Google Scholar profile</a>.</u>
{% endif %}

{% include base_path %}

This is a my collaboration network: the color of each node specifies either a <span style="color:#d6d2d2;font-weight:600;">co-author</span>, a <span style="color:#79addc;font-weight:600;">preprint</span> or <span style="color:#9e1910;font-weight:600;">journal article</span>. Click on a node for more information.
 <iframe src="/collab_net/network.html" height="300" width="100%" style="border: none"></iframe>
<br><br>

{% for post in site.publications reversed %}
  {% include archive-single-publication.html %}
{% endfor %}

<p>This is my collaboration network. Click a node for names; drag to explore.</p>
<div id="coauthor-graph"></div>


## RESEARCH ARTICLES

<ul class="pub-list">
  <li class="pub-card"><p class="pub-title"><a href="https://arxiv.org/abs/1906.11763">Asymptotic Charges and Coherent States in QCD</a></p><p class="pub-meta">arXiv:1906.11763</p></li>
  <li class="pub-card"><p class="pub-title"><a href="https://arxiv.org/abs/2002.00975">BMS Symmetry of Celestial OPE</a></p><p class="pub-meta">arXiv:2002.00975</p></li>
  <li class="pub-card"><p class="pub-title"><a href="https://arxiv.org/abs/2012.01406">Light-ray operators, detectors and gravitational event shapes</a></p><p class="pub-meta">arXiv:2012.01406</p></li>
  <li class="pub-card"><p class="pub-title"><a href="https://arxiv.org/abs/2107.10193">Waveforms from amplitudes</a></p><p class="pub-meta">arXiv:2107.10193</p></li>
  <li class="pub-card"><p class="pub-title"><a href="https://arxiv.org/abs/2109.01072">Geodesics from Classical Double Copy</a></p><p class="pub-meta">arXiv:2109.01072</p></li>
  <li class="pub-card"><p class="pub-title"><a href="https://arxiv.org/abs/2112.07036">Graviton particle statistics and coherent states from classical scattering amplitudes</a></p><p class="pub-meta">arXiv:2112.07036</p></li>
  <li class="pub-card"><p class="pub-title"><a href="https://arxiv.org/abs/2112.07556">The Uncertainty Principle and Classical Amplitudes</a></p><p class="pub-meta">arXiv:2112.07556</p></li>
  <li class="pub-card"><p class="pub-title"><a href="https://arxiv.org/abs/2207.13719">Celestial holography on Kerr-Schild backgrounds</a></p><p class="pub-meta">arXiv:2207.13719</p></li>
  <li class="pub-card"><p class="pub-title"><a href="https://arxiv.org/abs/2212.13269">Bethe-Salpeter equation for classical gravitational bound states</a></p><p class="pub-meta">arXiv:2212.13269</p></li>
  <li class="pub-card"><p class="pub-title"><a href="https://arxiv.org/abs/2304.06066">Boundary to bound dictionary for generic Kerr orbits</a></p><p class="pub-meta">arXiv:2304.06066</p></li>
  <li class="pub-card"><p class="pub-title"><a href="https://arxiv.org/abs/2305.17166">Wave scattering event shapes at high energies</a></p><p class="pub-meta">arXiv:2305.17166</p></li>
  <li class="pub-card"><p class="pub-title"><a href="https://arxiv.org/abs/2309.17429">Spinning waveforms from KMOC at leading order</a></p><p class="pub-meta">arXiv:2309.17429</p></li>
  <li class="pub-card"><p class="pub-title"><a href="https://arxiv.org/abs/2402.00124">Gravitational Bound Waveforms from Amplitudes</a></p><p class="pub-meta">arXiv:2402.00124</p></li>
  <li class="pub-card"><p class="pub-title"><a href="https://arxiv.org/abs/2405.09687">Scattering and bound observables for spinning particles in Kerr spacetime with generic spin orientations</a></p><p class="pub-meta">arXiv:2405.09687</p></li>
  <li class="pub-card"><p class="pub-title"><a href="https://arxiv.org/abs/2409.03437">The first law of binary black hole scattering</a></p><p class="pub-meta">arXiv:2409.03437</p></li>
  <li class="pub-card"><p class="pub-title"><a href="https://arxiv.org/abs/2504.02025">The spinning self-force EFT: 1SF waveform recursion relation and Compton scattering</a></p><p class="pub-meta">arXiv:2504.02025</p></li>
  <li class="pub-card"><p class="pub-title"><a href="https://arxiv.org/abs/2506.03249">Dirac brackets for classical radiative observables</a></p><p class="pub-meta">arXiv:2506.03249</p></li>
  <li class="pub-card"><p class="pub-title"><a href="https://arxiv.org/abs/2508.10761">Unexpected Symmetries of Kerr Black Hole Scattering</a></p><p class="pub-meta">arXiv:2508.10761</p></li>
</ul>
