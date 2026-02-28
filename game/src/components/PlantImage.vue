<script setup>
defineProps({
  src: { type: String, required: true },
  alt: { type: String, default: 'Photo de plante' },
})
</script>

<template>
  <div class="plant-image-container">
    <img :src="src" :alt="alt" class="plant-image" />
  </div>
</template>

<style scoped>
.plant-image-container {
  width: 100%;
  aspect-ratio: 4 / 3;
  background: #e8e0d8;
  border-radius: var(--radius);
  overflow: hidden;
  display: flex;
  align-items: center;
  justify-content: center;
}

.plant-image {
  width: 100%;
  height: 100%;
  object-fit: contain;
}
</style>
