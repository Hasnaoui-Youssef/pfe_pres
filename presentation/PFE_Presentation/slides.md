---
theme: default
title: From Halted State to Execution History
info: |
  ## From Halted State to Execution History
  An open instruction-trace pipeline for STM32 microcontrollers.
author: Youssef Hasnaoui
aspectRatio: 16/9
canvasWidth: 1280
drawings:
  enabled: false
transition: fade
colorSchema: light
---

<img class="title-slide-image" src="/title-slide.png" alt="STM32 Debugger — With Instruction Trace support — Youssef Hasnaoui">

<!-- Opening: “where did execution stop?” is different from “how did it get there?” -->

---
layout: center
class: section-slide
---
<div class="section-number">01</div>
<h1>Context</h1>
<p>Why a snapshot of a system is sometimes not enough.</p>

---
class: content-slide
---
<h1>The project context</h1>
<div class="title-rule"></div>
<div class="two-panel">
<div>
<h2>STMicroelectronics Tunis</h2>
<p class="lead">The project was carried out within the <b>Application &amp; Product Support</b> team.</p>
<v-clicks class="check-list">

- Supports customers using STM32 devices and tools
- Produces product documentation, application notes, and training material
- Investigates difficult field issues that conventional debugging cannot always explain
</v-clicks>
</div>
<div>
<div class="quote-card"><div class="quote-mark">“</div><p>Instruction trace is present in many STM32 devices, yet remains difficult to access outside proprietary, probe-bound environments.</p></div>
<div v-click class="stat-card"><b>A long-standing need</b><span>An independent, integrated way to use instruction trace.</span></div>
</div></div>

---
class: story-slide
clicks: 5
---
<div class="story-title">A missing apple is not an explanation.</div>
<div class="story-subtitle">A short analogy for the difference between a snapshot and a history.</div>
<div class="apple-story">
  <div class="kitchen">
    <div class="window"><div></div><div></div></div><div class="cabinet"><i></i><i></i><i></i><i></i></div><div class="counter"></div>
    <div class="plate"><span class="plate-label">APPLE</span><span v-click="[0, 2]" class="apple">●</span></div>
    <div class="person you" v-click="[0, 1]"><span></span><i></i><b>Youssef</b></div>
    <div class="exit-arrow" v-click="[1, 2]">Youssef leaves <b>→</b></div>
    <div class="question" v-click="[2, 4]">?</div>
    <div class="search-clues" v-click="[3, 4]"><span>FRIDGE</span><span>CUPBOARD</span><span>BASKET</span><small>no answer</small></div>
    <div class="person brother" v-click="[4, 5]"><span></span><i></i><b>Brother</b><em>●</em></div>
    <div class="camera" v-click="5"><i></i><b>CAMERA</b></div>
    <div class="camera-cone" v-click="5"></div>
    <div class="history-record" v-click="5"><span>12:01</span><b>brother enters</b><span>12:02</span><b>apple taken</b><span>12:03</span><b>brother leaves</b></div>
  </div>
  <div class="story-narration">
    <div class="step-label">A SIMPLE INVESTIGATION</div>
    <v-switch>
      <template #0><h2>Known state</h2><p>Youssef leaves an apple on the plate.</p><strong>We know the starting state.</strong></template>
      <template #1><h2>Time passes</h2><p>He leaves the kitchen; the relevant events happen while nobody is observing.</p><strong>The path is unobserved.</strong></template>
      <template #2><h2>Unexpected state</h2><p>He returns and the apple is gone.</p><strong>A final state is not an explanation.</strong></template>
      <template #3><h2>Looking for clues</h2><p>He checks the fridge, cupboard, and basket.</p><strong>Clues support guesses; they do not replay events.</strong></template>
      <template #4><h2>A likely hypothesis</h2><p>His brother may have taken it—but there is still no evidence.</p><strong>Hypotheses are not history.</strong></template>
      <template #5><h2>Recorded history</h2><p>A camera aimed at the plate records the sequence of events.</p><strong>The cause becomes evidence.</strong></template>
    </v-switch>
  </div>
</div>

<!-- Trace is like the footage: it reconstructs the sequence of events, not every property of the system. -->

