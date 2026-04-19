---
theme: seriph
css: ./style.css
title: Quando vai ficar pronto?
info: |
  Talk na Python Sul sobre previsibilidade de entregas com
  métricas de fluxo e simulação.
transition: fade
mdc: true
lineNumbers: true
highlighter: shiki
canvasWidth: 1280
aspectRatio: 16/9
layout: cover

---

# Quando vai ficar<br>pronto?

Respondendo a pergunta mais importante do cliente.

<img class="cover-logo" src="/pysul-logo.svg" alt="Python Sul 2026 Londrina - PR" />

---
layout: default
---

<div class="cartoon-pane pane-tl" role="img" aria-label="Cartoon painel superior esquerdo"></div>

---
layout: default
---

<div class="cartoon-pane pane-tr" role="img" aria-label="Cartoon painel superior direito"></div>

---
layout: default
---

<div class="cartoon-pane pane-bl" role="img" aria-label="Cartoon painel inferior esquerdo"></div>

---
layout: default
---

<div class="cartoon-pane pane-br" role="img" aria-label="Cartoon painel inferior direito"></div>

---
layout: default
---

# Como sair dessa armadilha?

## Queremos sair da estimativa que compromete a pessoa ou time...

- "Acho que leva 10 dias."

## ...para previsões orientadas a dados

- "De acordo com entregas recentes, temos 80% de confiança de terminar em 14 dias."

## Por quê?
- Estimativa com só uma data não captura a incerteza.
- Estimar dá trabalho e parece estar sempre errado, por mais que a gente capriche.


---
layout: default
---

# Por que a gente parece sempre estimar por baixo?

## Nosso cérebro (e otimismo) pensa em distruibuição normal

<img src="/normal_distribution_curve.png" alt="Curva normal de referência" style="width: 92%; max-height: 72%; object-fit: contain; display: block; margin: 1.2rem auto 0;" />

---
layout: default
---

# Nosso tipo de trabalho é de 'cauda longa'

## É mais fácil aparecer alguma surpresa que **atrase** a entrega, do que uma que adiante.

<img src="/skewed_distribution_curve.png" alt="Distribuição real de lead time com cauda longa" style="width: 92%; max-height: 72%; object-fit: contain; display: block; margin: 1.2rem auto 0;" />

---
layout: default
---

# Mas como fazer previsões sem reunião de estimativa?

## Você só precisa coletar duas coisas para cada item de trabalho:

- A data de início
- A data de fim

| Início | Fim | Dias |
|---|---|---|
| 03/03/2026 | 04/03/2026 | 2 |
| 03/03/2026 | 06/03/2026 | 4 |
| 04/03/2026 | 08/03/2026 | 5 |
| 05/03/2026 | 09/03/2026 | 5 |
| 06/03/2026 | 11/03/2026 | 6 |
| 07/03/2026 | 10/03/2026 | 4 |
| 10/03/2026 | 15/03/2026 | 6 |
| 12/03/2026 | 18/03/2026 | 7 |


