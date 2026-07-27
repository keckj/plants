<script setup>
import { ref } from 'vue'
import HomeScreen from './components/HomeScreen.vue'
import QuizGame from './components/QuizGame.vue'
import FlashcardGame from './components/FlashcardGame.vue'

const screen = ref('home')
const domain = ref('plants')
const difficulty = ref('beginner')

function startGame({ mode, domain: dom, difficulty: diff }) {
  domain.value = dom
  difficulty.value = diff
  screen.value = mode
}
</script>

<template>
  <HomeScreen v-if="screen === 'home'" :domain="domain" :difficulty="difficulty" @start="startGame" />
  <QuizGame
    v-else-if="screen === 'quiz'"
    :key="`quiz-${domain}-${difficulty}`"
    :domain="domain"
    :difficulty="difficulty"
    @back="screen = 'home'"
  />
  <FlashcardGame
    v-else-if="screen === 'flashcard'"
    :key="`fc-${domain}-${difficulty}`"
    :domain="domain"
    :difficulty="difficulty"
    @back="screen = 'home'"
  />
</template>
