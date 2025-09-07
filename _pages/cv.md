---
title: "Curriculum Vitae"
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
---

{% include base_path %}

You can download my full CV [here](/files/cv_Riccardo_Gonzo.pdf){:target="_blank"}<!--_-->.

## Summary
I am a theoretical physicist with over seven years of research experience spanning high-energy physics and general relativity. My current work focuses on the analytical description of gravitational binary systems and the modelling of their waveforms by combining modern particle physics tools — such as scattering amplitudes — with traditional general relativity methods like the self-force expansion.
My long-term vision is to develop a unified formalism that combines amplitude-based perturbation theory with self-force resummation, producing new waveform models relevant to detectors such as LISA, and to build an international research group at the interface of amplitudes, gravity, and gravitational-wave science.


## Academic appointments
<font size="5">
<table>
<tr>
  <td width="22%"><div align="right">2025&nbsp;–&nbsp;present<br>
    <img src='/images/qmul_logo.png' style="padding-top:7px;display:block;margin-right:10px;" width="130"></div>
  </td>
  <td width="80%">Postdoctoral Research Associate<br>
    Queen Mary University of London, UK
  </td>
</tr>

<tr><td></td></tr>

<tr>
  <td width="22%"><div align="right">2022&nbsp;–&nbsp;2025<br>
    <img src='/images/edinburgh_logo.png' style="padding-top:7px;display:block;margin-right:10px;" width="130"></div>
  </td>
  <td width="80%">Postdoctoral Research Associate<br>
    University of Edinburgh, UK
  </td>
</tr>
</table>
</font>


## Education
<font size="5">
<table>
<tr>
  <td width="22%"><div align="right">2018&nbsp;–&nbsp;2022<br>
    <img src='/images/tcd_logo.png' style="padding-top:7px;display:block;margin-right:10px;" width="130"></div>
  </td>
  <td width="80%">PhD in Theoretical Particle Physics, Trinity College Dublin (Ireland)<br>
    <span style="font-weight:600">Thesis:</span> <i>Coherent states and classical radiative observables in the S-matrix formalism</i> (<a href="http://www.tara.tcd.ie/handle/2262/98491" target="_blank">link</a>)<br>
    <span style="font-weight:600">Supervisor:</span> Prof. Ruth Britto<br>
    Marie-Curie ITN fellow (SAGEX) — training in research and professional skills (workshops, schools, 3-month Wolfram internship).
  </td>
</tr>

<tr><td></td></tr>

<tr>
  <td width="22%"><div align="right">2015&nbsp;–&nbsp;2017<br>
    <img src='/images/padova_logo.png' style="padding-top:7px;display:block;margin-right:10px;" width="130"></div>
  </td>
  <td width="80%">Master of Physics, University of Padova (Italy)<br>
    <span style="font-weight:600">Thesis:</span> <i>[Thesis title here]</i><br>
    <span style="font-weight:600">Advisors:</span> [Advisor names here]<br>
    <span style="font-weight:600">Final grade:</span> 110/110 cum laude &nbsp; &nbsp; &nbsp;
    <span style="font-weight:600">GPA:</span> [GPA here]
  </td>
</tr>

<tr><td></td></tr>

<tr>
  <td width="22%"><div align="right">2012&nbsp;–&nbsp;2015<br>
    <img src='/images/padova_logo.png' style="padding-top:7px;display:block;margin-right:10px;" width="130"></div>
  </td>
  <td width="80%">Bachelor of Physics, University of Padova (Italy)<br>
    <span style="font-weight:600">Thesis:</span> <i>[Thesis title here]</i><br>
    <span style="font-weight:600">Advisors:</span> [Advisor names here]<br>
    <span style="font-weight:600">Final grade:</span> 110/110 cum laude &nbsp; &nbsp; &nbsp;
    <span style="font-weight:600">GPA:</span> [GPA here]
  </td>
</tr>
</table>
</font>

<!---
## Funding
<font size="5">
<table>
  <tr>
    <td width="22%"><div align="right">Jan 2023 - Nov 2023<br>
		<img src="/images/logo_800anni.png" style="padding-top: 4px;display: block;margin-right:7px;" width="150"></div></td>
    <td width="80%">
	  <span style="font-weight:600">Research grant, Department of Mathematics, University of Padova</span><br>
    <span style="font-weight:600">Project: </span><i>Mathematical models for complex living systems: critical emergent phenomena from network interaction and optimization</i><br>
    <span style="font-weight:600">Amount: </span> € 23,889.84 <br>
   </td>
  </tr>
<td></td>
  <tr>
    <td width="22%"><div align="right">Oct 2019 - Dec 2022<br>
		<img src="/images/logo_800anni.png" style="padding-top: 4px;display: block;margin-right:7px;" width="150"></div></td>
    <td width="80%">
	  <span style="font-weight:600">Doctoral fellowship, University of Padova</span><br>
    <span style="font-weight:600">Amount: </span> ≈ € 70,000.00 <br>
   </td>
  </tr>
</table>
</font>
-->

## Publications & preprints
  <ul>{% for post in site.publications reversed %}
    {% include archive-single-cv-pub.html %}
  {% endfor %}</ul>


## Organized conferences, schools and workshops

