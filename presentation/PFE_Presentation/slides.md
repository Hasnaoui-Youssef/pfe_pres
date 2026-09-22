---
theme: default
title: "Design and Implementation of a Debugger with Instruction Trace Capabilities."
author: Youssef Hasnaoui
info: |
  Engineering defense · National Engineering School of Carthage · STMicroelectronics
  26 September 2026 · 23 main slides + 7 backup slides · 20 minutes
aspectRatio: 16/9
canvasWidth: 1280
colorSchema: light
transition: slide-left
drawings:
  enabled: false
fonts:
  sans: Arial
  mono: DejaVu Sans Mono
  provider: none
download: false
exportFilename: Youssef-Hasnaoui-PFE-Defense
class: cover
---
<div class="cover-masthead">
  <div class="university"><img src="/branding/university-of-carthage.png" alt="University of Carthage logo"><span>University of Carthage<small>National Engineering School of Carthage</small></span></div>
  <img class="enicar" src="/branding/enicarthage.jpg" alt="ENICarthage logo">
  <img class="st" src="/branding/stmicroelectronics.svg" alt="STMicroelectronics logo">
</div>
<div class="kicker">End-of-studies project · Engineering defense</div>
<h1>Design and Implementation of a Debugger with <em>Instruction Trace Capabilities.</em></h1>
<div class="author">Youssef Hasnaoui</div>
<p class="institution">Microelectronics &amp; Embedded Systems · End-of-studies project</p>
<div class="meta"><div><b>Host organization</b>STMicroelectronics</div><div><b>Academic supervisor</b>Faten Salem</div><div><b>Industry supervisor</b>Mohamed Hamrouni</div><div><b>Reviewer</b>Ms Nourelhouda BEN YOUSSEF</div><div><b>Jury President</b>Ms Samia HACHMI</div><div><b>Defense date</b>26 September 2026</div></div>

<!--
Timing: 20 seconds · 00:00–00:20.
Progressive reveals: 0. Advance with the normal presentation controls.

Introduce the work as the design and implementation of a debugger with instruction trace capabilities. Emphasize the software contribution; a particular development board is an experimental resource, not the definition of the project. The jury can be assumed to know software engineering, but not ETM, CoreSight or embedded debugging internals.
Source: report cover metadata and user-confirmed date/jury.
-->

---
title: "Host organization and team"
clicks: 2
transition: fade-out
class: defense-slide
---

<div class="kicker">Context and Problem Statement</div>
<h1>Host organization and team</h1>

<div class="diagram-sequence"><div class="diagram-node reused"><DefenseIcon name="organization" /><b>STMicroelectronics</b><small>Semiconductors and embedded systems</small></div><span class="diagram-arrow" aria-hidden="true">→</span><div class="diagram-node reused" v-click="1"><DefenseIcon name="organization" /><b>Tunis site</b><small>Engineering and technical support</small></div><span class="diagram-arrow" aria-hidden="true">→</span><div class="diagram-node built" v-click="2"><DefenseIcon name="team" /><b>Application &amp; Product Support</b><small>Host team</small></div></div><div class="team-activities" v-click="2"><span><DefenseIcon name="probe" />Customer investigations</span><span><DefenseIcon name="file" />Technical documentation</span><span><DefenseIcon name="team" />Developer support</span></div>

<!--
Timing: 45 seconds · 00:20–01:05.
Progressive reveals: 2. Advance with the normal presentation controls.

Explain ST briefly, then the Tunis site and the host team. [Click 1] Introduce the engineering setting. [Click 2] The team's investigations and developer-support work motivated making instruction trace easier to use. Do not give company statistics or a long corporate introduction. Transition: what information is missing when an embedded application fails?
Source: dissertation chap_01.tex, Host Organization.
-->

---
title: "Problem context: state and execution history"
clicks: 2
class: defense-slide
---

<div class="kicker">Context and Problem Statement</div>
<h1>Problem context: state and execution history</h1>

<div class="observation-figure"><div class="state-observation"><DefenseIcon name="snapshot" /><h2>State at the halt</h2><div class="state-registers"><span>Registers</span><span>Memory</span><span>Call stack</span></div></div><div class="history-observation" v-click="1"><DefenseIcon name="history" /><h2>Earlier execution</h2><div class="execution-timeline"><span>Function A</span><i>→</i><span>Function B</span><i>→</i><span class="fault-mark">Fault</span></div><div class="missing-history">Which path led to this state?</div></div></div><p class="figure-note"><span v-click="2">Returned calls and earlier branch decisions are absent from a state snapshot.</span></p>

<!--
Timing: 65 seconds · 01:05–02:10.
Progressive reveals: 2. Advance with the normal presentation controls.

A debugger lets the developer stop execution and inspect registers, memory and the current call stack. [Click 1] An error can originate in a function that has already returned. The final state does not give the complete path. [Click 2] This motivates recording execution, in addition to inspecting state. Explain the call stack as current nesting, not a log of every earlier call. Transition: the engineering objective is to make that execution record part of the debugger.
Source: dissertation chap_01.tex, Observing an Executing Program.
-->

---
title: "Problem statement and requirements"
clicks: 2
class: defense-slide
---

<div class="kicker">Context and Problem Statement</div>
<h1>Problem statement and requirements</h1>

<p class="research-question">Integrate instruction trace into an open debugger:<br><strong>from hardware capture to source-level analysis.</strong></p><div class="requirement-grid" v-click="1"><div><DefenseIcon name="probe" /><b>Acquire trace</b></div><div><DefenseIcon name="code" /><b>Reconstruct execution</b></div><div><DefenseIcon name="screen" /><b>Present source context</b></div><div><DefenseIcon name="file" /><b>Support offline analysis</b></div></div><p class="figure-note"><span v-click="2">Ordinary debug connection · existing development environment · Windows and Linux</span></p>

<!--
Timing: 50 seconds · 02:10–03:00.
Progressive reveals: 2. Advance with the normal presentation controls.

