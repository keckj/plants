import { ref, computed } from 'vue'

export function useScore() {
  const correct = ref(0)
  const total = ref(0)
  const failedPlants = ref([])

  const percentage = computed(() => {
    if (total.value === 0) return 0
    return Math.round((correct.value / total.value) * 100)
  })

  function record(isCorrect, plant) {
    total.value++
    if (isCorrect) {
      correct.value++
    } else if (plant) {
      failedPlants.value.push(plant)
    }
  }

  function reset() {
    correct.value = 0
    total.value = 0
    failedPlants.value = []
  }

  return { correct, total, percentage, failedPlants, record, reset }
}
