---
permalink: /
title: 'Riccardo Gonzo'
excerpt:
author_profile: true
description: 'A theoretical physicist exploring the intersection of high-energy physics and general relativity, who fell in love with amplitudes and gravitational waves.'
redirect_from:
  - /about/
  - /about.html
---

Welcome! I am Riccardo Gonzo, a Postdoctoral Research Associate at the [Centre for Theoretical Physics, Queen Mary University of London](https://www.seresearch.qmul.ac.uk/cfp/){:target="_blank"}<!--_-->. Previously, I was a postdoctoral researcher at the [Higgs Centre for Theoretical Physics, University of Edinburgh](https://www.ph.ed.ac.uk/higgs){:target="_blank"}<!--_-->. My research lies at the interface of high-energy physics and general relativity, with the goal of developing new analytical tools for modelling gravitational-wave signals from binary black hole systems.



## <span style="display: flex; align-items: center;">What is physics? <span onclick="toggleVisibility('physics')" style="cursor: pointer; display: inline-block; vertical-align: middle; margin-left: 5px;"><svg id="arrow-physics" style="display: inline-block; transform: rotate(0deg); transition: transform 0.5s; vertical-align: middle; transform-origin: center; fill: #4A4E52;" xmlns="http://www.w3.org/2000/svg" height="24" viewBox="0 0 24 24" width="24"><path d="M18.59 16.41L20 15l-8-8-8 8 1.41 1.41L12 9.83z"/></svg></span></span>

<div id="physics" style="max-height: 2000px; overflow: hidden; transition: max-height 0.5s ease-out;">

<p align="center">
  <img src="/images/Physics_map.jpeg" alt="Physics overview" style="max-width:100%; border-radius: 8px; margin-bottom: 20px;">
</p>

</div>


## <span style="display: flex; align-items: center;">What I think about all day (and sometimes all night) <span onclick="toggleVisibility('glance')" style="cursor: pointer; display: inline-block; vertical-align: middle; margin-left: 5px;"><svg id="arrow-glance" style="display: inline-block; transform: rotate(0deg); transition: transform 1s; vertical-align: middle; transform-origin: center; fill: #4A4E52;" xmlns="http://www.w3.org/2000/svg" height="24" viewBox="0 0 24 24" width="24"><path d="M18.59 16.41L20 15l-8-8-8 8 1.41 1.41L12 9.83z"/></svg></span></span>
<div id="glance" style="max-height: 2000px; overflow: hidden; transition: max-height 0.5s ease-out;">

<p> Most of my time goes into understanding how gravity works when two black holes interact and spiral together. To tackle this, I combine modern tools from particle physics — such as scattering amplitudes — with traditional methods from general relativity, including the self-force expansion. My goal is to develop a unified analytic framework that describes binary dynamics across regimes, from the weak-field inspiral to the strong-field merger and ringdown. </p>

<p> In practice, this means constructing compact analytical “building blocks” for gravitational waveforms — the signals detected today by LIGO–Virgo–KAGRA and in the future by LISA and the Einstein Telescope. I am particularly excited about how amplitude-based ideas can simplify calculations and uncover hidden structures in gravity, providing new ingredients for accurate waveform modelling and, ultimately, deeper insights into both fundamental physics and astrophysics. </p>

<p> Looking ahead, my dream is to establish an international research group dedicated to advancing the synergy between scattering amplitudes and gravitational-wave science. </p>

<!-- My works have been published in Physical Review X, Physical Review Letters, Proceedings of the National Academy of Sciences (PNAS), and Science Advances, among others. I have presented my work at several international conferences and workshops, -->

<h3>Who I work with</h3>
<p>This is my collaboration network: the color of each node specifies either a <span style="color:#d6d2d2;font-weight:600;">co-author</span>, a <span style="color:#79addc;font-weight:600;">preprint</span> or <span style="color:#9e1910;font-weight:600;">journal article</span>. Click on a node for more information.</p>

 <iframe src="/collab_net/network.html" height="300" width="100%" style="border: none"></iframe>

<h3>Where my research takes me</h3>
The markers on the map represent a conference, workshop, or institute where I presented my work: <span style="color:darkred;font-weight:600;">invited conference talks</span>, <span style="color:blue;font-weight:600;">invited seminars</span>, <span style="color:darkblue;font-weight:600;">contributed talks and posters</span>
<!-- optional if you enable it: --> and <span style="color:gray;font-weight:600;">discussion sessions</span>. Click on a marker for more information.

<div style="margin-bottom: 20px;"></div>
 <iframe src="/talkmap/talks_map.html" height="300" width="100%" style="border: none"></iframe>
</div>





<script>
  function toggleVisibility(id) {
    var element = document.getElementById(id);
    var arrow = document.getElementById('arrow-' + id);
    if (element.style.maxHeight === "2000px") {
      element.style.maxHeight = "0px";
      arrow.style.transform = "rotate(180deg)";
    } else {
      element.style.maxHeight = "2000px";
      arrow.style.transform = "rotate(0deg)";
    }
  }
</script>


<script type="application/ld+json">
{
  "@context": "http://schema.org",
  "@type": "ProfilePage",
  "mainEntity": {
    "@type": "Person",
    "@id": "https://riccardogonzo.com",
    "name": "Riccardo Gonzo",
    "nationality": "Italian",
    "honorificPrefix": "Dr.",
    "jobTitle": "Postdoctoral Research Associate",
    "affiliation": [
      {
        "@type": "Organization",
        "name": "University of Edinburgh, School of Physics and Astronomy",
        "sameAs": [
          "https://www.ed.ac.uk/physics-astronomy"
        ]
      },
      {
        "@type": "Organization",
        "name": "Queen Mary University of London",
        "sameAs": [
          "https://www.qmul.ac.uk/"
        ]
      }
    ],
    "alumniOf": [
      {
        "@type": "CollegeOrUniversity",
        "name": "Trinity College Dublin",
        "sameAs": "https://www.tcd.ie/"
      },
      {
        "@type": "CollegeOrUniversity",
        "name": "University of Padova",
        "sameAs": "https://www.unipd.it/"
      }
    ],
    "gender": "Male",
    "description": "A theoretical physicist exploring the intersection of high-energy physics and general relativity, who fell in love with amplitudes and gravitational waves.",
    "url": "https://riccardogonzo.com",
    "image": "https://riccardogonzo.com/images/profile_picture.jpg",
    "address": {
      "@type": "PostalAddress",
      "addressLocality": "Edinburgh",
      "addressCountry": "United Kingdom"
    },
    "sameAs": [
      "https://scholar.google.com/citations?user=TDT1fI0AAAAJ&hl=en",
      "https://orcid.org/0000-0001-7285-6295",
      "https://inspirehep.net/authors/1812058?ui-citation-summary=true",
      "https://www.researchgate.net/profile/Riccardo-Gonzo",
      "https://www.linkedin.com/in/riccardogonzo/"
    ]
  }
}
</script>
