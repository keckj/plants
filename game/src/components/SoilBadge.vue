<script setup>
import { soilTypes } from '../data/plants.js'

const props = defineProps({
  soil: { type: String, required: true },
})

const type = soilTypes[props.soil]
</script>

<template>
  <span class="soil-badge" :title="type.label" :style="{ '--soil-color': type.color }">
    <span class="soil-dot"></span>
    <span class="soil-label">{{ type.label }}</span>
  </span>
</template>

<style scoped>
.soil-badge {
  display: inline-flex;
  align-items: center;
  gap: 0.3em;
  font-size: 0.75rem;
  font-weight: 600;
  color: var(--soil-color);
}

.soil-dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: var(--soil-color);
  flex-shrink: 0;
}
</style>
