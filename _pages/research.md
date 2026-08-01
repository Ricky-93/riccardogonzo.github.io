---
title: 'Research interests'
excerpt:
author_profile: true
permalink: /research/
mathjax: true
---

<style>
  .research-results {
    margin-top: 0.75rem;
  }

  .research-result {
    display: grid;
    grid-template-columns: 190px minmax(0, 1fr);
    gap: 1.25rem;
    align-items: center;
    margin: 0 0 1.45rem;
  }

  .research-result-image {
    width: 190px;
    height: 132px;
    object-fit: contain;
    background: #fff;
  }

  .research-result h3 {
    margin: 0 0 0.3rem;
    font-size: 1.02em;
    line-height: 1.25;
  }

  .research-result-meta {
    margin: 0 0 0.45rem;
    color: #8a9298;
    font-size: 0.9em;
    line-height: 1.4;
  }

  .research-result-description {
    margin: 0;
    color: #51585e;
    font-size: 0.93em;
    line-height: 1.45;
  }

  .press-list li {
    margin-bottom: 0.55rem;
  }

  @media (max-width: 720px) {
    .research-result {
      grid-template-columns: 1fr;
      gap: 0.65rem;
    }

    .research-result-image {
      width: 100%;
      max-width: 390px;
      height: auto;
      max-height: 210px;
      justify-self: start;
    }
  }
</style>

<p align="center">
  <img src="/images/Research_diagram.jpg" alt="Research framework diagram" style="max-width:100%; border-radius: 8px; margin-bottom: 20px;">
</p>

## My Work at a Glance

I am a theoretical physicist working at the interface of high-energy physics and general relativity. I study gravitational binary systems and their waveforms, combining particle-physics tools—especially scattering amplitudes—with post-Newtonian and gravitational self-force methods. During my PhD, I developed a direct link between on-shell scattering amplitudes and gravitational waveforms. Since then, I have worked on methods for translating results between scattering and bound motion in Kerr spacetime, including their gravitational waveforms, and on an effective field theory formulation of gravitational self-force for bound orbits.

