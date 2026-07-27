<script setup>
import { computed } from 'vue'

const props = defineProps({
  types: { type: Object, required: true },
  value: { type: String, default: '' },
})

const FALLBACK = { label: '—', color: '#95a5a6', icon: '' }
const type = computed(() => props.types[props.value] ?? FALLBACK)
</script>

<template>
  <span class="trait-badge" :title="type.label" :style="{ '--trait-color': type.color }">
    <span v-if="type.icon" class="trait-icon">{{ type.icon }}</span>
    <span v-else class="trait-dot"></span>
    <span class="trait-label">{{ type.label }}</span>
  </span>
</template>

<style scoped>
.trait-badge {
  display: inline-flex;
  align-items: center;
  gap: 0.3em;
  font-size: 0.75rem;
  font-weight: 600;
  color: var(--trait-color);
}

.trait-dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: var(--trait-color);
  flex-shrink: 0;
}

.trait-icon {
  line-height: 1;
}
</style>
