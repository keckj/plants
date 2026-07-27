<script setup>
defineProps({
  src: { type: String, required: true },
  alt: { type: String, default: 'Photo' },
  href: { type: String, default: '' },
})
</script>

<template>
  <div class="plant-image-container">
    <a v-if="href" :href="href" target="_blank" rel="noopener noreferrer" class="plant-image-link">
      <img :src="src" :alt="alt" class="plant-image" />
    </a>
    <img v-else :src="src" :alt="alt" class="plant-image" />
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

.plant-image-link {
  display: contents;
  cursor: pointer;
}

.plant-image {
  width: 100%;
  height: 100%;
  object-fit: contain;
}
</style>
