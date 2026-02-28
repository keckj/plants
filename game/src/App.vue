<script setup>
import { ref } from 'vue'
import HomeScreen from './components/HomeScreen.vue'
import QuizGame from './components/QuizGame.vue'
import FlashcardGame from './components/FlashcardGame.vue'

const screen = ref('home')
const difficulty = ref('beginner')

function startGame({ mode, difficulty: diff }) {
  difficulty.value = diff
  screen.value = mode
}
</script>

<template>
  <HomeScreen v-if="screen === 'home'" @start="startGame" />
  <QuizGame v-else-if="screen === 'quiz'" :difficulty="difficulty" @back="screen = 'home'" />
  <FlashcardGame v-else-if="screen === 'flashcard'" :difficulty="difficulty" @back="screen = 'home'" />
</template>