State the objective directly. The debugger must acquire a trace, reconstruct the executed instructions and make the result usable at source level. [Click 1] These four capabilities define the work. [Click 2] The constraints include ordinary debug access, IDE integration and host portability. The intended architecture does not hard-code a development board; the implemented acquisition path still depends on supported trace capabilities. Transition: which pieces already exist, and which work remained to be implemented?
Source: dissertation chap_01.tex, Problem Statement; chap_04.tex, functional requirements.
-->

---
title: "Existing software foundations"
clicks: 2
transition: fade-out
class: defense-slide
---

<div class="kicker">Objectives and Technical Approach</div>
<h1>Existing software foundations</h1>

<div class="foundation-grid"><div class="diagram-node reused"><DefenseIcon name="probe" /><b>OpenOCD</b><small>Target access and run control</small></div><div class="diagram-node reused" v-click="1"><DefenseIcon name="code" /><b>LLDB / LLVM</b><small>Program image, symbols and debugging</small></div><div class="diagram-node reused" v-click="1"><DefenseIcon name="trace" /><b>OpenCSD</b><small>Trace-protocol decoding</small></div></div><div class="integration-gap" v-click="2"><span>Project integration</span><b>Capture → reconstruction → source-level trace views</b></div><p class="figure-note">The project combines and extends these foundations.</p>

<!--
Timing: 45 seconds · 03:00–03:45.
Progressive reveals: 2. Advance with the normal presentation controls.

OpenOCD reaches the target; LLDB/LLVM understand the program and provide debugging/analysis facilities. OpenCSD is the existing trace-protocol decoder. Expand these roles without introducing API names. [Click 2] The contribution is the acquisition, reconstruction and debugger integration around them. Vendor environments offer their own trace workflows; detailed positioning is in the backup, not a market-wide claim that no alternative supports trace. Transition: explicitly identify what I wrote or extended.
Sources: dissertation chap_01.tex, software survey; chap_04.tex, Division of Work.
-->

---
title: "Work carried out"
clicks: 2
class: defense-slide
---

<div class="kicker">Objectives and Technical Approach</div>
<h1>Work carried out</h1>

<div class="contribution-matrix"><div class="column-label">Existing foundation</div><div></div><div class="column-label">My implementation</div><div class="foundation-name">OpenOCD</div><div class="contribution-arrow">→</div><div class="contribution-result extended"><b>Trace-source and buffer drivers</b><small>Configuration and capture extraction</small></div><div class="foundation-name">OpenCSD</div><div class="contribution-arrow">→</div><div class="contribution-result built" v-click="1"><b>Trace-processing pipeline</b><small>Decoder setup, reconstruction and source attribution</small></div><div class="foundation-name">LLDB / LLVM</div><div class="contribution-arrow">→</div><div class="contribution-result built" v-click="2"><b>C++ debugger integration</b><small>Session coordination, providers and trace delivery</small></div><div class="foundation-name">VS Code</div><div class="contribution-arrow">→</div><div class="contribution-result built" v-click="2"><b>Debugger extension and trace views</b><small>Instruction history, function history and source navigation</small></div></div><div class="ownership-legend"><span class="reused">Reused</span><span class="extended">Extended</span><span class="built">Implemented in this project</span></div><p class="figure-note">Deliverables: application note · trace prototype · integrated debugger</p>

<!--
Timing: 45 seconds · 03:45–04:30.
Progressive reveals: 2. Advance with the normal presentation controls.

Keep this slide explicit and personal: “These are the components I implemented.” The trace drivers extend OpenOCD. The processing pipeline configures the existing decoder, retains its events, reconstructs instructions and attributes them to source. The C++ debugger coordinates these parts with conventional debugging; the VS Code extension presents the result. Yellow identifies newly implemented project components; the blue block with the yellow edge identifies an extension of an existing system. Explain that the libraries themselves were reused. The three deliverables are documentation, the trace proof of concept and the integrated debugger. Transition: explain the trace information those components operate on.
Sources: dissertation chap_04.tex, Scope of Deliverables and Implementation; engine trace module structure. Ownership follows the user's clarification.
-->

---
title: "Instruction trace: a compact execution record"
clicks: 2
class: defense-slide
---

<div class="kicker">Objectives and Technical Approach</div>
<h1>Instruction trace: a compact execution record</h1>

<div class="principle-grid"><div><div class="figure-label">Program</div><pre class="technical-code">if (condition)&#10;    A();&#10;else&#10;    B();&#10;continue_execution();</pre></div><div class="decision-record" v-click="1"><DefenseIcon name="trace" /><b>Recorded decision</b><span>Branch taken</span></div><div v-click="2"><div class="figure-label">Reconstructed path</div><div class="path-stack"><span>Evaluate condition</span><i>↓</i><span class="selected-path">A()</span><i>↓</i><span>Continue</span></div></div></div><p class="figure-note">The program provides the instructions; trace supplies the control-flow decisions.</p>

<!--
Timing: 50 seconds · 04:30–05:20.
Progressive reveals: 2. Advance with the normal presentation controls.

Use this language-level example before introducing ETM vocabulary. The compiled program already contains the instructions and possible direct paths. [Click 1] Trace records the decision needed to select a path. [Click 2] Combine that decision with the matching program image to reconstruct execution. This is illustrative pseudocode, not the literal ETM wire encoding. Instruction trace is not a record of all variable values. Transition: how can software obtain that record independently of a particular board?
Source: dissertation chap_02.tex, Trace Elements and Packet Encoding.
-->

---
title: "Device-independent capture architecture"
clicks: 2
class: defense-slide
---

<div class="kicker">Objectives and Technical Approach</div>
<h1>Device-independent capture architecture</h1>