---
class: content-slide
---
<h1>A halted target has the same problem</h1>
<div class="title-rule"></div>
<div class="two-panel">
<div>
<div class="snapshot-card"><div class="card-label">WHAT A HALT PROVIDES</div><div class="snapshot-grid"><span>Registers</span><span>Memory</span><span>Peripherals</span><span>Call stack*</span></div><p>A valuable view of the state <b>at one instant</b>.</p></div>
</div><div>
<div class="history-card"><div class="card-label">WHAT HAS ALREADY DISAPPEARED</div><ul><li v-click>Branches that were taken</li><li v-click>Calls that have returned</li><li v-click>Interrupts and preemption order</li><li v-click>The instruction that led to corruption</li></ul><p class="asterisk">*and the stack may itself be damaged.</p></div>
</div></div>

---
class: statement-slide
---
<div class="statement-side">OBSERVABILITY</div><div class="statement-content"><p class="statement-kicker">THE CORE LIMITATION</p><h1>State tells us <em>where</em><br>execution stopped.</h1><h2 v-click>Execution history tells us <span>how it got there.</span></h2></div>

---
layout: center
class: section-slide
---
<div class="section-number">02</div>
<h1>The opportunity</h1>
<p>Trace hardware exists. The missing piece is an accessible software path.</p>

---
class: content-slide
---
<h1>The gap this work addresses</h1>
<div class="title-rule"></div>
<table class="positioning"><thead><tr><th>Capability</th><th>Proprietary environments</th><th>Existing open tools</th><th>This work</th></tr></thead><tbody>
<tr><td>Conventional debugging</td><td>✓</td><td>✓</td><td class="ours">✓</td></tr><tr><td>Instruction trace</td><td>✓</td><td>—</td><td class="ours">✓</td></tr><tr><td>On-chip trace capture</td><td>Probe-bound</td><td>—</td><td class="ours">✓</td></tr><tr><td>No dedicated trace probe</td><td>✕</td><td>—</td><td class="ours">✓</td></tr><tr><td>Offline decoding</td><td>✕</td><td>Decode only</td><td class="ours">✓</td></tr><tr><td>IDE integration</td><td>✓</td><td>Partial</td><td class="ours">✓</td></tr>
</tbody></table>
<p v-click class="table-takeaway">The missing intersection: <b>on-chip capture through the ordinary debug connection, in an open integrated workflow.</b></p>

---
class: challenge-slide
---
<div class="challenge-copy"><div class="eyebrow">PROBLEM STATEMENT</div><h1>How can STM32 instruction trace be made reachable in an open, integrated debug chain?</h1><p>Without a dedicated trace probe. Without trace pins. Without dependence on a proprietary environment.</p></div>
<div class="constraint-stack"><div v-click><b>01</b> Use the probe already fitted to the board</div><div v-click><b>02</b> Retrieve capture over the ordinary debug cable</div><div v-click><b>03</b> Work on Windows and Linux</div><div v-click><b>04</b> Fit the developer's existing workflow</div></div>

---
layout: center
class: section-slide
---
<div class="section-number">03</div>
<h1>The trace chain</h1>
<p>From a compressed hardware record to source-level execution evidence.</p>

---
class: architecture-slide
---
<h1>The end-to-end trace chain</h1>
<div class="title-rule"></div>
<div class="pipeline">
<div class="pipe-stage hardware"><span>01</span><b>STM32H7S3L8</b><small>ETMv4 generates instruction trace</small></div><div class="pipe-arrow">→</div>
<div class="pipe-stage hardware"><span>02</span><b>On-chip TMC buffer</b><small>Retains the recent trace window</small></div><div class="pipe-arrow cyan">→</div>
<div class="pipe-stage contribution"><span>03</span><b>OpenOCD extensions</b><small>Configure and extract through SWD</small></div><div class="pipe-arrow cyan">→</div>
<div class="pipe-stage contribution"><span>04</span><b>Trace pipeline</b><small>Decode + reconstruct against ELF</small></div><div class="pipe-arrow cyan">→</div>
<div class="pipe-stage integration"><span>05</span><b>Debugger + VS Code</b><small>Source-level trace views</small></div></div>
<div class="legend">■ Target hardware &nbsp; <b>■</b> Project contribution &nbsp; <em>■</em> Workflow integration</div>

