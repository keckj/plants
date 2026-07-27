import { ref, computed } from 'vue'
import { shuffle } from '../utils/shuffle.js'
import { useScore } from './useScore.js'

export function useFlashcard(items) {
  const { correct, total, percentage, failedItems, record, reset } = useScore()

  const order = ref([])
  const currentIndex = ref(0)
  const revealed = ref(false)
  const finished = ref(false)

  const currentItem = computed(() => {
    if (currentIndex.value >= order.value.length) return null
    return order.value[currentIndex.value]
  })

  const itemCount = computed(() => order.value.length)

  function start() {
    reset()
    order.value = shuffle(items)
    currentIndex.value = 0
    revealed.value = false
    finished.value = false
  }

  function reveal() {
    revealed.value = true
  }

  function evaluate(knew) {
    record(knew, currentItem.value)
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
    currentItem,
    currentIndex,
    revealed,
    finished,
    start,
    reveal,
    evaluate,
    failedItems,
    itemCount,
  }
}
