<script setup>
defineProps({ name: { type: String, default: 'code' } })
const paths = {
  organization: 'M3 21h18M5 21V7l7-4 7 4v14M9 21v-4h6v4M8 9h1m6 0h1M8 13h1m6 0h1',
  team: 'M8 12a4 4 0 1 0 0-8 4 4 0 0 0 0 8M2 21v-3a6 6 0 0 1 12 0v3M17 5a3 3 0 0 1 0 6M17 15a5 5 0 0 1 5 5v1',
  chip: 'M6 6h12v12H6zM9 9h6v6H9zM9 2v4m6-4v4M9 18v4m6-4v4M2 9h4m-4 6h4m12-6h4m-4 6h4',
  code: 'm8 6-6 6 6 6m8-12 6 6-6 6M14 3l-4 18',
  file: 'M5 2h9l5 5v15H5zM14 2v6h5M8 12h8m-8 4h8',
  screen: 'M2 3h20v14H2zM8 22h8m-4-5v5M5 7h5m-5 4h10',
  history: 'M3 11a9 9 0 1 1 2 7M3 4v7h7M12 7v6l4 2',
  snapshot: 'M3 6h4l2-3h6l2 3h4v15H3zM16 13a4 4 0 1 1-8 0 4 4 0 0 1 8 0',
  probe: 'M7 2v5m10-5v5M5 7h14v5a7 7 0 0 1-14 0zM12 19v3',
  trace: 'M2 17h5V7h5v10h5V7h5M2 22h20',
  check: 'm4 12 5 5L20 5M21 13v8H3V3h12',
  test: 'M8 2h8m-6 0v7L3 20v2h18v-2L14 9V2M7 16h10',
  layers: 'm2 7 10-5 10 5-10 5zM2 12l10 5 10-5M2 17l10 5 10-5',
  route: 'M4 3h5v5H4zM15 16h5v5h-5zM9 5h8v6H6v7h9',
  clock: 'M21 12a9 9 0 1 1-18 0 9 9 0 0 1 18 0M12 6v6l4 3',
  gap: 'M2 12h6m8 0h6M11 4l-2 16m6-16-2 16',
}
</script>

<template>
  <svg class="defense-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path :d="paths[name] || paths.code" /></svg>
</template>
