<script setup>
defineProps({ active: { type: Number, default: -1 }, compact: Boolean })
const stages = [
  { name: 'Acquire', icon: 'probe', data: 'Capture bytes' },
  { name: 'Decode', icon: 'trace', data: 'Trace elements' },
  { name: 'Reconstruct', icon: 'code', data: 'Instructions' },
  { name: 'Attribute', icon: 'file', data: 'Source blocks' },
  { name: 'Present', icon: 'screen', data: 'Trace views' },
]
</script>

<template>
  <div class="pipeline-map" :class="{ compact }" aria-label="Instruction trace pipeline">
    <template v-for="(stage, i) in stages" :key="stage.name">
      <div v-if="i" class="pipeline-arrow" aria-hidden="true">→</div>
      <div class="pipeline-stage" :class="{ selected: active === i, foundation: i === 1 }">
        <DefenseIcon v-if="!compact" :name="stage.icon" />
        <b>{{ stage.name }}</b><small v-if="!compact">{{ stage.data }}</small>
      </div>
    </template>
  </div>
</template>
