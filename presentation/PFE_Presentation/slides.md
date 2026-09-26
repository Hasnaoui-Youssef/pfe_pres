---
theme: default
title: "Design & Implementation of a Debugger with Instruction Trace Capabilities"
author: "Youssef HASNAOUI"
info: |
  PFE Defense · STMicroelectronics · 26 September 2026
highlighter: shiki
drawings:
  persist: false
transition: fade
mdc: true
fonts:
  sans: Arial
  mono: monospace
---

<div class="cover-grid">
  <div class="cover-logos" aria-label="STMicroelectronics, ENICarthage and University of Carthage">
    <div class="cover-logo cover-logo-carthage"><img src="/assets/cover-university-carthage.png" alt="University of Carthage" /></div>
    <div class="cover-logo cover-logo-enicar"><img src="/assets/cover-enicarthage-transparent.png" alt="ENICarthage" /></div>
    <div class="cover-logo cover-logo-st"><img src="/assets/cover-stmicroelectronics-white.png" alt="STMicroelectronics" /></div>
  </div>
  <div class="cover-copy">
    <div class="eyebrow"><span class="eyebrow-mark"></span> PFE DEFENSE · STMICROELECTRONICS</div>
    <h1 class="cover-title">Design &amp; Implementation<br>of a Debugger with<br><span>Instruction Trace Capabilities</span></h1>
    <p class="cover-name">Youssef <b>HASNAOUI</b></p>
    <p class="cover-date">26 September 2026</p>
    <div class="cover-supervisors">
      <span>Academic supervisor <b>Mrs. Faten SALEM</b></span>
      <span>Professional supervisor <b>Mr. Mohamed HAMROUNI</b></span>
    </div>
    <div class="cover-jury">
      <span>Committee chair <b>Mrs. Samia HACHMI</b></span>
      <span>Reporter <b>Mrs. Nourelhouda BEN YOUSEF</b></span>
    </div>
    <div class="cover-representative"><span>STMicroelectronics representative <b>Mr. Chiheb MANAA</b></span></div>
  </div>
</div>

---
layout: default
class: agenda-slide
---

# Agenda

<div class="agenda-grid">
  <div class="agenda-item"><span>01</span><b>Project Context</b></div>
  <div class="agenda-item"><span>02</span><b>Theoretical Concepts</b></div>
  <div class="agenda-item"><span>03</span><b>Forking OpenOCD</b></div>
  <div class="agenda-item"><span>04</span><b>Proposed Instruction Trace Pipeline</b></div>
  <div class="agenda-item"><span>05</span><b>Debug Engine Implementation</b></div>
  <div class="agenda-item"><span>06</span><b>Validation &amp; Results</b></div>
  <div class="agenda-item"><span>07</span><b>Demo</b></div>
  <div class="agenda-item"><span>08</span><b>Conclusion &amp; Perspective</b></div>
</div>

---
layout: section
section: "01 / PROJECT CONTEXT"
---

# Project Context

---
layout: default
---

<div class="section-kicker">PROJECT CONTEXT · HOST ORGANIZATION</div>


<div class="stat-grid">
  <div class="stat-card stat-feature"><span class="stat-icon"><carbon-currency-dollar /></span><strong>$11.8B</strong><label>FY2025 revenue</label></div>
  <div class="stat-card"><span class="stat-icon"><carbon-group /></span><strong>50,000+</strong><label>employees worldwide</label></div>
  <div class="stat-card"><span class="stat-icon"><carbon-chemistry /></span><strong>9,500+</strong><label>people in R&amp;D</label></div>
  <div class="stat-card"><span class="stat-icon"><carbon-earth /></span><strong>200,000+</strong><label>customers globally</label></div>
  <div class="stat-card"><span class="stat-icon"><carbon-industry /></span><strong>14</strong><label>main manufacturing sites</label></div>
</div>

<div class="market-row"><span>WHERE ST’S TECHNOLOGIES GO</span><b>Automotive</b><b>Industrial</b><b>Personal electronics</b></div>

---
layout: default
---

<div class="section-kicker">PROJECT CONTEXT · ST TUNIS</div>


<div class="two-col tunis-layout">
  <div>
    <p class="large-copy">The Tunis site is an R&amp;D location where software, tools and product support meet.</p>
    <ul class="clean-list">
      <li><i class="list-dot cyan"></i><span><b>Embedded software</b></span></li>
      <li><i class="list-dot yellow"></i><span><b>Tools</b></span></li>
      <li class="internship-team"><i class="list-dot pink"></i><span><b>Application &amp; Product Support Team</b><small>Customer technical support, documentation maintenance and support for new products during development.</small><em>MY INTERNSHIP TEAM</em></span></li>
    </ul>
  </div>
  <img class="tunis-photo" src="/assets/stmicroelectronics-tunis-site.jpg" />
</div>

---
layout: default
---

<div class="section-kicker">PROJECT CONTEXT</div>

