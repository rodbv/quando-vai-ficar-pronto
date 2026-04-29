---
theme: seriph
colorSchema: auto
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


# Quem sou eu

<ul style="font-size: 2.5rem; line-height: 1.5; margin-bottom: 2.5rem;">
    <li>Pai do Henrique</li>
    <li>Co-organizador da Python Floripa</li>
    <li>Tech Lead na Vinta Software, empresa de Recife que nasceu na comunidade Python Nordeste</li>
    <li>Contribuidor do Django e outros projetos Open Source.</li>
</ul>

<img src="/vinta_logo.png" alt="Logo da Vinta" style="height: 48px; position: absolute; left: 2.5rem; bottom: 2.5rem;" />

---
layout: default
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



# O que vamos ver hoje

<ol style="font-size: 2.9rem; line-height: 1.5; margin-left: 2.2rem;">
    <li style="margin-bottom: 1.1rem; font-size: 2.2rem;">Estimativa vs. Previsão: por que são coisas diferentes</li>
    <li style="margin-bottom: 1.1rem; font-size: 2.2rem;">Como prever a entrega de 1 item</li>
    <li style="margin-bottom: 1.1rem; font-size: 2.2rem;">Como prever a entrega de vários itens</li>
    <li style="font-size: 2.2rem;">Como acelerar entregas do jeito certo</li>
</ol>


---
layout: default
class: definition-slide
---

# O que é uma previsão?

## **Previsão** é uma declaração sobre o futuro baseada em dados históricos, que expressa a probabilidade de um determinado resultado.


**O que compõe uma previsão:**

- **Uma data (ou intervalo de datas)** para o resultado
- **Uma medida de confiança** (ex: 85% de chance)

**Exemplos:**

- “Temos 85% de confiança de entregar até **11 de maio**.”
- “Temos 70% de chance de entregar entre **10 e 15 de maio**.”

<span style="font-size: 1.3rem; color: #4a8a84;">Baseado em <i>Actionable Agile Metrics</i></span>


---
layout: default
---

# Por que a gente parece sempre estimar por baixo?

## Nosso cérebro (e otimismo) pensa em distribuição normal

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

print(percentil(lead_time, 85)) # 11

```

---
layout: default
---

# Agora temos nosso SLE (Service Level Expectation)


## De acordo com os dados recentes, nosso SLE é de 11 dias com 85% de confiança.

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

# Previsão de entrega de um projeto com vários itens 

## Para diversos itens sendo trabalhados em paralelo, vamos usar Simulações de Monte Carlo.

A partir dos mesmos dados de antes, calculamos nossa **taxa de entrega diária** (*throughput*, TP).

| Data | Itens entregues (TP diário) |
|---|---|
| 03/03/2026 | 1 |
| 04/03/2026 | 0 |
| 05/03/2026 | 1 |
| 06/03/2026 | 3 |
| 07/03/2026 | 2 |
| ... | ... |
| 14/04/2026 | 2 | 

---
layout: default
---

# Rodando 1 simulação de Monte Carlo para 10 itens

##  Tendo o TP, simular a entrega de 10 itens seria sortear dentre esses valores o TP diário até completar a entrega dos 10 itens. Uma simulação seria algo assim:

| Dia | Itens entregues | Restantes |
|---|---|---|
| 1 | 0 | 10 |
| 2 | 1 | 9 |
| 3 | 0 | 9 |
| 4 | 2 | 7 |
| 5 | 0 | 7 |
| 6 | 1 | 6 |
| ... | ... | ... |
| 23 | 1 | 0 |

Essa minha primeira simulação deu resultado de 23 dias.

---
layout: default
---

# Passo 1: função simula_entrega (1 execução)

```python
import random

historico_tp = carrega_tp_csv()  # [1, 0, 1, 3, 2, 0, 0, ..., 2]

def simula_entrega(num_itens: int, historico: list[int]) -> int:
    restantes = num_itens
    dias = 0

    while restantes > 0:
        dias += 1
        restantes -= random.choice(historico)

    return dias

