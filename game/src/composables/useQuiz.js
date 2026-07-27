import { ref, computed } from 'vue'
import { shuffle } from '../utils/shuffle.js'
import { useScore } from './useScore.js'

export function useQuiz(items) {
  const { correct, total, percentage, failedItems, record, reset } = useScore()

  const pool = ref([])
  const order = ref([])
  const currentIndex = ref(0)
  const choices = ref([])
  const selected = ref(null)
  const answered = ref(false)
  const finished = ref(false)

  const currentItem = computed(() => {
    if (currentIndex.value >= order.value.length) return null
    return order.value[currentIndex.value]
  })

  const itemCount = computed(() => order.value.length)

  function start() {
    reset()
    pool.value = items
    order.value = shuffle(pool.value)
    currentIndex.value = 0
    selected.value = null
    answered.value = false
    finished.value = false
    generateChoices()
  }

  function generateChoices() {
    const current = order.value[currentIndex.value]
    const others = pool.value.filter((i) => i.id !== current.id)
    const distractors = shuffle(others).slice(0, 3)
    choices.value = shuffle([current, ...distractors])
  }

  const lastCorrect = ref(false)

  function answer(item) {
    if (answered.value) return
    selected.value = item.id
    answered.value = true
    lastCorrect.value = item.id === currentItem.value.id
    record(lastCorrect.value, currentItem.value)
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
    currentItem,
    currentIndex,
    choices,
    selected,
    answered,
    finished,
    lastCorrect,
    start,
    answer,
    next,
    failedItems,
    itemCount,
  }
}