<div class="context-buildup">
  <div><span>01</span><p>This project was hosted within <b>STMicroelectronics</b>.</p></div>
  <div><span>02</span><p>It was carried out within the <b>Application &amp; Product Support team</b>, which provides technical support to customers.</p></div>
  <div><span>03</span><p>The team needs the utmost visibility into microcontroller behavior, yet instruction trace is rarely available in its debugging workflow. <b>That gap motivates this project.</b></p></div>
</div>

---
layout: default
---

<div class="section-kicker">STATE OF THE ART</div>

<table class="state-art-table vendor-compare-table">
  <thead><tr><th>Debugger</th><th>Supports instruction trace</th><th>Requires dedicated hardware probe</th><th>Offline decoding</th></tr></thead>
  <tbody>
    <tr><th>IAR</th><td><span class="vendor-mark yes">✓</span></td><td><span class="vendor-mark yes">✓</span></td><td><span class="vendor-mark no">✗</span></td></tr>
    <tr><th>Keil</th><td><span class="vendor-mark yes">✓</span></td><td><span class="vendor-mark yes">✓</span></td><td><span class="vendor-mark no">✗</span></td></tr>
    <tr><th>SEGGER</th><td><span class="vendor-mark yes">✓</span></td><td><span class="vendor-mark yes">✓</span></td><td><span class="vendor-mark no">✗</span></td></tr>
    <tr><th>OpenOCD</th><td><span class="vendor-mark no">✗</span></td><td><span class="vendor-mark no">✗</span></td><td><span class="vendor-mark no">✗</span></td></tr>
    <tr><th>pyOCD</th><td><span class="vendor-mark no">✗</span></td><td><span class="vendor-mark no">✗</span></td><td><span class="vendor-mark no">✗</span></td></tr>
  </tbody>
</table>

---
layout: default
---

<div class="section-kicker">PROBLEM STATEMENT</div>

<ul class="feedback-bullets problem-bullets">
  <li>Vendor IDEs tie instruction trace to proprietary probes.</li>
  <li>Trace analysis stays within the debug session.</li>
  <li>Open-source debuggers lack an end-to-end instruction-trace workflow.</li>
</ul>

---
layout: default
---

<div class="section-kicker">PROPOSED SOLUTION</div>

<ul class="feedback-bullets">
  <li>Control trace components through OpenOCD.</li>
  <li>Decode captured trace offline.</li>
  <li>Develop a debugger with integrated trace analysis.</li>
</ul>

---
layout: default
---

<div class="section-kicker">OBJECTIVES</div>

<ul class="feedback-bullets">
  <li>Implement trace-component drivers in OpenOCD.</li>
  <li>Capture on-chip trace without a dedicated trace probe.</li>
  <li>Build an offline trace-analysis pipeline.</li>
  <li>Deliver a debugger that integrates the instruction-trace analysis pipeline.</li>
</ul>

---
layout: section
section: "02 / THEORETICAL CONCEPTS"
---

# Theoretical Concepts

---
layout: default
---

<div class="section-kicker">THEORETICAL CONTEXT · INSTRUCTION TRACE</div>

<div class="trace-definition">
  <p class="trace-definition-statement"><b>Instruction trace</b> is a hardware-generated record of a processor’s execution path as a program runs.</p>
  <div class="trace-definition-grid">
    <div><p>Captures changes such as branches and exceptions.</p></div>
    <div><p>Preserves the ordered sequence of the processor’s execution path.</p></div>
    <div><p>Can timestamp events to show when they occurred.</p></div>
  </div>
</div>

---
layout: default
---

<div class="section-kicker">THEORETICAL CONTEXT · DEBUG METHODS COMPARED</div>

<table class="trace-compare-table">
  <thead><tr><th>Method</th><th>What you observe</th><th>Side effects</th></tr></thead>
  <tbody>
    <tr><th>Halt &amp; inspect</th><td>Register and memory state at a breakpoint</td><td>Stops program execution</td></tr>
    <tr><th>Instrumentation</th><td>Events added to the program by the developer</td><td>Increased firmware size and I/O contention</td></tr>
    <tr class="trace-row-highlight"><th>Instruction trace</th><td>Time-ordered sequence of executed instructions</td><td>None</td></tr>
  </tbody>
</table>

---
layout: default
---

<div class="section-kicker">TRACE COMPONENT · EMBEDDED TRACE MACROCELL</div>

<div class="etm-summary">
  <p class="etm-lead">An Embedded Trace Macrocell (ETM) is hardware that monitors a processor’s execution and produces an instruction-trace stream.</p>
  <ul class="etm-points">
    <li>Observes control flow as the processor executes.</li>
    <li>Emits trace information for changes such as branches and exceptions.</li>
    <li>Sends the trace stream to trace infrastructure for storage or output.</li>
  </ul>
</div>

---
layout: default
class: trace-access-slide
---

