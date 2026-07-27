<script setup>
import { computed, onMounted } from 'vue'
import { useFlashcard } from '../composables/useFlashcard.js'
import { getDomain, itemDetails } from '../data/domains.js'
import ScoreBoard from './ScoreBoard.vue'
import TraitBadge from './TraitBadge.vue'

const props = defineProps({
  domain: { type: String, required: true },
  difficulty: { type: String, required: true },
})
const emit = defineEmits(['back'])

const domain = getDomain(props.domain)

const {
  correct,
  total,
  percentage,
  currentItem,
  currentIndex,
  revealed,
  finished,
  failedItems,
  start,
  reveal,
  evaluate,
  itemCount,
} = useFlashcard(domain.getItems(props.difficulty))

onMounted(start)

const currentDetails = computed(() => itemDetails(domain, currentItem.value))
</script>

<template>
  <div class="flashcard-game">
    <header v-if="!finished" class="fc-header">
      <button class="btn-secondary btn-small" @click="emit('back')">Quitter</button>
      <span class="progress">{{ currentIndex + 1 }} / {{ itemCount }}</span>
      <ScoreBoard :correct="correct" :total="total" :percentage="percentage" />
    </header>

    <template v-if="!finished && currentItem">
      <div class="flip-container" @click="!revealed && reveal()">
        <div :class="['flip-card', { flipped: revealed }]">
          <!-- Front: image only -->
          <div class="flip-card-front card">
            <div class="card-image-wrap">
              <img :src="currentItem.image" :alt="'Photo de plante'" class="card-image" />
            </div>
            <p class="tap-hint">Cliquez pour révéler</p>
          </div>

          <!-- Back: image + name -->
          <div class="flip-card-back card">
            <div class="card-image-wrap">
              <a
                v-if="revealed && currentItem.source"
                :href="currentItem.source"
                target="_blank"
                rel="noopener noreferrer"
                class="card-image-link"
                @click.stop
              >
                <img :src="currentItem.image" :alt="currentItem.name" class="card-image" />
              </a>
              <img v-else :src="currentItem.image" :alt="currentItem.name" class="card-image" />
            </div>
            <div v-if="revealed" class="card-answer">
              <p class="plant-name">{{ currentItem.name }}</p>
              <p class="plant-latin"><em>{{ currentItem.latin }}</em></p>
              <TraitBadge :types="domain.traits" :value="currentItem[domain.traitKey]" class="card-soil" />
              <div v-if="currentDetails.length" class="card-details">
                <p
                  v-for="d in currentDetails"
                  :key="d.key"
                  :class="['detail-line', { 'detail-note': d.key === 'note' }]"
                >
                  <strong>{{ d.label }} :</strong> {{ d.value }}
                </p>
              </div>
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
      :failed-items="failedItems"
      :domain="domain"
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
  display: grid;
  transition: transform 0.6s;
  transform-style: preserve-3d;
}

.flip-card.flipped {
  transform: rotateY(180deg);
}

.card {
  grid-area: 1 / 1;
  backface-visibility: hidden;
  background: var(--color-surface);
  border-radius: var(--radius);
  box-shadow: var(--shadow);
  overflow: hidden;
}

.flip-card-back {
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

.card-image-link {
  display: contents;
  cursor: pointer;
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
  max-height: 260px;
  overflow-y: auto;
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

.card-soil {
  margin-top: 0.4rem;
}

.card-details {
  text-align: left;
  margin-top: 0.75rem;
  font-size: 0.85rem;
  color: var(--color-text);
}

.detail-line {
  margin: 0.3rem 0;
}

.detail-note {
  background: #fff3cd;
  color: #7a5c00;
  border-radius: var(--radius);
  padding: 0.5rem 0.75rem;
  font-weight: 600;
}

.eval-buttons {
  display: flex;
  gap: 0.75rem;
  margin-top: 4rem;
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
