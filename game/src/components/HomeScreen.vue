<script setup>
import { ref, computed } from 'vue'
import { difficulties, getPlants } from '../data/plants.js'

const emit = defineEmits(['start'])

const selectedDifficulty = ref('beginner')

const plantCount = computed(() => getPlants(selectedDifficulty.value).length)
const selectedColor = computed(() => {
  const diff = difficulties.find((d) => d.id === selectedDifficulty.value)
  return diff ? diff.color : '#4a7c59'
})

function play(mode) {
  emit('start', { mode, difficulty: selectedDifficulty.value })
}
</script>

<template>
  <div class="home">
    <h1>Plantes calcicoles</h1>
    <p class="subtitle">Apprenez à reconnaître les plantes indicatrices de sol calcaire</p>

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
      <p class="plant-count">{{ plantCount }} plantes à découvrir</p>
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

.plant-count {
  color: var(--color-text-light);
  font-size: 0.9rem;
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