<div class="section-kicker">THEORETICAL CONTEXT · ACCESSING TRACE DATA</div>

<table class="trace-route-table">
  <thead><tr><th>On-chip capture</th><th>Off-chip capture</th></tr></thead>
  <tbody>
    <tr>
      <td><ul class="trace-route-list"><li>No additional trace hardware</li><li>No trace-pin I/O bandwidth limit</li></ul></td>
      <td><ul class="trace-route-list"><li>Virtually unlimited trace storage</li></ul></td>
    </tr>
  </tbody>
</table>

---
layout: default
---

<div class="section-kicker">TRACE COMPONENT · TRACE MEMORY CONTROLLER</div>

<div class="etm-summary">
  <p class="etm-lead">A Trace Memory Controller (TMC) is a trace sink that stores incoming trace data for later retrieval.</p>
  <ul class="etm-points">
    <li>Receives routed trace data from trace sources.</li>
    <li>Stores trace in an on-chip buffer or system memory.</li>
    <li>Exposes captured trace data through a memory-mapped interface.</li>
  </ul>
</div>

---
layout: section
section: "03 / FORKING OPENOCD"
---

# Forking OpenOCD

---
layout: default
---

<div class="section-kicker">DEBUG ACCESS · OPENOCD</div>

<p class="openocd-intro">OpenOCD is open-source software that manages communication with a debug target and makes its capabilities available to other software. It provides three interfaces for controlling the target:</p>

<ul class="openocd-interface-list">
  <li><b>API</b></li>
  <li><b>Script interface</b></li>
  <li><b>Remote protocol interface</b></li>
</ul>

---
layout: default
class: embed-openocd-slide
---

<div class="section-kicker">EMBEDDING OPENOCD</div>

### Default · Standalone OpenOCD

```mermaid {theme: 'base', scale: 0.9}
flowchart LR
  OPENOCD["OpenOCD"] <-->|RSP / TCL| DEBUGGER["Debugger"]
  classDef server fill:#03234b,stroke:#3cb4e6,color:#ffffff,stroke-width:3px
  classDef client fill:#e8f3f8,stroke:#3cb4e6,color:#03234b,stroke-width:2px
  class OPENOCD server
  class DEBUGGER client
```

<p class="openocd-mode-note">OpenOCD runs separately and is controlled by a client through RSP or TCL.</p>

### This project · Embedded OpenOCD

```mermaid {theme: 'base', scale: 0.82}
flowchart LR
  subgraph ENGINE["Debug Engine"]
    direction LR
    CORE["Engine Core"] <-->|Direct API calls| OPENOCD["OpenOCD"]
  end
  classDef engine fill:#03234b,stroke:#03234b,color:#ffffff,stroke-width:3px
  classDef runtime fill:#fbe6f1,stroke:#e6007e,color:#03234b,stroke-width:2px
  class CORE engine
  class OPENOCD runtime
  style ENGINE fill:#f3f8fc,stroke:#3cb4e6,stroke-width:2px
```

<p class="openocd-mode-note">OpenOCD is embedded in the Debug Engine and controlled through direct API calls.</p>

---
layout: default
---

<div class="section-kicker">TRACE SOURCE · ETMv4 MODULE</div>

<div class="single-content module-content">
  <p class="narrative-copy">The ETMv4 extension adds named-component discovery, staged configuration and explicit enable/disable control to OpenOCD. Its register access is performed through the target’s debug access port.</p>
  <div class="module-capabilities">
    <div><span class="cap-dot pink"></span><b>Discover</b><small>Identify ETMv4 instances and read architecture capabilities.</small></div>
    <div><span class="cap-dot cyan"></span><b>Configure</b><small>Stage trace ID and source options, then commit them to the component.</small></div>
    <div><span class="cap-dot yellow"></span><b>Control</b><small>Keep trace requested across run-state events; apply configuration and enable generation when the target resumes.</small></div>
  </div>
</div>

---
layout: default
---

<div class="section-kicker">TRACE SINK · TMC MODULE</div>

<div class="tmc-implementation">
  <p class="narrative-copy">The TMC module exposes capture configuration and output selection. On a halt event, it checks the capture state, drains the selected buffer mode, and hands the result to its consumer.</p>
  <div class="tmc-module-layout">
    <div class="tmc-module-stage"><span class="stage-num">01</span><b>Configure</b><small>Choose a supported TMC mode and its buffer options.</small></div>
    <div class="tmc-module-stage"><span class="stage-num">02</span><b>Extract on halt</b><small>Read captured words through the TMC FIFO data register after capture stops.</small></div>
    <div class="tmc-module-stage"><span class="stage-num">03</span><b>Deliver capture</b><small>Send a frame-aligned sync barrier, then the captured bytes.</small></div>
  </div>
  <div class="callback-band"><span><carbon-data-share /></span><p><b>The callback carries the capture</b><small>Consumers can write it to a file, stream it over the trace service, or pass it to the decoding pipeline.</small></p><div class="callback-dest"><b>FILE</b><span>·</span><b>SOCKET</b><span>·</span><b>DECODER</b></div></div>
