<script setup>
import { onMounted } from 'vue'
import { useFlashcard } from '../composables/useFlashcard.js'
import ScoreBoard from './ScoreBoard.vue'

const props = defineProps({
  difficulty: { type: String, required: true },
})
const emit = defineEmits(['back'])

const {
  correct,
  total,
  percentage,
  currentPlant,
  currentIndex,
  revealed,
  finished,
  failedPlants,
  start,
  reveal,
  evaluate,
  plantCount,
} = useFlashcard(props.difficulty)

onMounted(start)
</script>

<template>
  <div class="flashcard-game">
    <header v-if="!finished" class="fc-header">
      <button class="btn-secondary btn-small" @click="emit('back')">Quitter</button>
      <span class="progress">{{ currentIndex + 1 }} / {{ plantCount }}</span>
      <ScoreBoard :correct="correct" :total="total" :percentage="percentage" />
    </header>

    <template v-if="!finished && currentPlant">
      <div class="flip-container" @click="!revealed && reveal()">
        <div :class="['flip-card', { flipped: revealed }]">
          <!-- Front: image only -->
          <div class="flip-card-front card">
            <div class="card-image-wrap">
              <img :src="currentPlant.image" :alt="'Photo de plante'" class="card-image" />
            </div>
            <p class="tap-hint">Cliquez pour révéler</p>
          </div>

          <!-- Back: image + name -->
          <div class="flip-card-back card">
            <div class="card-image-wrap">
              <img :src="currentPlant.image" :alt="currentPlant.name" class="card-image" />
            </div>
            <div v-if="revealed" class="card-answer">
              <p class="plant-name">{{ currentPlant.name }}</p>
              <p class="plant-latin"><em>{{ currentPlant.latin }}</em></p>
            </div>
          </div>
        </div>
      </div>

      <div v-if="revealed" class="eval-buttons">
        <button class="btn-eval btn-knew" @click="evaluate(true)">Je savais</button>
        <button class="btn-eval btn-didnt" @click="evaluate(false)">Je ne savais pas</button>
      </div>
    </template>

    <ScoreBoard
      v-else
      :correct="correct"
      :total="total"
      :percentage="percentage"
      :failed-plants="failedPlants"
      :final="true"
      @back="emit('back')"
    />
  </div>
</template>

<style scoped>
.fc-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 1rem;
}

.btn-small {
  padding: 0.4rem 0.8rem;
  font-size: 0.85rem;
}

.progress {
  font-weight: 600;
  color: var(--color-text-light);
}

.flip-container {
  perspective: 800px;
  cursor: pointer;
  margin-bottom: 1rem;
}

.flip-card {
  position: relative;
  width: 100%;
  transition: transform 0.6s;
  transform-style: preserve-3d;
}

.flip-card.flipped {
  transform: rotateY(180deg);
}

.card {
  backface-visibility: hidden;
  background: var(--color-surface);
  border-radius: var(--radius);
  box-shadow: var(--shadow);
  overflow: hidden;
}

.flip-card-back {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  transform: rotateY(180deg);
}

.card-image-wrap {
  width: 100%;
  aspect-ratio: 4 / 3;
  background: #e8e0d8;
  display: flex;
  align-items: center;
  justify-content: center;
}

.card-image {
  width: 100%;
  height: 100%;
  object-fit: contain;
}

.tap-hint {
  text-align: center;
  padding: 1rem;
  color: var(--color-text-light);
  font-size: 0.95rem;
}

.card-answer {
  text-align: center;
  padding: 1rem;
}

.plant-name {
  font-size: 1.3rem;
  font-weight: 700;
  color: var(--color-text);
  margin-bottom: 0.25rem;
}

.plant-latin {
  font-size: 1rem;
  color: var(--color-text-light);
}

.eval-buttons {
  display: flex;
  gap: 0.75rem;
}

.btn-eval {
  flex: 1;
  padding: 0.85rem;
  font-size: 1.05rem;
  font-weight: 600;
  border-radius: var(--radius);
}

.btn-knew {
  background: var(--color-correct);
  color: white;
}

.btn-knew:hover {
  background: #248a42;
}

.btn-didnt {
  background: var(--color-wrong);
  color: white;
}

.btn-didnt:hover {
  background: #a93226;
}
</style>