---
class: content-slide
---
<h1>Why reconstruction is necessary</h1>
<div class="title-rule"></div>
<div class="two-panel">
<div>
<h2>The target does not emit a verbose instruction log</h2>
<p class="lead">ETM trace is compressed: it reports information that cannot be inferred from the program image.</p>
<div class="trace-elements"><span v-click>branch outcome</span><span v-click>indirect target</span><span v-click>exception</span><span v-click>synchronization</span></div>
</div><div>
<div class="reconstruct-flow"><div>Trace byte stream</div><i>+</i><div>Exact ELF image</div><strong>↓</strong><div class="reconstruct-result">Reconstructed executed instructions</div></div>
<p v-click class="side-note">Compact trace + exact program image = meaningful execution history.</p>
</div></div>

---
class: content-slide
---
<h1>What the pipeline contributes</h1>
<div class="title-rule"></div>
<div class="contribution-grid"><div v-click><b>Configure</b><span>Discover and arm the trace source and on-chip sink.</span></div><div v-click><b>Extract</b><span>Drain the captured byte stream over the debug connection.</span></div><div v-click><b>Decode</b><span>Turn packets into trace elements.</span></div><div v-click><b>Reconstruct</b><span>Recover executed instructions using the ELF image.</span></div><div v-click><b>Attribute</b><span>Tie instructions to functions and source locations.</span></div><div v-click><b>Preserve gaps</b><span>Keep discontinuities explicit rather than inventing history.</span></div></div>

---
layout: center
class: section-slide
---
<div class="section-number">04</div>
<h1>Evidence</h1>
<p>A fault case where the halted state alone cannot identify the cause.</p>

---
class: case-slide
---
<h1>A fault is observed</h1>
<div class="two-panel">
<div>
<div class="fault-card"><div class="card-label">AT THE HALT</div><div class="fault-icon">!</div><b>Invalid-state fault<br>escalated to a hard fault</b><p>The processor stopped at a bad indirect call.</p></div>
</div><div>
<div class="question-card"><div class="card-label">WHAT IS STILL UNKNOWN?</div><p>Which function corrupted the function pointer?</p><p>When did the corruption occur?</p><p>What execution path led to the fault?</p><div v-click class="answer">The halted state does not contain that history.</div></div>
</div></div>

---
class: case-slide
---
<h1>The trace supplies the missing sequence</h1>
<div class="fault-timeline"><div class="timeline-step corruption" v-click><span>1</span><b>Copy loop executes</b><small>Writes one byte past a buffer</small></div><div class="timeline-line" v-click></div><div class="timeline-step" v-click><span>2</span><b>Function returns</b><small>The corrupted pointer remains in memory</small></div><div class="timeline-line" v-click></div><div class="timeline-step fault" v-click><span>3</span><b>Corrupted indirect call</b><small>Execution enters the fault handler</small></div></div>
<div v-click class="case-conclusion">The trace does not record every data value. It reveals the <b>control-flow evidence</b> that connects the corruption to the fault.</div>

---
class: results-slide
---
<h1>What was demonstrated</h1>
<div class="result-grid"><div><strong>2 KiB</strong><span>on-chip trace buffer on the STM32H7S3L8</span></div><div><strong>~1.6k–9k</strong><span>reconstructed instructions per capture window</span></div><div><strong>100%</strong><span>agreement with an independent reconstruction oracle</span></div><div><strong>229,424</strong><span>consecutive instruction transitions structurally checked</span></div><div class="wide"><strong>No trace pins. No dedicated trace probe.</strong><span>Every demonstrated capture travelled over the ordinary debug cable.</span></div></div>

---
class: content-slide
---
<h1>Scope and next steps</h1>
<div class="title-rule"></div>
<div class="two-panel">
<div>
<h2>Current scope</h2>
<ul class="scope-list"><li>One target configuration, one trace source, one on-chip sink</li><li>A bounded recent-execution window</li><li>Instruction/control-flow trace, not data trace</li><li>Timing packets are not usable on the validated target</li></ul>
</div><div>
<h2>Natural extensions</h2>
<ul class="future-list"><li>Trace filtering for a chosen code region</li><li>Timing/profile analysis with a capable decoder</li><li>Live exception naming in the frontend</li><li>Automatic discovery from ROM tables</li></ul>
</div></div>

---
class: closing-slide
---
<div class="closing-grid"></div><div class="closing-content"><div class="eyebrow">CONCLUSION</div><h1>Debugging tells us where execution stopped.</h1><h2>Instruction trace helps explain <span>how it got there.</span></h2><div class="closing-points">An open trace chain <i>·</i> Ordinary debug hardware <i>·</i> Execution history in the developer's workflow</div><p class="thanks">Thank you.</p></div>