simula_entrega(10, historico_tp) # ex: 23
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
# P50=24  P85=30  P95=34 dias
```

Ou seja, agora podemos dizer que temos 85% de confiança de entregar os 10 itens em 30 dias ou menos, e 95% de confiança de entregar em 34 dias ou menos.

Sem chute, sem reunião de estimativa, só com dados reais e simulação.


---
layout: default
class: full-height-img-slide
---

# Resultado: 10.000 simulações de Monte Carlo

## Distribuição dos resultados com percentis de confiança

<img src="/monte_carlo_resultado_daily.png" alt="Histograma das 10.000 simulações de Monte Carlo com linhas P50, P85 e P95" style="width: 96%; max-height: 72%; object-fit: contain; display: block; margin: 1rem auto 0;" />


---
layout: default
---

# Rodando 1 simulação para "quantos itens até 01/06?"

## Para cada dia restante até o prazo, sorteamos um TP do histórico e acumulamos os itens entregues:

| Dia | TP sorteado | Entregues (acumulado) |
|---|---|---|
| 1 | 1 | 1 |
| 2 | 0 | 1 |
| 3 | 2 | 3 |
| 4 | 1 | 4 |
| 5 | 0 | 4 |
| 6 | 3 | 7 |
| ... | ... | ... |
| 34 | 1 | 26 |

Essa simulação resultou em **26 itens** entregues até 01/06/2026.

---
layout: default
---

# Passo 2: 10.000 simulações — "quantos itens até o dia X?"

```python
def simula_itens(prazo: date, historico: list[int]) -> int:
    entregues = 0
    for _ in range((prazo - date.today()).days):
        entregues += random.choice(historico)
    return entregues

resultados = [simula_itens(date(2026, 6, 1), historico_tp) for _ in range(10_000)]
p15, p50, p85 = np.percentile(resultados, [15, 50, 85])

