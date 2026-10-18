<script setup lang="ts">
import { watchEffect } from 'vue'
import { useSlideContext } from '@slidev/client'

// The brand comes from `brand:` in the first slide's front matter; brands/*/brand.css match on it.
const { $slidev } = useSlideContext()
watchEffect(() => {
  document.documentElement.dataset.brand = String($slidev.configs.brand ?? 'python-brasil')
})
</script>

<template><span /></template>