In 2026, I was awarded the [Royal Society University Research Fellowship](https://royalsociety.org/grants/university-research/) for my project *High-precision effective field theory for extreme-mass-ratio inspirals*. At Southampton, I am now building a research group around these questions, with PhD students and postdocs. My long-term goal is to connect weak-field post-Minkowskian and post-Newtonian theory with strong-field self-force methods, and use that connection to improve waveform models for current detectors—LIGO, Virgo and KAGRA—and future observatories such as LISA, ET and CE.

## <span style="display: flex; align-items: center;">Gravitational Waveforms from Scattering Amplitudes <span onclick="toggleVisibility('waveforms')" style="cursor: pointer; display: inline-block; vertical-align: middle; margin-left: 5px;"><svg id="arrow-waveforms" style="display: inline-block; transform: rotate(180deg); transition: transform 0.5s; vertical-align: middle; transform-origin: center; fill: #4A4E52;" xmlns="http://www.w3.org/2000/svg" height="24" viewBox="0 0 24 24" width="24"><path d="M18.59 16.41L20 15l-8-8-8 8 1.41 1.41L12 9.83z"/></svg></span></span>
<div id="waveforms" style="max-height: 0px; overflow: hidden; transition: max-height 0.5s ease-out; text-align: left;">
  Together with A. Cristofoli, D. Kosower and D. O’Connell, I helped establish a framework for computing gravitational waveforms directly from on-shell scattering amplitudes in the post-Minkowskian expansion. With other collaborators, I explored how coherent states extend the eikonal description and how classical gravitational waves emerge from the quantum point-particle picture. <br><br>

  With F. Alessio and C. Shi, I later introduced a set of classical generating functionals built from the S-matrix. Within this formulation, two-body scattering observables follow in a gauge-invariant way from Dirac brackets, providing a compact framework for radiative observables in spinning black-hole scattering.
</div>

## <span style="display: flex; align-items: center;">Scatter-to-Bound Dictionary for Kerr Geodesics and Waveforms <span onclick="toggleVisibility('dictionary')" style="cursor: pointer; display: inline-block; vertical-align: middle; margin-left: 5px;"><svg id="arrow-dictionary" style="display: inline-block; transform: rotate(180deg); transition: transform 0.5s; vertical-align: middle; transform-origin: center; fill: #4A4E52;" xmlns="http://www.w3.org/2000/svg" height="24" viewBox="0 0 24 24" width="24"><path d="M18.59 16.41L20 15l-8-8-8 8 1.41 1.41L12 9.83z"/></svg></span></span>
<div id="dictionary" style="max-height: 0px; overflow: hidden; transition: max-height 0.5s ease-out; text-align: left;">
  With C. Shi, I developed gauge-invariant maps between scattering and bound geodesic observables in Kerr spacetime, formulating the analytic continuation between scattering and bound actions and related observables for generic orbits. <br><br>

  With T. Adamo and A. Ilderton, I developed a classical Bethe–Salpeter framework connecting the analytic S-matrix to bound dynamics. In this framework, scattering waveforms can be analytically continued and resummed into periodic bound-state waveforms. The construction shows why resummation of the weak-field expansion is needed to recover orbital periodicity, and how gravitational self-force can provide a bridge between perturbative scattering data and bound motion. <br><br>

  Along this line, with J. Lewis and A. Pound, I developed the “first law of black-hole scattering”, relating elapsed proper time in scattering to the Detweiler redshift for bound motion—a central gauge-invariant building block for waveform modelling. <br><br>

  More recently, with G. Mogull, I have been developing a Magnus perturbation theory for bound orbits, building on the generating-functional approach and Dirac-bracket formalism developed for scattering. The idea is to expand the logarithm of the finite-time evolution operator, organising perturbation theory directly for periodic motion while keeping a clear link with scattering observables. This opens a promising new way of studying bound-orbit dynamics using tools from particle physics.
</div>

## <span style="display: flex; align-items: center;">Self-Force Effective Field Theory: From Weak to Strong Field <span onclick="toggleVisibility('selforce')" style="cursor: pointer; display: inline-block; vertical-align: middle; margin-left: 5px;"><svg id="arrow-selforce" style="display: inline-block; transform: rotate(180deg); transition: transform 0.5s; vertical-align: middle; transform-origin: center; fill: #4A4E52;" xmlns="http://www.w3.org/2000/svg" height="24" viewBox="0 0 24 24" width="24"><path d="M18.59 16.41L20 15l-8-8-8 8 1.41 1.41L12 9.83z"/></svg></span></span>
<div id="selforce" style="max-height: 0px; overflow: hidden; transition: max-height 0.5s ease-out; text-align: left;">
  With D. Akpinar and V. del Duca, I constructed the first effective field theory description of spinning black holes at first self-force order (1SF). We derived the effective action through quadratic order in spin and reformulated the metric perturbation in this language. The framework revealed new spinning recoil operators and made the connection between weak-field post-Minkowskian calculations and strong-field self-force results more direct. <br><br>

  With L. Barack, B. Leather, O. Long and N. Warburton, I also developed a resummation of the energy loss that combines post-Minkowskian and post-Newtonian results with the known strong-field behaviour near the scattering–plunge separatrix, using information from the critical orbits. The agreement with numerical black-hole perturbation theory is encouraging, and I look forward to extending this strategy towards more accurate analytic models of fluxes and other observables for eccentric orbits.
</div>

## Selected research results

<div class="research-results">

  <div class="research-result">
    <img class="research-result-image" src="/images/research/waveforms_from_amplitudes.png" alt="Scattering process with a radiated waveform">
    <div>
      <h3><a href="https://doi.org/10.1103/PhysRevD.106.056007" target="_blank" rel="noopener">Waveforms from amplitudes</a></h3>
      <p class="research-result-meta">Andrea Cristofoli, <strong>Riccardo Gonzo</strong>, David A. Kosower, Donal O'Connell &mdash; <em>Physical Review D</em> 106, 056007 (2022), <strong>Editor's Suggestion</strong></p>
      <p class="research-result-description">Established a framework for computing gravitational waveforms directly from on-shell scattering amplitudes.</p>
    </div>
  </div>

  <div class="research-result">
    <img class="research-result-image" src="/images/research/first_law_scatter_to_bound.png" alt="Scattering-to-bound continuation from an unbound trajectory to a bound orbit">
    <div>
      <h3><a href="https://doi.org/10.1103/s85p-gh7b" target="_blank" rel="noopener">First Law of Binary Black Hole Scattering</a></h3>
      <p class="research-result-meta"><strong>Riccardo Gonzo</strong>, Jack Lewis, Adam Pound &mdash; <em>Physical Review Letters</em> 135, 131401 (2025), <strong>Editor's Suggestion</strong>; <strong>PRL Collection of the Year 2025</strong></p>
      <p class="research-result-description">Extended the first law of binary mechanics to scattering orbits, including dissipative effects, and related the elapsed proper time in scattering to the Detweiler redshift for bound orbits.</p>
    </div>
  </div>

  <div class="research-result">
    <img class="research-result-image" src="/images/research/scatter_to_bound_table.png" alt="Table relating scattering observables to bound frequencies for spinning particles in Kerr">
    <div>
      <h3><a href="https://doi.org/10.1103/PhysRevLett.133.221401" target="_blank" rel="noopener">Scattering and bound observables for spinning particles in Kerr spacetime with generic spin orientations</a></h3>
      <p class="research-result-meta"><strong>Riccardo Gonzo</strong>, Canxin Shi &mdash; <em>Physical Review Letters</em> 133, 221401 (2024)</p>
      <p class="research-result-description">Related the impulse and spin kick in scattering to bound frequencies and precessions for generic spin orientations in Kerr spacetime.</p>
    </div>
  </div>

  <div class="research-result">
    <img class="research-result-image" src="/images/research/self_force_eft.png" alt="Spinning compact object orbiting a Kerr black hole">
    <div>
      <h3><a href="https://doi.org/10.1103/fs74-84v6" target="_blank" rel="noopener">The spinning self-force EFT: 1SF waveform recursion relation and Compton scattering</a></h3>
      <p class="research-result-meta">Dogan Akpinar, Vittorio Del Duca, <strong>Riccardo Gonzo</strong> &mdash; <em>Physical Review D</em> 112, 084014 (2025), <strong>Editor's Suggestion</strong></p>
      <p class="research-result-description">Developed an effective field theory description of spinning black holes at first self-force order, connecting the metric perturbation, waveform and Compton amplitude.</p>
    </div>
  </div>

  <div class="research-result">
    <img class="research-result-image" src="/images/research/critical_orbits_resummation.png" alt="Comparison of resummed energy-loss formulas with black-hole perturbation-theory data">
    <div>
      <h3><a href="https://doi.org/10.1103/pxzz-dl2b" target="_blank" rel="noopener">Resummed energy loss in extreme-mass-ratio scattering using critical orbits</a></h3>
      <p class="research-result-meta">Leor Barack, <strong>Riccardo Gonzo</strong>, Benjamin Leather, Oliver Long, Niels Warburton &mdash; <em>Physical Review D</em> 113, 104042 (2026)</p>
      <p class="research-result-description">Used the known strong-field divergence near the scattering–plunge separatrix to resum post-Minkowskian and post-Newtonian energy-loss results, and tested the formulas against numerical black-hole perturbation theory.</p>
    </div>
  </div>

</div>

## Press and features

<ul class="press-list">
  <li><a href="https://www.quantamagazine.org/massive-black-holes-shown-to-act-like-quantum-particles-20220329/" target="_blank" rel="noopener"><em>Massive Black Holes Shown to Act Like Quantum Particles</em></a>, <em>Quanta Magazine</em> (2022), discussing my work on coherent graviton states and the quantum-to-classical transition in black-hole scattering.</li>
  <li><a href="https://nordita.org/news-archive/news-2026/bringing-together-communities-to-improve-precision-in-gravitational-wave-modeling/" target="_blank" rel="noopener"><em>Bringing together communities to improve precision in gravitational-wave modeling</em></a>, Nordita (2026), about the scientific aims of the programme and the experience of students and postdocs who took part.</li>
  <li>Discussion on the 4Gravitons blog: <a href="https://4gravitons.com/2021/12/31/classicality-has-consequences/" target="_blank" rel="noopener"><em>Classicality Has Consequences</em></a> (2021).</li>
</ul>

<script>
  function toggleVisibility(id) {
    var element = document.getElementById(id);
    var arrow = document.getElementById('arrow-' + id);
    if (element.style.maxHeight === "1000px") {
      element.style.maxHeight = "0px";
      arrow.style.transform = "rotate(180deg)";
    } else {
      element.style.maxHeight = "1000px";
      arrow.style.transform = "rotate(0deg)";
    }
  }
</script>
