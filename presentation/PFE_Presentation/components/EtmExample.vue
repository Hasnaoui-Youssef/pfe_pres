<script setup>
import { computed } from 'vue'
import { useSlideContext } from '@slidev/client'
const { $clicks } = useSlideContext()
const step = computed(() => Math.min(4, Math.max(0, $clicks.value)))
const atoms = ['E', 'E', 'E', 'N']
const instructions = [
  ['0x08000100', 'ldr.w r2, [r1], #4', 'Load value'],
  ['0x08000104', 'add   r0, r2', 'Accumulate'],
  ['0x08000106', 'subs  r3, #1', 'Decrement'],
  ['0x08000108', 'bne.n 0x08000100', 'Repeat?'],
]
</script>

<template>
  <div class="etm-example">
    <div class="etm-program">
      <div class="figure-label">Program image <span>r3 = 4 at entry</span></div>
      <div class="assembly-list">
        <div v-for="(ins, i) in instructions" :key="ins[0]" class="assembly-line" :class="{ branch: i === 3, evaluating: i === 3 && step > 0 }">
          <code>{{ ins[0] }}</code><code>{{ ins[1] }}</code><small>{{ ins[2] }}</small>
        </div>
      </div>
      <div class="branch-path" :class="{ exited: step === 4 }">
        <span class="loop-back">↶ E: take the branch</span><span class="loop-exit">N: continue →</span>
      </div>
      <p class="figure-caption">ETM: hardware instruction-trace unit.</p>
    </div>
    <div class="etm-record">
      <div class="figure-label">Trace elements <span>Synchronization omitted</span></div>
      <div class="trace-address">ADDRESS <code>0x08000100</code></div>
      <div class="atom-sequence"><span v-for="(atom, i) in atoms" :key="i" :class="{ consumed: i < step, current: i === step - 1 }">{{ atom }}</span></div>
      <div class="iteration-list">
        <div v-for="(atom, i) in atoms" :key="i" class="iteration" :class="{ revealed: i < step }">
          <b>{{ i + 1 }}</b><span>load → add → decrement → branch</span><strong>{{ atom === 'E' ? '↶' : '→ exit' }}</strong>
        </div>
      </div>
      <div class="execution-count"><b>{{ step * 4 }}</b> instructions reconstructed<span v-if="step === 4">4 atoms · 4 iterations</span></div>
    </div>
  </div>
</template>
