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
class: planilha-slide
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
| 03/03/2026 | 03/03/2026 | 1 |
| 03/03/2026 | 06/03/2026 | 4 |
| 04/03/2026 | 08/03/2026 | 5 |
| 05/03/2026 | 09/03/2026 | 5 |
| 06/03/2026 | 11/03/2026 | 6 |
| 07/03/2026 | 10/03/2026 | 4 |
| 10/03/2026 | 15/03/2026 | 6 |
| 12/03/2026 | 18/03/2026 | 7 |



---
layout: default
class: full-height-img-slide
---

# Com isso podemos dizer qual nossa previsão para 1 item


## Baseado nos dados, vemos que nós terminamos 85% dos itens em 8 dias ou menos.
<img class="slide-full-img" src="/planilha-explicacao-p85.png" alt="Planilha com explicacao visual do percentil p85" />



---
layout: default
class: full-height-img-slide
---

# Deixa o Excel te ajudar

<img class="slide-full-img" src="/planilha-formula-percentil.png" alt="Planilha com explicacao visual do percentil p85" />

---
layout: default
class: code-slide
---

# Ou melhor ainda, o Python


```python
import math
import numpy as np

lead_times = carrega_dias_csv()

def percentil(dados: list[int], p: float) -> int:
    return math.ceil(np.percentile(dados, p))

percentil(lead_times, 50)  # 5 dias
percentil(lead_times, 75)  # 7 dias
percentil(lead_times, 85)  # 8 dias
```

---
layout: default
---

# Agora temos nosso SLE (Service Level Expectation)


## Nosso SLE atual é de 8 dias com 85% de confiança.

Ou seja, sabemos que qualquer trabalho termina em 8 dias ou menos em 85% dos casos.



---
layout: default
class: sle-actions-slide
---

# Mas se o meu SLE estiver alto?


## O que podemos fazer é diminuir a dispersão dos valores, ou seja, reduzir o comprimento da cauda longa.

<p class="section-label">Para isso, devemos adotar duas práticas:</p>

1. Reduzir WIP (Work in Progress), ou seja, fazer menos multitasking
2. Monitorar quanto tempo cada item está levando ("Idade do item")

No nosso exemplo, um item começa com 15% de chance de estourar o SLE, mas depois de 4 dias, a chance já é de 30%.

<div style="margin-top:5rem">
<blockquote class="quote-block">Para de começar e começa a terminar</blockquote>
</div>
