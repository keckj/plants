import { ref, computed } from 'vue'
import { getPlants } from '../data/plants.js'
import { shuffle } from '../utils/shuffle.js'
import { useScore } from './useScore.js'

export function useFlashcard(difficulty) {
  const { correct, total, percentage, failedPlants, record, reset } = useScore()

  const order = ref([])
  const currentIndex = ref(0)
  const revealed = ref(false)
  const finished = ref(false)

  const currentPlant = computed(() => {
    if (currentIndex.value >= order.value.length) return null
    return order.value[currentIndex.value]
  })

  const plantCount = computed(() => order.value.length)

  function start() {
    reset()
    order.value = shuffle(getPlants(difficulty))
    currentIndex.value = 0
    revealed.value = false
    finished.value = false
  }

  function reveal() {
    revealed.value = true
  }

  function evaluate(knew) {
    record(knew, currentPlant.value)
    revealed.value = false
    currentIndex.value++
    if (currentIndex.value >= order.value.length) {
      finished.value = true
    }
  }

  return {
    correct,
    total,
    percentage,
    currentPlant,
    currentIndex,
    revealed,
    finished,
    start,
    reveal,
    evaluate,
    failedPlants,
    plantCount,
  }
}
