<script setup lang="ts">
import { computed } from 'vue'
import { useSlideContext } from '@slidev/client'

const { $frontmatter, $page } = useSlideContext()
// Capa, seção, frase e encerramento ficam sem rodapé, para não competir com o conteúdo.
const semRodape = ['cover', 'section', 'statement', 'end', 'image', 'full']
const mostrar = computed(() => !semRodape.includes(String($frontmatter.layout ?? 'default')) && !$frontmatter.semRodape)
</script>

<template>
  <div v-if="mostrar" class="rodape">
    <span class="rodape-marca" />
    <span class="rodape-numero">{{ $page }}</span>
  </div>
</template>

<style>
.rodape {
  position: absolute;
  left: 3.2rem;
  right: 3.2rem;
  bottom: 1rem;
  display: flex;
  justify-content: space-between;
  font-family: var(--font-head);
  font-size: 14px;
  color: var(--muted);
}
.rodape-marca::before { content: var(--footer); }
/* Marcas com logo horizontal mostram o logo no lugar do texto. */
.rodape-marca {
  width: var(--footer-logo-width, auto);
  min-height: 22px;
  background: var(--footer-logo, none) left center / contain no-repeat;
}
</style>
