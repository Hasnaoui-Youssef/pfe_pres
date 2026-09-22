<script setup>
import { computed } from 'vue'
import { useSlideContext } from '@slidev/client'
const { $slidev } = useSlideContext()
const sections = ['Context & problem', 'Objectives & approach', 'Design & implementation', 'Demonstration', 'Validation & results', 'Conclusion']
const page = computed(() => $slidev.nav.currentPage)
const section = computed(() => page.value <= 4 ? 0 : page.value <= 8 ? 1 : page.value <= 16 ? 2 : page.value <= 18 ? 3 : page.value <= 21 ? 4 : 5)
</script>

<template>
  <footer v-if="page > 1" class="deck-footer" :class="{ inverse: page === 23 }">
    <nav v-if="page <= 23" aria-label="Presentation sections">
      <span v-for="(label, i) in sections" :key="label" class="section-item" :class="{ active: i === section }"><i class="section-number">{{ i + 1 }}</i><span class="section-name">{{ label }}</span></span>
    </nav>
    <span v-else class="backup-label">Discussion / supporting evidence</span>
    <b>{{ page <= 23 ? String(page).padStart(2, '0') + ' / 23' : 'B' + (page - 23) }}</b>
  </footer>
</template>