<div class="generic-target"><div class="target-boundary-label">Target trace capabilities</div><div class="hardware-chain"><div class="diagram-node reused"><DefenseIcon name="chip" /><b>Processor</b></div><span class="diagram-arrow" aria-hidden="true">→</span><div class="diagram-node reused"><DefenseIcon name="trace" /><b>Trace source</b></div><span class="diagram-arrow" aria-hidden="true">→</span><div class="optional-router">Routing<br><small>if required</small></div><span class="diagram-arrow" aria-hidden="true">→</span><div class="diagram-node reused"><DefenseIcon name="layers" /><b>On-chip sink</b></div></div></div>
<div class="host-capture" v-click="1"><div class="config-input"><DefenseIcon name="file" /><span>Device configuration<small>Addresses and capabilities</small></span></div><div class="host-driver extended">Acquisition drivers</div><div class="transport-link">↔ Debug connection ↔</div><div class="probe-node"><DefenseIcon name="probe" /><span>Debug probe</span></div><span class="sink-link">↑<small>Read capture</small></span></div><p class="figure-note"><span v-click="2">Implemented acquisition: ETMv4 instruction trace + on-chip sink. Device details enter through configuration.</span></p>

<!--
Timing: 40 seconds · 05:20–06:00.
Progressive reveals: 2. Advance with the normal presentation controls.

The diagram is generic: a processor produces execution information through a trace source, optional routing and a sink. Routing can include a funnel, but it is not a mandatory stage in every topology. [Click 1] The host configures and reads supported components over the debug connection; component addresses and capabilities come from configuration. [Click 2] Distinguish architecture from implemented scope: acquisition currently targets ETMv4 and an on-chip sink, rather than claiming every architecture or protocol is supported. The Cortex-M7 development board is introduced only as validation equipment later. Transition: place acquisition inside the complete debugger.
Sources: dissertation chap_04.tex, external-system providers and CoreSight drivers; user clarification of device-independent project scope.
-->

---
title: "Debugger architecture and implementation"
clicks: 2
transition: fade-out
class: defense-slide
---

<div class="kicker">Design and Implementation</div>
<h1>Debugger architecture and implementation</h1>

<div class="system-architecture"><div class="system-ui built"><DefenseIcon name="screen" /><span><b>VS Code extension</b><small>Trace views and source navigation</small></span></div><div class="system-link">↕ Debug Adapter Protocol</div><div class="engine-boundary"><span class="boundary-title">C++ debugger engine</span><div class="engine-coordination built" v-click="1">Session coordination · requests · events</div><div class="engine-providers"><div class="reused">LLDB / LLVM<small>Debugging and program context</small></div><div class="built" v-click="2">Trace pipeline<small>Reconstruction and source attribution</small><span class="embedded-foundation">OpenCSD · reused decoder</span></div><div class="extended">OpenOCD<small>Extended acquisition drivers</small></div></div></div><div class="system-link">↕ Debug probe / target interface</div><div class="generic-device"><DefenseIcon name="chip" /><span>Configured target</span></div></div><div class="ownership-legend"><span class="reused">Reused</span><span class="extended">Extended</span><span class="built">Implemented in this project</span></div>

<!--
Timing: 50 seconds · 06:00–06:50.
Progressive reveals: 2. Advance with the normal presentation controls.

Show the complete responsibility map. The extension communicates through DAP, the Debug Adapter Protocol: define it as the message interface between IDE and debugger. [Click 1] The C++ engine coordinates session state and backend events. [Click 2] Highlight your trace pipeline and the reused OpenCSD decoder inside it. LLDB supplies conventional debugging and program context; OpenOCD supplies target access and the acquisition extensions. Their direct and GDB-remote connections are implementation detail for backup discussion. The generic target is intentionally not a named development board.
Sources: dissertation chap_04.tex, Debugger Architecture and Division of Work; engine/docs/architecture. Legend distinguishes reuse, extension and implementation.
-->

---
title: "Trace-processing pipeline"
clicks: 2
class: defense-slide
---

<div class="kicker">Design and Implementation</div>
<h1>Trace-processing pipeline</h1>

<PipelineMap /><div class="pipeline-inputs"><div v-click="1"><DefenseIcon name="file" /><span><b>Matching ELF + debug information</b><small>Program instructions and source locations</small></span><i>↑ Decode · reconstruct · attribute</i></div><div v-click="2"><DefenseIcon name="trace" /><span><b>Trace configuration</b><small>Encoding settings used during capture</small></span><i>↑ Decode</i></div></div><div class="ownership-legend"><span class="reused">Reused</span><span class="extended">Extended</span><span class="built">Implemented in this project</span></div>

<!--
Timing: 40 seconds · 06:50–07:30.
Progressive reveals: 2. Advance with the normal presentation controls.

Follow the data through five responsibilities, using the icons as a locator for the next slides. Acquisition yields bytes, OpenCSD decoding yields elements, reconstruction expands executed instruction ranges, attribution produces source blocks, and presentation delivers the views. [Click 1] ELF is the compiled program file; its debug information maps machine addresses to source. [Click 2] Decoder configuration must match the captured stream. OpenCSD is reused, while the pipeline around it is your work. Transition: show how a debug session triggers acquisition.
Source: dissertation chap_04.tex, Instruction Trace Pipeline.
-->

---
title: "Capture lifecycle"
clicks: 2
class: defense-slide
---

<div class="kicker">Design and Implementation</div>
<h1>Capture lifecycle</h1>

<PipelineMap :active="0" compact /><svg class="lifecycle-diagram" viewBox="0 0 1100 340" role="img" aria-label="Debugger and target sequence: configure, arm, run, halt, read capture and rearm"><defs><marker id="life-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10Z" fill="#03234B"/></marker></defs><rect x="110" y="8" width="230" height="48" class="svg-built"/><text x="225" y="39" text-anchor="middle">Debugger engine</text><rect x="760" y="8" width="230" height="48" class="svg-reused"/><text x="875" y="39" text-anchor="middle">Configured target</text><path d="M225 56V330M875 56V330" class="lifeline"/><g><path d="M225 95H875" class="sequence-arrow"/><text x="550" y="84" text-anchor="middle">Configure source and sink</text><path d="M225 145H875" class="sequence-arrow"/><text x="550" y="134" text-anchor="middle">Arm capture</text></g><g v-click="1"><path d="M225 195H875" class="sequence-arrow"/><text x="550" y="184" text-anchor="middle">Resume execution</text><rect x="854" y="195" width="42" height="50" fill="#FFD200"/><text x="920" y="225">Record trace</text><path d="M875 245H225" class="sequence-arrow"/><text x="550" y="234" text-anchor="middle">Target halted</text></g><g v-click="2"><path d="M875 295H225" class="sequence-arrow"/><text x="550" y="284" text-anchor="middle">Extract buffered capture</text><text x="225" y="330" text-anchor="middle" class="svg-small">Process → rearm</text></g></svg><p class="figure-note">My work: trace-component drivers and coordination with debugger run state.</p>

