<script setup>
import { onMounted } from 'vue'
import { useQuiz } from '../composables/useQuiz.js'
import PlantImage from './PlantImage.vue'
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
  choices,
  selected,
  answered,
  finished,
  lastCorrect,
  failedPlants,
  start,
  answer: rawAnswer,
  next,
  plantCount,
} = useQuiz(props.difficulty)

onMounted(start)

function answer(choice) {
  rawAnswer(choice)
  if (lastCorrect.value) {
    setTimeout(next, 100)
  }
}

function choiceClass(choice) {
  if (!answered.value) return 'btn-choice'
  if (choice.id === currentPlant.value.id) return 'btn-choice choice-correct'
  if (choice.id === selected.value) return 'btn-choice choice-wrong'
  return 'btn-choice choice-dim'
}
</script>

<template>
  <div class="quiz">
    <header v-if="!finished" class="quiz-header">
      <button class="btn-secondary btn-small" @click="emit('back')">Quitter</button>
      <span class="progress">{{ currentIndex + 1 }} / {{ plantCount }}</span>
      <ScoreBoard :correct="correct" :total="total" :percentage="percentage" />
    </header>

    <template v-if="!finished && currentPlant">
      <PlantImage :src="currentPlant.image" :alt="'Photo de ' + currentPlant.name" />

      <p class="question">Quelle est cette plante ?</p>

      <div class="choices">
        <button
          v-for="choice in choices"
          :key="choice.id"
          :class="choiceClass(choice)"
          :disabled="answered"
          @click="answer(choice)"
        >
          <span class="choice-name">{{ choice.name }}</span>
          <span class="choice-latin"><em>{{ choice.latin }}</em></span>
        </button>
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
      :failed-plants="failedPlants"
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