</div>

---
layout: section
section: "04 / PROPOSED INSTRUCTION TRACE PIPELINE"
---

# Proposed Instruction Trace Pipeline

---
layout: default
class: capture-pipeline-slide
---

<div class="section-kicker">01 · GENERATION &amp; CAPTURE</div>

<div class="capture-flow generation-flow">
  <div class="capture-node core-node">
    <small class="capture-overline">PROCESSOR</small>
    <b>M-profile core</b>
    <span>Executes the program</span>
  </div>
  <div class="capture-link"><span class="capture-arrow-svg"><Arrow x1="0" y1="50" x2="64" y2="50" color="#3cb4e6" width="3" /></span></div>
  <div class="capture-node etm-node">
    <small class="capture-overline">TRACE SOURCE</small>
    <b>ETMv4</b>
    <span>Generates instruction trace</span>
    <em>GENERATION ENABLED</em>
  </div>
  <div class="capture-link"><span class="capture-arrow-svg"><Arrow x1="0" y1="50" x2="64" y2="50" color="#e6007e" width="3" /></span></div>
  <div class="capture-node infra-node">
    <b>Trace Infrastructure</b>
    <span>Routes the stream to the sink</span>
  </div>
  <div class="capture-link"><span class="capture-arrow-svg"><Arrow x1="0" y1="50" x2="64" y2="50" color="#3cb4e6" width="3" /></span></div>
  <div class="capture-node tmc-node">
    <small class="capture-overline">TRACE SINK</small>
    <b>TMC</b>
    <span>Formats and captures in its buffer</span>
    <em>CAPTURE ACTIVE</em>
  </div>
</div>

<p class="pipeline-narrative capture-summary">We enable ETM and TMC, configure both components, then run the program to generate and capture trace.</p>

---
layout: default
---

<div class="section-kicker">02 · TRACE EXTRACTION</div>

<div class="mcu-trace-extraction">
  <div class="mcu-trace-boundary">
    <b class="mcu-trace-title">MCU</b>
    <div class="mcu-trace-components">
      <div class="trace-component fifo-component">
        <div class="fifo-cells"><i></i><i></i><i></i><i></i><i></i><i></i></div>
        <b>FIFO</b>
      </div>
      <span class="mcu-component-link"></span>
      <div class="trace-component tmc-component"><b>TMC</b></div>
    </div>
  </div>
  <div class="host-access-arrow"><Arrow x1="186" y1="40" x2="18" y2="40" color="#71869a" width="3" /></div>
  <div class="host-computer"><carbon-laptop /><b>Host computer</b></div>
</div>

<ul class="extract-steps">
  <li>Trace data is accessible through the RRD (RAM Read Data) register.</li>
  <li>Repeated RRD reads retrieve successive FIFO data until the FIFO is empty.</li>
</ul>

---
layout: default
---

<div class="section-kicker">03 · TRACE DECODING</div>

<p class="pipeline-narrative">We are able to decode the saved capture without needing the target to be connected. OpenCSD is configured with the trace protocol, the ETM register values and the formatter settings and produces higher-level trace elements.</p>
<div class="decode-equation">
  <div class="equation-card"><span class="equation-icon"><carbon-document /></span><b>Captured Trace bytes</b></div><span class="plus-sign">+</span>
  <div class="equation-card"><span class="equation-icon"><carbon-settings /></span><b>Firmware Image & ETM Identification Registers</b></div><span class="equation-arrow"><Arrow x1="2" y1="13" x2="29" y2="13" color="#ffd200" width="2" /></span>
  <div class="equation-card equation-result"><span class="equation-icon"><carbon-list /></span><b>Trace elements</b></div>
</div>

---
layout: default
---

<div class="section-kicker">04 · SOURCE CORRELATION · RECONSTRUCTION</div>

<p class="pipeline-narrative">The decoder reports ranges of executed addresses rather than a row for every instruction. The program image supplies the instruction bytes, so disassembly expands each range into its exact instruction sequence while preserving control-flow order.</p>
<div class="correlation-flow">
  <div class="correlation-input"><span>DECODED Element</span><b>INSTRUNCTION_RANGE(0x100, 0x108)</b></div>
  <div class="correlation-arrow"><Arrow x1="2" y1="13" x2="34" y2="13" color="#ffd200" width="2" /></div>
  <div class="correlation-middle"><span>ELF LOAD SEGMENTS</span><div class="code-fragment"><code>push {r4, lr}<br>mov r4, r0<br>cmp r0, #1<br>bne.n 0x080012AA</code></div></div>
  <div class="correlation-arrow"><Arrow x1="2" y1="13" x2="34" y2="13" color="#ffd200" width="2" /></div>
  <div class="correlation-output"><span>ORDERED INSTRUCTION STREAM</span><b>4 reconstructed instructions</b><small>chronological · instruction by instruction</small></div>