<!--
Timing: 55 seconds · 07:30–08:25.
Progressive reveals: 2. Advance with the normal presentation controls.

Explain the sequence in three phases. Configure and arm while halted. [Click 1] Resume lets the hardware record execution; a subsequent halt bounds a capture. [Click 2] Stop/flush the trace path as needed, drain the sink and process the data before the next interval. The source and sink require sequencing; this is part of the implementation, not a user script left outside the debugger. This capture path provides bounded intervals, not continuous unlimited recording.
Source: dissertation chap_04.tex, Trace Lifecycle and Trace Extraction.
-->

---
title: "Decoding: bytes, packets and elements"
clicks: 2
class: defense-slide
---

<div class="kicker">Design and Implementation</div>
<h1>Decoding: bytes, packets and elements</h1>

<PipelineMap :active="1" compact /><div class="decode-example"><div><div class="figure-label">Captured bytes</div><pre class="technical-code">00 05 00 00&#10;04 83 0a 12&#10;00 08 00 f7&#10;…</pre></div><span class="diagram-arrow">→</span><div v-click="1"><div class="figure-label">Decoded packets</div><pre class="technical-code">TRACE_ON&#10;ADDRESS 0x08001214&#10;ATOM E</pre></div><span class="diagram-arrow" v-click="2">→</span><div v-click="2"><div class="figure-label">Generic elements</div><pre class="technical-code">TRACE_ON&#10;RANGE [0x08001214,&#10;       0x0800121c)&#10;3 instructions</pre></div></div><div class="decode-ownership"><span class="reused">OpenCSD: protocol decoding</span><span class="built" v-click="2">My work: configure · provide image · retain events</span></div>

<!--
Timing: 50 seconds · 08:25–09:15.
Progressive reveals: 2. Advance with the normal presentation controls.

This excerpt is based on the report's saved-capture figure. Packet names are shortened for readability; the byte excerpt is not presented as a complete standalone decodable stream. [Click 1] Bytes are de-formatted and parsed into packets. ETM means Embedded Trace Macrocell; an atom reports a control-flow outcome. [Click 2] The decoder interprets packets against the program and produces generic elements, including instruction ranges. The end address here is exclusive. OpenCSD performs protocol decoding; your code supplies the image and actual settings and retains the resulting events. Transition: expand what an atom means using the report's loop.
Source: dissertation/img/gen_fig/fig_bytes_to_elements.tex and chap_04.tex, Decoding.
-->

---
title: "Worked example: ETM atoms and execution"
clicks: 4
class: defense-slide
---

<div class="kicker">Design and Implementation</div>
<h1>Worked example: ETM atoms and execution</h1>

<EtmExample />

<!--
Timing: 65 seconds · 09:15–10:20.
Progressive reveals: 4. Advance with the normal presentation controls.

Use the four-instruction loop in the report. r3 starts at four. ldr loads a value, add accumulates it, subs decrements the counter, and bne branches back if the result is nonzero. An E atom says this branch is taken; N says it is not taken. [Clicks 1–3] Each E accounts for another pass through the four instructions. [Click 4] N means the final branch falls through; that evaluated branch still appears in the instruction listing. Four atoms plus the start address and exact program imply sixteen listed instructions. This is a pedagogical element sequence, not raw wire bytes: synchronization is omitted, and one packet can carry multiple atoms. Do not generalize E/N wording to every predicated instruction. Transition: show how your code expands these ranges and attaches source context.
Source: dissertation/img/gen_fig/fig_trace_elements_loop.tex; chap_02.tex, Trace Elements. Final instruction-list behavior is documented by validation Finding 11.
-->

---
title: "Instruction reconstruction and source correlation"
clicks: 2
class: defense-slide
---

<div class="kicker">Design and Implementation</div>
<h1>Instruction reconstruction and source correlation</h1>

<PipelineMap :active="2" compact /><div class="reconstruction-grid"><div><div class="figure-label">Implemented range expansion · pseudocode</div><pre class="technical-code">for each instruction_range:&#10;  address = range.start&#10;  while address &lt; range.end:&#10;    instruction = image.lookup(address)&#10;    emit(instruction, source(address))&#10;    address += instruction.size</pre></div><div v-click="1"><div class="figure-label">Representations of the same execution</div><div class="representation-stack"><div><b>Instructions</b><code>load → add → decrement → branch</code></div><i>↓ source information</i><div><b>Line blocks</b><code>sum += *p++ &nbsp; / &nbsp; --remaining</code></div><i>↓ chronological grouping</i><div><b>Function blocks</b><span>Consecutive execution in the same function</span></div></div></div></div><p class="figure-note"><span v-click="2">Variable instruction sizes · repeated iterations retained · complete inline context</span></p>

<!--
Timing: 50 seconds · 10:20–11:10.
Progressive reveals: 2. Advance with the normal presentation controls.

The pseudocode mirrors the instruction-range transform, omitting checks and model bookkeeping for readability. The real implementation uses precomputed instruction information and stops when a required address cannot be resolved. Increment by instruction size; Thumb instructions are not all the same length. [Click 1] Resolve source context and form line/function representations. The source expressions shown are a teaching equivalent of the previous loop, not a claim about that example's real DWARF records. [Click 2] Keep repeated chronology and full inline source chains. Distinguish your range expansion and grouping from the reused decoder and LLVM facilities.
Sources: trace_transform/reconstructed_instruction_transform.hpp, function_block_transform.hpp; dissertation chap_04.tex, Static Program Analysis and Reconstruction.
-->

---
title: "Trace continuity and offline analysis"
clicks: 2
class: defense-slide
---

