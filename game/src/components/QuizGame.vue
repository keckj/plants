<script setup>
import { computed, onMounted } from 'vue'
import { useQuiz } from '../composables/useQuiz.js'
import { getDomain, itemDetails } from '../data/domains.js'
import PlantImage from './PlantImage.vue'
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
  choices,
  selected,
  answered,
  finished,
  lastCorrect,
  failedItems,
  start,
  answer: rawAnswer,
  next,
  itemCount,
} = useQuiz(domain.getItems(props.difficulty))

onMounted(start)

const currentDetails = computed(() => itemDetails(domain, currentItem.value))

function answer(choice) {
  rawAnswer(choice)
  if (lastCorrect.value) {
    setTimeout(next, 100)
  }
}

function choiceClass(choice) {
  if (!answered.value) return 'btn-choice'
  if (choice.id === currentItem.value.id) return 'btn-choice choice-correct'
  if (choice.id === selected.value) return 'btn-choice choice-wrong'
  return 'btn-choice choice-dim'
}
</script>

<template>
  <div class="quiz">
    <header v-if="!finished" class="quiz-header">
      <button class="btn-secondary btn-small" @click="emit('back')">Quitter</button>
      <span class="progress">{{ currentIndex + 1 }} / {{ itemCount }}</span>
      <ScoreBoard :correct="correct" :total="total" :percentage="percentage" />
    </header>

    <template v-if="!finished && currentItem">
      <PlantImage :src="currentItem.image" :alt="'Photo de ' + currentItem.name" :href="currentItem.source" />

      <p class="question">{{ domain.question }}</p>

      <div class="choices">
        <button
          v-for="choice in choices"
          :key="choice.id"
          :class="choiceClass(choice)"
          :disabled="answered"
          @click="answer(choice)"
        >
          <span class="choice-name">{{ choice.name }} <TraitBadge :types="domain.traits" :value="choice[domain.traitKey]" /></span>
          <span class="choice-latin"><em>{{ choice.latin }}</em></span>
        </button>
      </div>

      <div v-if="answered && currentDetails.length" class="answer-details">
        <p v-for="d in currentDetails" :key="d.key" class="detail-line">
          <strong>{{ d.label }} :</strong> {{ d.value }}
        </p>
      </div>

      <div v-if="answered && !lastCorrect" class="next-container">
        <button class="btn-primary btn-next" @click="next">Suivant</button>
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
.quiz-header {
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

.question {
  text-align: center;
  font-size: 1.1rem;
  font-weight: 600;
  margin: 0.5rem 0;
}

.choices {
  display: flex;
  flex-direction: column;
  gap: 0.4rem;
}

.btn-choice {
  text-align: left;
  padding: 0.6rem 0.85rem;
  background: var(--color-surface);
  border: 2px solid var(--color-border);
  border-radius: var(--radius);
  display: flex;
  flex-direction: column;
  gap: 0.1rem;
  transition: border-color 0.2s, background-color 0.2s;
}

.btn-choice:not(:disabled):hover {
  border-color: var(--color-primary);
}

.choice-name {
  font-weight: 600;
}

.choice-latin {
  font-size: 0.85rem;
  color: var(--color-text-light);
}

.choice-correct {
  border-color: var(--color-correct);
  background: var(--color-correct-bg);
}

.choice-correct .choice-name {
  color: var(--color-correct);
}

.choice-wrong {
  border-color: var(--color-wrong);
  background: var(--color-wrong-bg);
}

.choice-wrong .choice-name {
  color: var(--color-wrong);
}

.choice-dim {
  opacity: 0.5;
}

.answer-details {
  background: var(--color-surface);
  border: 1px solid var(--color-border);
  border-radius: var(--radius);
  padding: 0.75rem 1rem;
  margin-top: 0.75rem;
}

.detail-line {
  font-size: 0.9rem;
  margin: 0.25rem 0;
}

.next-container {
  text-align: center;
  margin-top: 0.5rem;
}

.btn-next {
  width: 100%;
  padding: 0.7rem;
  font-size: 1rem;
}
</style>
