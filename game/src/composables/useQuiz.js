import { ref, computed } from 'vue'
import { getPlants } from '../data/plants.js'
import { shuffle } from '../utils/shuffle.js'
import { useScore } from './useScore.js'

export function useQuiz(difficulty) {
  const { correct, total, percentage, failedPlants, record, reset } = useScore()

  const pool = ref([])
  const order = ref([])
  const currentIndex = ref(0)
  const choices = ref([])
  const selected = ref(null)
  const answered = ref(false)
  const finished = ref(false)

  const currentPlant = computed(() => {
    if (currentIndex.value >= order.value.length) return null
    return order.value[currentIndex.value]
  })

  const plantCount = computed(() => order.value.length)

  function start() {
    reset()
    pool.value = getPlants(difficulty)
    order.value = shuffle(pool.value)
    currentIndex.value = 0
    selected.value = null
    answered.value = false
    finished.value = false
    generateChoices()
  }

  function generateChoices() {
    const current = order.value[currentIndex.value]
    const others = pool.value.filter((p) => p.id !== current.id)
    const distractors = shuffle(others).slice(0, 3)
    choices.value = shuffle([current, ...distractors])
  }

  const lastCorrect = ref(false)

  function answer(plant) {
    if (answered.value) return
    selected.value = plant.id
    answered.value = true
    lastCorrect.value = plant.id === currentPlant.value.id
    record(lastCorrect.value, currentPlant.value)
  }

  function next() {
    currentIndex.value++
    selected.value = null
    answered.value = false
    if (currentIndex.value >= order.value.length) {
      finished.value = true
    } else {
      generateChoices()
    }
  }

  return {
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
    start,
    answer,
    next,
    failedPlants,
    plantCount,
  }
}