<div class="kicker">Design and Implementation</div>
<h1>Trace continuity and offline analysis</h1>

<div class="continuity-figure"><div class="figure-label">Execution history</div><div class="known-interval"><span>Call</span><span>Loop</span><span>Return</span></div><div class="trace-gap" v-click="1"><DefenseIcon name="gap" /><b>Explicit gap</b></div><div class="known-interval" v-click="1"><span>Resume</span><span>Call</span><span>Return</span></div></div><div class="offline-figure" v-click="2"><div class="figure-label">Replay without a connected target</div><div class="diagram-sequence"><div class="diagram-node reused"><DefenseIcon name="trace" /><b>Saved trace</b><small>+ capture configuration</small></div><span class="diagram-arrow" aria-hidden="true">→</span><div class="diagram-node reused"><DefenseIcon name="file" /><b>Matching ELF</b><small>+ debug information</small></div><span class="diagram-arrow" aria-hidden="true">→</span><div class="diagram-node built"><DefenseIcon name="layers" /><b>Same processing pipeline</b></div></div></div>

<!--
Timing: 55 seconds · 11:10–12:05.
Progressive reveals: 2. Advance with the normal presentation controls.

The trace model carries discontinuities rather than joining separated intervals into invented history. [Click 1] A gap can arise from synchronization loss or encoder overflow; a wrapped circular sink limits how far the retained prefix reaches and is a distinct phenomenon. [Click 2] The same pipeline runs offline given saved trace, matching ELF and capture configuration. This is enabled by separation of acquisition from interpretation, not a second decoder implementation. The saved capture becomes a repeatable regression input as well as a diagnostic artifact.
Sources: dissertation chap_04.tex, Trace Data Model and Lifecycle; validation Findings 12 and 14; offline replay CLI.
-->

---
title: "Implemented trace views in VS Code"
clicks: 2
class: defense-slide
---

<div class="kicker">Design and Implementation</div>
<h1>Implemented trace views in VS Code</h1>

<div class="implementation-views"><figure class="instruction-view"><div class="figure-label">Instruction history</div><div class="screenshot-window"><img src="/evidence/instruction-trace.png" alt="Implemented instruction trace view: address, disassembly and source location"><div class="source-highlight" v-click="2"></div></div><figcaption><span>Address</span><span>Instruction</span><span v-click="2">↗ Source location</span></figcaption></figure><figure class="function-view" v-click="1"><div class="figure-label">Function history</div><div class="screenshot-window"><img src="/evidence/function-trace.png" alt="Implemented function trace view showing chronological function blocks"></div><figcaption>Chronological function blocks</figcaption></figure></div><p class="figure-note">My work: trace requests/events, incremental view updates and source navigation.</p>

<!--
Timing: 55 seconds · 12:05–13:00.
Progressive reveals: 2. Advance with the normal presentation controls.

These are actual implemented UI screenshots from the report, showing a startup capture. Do not imply this is the later fault recording. Introduce the instruction fields. [Click 1] Show the alternate function-oriented view. [Click 2] Highlight the source reference and explain that selecting it navigates to the source. The views receive incremental results through DAP extensions. Existing breakpoint, variable, memory and peripheral facilities support the same debug session but are not the focus of this slide. Transition: use the implemented trace capability for an actual fault investigation.
Sources: report debugger_screenshots; chap_04.tex, Frontend and Protocol Extensions.
-->

---
title: "Case study: a corrupted function pointer"
clicks: 2
transition: fade-out
class: defense-slide
---

<div class="kicker">Demonstration</div>
<h1>Case study: a corrupted function pointer</h1>

<div class="fault-investigation"><div class="fault-outcome"><DefenseIcon name="snapshot" /><b>Indirect call fails</b><code>record.on_complete();</code><span>Invalid execution state</span></div><div class="fault-cause" v-click="1"><div class="figure-label">Adjacent fields in memory</div><div class="buffer-diagram"><div>buffer[0 … 7]</div><div class="corrupted-field">on_complete</div></div><p class="overwrite-arrow">buffer[8] ↑</p><pre class="technical-code">for (int i = 0; i &lt;= len; i++)&#10;  record.buffer[i] = data[i % len];</pre><small>len = 8 · one write beyond the buffer</small></div></div><p class="figure-note"><span v-click="2">Investigation: connect the earlier copy operation to the failing call.</span></p>

<!--
Timing: 30 seconds · 13:00–13:30.
Progressive reveals: 2. Advance with the normal presentation controls.

Start at the observed invalid-state fault. [Click 1] Introduce the controlled source defect: an inclusive loop bound writes a ninth byte into an eight-byte array, corrupting an adjacent function pointer. The selected payload clears the pointer's Thumb-state bit on the validation target. [Click 2] The purpose is to demonstrate how execution evidence connects the copy loop to the later call. The source defect is controlled; this is not a rare-fault detection claim. Break at fault-handler entry so its spin loop cannot overwrite the useful trace.
Source: validation Finding 07 and its fault firmware. Workload codes are intentionally omitted from the audience-facing material.
-->

---
title: "Trace-assisted fault investigation"
clicks: 2
class: defense-slide
---

<div class="kicker">Demonstration</div>
<h1>Trace-assisted fault investigation</h1>

<DemoWalkthrough />

<!--
Timing: 90 seconds · 13:30–15:00.
Progressive reveals: 2. Advance with the normal presentation controls.

Allow ninety seconds. The real recording remains pending hardware availability, as agreed with Youssef. The current interactive walkthrough uses saved experimental evidence. Click 1 advances from failure state to the recorded sequence; click 2 advances to source diagnosis. Use the on-screen tabs or normal presentation controls. Explain: Process executes the copy loop, returns, then the indirect call faults. The trace records the sequence, not the overwritten byte value. Keep raw register bit interpretation brief; it is supporting detail, not a prerequisite for understanding the demonstration.
Sources: validation Finding 07, saved fault-state JSON and fault firmware. See DEMO.md for the future recording integration.
-->

---
title: "Validation setup and method"
clicks: 2
transition: fade-out
class: defense-slide
---