</div>

---
layout: default
---

<div class="section-kicker">05 · SOURCE CORRELATION · DWARF</div>

<p class="pipeline-narrative">Once the instruction sequence is reconstructed, DWARF debug information maps each address to its source location and inline-call chain. The result connects machine-level execution back to the code the developer recognizes.</p>
<div class="source-map-layout">
  <div class="instruction-stream"><small>RECONSTRUCTED FLOW</small><div><b>0x080012A0</b><code>push {r4, lr}</code><span></span></div><div><b>0x080012A2</b><code>mov r4, r0</code><span></span></div><div><b>0x080012A4</b><code>cmp r0, #1</code><span></span></div><div><b>0x080012A6</b><code>bne.n 0x080012AA</code><span></span></div></div>
  <div class="source-map-arrow">DWARF<br>LOOKUP<br><span><Arrow x1="4" y1="13" x2="58" y2="13" color="#ffd200" width="2" /></span></div>
  <div class="source-mapped"><small>SOURCE + INLINE CHAIN</small><div class="source-highlight"><b>motor.c : 42</b><span>if (ready) {</span></div><div><b>motor.c : 43</b><span>enable_motor();</span></div><div><b>control.c : 18</b><span>set_output(true);</span></div><div class="inline-tag">inline frames kept</div></div>
</div>

---
layout: default
---

<div class="section-kicker">06 · SOURCE CORRELATION · USEFUL VIEWS</div>

<p class="pipeline-narrative">The same chronological record can be explored at three levels of detail: individual instructions, source-line blocks, or function blocks.</p>
<div class="trace-views">
  <div class="trace-view-card"><span class="view-mark instruction-mark">I</span><div><b>Instruction view</b><small>One row per reconstructed instruction.</small></div><div class="view-preview"><span>0x080012A0</span><code>push {r4, lr}</code><em>motor.c:42</em></div></div>
  <div class="view-view-connector">GROUP</div>
  <div class="trace-view-card"><span class="view-mark line-mark">L</span><div><b>Line blocks</b><small>Adjacent instructions mapped to the same source context.</small></div><div class="view-preview"><span>12 instr</span><code>motor.c:42</code><em>3 occurrences</em></div></div>
  <div class="view-view-connector">GROUP</div>
  <div class="trace-view-card"><span class="view-mark function-mark">F</span><div><b>Function blocks</b><small>Consecutive line blocks grouped by function.</small></div><div class="view-preview"><span>4 functions</span><code>motor_control()</code><em>chronological</em></div></div>
</div>

---
layout: default
---

<div class="section-kicker">IMPLEMENTATION SNAPSHOT · INSTRUCTION VIEW</div>

<figure class="ui-snapshot-single">
  <img src="/assets/instruction_trace_ui.png" alt="Instruction trace view showing addresses, disassembly and correlated source locations" />
  <figcaption><b>Trace instructions</b><span>Addresses, disassembly and correlated source locations.</span></figcaption>
</figure>

---
layout: default
---

<div class="section-kicker">IMPLEMENTATION SNAPSHOT · FUNCTION VIEW</div>

<figure class="ui-snapshot-single">
  <img src="/assets/function_trace_ui.png" alt="Function trace view showing chronological function blocks" />
  <figcaption><b>Trace by function</b><span>Chronological function blocks for a higher-level view.</span></figcaption>
</figure>

---
layout: section
section: "05 / DEBUG ENGINE IMPLEMENTATION"
---

# Debug Engine Implementation

---
layout: default
class: debug-architecture-slide
---

<div class="section-kicker">ARCHITECTURE</div>

<div class="debug-architecture">
  <div class="architecture-panel dap-panel">
    <b class="architecture-panel-title">DAP Interface</b>
    <div class="dap-flow">
      <div class="architecture-node">Transport</div>
      <span class="architecture-arrow"></span>
      <div class="architecture-node architecture-node-primary">Orchestrator</div>
      <span class="architecture-arrow"></span>
      <div class="architecture-node">Request Queue</div>
      <span class="architecture-arrow"></span>
      <div class="architecture-node">Request Handlers</div>
    </div>
    <div class="translator-link"><span>Session Translator</span></div>
  </div>

  <div class="context-connector"><span>requests / events</span><i></i></div>

  <div class="architecture-panel debug-context-panel">
    <b class="architecture-panel-title">Debug Context</b>
    <div class="debug-context-content">
      <div class="manager-stack-group">
        <div class="manager-stack" aria-label="Domain Managers">
          <span class="manager-layer layer-back"></span>
          <span class="manager-layer layer-three"></span>
          <span class="manager-layer layer-two"></span>
          <span class="manager-layer layer-one"></span>
          <span class="manager-stack-face">Domain<br>Managers</span>
        </div>
      </div>
      <div class="context-services">
        <b>Context Services</b>
        <div class="context-service-row">
          <span>EventBus</span><span>LLDB Provider</span><span>OpenOCD Provider</span>
        </div>
      </div>
    </div>
  </div>
</div>

---
layout: default
class: domain-managers-slide
---

<div class="section-kicker">DOMAIN MANAGERS</div>

<p class="domain-managers-narrative">Each request is routed to the manager responsible for that debugger domain. The manager coordinates provider work and publishes relevant session updates through the EventBus.</p>

```mermaid {theme: 'base', scale: 0.8}
%%{init: {'flowchart': {'nodeSpacing': 48, 'rankSpacing': 52, 'curve': 'basis'}}}%%
flowchart LR
  SESSION["DAP Session"] --> HANDLER["Request Handler"]
  HANDLER --> MANAGER["Domain Manager"]
  MANAGER --> PROVIDERS["Providers"]
  MANAGER --> BUS["EventBus"]

  classDef interface fill:#e8f3f8,stroke:#3cb4e6,color:#03234b,stroke-width:2px
  classDef manager fill:#03234b,stroke:#03234b,color:#ffffff,stroke-width:2px
  classDef updates fill:#fbe6f1,stroke:#e6007e,color:#03234b,stroke-width:2px
  class SESSION,HANDLER,PROVIDERS interface
  class MANAGER manager
  class BUS updates
```

<div class="domain-manager-example">
  <b>TraceManager</b>
  <ul>
    <li>Prepares the trace session</li>
    <li>Coordinates capture through OpenOCD</li>
    <li>Feeds captured data into analysis</li>
  </ul>
</div>

---
layout: default
class: provider-comparison-slide
---

<div class="section-kicker">PROVIDERS</div>

<div class="provider-table-wrap">
  <table class="provider-table">
    <thead><tr><th>Provider</th><th>Responsibilities</th></tr></thead>
    <tbody>
      <tr><td><b>LLDB</b></td><td><ul><li>Execution control</li><li>Symbols</li><li>Registers</li><li>Memory</li><li>Breakpoints</li></ul></td></tr>
      <tr><td><b>OpenOCD</b></td><td><ul><li>Target access</li><li>Direct TCL commands</li><li>Trace component control</li></ul></td></tr>
      <tr><td><b>Device</b></td><td><ul><li>Device identity</li><li>Memory map</li><li>Peripheral descriptions</li></ul></td></tr>
      <tr><td><b>Trace</b></td><td><ul><li>ETM decode</li><li>Instruction reconstruction</li><li>Source mapping</li></ul></td></tr>
    </tbody>
  </table>
</div>

---
layout: default
class: trace-start-sequence-slide
---

<div class="section-kicker">TRACE START · REQUEST FLOW</div>

```mermaid {theme: 'base', scale: 0.60}
%%{init: {'sequence': {'actorMargin': 150, 'actorFontSize': 22, 'actorFontWeight': 600, 'messageFontSize': 24, 'messageFontWeight': 500, 'messageMargin': 6, 'diagramMarginY': 8, 'mirrorActors': false}}}%%
sequenceDiagram
  participant Session as DAP Session
  participant Handler as TraceEnable Handler
  participant TM as TraceManager
  participant Provider as OpenOCD Provider

  Session->>Handler: trailerTraceEnable
  Handler->>TM: Enable()
  TM->>TM: Prepare decode session
  TM->>TM: Clear prior trace state
  TM->>Provider: Enable TMC
  Provider->>Provider: Enable capture
  Provider-->>TM: Success
  TM->>Provider: Enable ETMv4
  Provider->>Provider: Enable trace generation
  Provider-->>TM: Success
  TM-->>Handler: TraceStatusResponse
  Handler-->>Session: DAP response
```

---
layout: default
---

<div class="section-kicker">THREAD MODEL</div>


<div class="thread-lanes">
  <div class="thread-lane"><span class="thread-title">READER</span><div class="thread-task">Read framed request</div><span class="lane-arrow"><Arrow x1="2" y1="12" x2="26" y2="12" color="#ffd200" width="2" /></span><div class="thread-task">Queue dispatch</div></div>
  <div class="thread-lane"><span class="thread-title">DISPATCH</span><div class="thread-task">Validate request</div><span class="lane-arrow"><Arrow x1="2" y1="12" x2="26" y2="12" color="#ffd200" width="2" /></span><div class="thread-task">Call handler</div></div>
  <div class="thread-lane"><span class="thread-title">WORKERS</span><div class="thread-task">Trace / watch work</div><span class="lane-arrow"><Arrow x1="2" y1="12" x2="26" y2="12" color="#ffd200" width="2" /></span><div class="thread-task">Publish event</div></div>
</div>

---
layout: default
class: event-bus-slide
---

<div class="section-kicker">EVENT BUS</div>

```mermaid {theme: 'base', scale: 0.68}
%%{init: {'flowchart': {'nodeSpacing': 38, 'rankSpacing': 58, 'curve': 'basis'}}}%%
flowchart LR
  subgraph SOURCES["Event sources"]
    direction TB
    LLDB["LLDB"]
    TRACE["Trace worker"]
    MEMORY["Memory watches"]
    TARGET["Target lifecycle"]
  end
  LLDB --> BUS["Event Bus"]
  TRACE --> BUS
  MEMORY --> BUS
  TARGET --> BUS
  BUS --> SESSION["Session translator"]
  SESSION --> FRONTEND["DAP frontend"]

  classDef source fill:#e8f3f8,stroke:#3cb4e6,color:#03234b,stroke-width:2px
  classDef bus fill:#03234b,stroke:#ffd200,color:#ffffff,stroke-width:3px
  classDef output fill:#fbe6f1,stroke:#e6007e,color:#03234b,stroke-width:2px
  class LLDB,TRACE,MEMORY,TARGET source
  class BUS bus
  class SESSION,FRONTEND output
```

<div class="event-bus-example">
  <div>
    <p>The Event Bus is a publish-subscribe registry that allows the debugger to support asynchronous events.</p>
    <ul>
      <li>Components publish domain events to the Event Bus.</li>
      <li>The debugger session subscribes to receive those events.</li>
      <li>It translates them into frontend notifications, without requiring a request.</li>
    </ul>
  </div>
</div>

---
layout: section
section: "06 / VALIDATION & RESULTS"
---

# Validation &amp; Results

---
layout: default
---

<div class="section-kicker">TEST PLATFORM · BOARD &amp; PROBE</div>

<div class="board-probe-layout">
  <div class="board-probe-photo"><img src="/assets/nucleo_h7s3.jpg" alt="NUCLEO-H7S3L8 development board" /><span class="photo-label">NUCLEO-H7S3L8</span></div>
  <div class="board-probe-details">
    <p class="large-copy">A single board provides the target and the debug connection used for hardware validation.</p>
    <div class="platform-fact"><span><carbon-chip /></span><div><b>Target board</b><small>NUCLEO-H7S3L8 · STM32H7S3L8</small></div></div>
    <div class="platform-fact"><span><carbon-usb /></span><div><b>On-board ST-LINK</b><small>Connects to the host over USB and to the MCU over SWD.</small></div></div>
    <div class="platform-trace-note"><b>No external trace probe</b><small>The captured trace is read through the ordinary debug connection.</small></div>
  </div>
</div>

---
layout: default
class: trace-infrastructure-slide
---

<div class="section-kicker">TEST PLATFORM · TRACE INFRASTRUCTURE</div>


<div class="infrastructure-image"><img src="/assets/fig1002_debug_infrastructure.png" alt="STM32H7RS on-chip trace infrastructure" /></div>
<div v-drag="[513, 238, 117, 184, 0]" class="infra-highlight"></div>

---
layout: default
class: validation-workloads-slide
---

<div class="section-kicker">VALIDATION · WORKLOADS</div>

<p class="workload-intro">Six firmware images exercise different execution patterns on the target.</p>

<div class="validation-workloads">
  <div><b>W1</b><strong>Nested decisions</strong></div>
  <div><b>W2</b><strong>Function-call chain</strong></div>
  <div><b>W3</b><strong>Branch-heavy sorting</strong></div>
  <div><b>W4</b><strong>Timer interrupt</strong></div>
  <div><b>W5</b><strong>DMA transfer + idle wait</strong></div>
  <div><b>W6</b><strong>Dense branch loop</strong></div>
</div>

---
layout: default
class: validation-layout-slide
---

<div class="section-kicker">VALIDATION · SOFTWARE LAYOUT</div>

```mermaid {theme: 'base', scale: 0.95}
flowchart LR
  subgraph CAMPAIGN["PYTHON CAMPAIGN"]
    direction LR
    FLASH["Flash workload image"] --> SESSION["Launch debug session"] --> CONFIG["Configure trace output"] --> RUN["Enable · run · pause"] --> SAVE["Save capture + run records"]
  end
  SAVE --> REPLAY["Offline trace replay"]
  classDef stage fill:#e8f3f8,stroke:#3cb4e6,stroke-width:2px,color:#03234b,font-size:20px
  classDef artifact fill:#03234b,stroke:#ffd200,stroke-width:2px,color:#ffffff,font-size:20px
  class FLASH,SESSION,CONFIG,RUN stage
  class SAVE,REPLAY artifact
```

<ul class="validation-campaign-points">
  <li>The Python runner drives the project debugger over DAP and configures ETF output through OpenOCD.</li>
  <li>Each run saves the raw capture, trace events, status and run metadata.</li>
  <li>Workload, duration, trace options and repeat count are selected per campaign.</li>
</ul>

---
layout: default
---

<div class="section-kicker">RECONSTRUCTION VALIDATION</div>

<div class="oracle-validation">
  <div class="oracle-lanes">
    <div class="oracle-lane"><b>LLDB single-step reference</b><div class="oracle-sequence"><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i></div></div>
    <div class="oracle-match"><strong>400 / 400</strong><span>addresses match</span></div>
    <div class="oracle-lane oracle-hardware"><b>Hardware trace reconstruction</b><div class="oracle-sequence"><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i></div></div>
  </div>
  <p class="oracle-scope">Same starting breakpoint · one interrupt-free workload</p>
</div>

---
layout: default
---

<div class="section-kicker">VALIDATION · CAPTURE CHARACTERIZATION</div>

<div class="density-validation">
  <div class="density-axis"><span class="density-axis-title">Mean reconstructed instructions in one full buffer</span><div class="density-ticks"><i>0</i><i>1,750</i><i>3,500</i><i>5,250</i><i>7,000</i></div></div>
  <div class="density-row"><b>W2 <span>Calls</span></b><div class="density-track"><i style="--density:24.4%"></i></div><strong>1,710</strong></div>
  <div class="density-row"><b>W5 <span>DMA</span></b><div class="density-track"><i style="--density:32.3%"></i></div><strong>2,261</strong></div>
  <div class="density-row"><b>W4 <span>Interrupt</span></b><div class="density-track"><i style="--density:41.7%"></i></div><strong>2,922</strong></div>
  <div class="density-row"><b>W1 <span>Baseline</span></b><div class="density-track"><i style="--density:65.4%"></i></div><strong>4,579</strong></div>
  <div class="density-row"><b>W3 <span>Branches</span></b><div class="density-track"><i style="--density:74.6%"></i></div><strong>5,222</strong></div>
  <div class="density-row"><b>W6 <span>Dense loop</span></b><div class="density-track"><i style="--density:88.5%"></i></div><strong>6,193</strong></div>
</div>

---
layout: default
---

<div class="section-kicker">VALIDATION · PIPELINE OPTIMIZATION</div>

<div class="optimization-validation">
  <div class="optimization-flow">
    <section class="optimization-lane optimization-before"><h2>Before</h2><div class="optimization-nodes"><b>Trace records</b><i></i><b>Reconstruct instructions</b><i></i><b>Build function blocks<small>reconstructed again</small></b></div></section>
    <section class="optimization-lane optimization-after"><h2>After</h2><div class="optimization-nodes"><b>Reconstructed instructions</b><i></i><b>Build function blocks<small>reuse existing instructions</small></b></div></section>
  </div>
  <div class="optimization-result"><strong>54–61%</strong><span>less time in function-block transformation</span><b>Instruction, block and gap counts remained unchanged.</b></div>
  <div class="optimization-method">Measured on three workloads using identical captures · offline host processing</div>
</div>

---
layout: section
section: "07 / DEMO"
---

# Demo

---
layout: default
class: demo-slide
---

<div class="demo-video-frame">
  <SlidevVideo controls class="demo-video">
    <source src="/assets/debugger_demo.mp4" type="video/mp4" />
    Your browser cannot play this video.
  </SlidevVideo>
</div>

---
layout: section
section: "08 / CONCLUSION & PERSPECTIVE"
---

# Conclusion &amp; Perspective

---
layout: default
---

<div class="section-kicker">CONCLUSION</div>

<ul class="conclusion-points">
  <li>Extended OpenOCD with ETMv4 and TMC modules for trace configuration and capture.</li>
  <li>Built an offline instruction-trace decoding and source-correlation pipeline.</li>
  <li>Integrated trace control and analysis into the Debug Engine.</li>
  <li>Exposed trace capture and analysis through a unified debugger workflow.</li>
  <li>Kept the implementation device-agnostic, with hardware-specific details confined to target configuration.</li>
</ul>

---
layout: default
---

<div class="section-kicker">PERSPECTIVE</div>


<div class="perspective-grid">
  <div class="perspective-card"><span class="perspective-icon"><carbon-network-4 /></span><small>01</small><b>Multi-core tracing</b><p>Correlate execution across processors and reason about cross-core causality.</p><div class="perspective-lines"></div></div>
  <div class="perspective-card"><span class="perspective-icon"><carbon-filter /></span><small>02</small><b>Trace filtering</b><p>Capture only selected address ranges, events or execution contexts.</p><div class="perspective-lines"></div></div>
  <div class="perspective-card"><span class="perspective-icon"><carbon-chart-line /></span><small>03</small><b>Profiling</b><p>Turn execution history into time, call-graph and hot-path analysis.</p><div class="perspective-lines"></div></div>
</div>

---
layout: center
class: thank-you-slide
---

<div class="thank-you-mark"><span></span><span></span><span></span></div>
<div class="section-kicker">THANK YOU</div>

<p class="thank-you-name">Youssef HASNAOUI <i>·</i> 26 September 2026</p>
<div class="thank-you-footer">Design &amp; Implementation of a Debugger with <b>Instruction Trace Capabilities</b></div>
