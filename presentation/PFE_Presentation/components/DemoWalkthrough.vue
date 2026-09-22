<script setup>
import { ref, watch, unref } from 'vue'
import { useSlideContext } from '@slidev/client'
const props = defineProps({ videoSrc: { type: String, default: '' } })
const { $clicks, $nav, $page } = useSlideContext()
const active = ref(0)
const failed = ref(false)
const steps = ['Failure state', 'Execution path', 'Source diagnosis']
watch($clicks, n => { active.value = Math.min(2, Math.max(0, n)) }, { immediate: true })
function selectStep(index) {
  active.value = index
  unref($nav).go(unref($page), index)
}
</script>

<template>
  <div class="demo-panel academic-demo">
    <template v-if="props.videoSrc && !failed">
      <video :src="props.videoSrc" controls preload="metadata" playsinline aria-label="Recorded fault investigation" @error="failed = true">
        Your browser cannot play this recording.
      </video>
      <button class="fallback-button" @click="failed = true">Show evidence walkthrough</button>
    </template>
    <template v-else>
      <div class="demo-tabs" role="tablist" aria-label="Fault investigation steps">
        <button v-for="(step, index) in steps" :id="`demo-tab-${index}`" :key="step" role="tab" :aria-selected="active === index" aria-controls="demo-evidence" :class="{ active: active === index }" @click="selectStep(index)"><span>{{ index + 1 }}</span>{{ step }}</button>
      </div>
      <Transition name="evidence" mode="out-in">
        <div id="demo-evidence" :key="active" class="demo-story" role="tabpanel" :aria-labelledby="`demo-tab-${active}`">
          <template v-if="active === 0">
            <div class="demo-summary"><DefenseIcon name="snapshot" /><h2>Stopped in the fault handler</h2><p>The indirect call entered an invalid execution state.</p></div>
            <div class="fault-observations"><div><small>Fault type</small><b>Invalid state</b></div><div><small>Capture boundary</small><b>Handler entry</b></div><div><small>Question</small><b>What executed before the call?</b></div></div>
          </template>
          <template v-else-if="active === 1">
            <div class="demo-summary"><DefenseIcon name="history" /><h2>Recovered execution path</h2><p>The capture retains the copy operation and the subsequent call.</p></div>
            <div class="demo-sequence"><div><b>Process()</b><span>Copy loop executes</span></div><i>↓</i><div><b>Return</b><span>Control returns to main</span></div><i>↓</i><div class="faulting-call"><b>on_complete()</b><span>Indirect call faults</span></div></div>
          </template>
          <template v-else>
            <div class="demo-summary"><DefenseIcon name="code" /><h2>Source-level diagnosis</h2><p>The inclusive bound writes beyond the buffer into the adjacent pointer.</p><div class="demo-memory"><span>buffer[0 … 7]</span><b>on_complete</b></div></div>
            <pre class="code">for (int i = 0;
     <span class="warn">i &lt;= len</span>; i++) {
  record.buffer[i] =
    data[i % len];
}
<span class="dim">// len = 8</span></pre>
          </template>
        </div>
      </Transition>
      <p class="demo-source">Experimental evidence · instruction trace and source code · <a href="/evidence/fault-state.json" target="_blank" rel="noopener">Saved fault state</a></p>
    </template>
  </div>
</template>

<style scoped>
.academic-demo { padding: 24px 28px; }
.demo-tabs button { display: flex; align-items: center; gap: 12px; }
.demo-tabs button > span { border: 1px solid currentColor; border-radius: 50%; width: 23px; height: 23px; display: grid; place-items: center; font-size: 13px; }
.demo-story { min-height: 270px; display: grid; grid-template-columns: 1fr 1fr; align-items: center; gap: 48px; }
.demo-summary .defense-icon { color: var(--yellow); width: 42px; height: 42px; }
.demo-summary h2 { margin-top: 17px; font-size: 25px; }
.demo-summary p { font-size: 21px; }
.fault-observations { display: grid; gap: 22px; border-left: 3px solid var(--yellow); padding-left: 27px; }
.fault-observations small { display: block; font-size: 14px; color: var(--panel); margin-bottom: 5px; }
.fault-observations b { font-size: 21px; }
.demo-sequence { display: grid; gap: 3px; text-align: center; }
.demo-sequence > div { padding: 9px; border: 1px solid var(--line); }
.demo-sequence b { display: block; font-size: 22px; }.demo-sequence span { font-size: 15px; }
.demo-sequence i { font-style: normal; color: var(--yellow); }
.demo-sequence .faulting-call { background: var(--yellow); color: var(--blue); border-color: var(--yellow); }
.demo-memory { display: flex; margin-top: 20px; font-size: 17px; }.demo-memory > * { padding: 12px; border: 1px solid var(--line); }.demo-memory b { background: var(--yellow); color: var(--blue); border-color: var(--yellow); }
.demo-panel .demo-source { color: var(--panel); font-size: 14px; margin: 24px 0 0; }
.fallback-button { color: var(--panel); font-size: 14px; text-decoration: underline; margin-top: 10px; cursor: pointer; }
button:focus-visible { outline: 3px solid var(--yellow); outline-offset: 3px; }
.evidence-enter-active, .evidence-leave-active { transition: opacity 180ms ease, transform 180ms ease; }
.evidence-enter-from { opacity: 0; transform: translateX(12px); }.evidence-leave-to { opacity: 0; transform: translateX(-12px); }
@media (prefers-reduced-motion: reduce) { .evidence-enter-active, .evidence-leave-active { transition: none; } }
</style>