<div class="kicker">Validation and Results</div>
<h1>Validation setup and method</h1>

<div class="validation-layout"><div class="validation-bench"><div class="figure-label">Experimental resources</div><DefenseIcon name="chip" /><h2>NUCLEO-H7S3L8</h2><p>STM32H7S3L8 · Cortex-M7</p><div class="bench-spec"><span>Onboard ST-LINK</span><span>2 KiB trace buffer</span></div><small>One validation platform</small></div><div class="validation-methods"><div><DefenseIcon name="file" /><span><b>Saved captures</b><small>Repeatable regression inputs</small></span></div><div v-click="1"><DefenseIcon name="check" /><span><b>Independent single-step reference</b><small>Instruction-address comparison</small></span></div><div v-click="2"><DefenseIcon name="route" /><span><b>Control-flow checks</b><small>Branches, calls, returns and boundaries</small></span></div></div></div>

<!--
Timing: 50 seconds · 15:00–15:50.
Progressive reveals: 2. Advance with the normal presentation controls.

Only now name the test equipment. These are experimental resources, not mandatory parts of the architecture: NUCLEO-H7S3L8, its STM32H7S3L8 Cortex-M7 processor, onboard STLINK-V3EC and two-kilobyte on-chip buffer. Separate supported design interfaces from hardware configurations actually validated. Describe calls, branches, interrupt-driven code, DMA and the controlled fault in plain language, without internal workload codes. [Click 1] The single-step reference independently records PC addresses. [Click 2] Structural checks extend coverage over many captures, with explicit gap and exception boundaries.
Sources: dissertation chap_06.tex, Hardware Environment; validation Findings 02, 11 and 12.
-->

---
title: "Execution-order validation"
clicks: 2
class: defense-slide
---

<div class="kicker">Validation and Results</div>
<h1>Execution-order validation</h1>

<div class="oracle-comparison"><div class="oracle-row"><b>Single-step reference</b><code>0x80003d4</code><code>0x80003d6</code><code>0x80003dc</code><code>0x80003de</code><span>…</span></div><div class="agreement-links" v-click="1"><span>↕</span><span>↕</span><span>↕</span><span>↕</span></div><div class="oracle-row" v-click="1"><b>Trace reconstruction</b><code>0x80003d4</code><code>0x80003d6</code><code>0x80003dc</code><code>0x80003de</code><span>…</span></div></div><div class="research-results" v-click="2"><div><strong>400 / 400</strong><span>Exact address matches · 100%</span><small>One interrupt-free reference interval</small></div><div><strong>229,424</strong><span>Transitions structurally checked</span><small>61 recorded captures</small></div></div>

<!--
Timing: 60 seconds · 15:50–16:50.
Progressive reveals: 2. Advance with the normal presentation controls.

The displayed addresses are the first four entries of the saved independent single-step sequence. [Click 1] The reconstructed sequence agrees. [Click 2] The complete interval contains 400 addresses, all exact matches. This validates instruction order for that interval; do not imply universal accuracy on every possible input. The separate structural coverage count is 229,424 transitions across 61 captures. It is complementary evidence, not a second accuracy percentage. Explain gaps/exception exclusions and indirect-target limitations only if asked. Present the final behavior without the implementation's fix history.
Sources: validation/captures/w1_baseline/shadow_trace/shadow_addresses.json; Findings 11 and 12.
-->

---
title: "Capture capacity on the validation platform"
clicks: 1
class: defense-slide
---

<div class="kicker">Validation and Results</div>
<h1>Capture capacity on the validation platform</h1>

<div class="chart-heading"><span>Retained execution by workload type</span><b>2 KiB buffer</b></div><img class="history-chart" src="/evidence/history-capacity.svg" alt="Mean and observed range of instructions retained in six workload classes, approximately 1.6 to 8.7 thousand overall"><p class="figure-note"><span v-click="1">Retention depends on control-flow density; the relevant execution must remain inside the window.</span></p>

<!--
Timing: 70 seconds · 16:50–18:00.
Progressive reveals: 1. Advance with the normal presentation controls.

This is a measured property of the validation platform, not a hard-coded capacity or limit of the software architecture. The bars show means, and whiskers show observed minima/maxima across six captures per workload. Counts are derived from measured instruction density times 2048 usable bytes. [Click 1] Call-heavy execution consumes more trace per retained instruction than a compact loop. The observed total span is approximately 1.6 to 8.7 thousand instructions. Do not convert to a universal wall-clock duration. Explain why the fault investigation halts promptly.
Sources: validation/analysis/density_summary.csv and Findings 10/17; chart generator in the presentation.
-->

---
title: "Limitations and further work"
clicks: 2
transition: fade-out
class: defense-slide
---

<div class="kicker">Limitations and Conclusion</div>
<h1>Limitations and further work</h1>

<div class="further-work"><div class="column-label">Current scope</div><div></div><div class="column-label">Extension</div><div class="limit-item"><DefenseIcon name="layers" />Bounded on-chip capture</div><span class="diagram-arrow">→</span><div class="extension-item">Region-based trace filtering</div><div class="limit-item"><DefenseIcon name="file" />Configured component topology</div><span class="diagram-arrow">→</span><div class="extension-item" v-click="1">Automatic component discovery</div><div class="limit-item"><DefenseIcon name="test" />Focused hardware validation</div><span class="diagram-arrow">→</span><div class="extension-item" v-click="1">Additional target configurations</div><div class="limit-item"><DefenseIcon name="clock" />Offline timing analysis</div><span class="diagram-arrow">→</span><div class="extension-item" v-click="2">Integrated profiling views</div></div>

<!--
Timing: 60 seconds · 18:00–19:00.
Progressive reveals: 2. Advance with the normal presentation controls.

Discuss engineering boundaries directly. The buffer belongs to the target, and filtering could use that capacity more selectively. Topology configuration could be replaced by discovery where available. The architecture is device-independent, but empirical validation should cover more configurations. Timing decoding and one cross-validated ISR-span experiment already work; fuller frontend profiling is an extension, not a claim that timing is blocked. Do not imply these extensions have already been implemented.
Sources: validation Findings 14 and 17; configured target/provider architecture.
-->

