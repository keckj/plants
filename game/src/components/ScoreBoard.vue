<script setup>
import SoilBadge from './SoilBadge.vue'

defineProps({
  correct: { type: Number, required: true },
  total: { type: Number, required: true },
  percentage: { type: Number, required: true },
  final: { type: Boolean, default: false },
  failedPlants: { type: Array, default: () => [] },
})

defineEmits(['back'])
</script>

<template>
  <div :class="['scoreboard', { 'scoreboard-final': final }]">
    <template v-if="!final">
      <span class="score-inline">{{ correct }} / {{ total }}</span>
    </template>

    <template v-else>
      <h2>Partie terminée !</h2>
      <div class="score-big">{{ correct }} / {{ total }}</div>
      <div class="score-percent">{{ percentage }}% de bonnes réponses</div>
      <div class="score-message">
        <template v-if="percentage === 100">Parfait ! Vous connaissez toutes les plantes.</template>
        <template v-else-if="percentage >= 75">Très bien ! Encore un peu de pratique.</template>
        <template v-else-if="percentage >= 50">Pas mal ! Continuez à vous entraîner.</template>
        <template v-else>Courage, recommencez pour progresser !</template>
      </div>
      <div v-if="failedPlants.length > 0" class="failed-section">
        <h3>Plantes à revoir</h3>
        <div class="failed-list">
          <div v-for="plant in failedPlants" :key="plant.id" class="failed-item">
            <div class="thumb-wrap">
              <img :src="plant.image" :alt="plant.name" class="failed-thumb" />
              <img :src="plant.image" :alt="plant.name" class="failed-preview" />
            </div>
            <div class="failed-info">
              <span class="failed-name">{{ plant.name }} <SoilBadge :soil="plant.soil" /></span>
              <span class="failed-latin"><em>{{ plant.latin }}</em></span>
            </div>
          </div>
        </div>
      </div>

      <button class="btn-primary" @click="$emit('back')">Retour à l'accueil</button>
    </template>
  </div>
</template>

<style scoped>
.scoreboard {
  text-align: center;
}

.score-inline {
  font-weight: 600;
  color: var(--color-text-light);
}

.scoreboard-final {
  padding: 2rem 1rem;
}

h2 {
  font-size: 1.5rem;
  margin-bottom: 1rem;
  color: var(--color-primary);
}

.score-big {
  font-size: 3rem;
  font-weight: 700;
  color: var(--color-text);
  margin-bottom: 0.25rem;
}

.score-percent {
  font-size: 1.2rem;
  color: var(--color-text-light);
  margin-bottom: 1rem;
}

.score-message {
  font-size: 1.1rem;
  margin-bottom: 2rem;
}

button {
  font-size: 1.1rem;
}

.failed-section {
  text-align: left;
  margin-bottom: 1.5rem;
}

.failed-section h3 {
  font-size: 1.1rem;
  color: var(--color-wrong);
  margin-bottom: 0.75rem;
  text-align: center;
}

.failed-list {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.failed-item {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  padding: 0.5rem;
  background: var(--color-surface);
  border-radius: var(--radius);
  border: 1px solid var(--color-border);
}

.thumb-wrap {
  position: relative;
  flex-shrink: 0;
}

.failed-thumb {
  width: 50px;
  height: 50px;
  object-fit: cover;
  border-radius: 4px;
  cursor: pointer;
}

.failed-preview {
  display: none;
  position: absolute;
  left: 60px;
  top: 50%;
  transform: translateY(-50%);
  width: 250px;
  border-radius: var(--radius);
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
  z-index: 10;
  pointer-events: none;
}

.thumb-wrap:hover .failed-preview {
  display: block;
}

.failed-info {
  display: flex;
  flex-direction: column;
}

.failed-name {
  font-weight: 600;
  font-size: 0.95rem;
}

.failed-latin {
  font-size: 0.85rem;
  color: var(--color-text-light);
}
</style>
