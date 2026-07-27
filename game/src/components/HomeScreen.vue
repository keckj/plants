<script setup>
import { ref, computed } from 'vue'
import { difficulties } from '../data/difficulties.js'
import { domains, getDomain } from '../data/domains.js'

const props = defineProps({
  domain: { type: String, default: 'plants' },
  difficulty: { type: String, default: 'beginner' },
})
const emit = defineEmits(['start'])

const selectedDomainId = ref(props.domain)
const selectedDifficulty = ref(props.difficulty)

const domain = computed(() => getDomain(selectedDomainId.value))
const itemCount = computed(() => domain.value.getItems(selectedDifficulty.value).length)
const selectedColor = computed(() => {
  const diff = difficulties.find((d) => d.id === selectedDifficulty.value)
  return diff ? diff.color : '#4a7c59'
})

function play(mode) {
  emit('start', { mode, domain: selectedDomainId.value, difficulty: selectedDifficulty.value })
}
</script>

<template>
  <div class="home">
    <div class="domain-tabs">
      <button
        v-for="d in domains"
        :key="d.id"
        :class="['domain-btn', { active: selectedDomainId === d.id }]"
        @click="selectedDomainId = d.id"
      >
        <span class="domain-icon">{{ d.icon }}</span> {{ d.label }}
      </button>
    </div>

    <h1>{{ domain.title }}</h1>
    <p class="subtitle">{{ domain.subtitle }}</p>

    <div class="difficulty">
      <p class="section-label">Niveau</p>
      <div class="difficulty-buttons">
        <button
          v-for="diff in difficulties"
          :key="diff.id"
          :class="['diff-btn', { active: selectedDifficulty === diff.id }]"
          :style="selectedDifficulty === diff.id ? { background: diff.color, borderColor: diff.color } : {}"
          @click="selectedDifficulty = diff.id"
        >
          {{ diff.label }}
        </button>
      </div>
      <p class="item-count">{{ domain.countLabel(itemCount) }}</p>
    </div>

    <div class="trait-legend">
      <span v-for="(info, key) in domain.traits" :key="key" class="legend-item" :title="info.definition">
        <span class="legend-dot" :style="{ background: info.color }"></span>
        {{ info.label }}
      </span>
    </div>

    <div class="modes">
      <button class="mode-card" :style="{ borderColor: selectedColor }" @click="play('quiz')">
        <span class="mode-icon">?</span>
        <span class="mode-title">QCM</span>
        <span class="mode-desc">4 choix par question, testez vos connaissances</span>
      </button>

      <button class="mode-card" :style="{ borderColor: selectedColor }" @click="play('flashcard')">
        <span class="mode-icon">&#x21C4;</span>
        <span class="mode-title">Flashcards</span>
        <span class="mode-desc">Retournez la carte pour révéler le nom</span>
      </button>
    </div>
  </div>
</template>

<style scoped>
.home {
  text-align: center;
  padding: 2rem 0;
}

h1 {
  font-size: 2rem;
  margin-bottom: 0.5rem;
  color: var(--color-primary);
}

.subtitle {
  color: var(--color-text-light);
  margin-bottom: 2rem;
  font-size: 1.1rem;
}

.domain-tabs {
  display: flex;
  gap: 0.4rem;
  justify-content: center;
  margin-bottom: 1.5rem;
  flex-wrap: wrap;
}

.domain-btn {
  padding: 0.5rem 1rem;
  border-radius: var(--radius);
  background: var(--color-surface);
  border: 2px solid var(--color-border);
  font-weight: 600;
  font-size: 0.9rem;
  color: var(--color-text);
  transition: border-color 0.2s, background-color 0.2s, color 0.2s;
}

.domain-btn:hover {
  opacity: 0.85;
}

.domain-btn.active {
  background: var(--color-primary);
  border-color: var(--color-primary);
  color: white;
}

.domain-icon {
  margin-right: 0.2rem;
}

.section-label {
  font-weight: 600;
  margin-bottom: 0.5rem;
  font-size: 1rem;
}

.difficulty {
  margin-bottom: 2rem;
}

.difficulty-buttons {
  display: flex;
  gap: 0.4rem;
  justify-content: center;
  margin-bottom: 0.5rem;
  flex-wrap: wrap;
}

.diff-btn {
  padding: 0.5rem 1rem;
  border-radius: var(--radius);
  background: var(--color-surface);
  border: 2px solid var(--color-border);
  font-weight: 600;
  font-size: 0.9rem;
  color: var(--color-text);
  transition: border-color 0.2s, background-color 0.2s, color 0.2s;
}

.diff-btn:hover {
  opacity: 0.85;
}

.diff-btn.active {
  color: white;
}

.item-count {
  color: var(--color-text-light);
  font-size: 0.9rem;
}

.trait-legend {
  display: grid;
  grid-template-columns: repeat(3, auto);
  justify-content: center;
  gap: 0.5rem 1.5rem;
  margin-bottom: 1.5rem;
  font-size: 0.85rem;
  color: var(--color-text-light);
}

.legend-item {
  display: inline-flex;
  align-items: center;
  gap: 0.3rem;
}

.legend-dot {
  width: 10px;
  height: 10px;
  border-radius: 50%;
  flex-shrink: 0;
}

.modes {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.mode-card {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.5rem;
  padding: 1.5rem;
  background: var(--color-surface);
  border: 2px solid var(--color-border);
  border-radius: var(--radius);
  box-shadow: var(--shadow);
  transition: border-color 0.2s, box-shadow 0.2s;
  cursor: pointer;
  font-size: 1rem;
}

.mode-card:hover {
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.12);
}

.mode-icon {
  font-size: 2rem;
}

.mode-title {
  font-size: 1.3rem;
  font-weight: 700;
  color: var(--color-text);
}

.mode-desc {
  color: var(--color-text-light);
  font-size: 0.9rem;
}
</style>