---
title: "Contributions and conclusion"
clicks: 2
class: defense-slide defense-conclusion
---

<div class="kicker">Limitations and Conclusion</div>
<h1>Contributions and conclusion</h1>

<div class="conclusion-artifacts"><div class="diagram-node extended"><DefenseIcon name="probe" /><b>Acquisition drivers</b><small>Configure and extract trace</small></div><div class="diagram-node built" v-click="1"><DefenseIcon name="code" /><b>Trace-processing pipeline</b><small>Reconstruct and attribute execution</small></div><div class="diagram-node built" v-click="2"><DefenseIcon name="screen" /><b>Integrated debugger</b><small>Inspect trace inside VS Code</small></div></div><div class="conclusion-evidence"><span><DefenseIcon name="file" />Documented procedure</span><span><DefenseIcon name="check" />Experimental validation</span></div><p class="closing-thanks">Thank you for your attention.</p>

<!--
Timing: 60 seconds · 19:00–20:00.
Progressive reveals: 2. Advance with the normal presentation controls.

Conclude with the actual engineering deliverables: trace acquisition extensions, a processing pipeline and the debugger/frontend integration. The application note records how to reproduce the workflow. The experiments provide execution-order and hardware-capture evidence, with their scope stated in the results. Do not end with a marketing slogan. Invite questions and stop on this slide; the following seven slides are supporting technical material. The timing allocation remains twenty minutes including the demonstration.
-->

---
title: "Detailed Tool Comparison"
clicks: 0
class: backup-slide
---

<div class="kicker">Backup 1 · Backup</div>
<h1>Detailed Tool Comparison</h1>

<table class="matrix compact"><thead><tr><th>Tool family</th><th>Relevant strength</th><th>Project positioning</th></tr></thead><tbody><tr><td>IAR / Keil / SEGGER</td><td>Integrated debug and trace workflows</td><td>Probe, target and environment support are product-specific</td></tr><tr><td>OpenOCD</td><td>Debug transport and target access</td><td>Extended here for ETMv4 / TMC configuration and extraction</td></tr><tr><td>pyOCD</td><td>Cortex-M debug and instrumentation support</td><td>Distinct from this instruction-trace acquisition chain</td></tr><tr><td>OpenCSD</td><td>Trace-protocol decoder</td><td>Reused with capture, firmware context and result presentation</td></tr><tr><td>emTrailer</td><td>On-chip capture through the onboard probe</td><td>Instruction history integrated into a VS Code debugging session</td></tr></tbody></table><p class="caption">Scope: the project’s STM32 / M-profile survey. Capabilities vary by product version, probe and target.</p>

<!--
Backup only — outside the 20-minute presentation.

Use only if asked about positioning. Explain the evaluated workflow rather than making categorical product claims. Report references: chap_01.tex, State of the Art; bibliography keys iar_etm_trace, openocd, pyocd, opencsd, perf_cs_etm, frankentrace and ninja. This deck reproduces the project's research scope and does not claim a new market survey.
-->

---
title: "CoreSight Configuration and Capture Lifecycle"
clicks: 0
class: backup-slide
---

<div class="kicker">Backup 2 · Backup</div>
<h1>CoreSight Configuration and Capture Lifecycle</h1>

<div class="flow"><div class="node"><b>ETMv4 source</b><small>Source · encode execution</small></div><div class="arrow">→</div><div class="node"><b>Optional routing</b><small>Route active source</small></div><div class="arrow">→</div><div class="node hot"><b>TMC</b><small>Retain the byte stream</small></div></div><div class="cols"><div class="card"><span class="label">Setup while halted</span><h2>Prepare the trace path</h2><p>Read configuration, unlock/configure components, prepare sink and source.</p></div><div class="card dark"><span class="label">At a capture boundary</span><h2>Stop, flush and extract</h2><p>Drain the sink, process the capture, then prepare the next interval.</p></div></div><div class="takeaway">TMC wrap truncates retained history. ETMv4 source encoder overflow can create an in-stream discontinuity.</div>

<!--
Backup only — outside the 20-minute presentation.

Component locations are device-specific and supplied through configuration. The ordering must honor each component's programming model. The target's ETM, funnel and TMC form the selected trace path; the external trace port is unused. Do not conflate the sink's circular-buffer wrap with the encoder's internal FIFO overflow. A reset clears session history because it begins another program run.
Sources: dissertation chap_04.tex, CoreSight Drivers and Trace Extraction; validation Finding 12, gap and overflow discussion.
-->

---
title: "ETM reconstruction: supplementary detail"
clicks: 0
class: backup-slide
---

<div class="kicker">Backup 3 · Backup</div>
<h1>ETM reconstruction: supplementary detail</h1>

<div class="flow"><div class="node"><b>Trace records</b><small>Ranges + event context</small></div><div class="arrow">→</div><div class="node"><b>Instructions</b><small>Ordered address sequence</small></div><div class="arrow">→</div><div class="node"><b>Source blocks</b><small>Lines + inline chains</small></div><div class="arrow">→</div><div class="node hot"><b>Views</b><small>Instructions + function history</small></div></div><table class="matrix compact"><tbody><tr><td>Conditional branch</td><td>Keep the listing entry even when control flow falls through</td></tr><tr><td>Exceptions and gaps</td><td>Carry boundary positions; do not infer continuity across missing trace</td></tr><tr><td>Inlining</td><td>Resolve and compare the complete source-location chain</td></tr><tr><td>Repeated execution</td><td>Group consecutive context without deduplicating chronology</td></tr></tbody></table>

<!--
Backup only — outside the 20-minute presentation.

The instruction listing and grouped function representation are related views, not identical row-for-row arrays. The branch outcome flag follows decoder semantics and should not be read as a universal CPU-retirement predicate. Gap/exception indices must be interpreted in their own model rather than assumed to equal arbitrary list positions. Source attribution requires suitable firmware debug information.
Sources: Finding 11, final instruction listing behavior; Finding 12, ExceptionEvent model; dissertation chap_04.tex, Trace Data Model and transforms.
-->

