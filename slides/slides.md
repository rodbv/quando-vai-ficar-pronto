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
class: full-height-img-slide
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

- "Acho que leva uns 4 ou 5 dias."

## ...para previsões orientadas a dados

- "De acordo com entregas recentes, temos 85% de confiança de terminar em 11 dias corridos."


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

| Início | Fim |
|---|---|
| 03/03/2026 | 03/03/2026 |
| 03/03/2026 | 06/03/2026 |
| 04/03/2026 | 08/03/2026 |
| 05/03/2026 | 09/03/2026 |
| 06/03/2026 | 11/03/2026 |
| 07/03/2026 | 10/03/2026 |
| 10/03/2026 | 15/03/2026 |
| 12/03/2026 | 18/03/2026 |


---
layout: default
---

# Mas como fazer previsões sem reunião de estimativa?

## E a partir disso, calcular quantos dias cada item levou ("Lead time").

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


## Baseado nos dados limpos de 2026, vemos que nós terminamos 85% dos itens em 11 dias ou menos.

<img src="/cycle_time_scatterplot.png" alt="Scatterplot de lead time com dados reais e linhas de P50 e P85" style="width: 95%; max-height: 68%; object-fit: contain; display: block; margin: 1rem auto 0;" />



---
layout: default
class: full-height-img-slide
---

# Deixa o Excel te ajudar

<img class="slide-full-img" src="/excel-p85.png" alt="Planilha com explicacao visual do percentil p85" />

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

percentil(lead_times, 50)  # 4 dias
percentil(lead_times, 75)  # 8 dias
percentil(lead_times, 85)  # 11 dias
```

---
layout: default
---

# Agora temos nosso SLE (Service Level Expectation)


## Nosso SLE atual é de 11 dias com 85% de confiança.

**Ou seja, sabemos que qualquer trabalho termina em 11 dias ou menos em 85% dos casos.**

<p>
Por ser baseado em seus dados recentes, nesse número já está embutido tudo aquilo que a gente normalmente não inclui numa estimativa:
</p>

- Interrupções
- Troca de contexto
- Reuniões
- Multitasking
- Dias menos produtivos
- ...e tudo mais do tal "mundo real".

---
layout: default
---

# E como fazer previsão de entrega de um projeto com vários itens?

## Para isso, a gente pode usar Simulação de Monte Carlo.

Tudo começa calculando um outro número dos nossos dados de início e fim: quantos items terminaram por dia ("throughput", TP).

| Data | Itens terminados |
|---|---|
| 03/03/2026 | 1 |
| 04/03/2026 | 0 |
| 05/03/2026 | 1 |
| 06/03/2026 | 3 |
| 07/03/2026 | 2 |
| 08/03/2026 | 0 |
| 09/03/2026 | 0 |
| ... | ... |
| 14/04/2026 | 2 | 

---
layout: default
---

# Rodando 1 simulação de Monte Carlo

##  Tendo o TP, simular a entrega de 10 itens seria sortear dentre esses valores o TP diário até completar a entrega dos 10 itens. Uma simulação seria algo assim:

| Dia | Itens entregues | Itens restantes |
|---|---|---|
| 1 | 2 | 8 |
| 2 | 0 | 8 |
| 3 | 1 | 7 |
| 4 | 3 | 4 | 
| 5 | 0 | 4 |
| 6 | 2 | 2 |
| 7 | 1 | 1 |
| 8 | 1 | 0 |

Ou seja essa minha primeira simulação deu resultado de 8 dias.

---
layout: default
---

# Passo 1: função simula_entrega (1 execução)

```python
historico_tp = carrega_tp_csv()  # [1, 0, 1, 3, 2, 0, 0, ..., 2]

def simula_entrega(num_itens: int, historico: list[int]) -> int:
    restantes = num_itens
    dias = 0

    while restantes > 0:
        dias += 1
        restantes -= random.choice(historico)

    return dias

dias_para_10_itens = simula_entrega(10, historico_tp)
print(dias_para_10_itens)  # ex.: 8
```

---
layout: default
---

# Passo 2: 10.000 simulações + percentis com NumPy

```python
import numpy as np

