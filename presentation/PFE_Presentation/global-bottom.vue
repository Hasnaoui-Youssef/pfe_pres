<template>
  <div v-if="$slidev.nav.currentPage > 1" class="slide-number">
    {{ String($slidev.nav.currentPage).padStart(2, '0') }}
  </div>
</template>