---
title: "Engine Concurrency and DAP Extensions"
clicks: 0
class: backup-slide
---

<div class="kicker">Backup 4 · Backup</div>
<h1>Engine Concurrency and DAP Extensions</h1>

<div class="cols"><div class="stack"><div class="row">DAP transport and dispatch<small>Frame messages, route requests, emit responses</small></div><div class="row">Domain components and providers<small>Coordinate debugger state and backend access</small></div><div class="row">Events from backend workers<small>Deliver state and trace updates to the frontend</small></div></div><div class="card dark"><span class="label">Trace interface</span><h2>Requests + events</h2><p>Control and query trace state.<br>Deliver trace increments asynchronously.</p><p class="small">Standard debug operations coexist with custom embedded views and trace events.</p></div></div><div class="takeaway">The frontend consumes structured results; target access and reconstruction stay in the engine.</div>

<!--
Backup only — outside the 20-minute presentation.

For deeper discussion, refer to engine/docs/architecture/03-request-sequence.md and 04-event-dataflow.md. The domain event path joins backend worker activity with frontend delivery. DAP stdout carries framed protocol messages; diagnostics belong on stderr. Avoid saying every DAP handler is independent of LLDB: the actual architecture permits some handlers to use LLDB APIs. The overview diagram is a responsibility view, not a claim of complete type isolation.
Sources: engine/docs/architecture/00-overview.md, 03-request-sequence.md, 04-event-dataflow.md and dissertation chap_04.tex, Protocol Extensions.
-->

---
title: "Validation Methods and Coverage"
clicks: 0
class: backup-slide
---

<div class="kicker">Backup 5 · Backup</div>
<h1>Validation Methods and Coverage</h1>

<table class="matrix"><thead><tr><th>Check</th><th>Method</th><th>Interpretation</th></tr></thead><tbody><tr><td>Independent oracle</td><td>400 LLDB-driven instruction steps compared with a hardware capture</td><td>400 / 400 exact address matches in the reference program</td></tr><tr><td>Control-flow analysis</td><td>229,424 transitions across 61 recorded captures</td><td>Broad structural coverage, complementary to the oracle</td></tr><tr><td>Boundary handling</td><td>Separate gaps and exception boundaries</td><td>Missing intervals are not adjacency checks</td></tr><tr><td>Fault case</td><td>Controlled out-of-bounds write</td><td>Execution history connects the copy loop to the failing call</td></tr></tbody></table>

<!--
Backup only — outside the 20-minute presentation.

Present current behavior and scope, not the development history. The oracle uses an independently observed PC sequence, but is limited to one short, interrupt-free workload interval. The structural check accepts dynamic indirect destinations and uses a simplified visible call stack; it does not independently prove every branch destination was observed on hardware. The reported transition count is campaign coverage, not an aggregate accuracy claim. No outdated decoder-limitation explanation belongs in this discussion.
Sources: Findings 07, 11 and 12, methods and coverage.
-->

---
title: "Timing Reconstruction Results"
clicks: 0
class: backup-slide
---

<div class="kicker">Backup 6 · Backup</div>
<h1>Timing Reconstruction Results</h1>

<p class="subtitle">One measured ISR span, independently compared with the DWT cycle counter.</p><table class="matrix"><thead><tr><th>Repeat</th><th>Trace-derived cycles</th><th>DWT cycles</th><th>Difference</th></tr></thead><tbody><tr><td>1</td><td>316</td><td>324</td><td>8 cycles · 2.5%</td></tr><tr><td>2</td><td>316</td><td>324</td><td>8 cycles · 2.5%</td></tr><tr><td>3</td><td>314</td><td>322</td><td>8 cycles · 2.5%</td></tr></tbody></table><div class="takeaway">Timestamp and cycle-count information is decoded and retained for offline analysis.</div>

<!--
Backup only — outside the 20-minute presentation.

DWT means Data Watchpoint and Trace; here its CYCCNT register provides an independent cycle-counter delta. The experiment brackets a span inside TIM6_IRQHandler with source breakpoints, ensuring both methods cover the same interval. The fixed eight-cycle difference is reported, not treated as random noise or a proven cause. The 2.5% figure is rounded. This demonstrates one bounded timing use case over three repeats, not a complete profiling product or all-workload timing accuracy.
Source: Finding 14, Phase 9.5 methodology and final three-repeat results. Present working timing capability without the earlier investigation history.
-->

---
title: "Fault Investigation and Cache Visibility"
clicks: 0
class: backup-slide
---

<div class="kicker">Backup 7 · Backup</div>
<h1>Fault Investigation and Cache Visibility</h1>

<div class="cols"><div class="card"><span class="label">Observed with D-cache enabled</span><h2>Debug-port read: 0x00000000</h2><p>The core had already used a different pointer value from its write-back cache.</p></div><div class="card dark"><span class="label">Cache-disabled comparison</span><h2>Debug-port read: 0x08000300</h2><p>The deliberately corrupted pointer becomes visible in SRAM.</p></div></div><div class="flow"><div class="node"><b>Known-good assignment</b><small>on_complete = SafeAction</small></div><div class="arrow">→</div><div class="node"><b>Copy loop</b><small>One-byte overwrite</small></div><div class="arrow">→</div><div class="node hot"><b>Indirect call</b><small>Invalid-state fault</small></div></div><div class="takeaway">Combine fault state, source code and execution order; instruction trace does not expose the written value.</div>

<!--
Backup only — outside the 20-minute presentation.

The saved halt JSON reports CFSR 0x00020000, HFSR 0x40000000 and a debug-port pointer read of zero. The documented A/B experiment with cache disabled observes 0x08000300. Debug-port SRAM reads can miss dirty write-back cache data. This is a property of the target access path, not an instruction-trace data-value observation. The case study and cache A/B comparison each have the documented narrow scope; avoid generalizing to every debugger memory read.
Source: Finding 07 and w7_fault/state_at_halt.json.
-->