resultados = [simula_entrega(10, historico_tp) for _ in range(10_000)]
# [8, 12, 9, 7, 15, 10, 11, 9, 14, 13, ..., 10]

p50, p85, p95 = np.percentile(resultados, [50, 85, 95])

print(f"P50={p50:.0f}  P85={p85:.0f}  P95={p95:.0f} dias")
# P50=10  P85=15  P95=20 dias
```

Ou seja, agora podemos dizer que temos 85% de confiança de entregar os 10 itens em 15 dias ou menos, e 95% de confiança de entregar em 20 dias ou menos.

Sem chute, sem reunião de estimativa, só com dados reais e simulação.


---
layout: default
---

# Simulando "Quantos itens até o dia X?"

## Também podemos simular "Quantos itens podemos entregar até o dia X?"

```python
def simula_itens(prazo: date, historico: list[int]) -> int:
    entregues = 0
    for _ in range((prazo - date.today()).days):
        entregues += random.choice(historico)
    return entregues

resultados = [simula_itens(date(2026, 6, 1), historico_tp) for _ in range(10_000)]
p50, p85, p95 = np.percentile(resultados, [50, 85, 95])

print(f"P50={p50:.0f}  P85={p85:.0f}  P95={p95:.0f} itens")
# P50=25  P85=30  P95=35 itens
```

Ou seja, temos 85% de confiança de entregar pelo menos 30 itens até o dia 01/06/2026.

---
layout: default
---

# E se o time precisa entregar mais rápido?

## O que **não** queremos é:

- Selecionar dados mais "bonitos", tirar outliers, ficar encontrando motivo para excluir dados.
- Pedir pro time "se esforçar mais", "focar", "evitar interrupções".
- Trabalhar com percentil 50 - isso significa que vocês vão errar metade das vezes, por definição.

<div class="m16"></div>

## O que **devemos** fazer é:

- Visualizar e gerenciar o fluxo de trabalho

---
layout: default
---

# Princípios de gestão de fluxo: Visualize o trabalho

<img class="slide-full-img" src="/kanban.png" alt="Quadro Kanban com colunas e cartões de trabalho" />

---
layout: default
class: little-law-slide
---

# Limite o trabalho em andamento (WIP)

## O WIP (Work In Progress) é o número de itens que estão sendo trabalhados ao mesmo tempo. 

Limitar o WIP ajuda a reduzir o tempo de ciclo, melhorar a qualidade e aumentar a satisfação do time.

A [Lei de Little](https://pt.wikipedia.org/wiki/Teoria_das_filas#Lei_de_Little) relaciona o tempo de ciclo, o WIP e a taxa de entrega (throughput):

$$
\Large\text{ Tempo de Ciclo} = \frac{\text{WIP}}{\text{ Taxa de Entrega (TP)}}
$$

---
layout: default
class: little-law-slide
---

# Limite o trabalho em andamento (WIP)

## O WIP (Work In Progress) é o número de itens que estão sendo trabalhados ao mesmo tempo. 

Limitar o WIP ajuda a reduzir o tempo de ciclo, melhorar a qualidade e aumentar a satisfação do time.

A [Lei de Little](https://pt.wikipedia.org/wiki/Teoria_das_filas#Lei_de_Little) relaciona o tempo de ciclo, o WIP e a taxa de entrega (throughput):

$$
\Large\text{🔽 Tempo de Ciclo} = \frac{\text{WIP}}{\text{🔼 Taxa de Entrega (TP)}}
$$

---
layout: default
class: little-law-slide
---

# Limite o trabalho em andamento (WIP)

## O WIP (Work In Progress) é o número de itens que estão sendo trabalhados ao mesmo tempo. 

Limitar o WIP ajuda a reduzir o tempo de ciclo, melhorar a qualidade e aumentar a satisfação do time.

A [Lei de Little](https://pt.wikipedia.org/wiki/Teoria_das_filas#Lei_de_Little) relaciona o tempo de ciclo, o WIP e a taxa de entrega (throughput):

$$
\Large\text{🔽 Tempo de Ciclo} = \frac{\text{🔽 WIP}}{\text{🔼 Taxa de Entrega (TP)}}
$$