<style>
  /* EVENTS LIST */
  .events { font-size: 1.05rem; }
  .event {
    display: flex;
    gap: 1rem;
    padding: 1rem 0;
    border-top: 1px solid #eee;
  }
  .event:first-child { border-top: 0; }

  .event .year {
    width: 4.5rem;
    text-align: right;
    color: #6c757d;
    font-weight: 600;
    line-height: 1.2;
    flex: 0 0 auto;
  }

  .event .thumb {
    width: 120px;
    height: 160px;
    flex: 0 0 auto;
    object-fit: cover;
    border-radius: 8px;
    box-shadow: 0 2px 6px rgba(0,0,0,0.08);
    background: #f8f9fa; /* graceful if image missing */
  }

  .event .body { flex: 1 1 auto; }

  .event .title { font-weight: 600; }
  .event .role  { color: #6c757d; }
  .event .loc   { color: #6c757d; margin-top: 0.25rem; }

  .event .links { margin-top: 0.35rem; }
  .event .link {
    display: inline-block;
    padding: 0.15rem 0.5rem;
    border-radius: 6px;
    border: 1px solid #dee2e6;
    text-decoration: none;
    color: #0d6efd;
    font-weight: 500;
    line-height: 1.2;
  }
  .event .link:hover { text-decoration: underline; }

  /* Mobile tweaks */
  @media (max-width: 640px) {
    .event { align-items: flex-start; }
    .event .year { width: 3.2rem; text-align: left; }
    .event .thumb { width: 100px; height: 140px; }
  }
</style>

<div class="events">

  <div class="event">
    <div class="year">2026</div>
    <img class="thumb" src="/images/nordita_logo.png" alt="Nordita program" loading="lazy">
    <div class="body">
      <div class="role">Organizer —</div>
      <div class="title"><i>Nordita program: Amplitudes, Strong-Field Gravity, and Resummation</i></div>
      <div class="loc">Nordita Institute, Stockholm</div>
      <!-- <div class="links"><a class="link" href="#" target="_blank" rel="noopener">Details</a></div> -->
    </div>
  </div>

  <div class="event">
    <div class="year">2025</div>
    <img class="thumb" src="/images/SFmeetsAmpl2.png" alt="2nd Annual Workshop on Self-Force and Amplitudes" loading="lazy">
    <div class="body">
      <div class="role">Organizer —</div>
      <div class="title"><i>2nd Annual Workshop on Self-Force and Amplitudes</i></div>
      <div class="loc">University of Southampton</div>
      <div class="links">
        <a class="link" href="https://indico.cern.ch/event/1485758/" target="_blank" rel="noopener">Event page</a>
      </div>
    </div>
  </div>

  <div class="event">
    <div class="year">2024</div>
    <img class="thumb" src="/images/SFmeetsAmpl1.png" alt="Gravitational self-force and scattering amplitudes" loading="lazy">
    <div class="body">
      <div class="role">Organizer —</div>
      <div class="title"><i>Gravitational self-force and scattering amplitudes</i></div>
      <div class="loc">Higgs Centre, University of Edinburgh</div>
      <div class="links">
        <a class="link" href="https://higgs.ph.ed.ac.uk/workshops/gravitational-self-force-and-scattering-amplitudes/" target="_blank" rel="noopener">Workshop page</a>
      </div>
    </div>
  </div>

  <div class="event">
    <div class="year">2021</div>
    <img class="thumb" src="/images/SAGEX_school.JPG" alt="SAGEX amplitude school" loading="lazy">
    <div class="body">
      <div class="role">Organizer —</div>
      <div class="title"><i>SAGEX amplitude school</i></div>
      <div class="loc">NBI Institute, Copenhagen</div>
      <div class="links">
        <a class="link" href="https://indico.nbi.ku.dk/event/1530/" target="_blank" rel="noopener">School page</a>
      </div>
    </div>
  </div>

</div>


## Talks, presentations and posters
  <ul>{% for post in site.talks reversed %}
    {% include archive-single-talk-cv.html %}
  {% endfor %}</ul>

## Honors and awards
* **Marie Skłodowska-Curie grant “SAGEX”** from the European Union’s Horizon 2020 programme (2019) — *Scattering Amplitudes: from Geometry to Experiments*  
* **First place, “Riccardo Rossi” scholarship** (2011), awarded by Associazione Nemesis, Italy  
* **Funding award** of £10.4k for the organization of the workshop *Gravitational Self-Force and Amplitudes* at the Higgs Centre, University of Edinburgh (2023)  
* **Funding award** of £16.4k for the Nordita program *Amplitudes, Strong-Field Gravity, and Resummation* (2025)  

## Supervision
* Co-supervision of one PhD student at Sapienza University of Rome (Emanuele Rosi), with Vittorio Del Duca.
* Supervision of one MSc thesis at Sapienza University of Rome (Andrea de Simone), with Vittorio Del Duca — *Gravitational self-force from scattering amplitudes*.
* Supervision of one MSc thesis at Sapienza University of Rome (Damiano Barcaro), with Vittorio Del Duca — *[Scattering waveforms for Kerr black holes from the soft expansion](https://arxiv.org/abs/2411.18632)* (→ PhD at Mainz University).
* Supervision of one MSc thesis at the University of Edinburgh (Leixi Wang) — *Classical spacetimes from amplitudes*.

## Teaching
  <ul>{% for post in site.teaching reversed %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>