print(f"P15={p15:.0f}  P50={p50:.0f}  P85={p85:.0f} itens")
# P15=59  P50=72  P85=86 itens
```

Aqui os percentis são **invertidos** em relação à previsão de data: P85=86 significa que 85% das simulações entregaram **86 ou menos** — só 15% de confiança de chegar lá.

Para dizer "85% de confiança de entregar **pelo menos** N itens", usamos o **P15**: temos 85% de confiança de entregar pelo menos **59 itens** até 01/06/2026.

---
layout: default
class: full-height-img-slide
---

# Resultado: 10.000 simulações — "quantos itens até 01/06?"

## A área verde mostra que 85% das simulações entregam P15 itens **ou mais**

<img src="/monte_carlo_itens.png" alt="Histograma das 10.000 simulações de quantos itens até o prazo, com P15 destacado como estimativa conservadora" style="width: 96%; max-height: 72%; object-fit: contain; display: block; margin: 1rem auto 0;" />

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
hide: true
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
hide: true
---

# Limite o trabalho em andamento (WIP)

## O WIP (Work In Progress) é o número de itens que estão sendo trabalhados ao mesmo tempo. 

Limitar o WIP ajuda a reduzir o tempo de ciclo, melhorar a qualidade e aumentar a satisfação do time.

A [Lei de Little](https://pt.wikipedia.org/wiki/Teoria_das_filas#Lei_de_Little) relaciona o tempo de ciclo, o WIP e a taxa de entrega (throughput):

$$
\Large\textcolor{#02c39a}{\downarrow}\!\text{Tempo de Ciclo} = \frac{\text{WIP}}{\textcolor{#02c39a}{\uparrow}\!\text{Taxa de Entrega (TP)}}
$$

---
layout: default
class: little-law-slide
hide: true
---

# Limite o trabalho em andamento (WIP)

## O WIP (Work In Progress) é o número de itens que estão sendo trabalhados ao mesmo tempo. 

Limitar o WIP ajuda a reduzir o tempo de ciclo, melhorar a qualidade e aumentar a satisfação do time.

A [Lei de Little](https://pt.wikipedia.org/wiki/Teoria_das_filas#Lei_de_Little) relaciona o tempo de ciclo, o WIP e a taxa de entrega (throughput):

$$
\Large\textcolor{#02c39a}{\downarrow}\!\text{Tempo de Ciclo} = \frac{\textcolor{#02c39a}{\downarrow}\!\text{WIP}}{\text{Taxa de Entrega (TP)}}
$$

---
layout: default
---

# "Stop starting, start finishing"

## Cada item novo que você inicia aumenta o WIP - e envelhece tudo que já está em andamento.

- Trabalho deve ser "puxado" e não "empurrrado", ou seja, só inicie um novo item quando tiver capacidade para isso.
- Priorize itens à direita no quadro - inclusive itens de colegas!
- Um limite estrito de WIP garante que o time foque em terminar o que já começou, ao invés de começar mais coisas.


---
layout: default
---

# Monitore a idade dos itens em andamento

## "Item Age" é há quantos dias um item está em progresso - sem ter terminado.

Todo item novo tem **15% de chance de estourar o SLE de 11 dias**.

Mas um item com 6 dias em andamento já entrou na cauda longa da distribuição - essa chance sobe para **~40%**.

| Item | Iniciado em | Idade atual | Risco de estourar SLE |
|---|---|---|---|
| Bug fix | 22/04 | 6 dias | 40% - zona de atenção |
| Feature A | 14/04 | 12 dias | já estourou |
| Relatório | 10/04 | 16 dias | 🚨 investigar bloqueio |

---
layout: default
---

# Reduza o tamanho dos itens (Right-Sizing)

## Para cada card novo, faça uma pergunta simples a partir do SLE atual:

<div class="quote-block">
"Estamos confiantes de que isso termina abaixo do nosso SLE?"
</div>

Se a resposta for hesitante, quebre o card: reavalie o escopo, discuta o que pode ser entregue antes, negocie o que é necessário.

Não precisa estimar com precisão. Só precisa de confiança suficiente.


---
layout: default
---

# Conclusão

- Quando o cliente pede estimativa e velocidade, normalmente o que ele precisa é **previsibilidade e transparência**.
- Para 1 item use percentis de lead time, para vários itens use simulação de Monte Carlo.
- Sempre comunique a incerteza: data + confiança.
- Comece pequeno: registre data de início e fim, calcule SLE, torne o trabalho visível.
- Estimativa é um nome bonito pra chute, e otimismo não é estratégia.

---
layout: default
---

# Para aprender mais

<div class="flex items-center gap-10 mt-4">
  <div class="flex flex-col items-center gap-3">
    <a href="https://actionableagile.com/books/aamfp/" target="_blank" rel="noopener">
      <img src="/vacanti.webp" alt="Actionable Agile Metrics for Predictability - Daniel S. Vacanti" style="height: 384px; border-radius: 8px; box-shadow: 0 4px 24px rgba(0,0,0,0.18);" />
    </a>
  </div>
  <div class="flex flex-col items-center gap-3">
    <a href="https://actionableagile.com/books/wwibd/" target="_blank" rel="noopener">
      <img src="/wwibd.jpeg" alt="When Will It Be Done? - Daniel S. Vacanti" style="height: 384px; border-radius: 8px; box-shadow: 0 4px 24px rgba(0,0,0,0.18);" />
    </a>
  </div>
  <ul style="font-size: 1.7rem; line-height: 1.6; color: var(--secondary);">
    <li style="margin-bottom: 2rem;">Livros e vídeos do Daniel Vacanti<br><a href="https://actionableagile.com" target="_blank" rel="noopener" style="color: var(--teal); font-size: 1.6rem;">actionableagile.com</a></li>
    <li>Blog posts do Troy Magennis<br><a href="https://www.focusedobjective.com" target="_blank" rel="noopener" style="color: var(--teal); font-size: 1.6rem;">focusedobjective.com</a></li>
  </ul>
</div>

---
layout: default
footer: false
---

# Obrigado! {.text-center}

<div class="flex justify-center gap-10 mt-3 text-2xl font-medium" style="color: var(--teal);">
  <span>📧 rodrigo.vieira@gmail.com</span>
  <span>🐘 @rodbv@pynews.com.br</span>
</div>

<img src="/qrcode.png" alt="QR Code" class="block mx-auto mt-6 h-auto rounded-2xl shadow-md" style="width: 42%; max-width: 540px; min-width: 220px;" />

<div class="text-center mt-8">
  <div class="text-2xl font-semibold" style="color: var(--baltic-blue);">github.com/rodbv/quando-vai-ficar-pronto</div>
  <div class="text-xl mt-1 text-gray-500">slides, código e notebook</div>
</div>

<div class="absolute bottom-0 left-0 pb-6 px-10">
  <img src="/vinta_logo.png" alt="Logo da Vinta" class="h-10" />
</div>
