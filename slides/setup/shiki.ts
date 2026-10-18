import { defineShikiSetup } from '@slidev/types'

// O código fica num cartão claro também nos slides escuros: texto escuro sobre fundo claro
// se lê melhor, em especial em letra pequena (Piepenbrock, Mayr e Buchner, 2014).
export default defineShikiSetup(() => ({
  themes: {
    dark: 'github-light',
    light: 'github-light',
  },
}))
