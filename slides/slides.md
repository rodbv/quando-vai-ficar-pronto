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

<ul style="font-size: 2.2rem; line-height: 1.5; margin-bottom: 1.5rem;">
    <li>Pai do Henrique</li>
    <li>Tech Lead na Vinta Software, empresa de Recife que nasceu na comunidade Python Nordeste</li>
    <li>Contribuidor do Django e outros projetos open source</li>
    <li>Co-organizador da Python Floripa</li>
</ul>

<img src="/pyfln.png" alt="Python Floripa" style="height: 265px; border-radius: 16px; box-shadow: 0 4px 24px rgba(2, 128, 144, 0.15); margin-left: 2.8rem;" />

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

<p style="position: absolute; bottom: 3.5rem; left: 2.8rem; right: 2.8rem; font-size: 1.35rem; color: var(--teal); opacity: 0.75;">
  Todo o código, links e referências desta apresentação estarão disponíveis ao final — vou mostrar um QR Code.
</p>


---
layout: default
---

# O que é uma estimativa?

<div class="flex justify-center mt-6">
  <img src="/bug.png" alt="Chute vs Estimativa" class="h-auto rounded-xl" style="max-height: 380px; margin-bottom: 1.5rem;" />
</div>

<h3 style="text-align: center; color: #000;">É impossível evitar estimativas totalmente, porém, podemos minimizá-las</h3>

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

- “Temos 85% de confiança de entregar **este item** até **11 de maio**.”
- “Temos 70% de chance de entregar **esses 5 itens** entre **10 e 15 de maio**.”
- “Temos 85% de confiança que vamos terminar **pelo menos** **12 itens** até o dia **20 de maio**.”

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

## E a partir disso, calcular quantos dias cada item levou ("Tempo de ciclo").

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
hide: true
---

# Distribuição do lead time

## A área à esquerda de 11 dias representa 85% dos itens

<img src="/cycle_time_histogram.png" alt="Histograma de lead time com percentil 85 destacado" style="width: 95%; max-height: 68%; object-fit: contain; display: block; margin: 1rem auto 0;" />


---
layout: default
class: full-height-img-slide
---

# Com isso podemos dizer qual nossa previsão para 1 item


## Baseado nos dados recentes, vemos que nós terminamos 85% dos itens em 11 dias ou menos.

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

# Previsão de vários itens: O método Monte Carlo

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 2rem; margin-top: 1rem;">
  <div style="display: flex; align-items: center; justify-content: center;">
    <img src="/mcs.png" alt="Método Monte Carlo" style="width: 90%;" />
  </div>
  <div>
    <ul style="font-size: 1.5rem; line-height: 2.4rem;">
      <li>Concebido por Ulam, Von Neumann e Metropolis em <strong>Los Alamos</strong> (1946–47), no programa nuclear americano</li>
      <li>Ideia central: <strong>amostragem aleatória</strong> para aproximar problemas sem solução analítica — em vez de calcular todas as possibilidades (inviável), amostras aleatórias suficientes <strong>convergem para a resposta correta</strong></li>
    </ul>
  </div>
</div>

---
layout: default
---

# Previsão de entrega de um projeto com vários itens 


### A partir dos mesmos dados de antes, calculamos nossa **taxa de entrega diária** (*throughput*, TP).


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

###  Para 10 itens, vamos sortear dentre esses valores o TP diário até completar essa quantidade. Uma rodada seria assim:


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

Essa primeira simulação deu resultado de 23 dias.

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

# Simulando entregas até uma data limite

## Para cada dia restante até a data limite, sorteamos um TP do histórico e acumulamos os itens entregues:

| Dia | TP sorteado | Entregues (acumulado) |
|---|---|---|
| 1 | 1 | 1 |
| 2 | 0 | 1 |
| 3 | 2 | 3 |
| 4 | 1 | 4 |
| 5 | 0 | 4 |
| 6 | 3 | 7 |
| ... | ... | ... |
| N | 1 | 26 |

Essa simulação resultou em **26 itens** entregues até a data limite.

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

Aqui os percentis são crescentes, então a maior confiança vem do valor à esquerda: temos **85% de confiança** de entregar pelo menos **59 itens** até 01/06/2026.

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
class: full-height-img-slide
---

# Visualize o trabalho

<img class="slide-full-img" src="/trello-kanban.png" alt="Quadro Kanban com colunas e cartões de trabalho" />

---
layout: default
class: little-law-slide
---

# Limite o trabalho em andamento (WIP)

## O WIP (Work In Progress) é o número de itens que estão sendo trabalhados ao mesmo tempo. 

Limitar o WIP ajuda a reduzir o tempo de ciclo e nos leva a focar em terminar o trabalho antes de iniciar outro (reduzir multitasking).

<div class="quote-block">
Stop starting, start finishing!
</div>

---
layout: default
class: little-law-slide
---

# Lei de Little

<div style="display: grid; grid-template-columns: 1fr auto; gap: 2rem; align-items: start;">
<div>

## Relaciona o tempo de ciclo, o WIP e a taxa de entrega (throughput):

$$
\Large\text{ Tempo de Ciclo} = \frac{\text{WIP}}{\text{ Taxa de Entrega (TP)}}
$$

</div>
<div style="text-align: center; padding-top: 0.5rem;">
  <img src="/stuartlittle.jpeg" alt="Stuart Little" style="width: 240px; aspect-ratio: 4/3; object-fit: cover; border-radius: 8px;" />
  <p style="font-size: 0.9rem; margin-top: 0.4rem; opacity: 0.7;">Stuart Little</p>
</div>
</div>

---
layout: default
class: little-law-slide
---

# Lei de Little

<div style="display: grid; grid-template-columns: 1fr auto; gap: 2rem; align-items: start;">
<div>

## Relaciona o tempo de ciclo, o WIP e a taxa de entrega (throughput):

$$
\Large\text{ Tempo de Ciclo} = \frac{\text{WIP}}{\text{ Taxa de Entrega (TP)}}
$$

</div>
<div style="text-align: center; padding-top: 0.5rem;">
  <img src="/johnlittle.png" alt="John Little" style="width: 240px; border-radius: 8px;" />
  <p style="font-size: 0.9rem; margin-top: 0.4rem; opacity: 0.7;">John Little</p>
</div>
</div>

---
layout: default
class: little-law-slide
---

# Lei de Little

<div style="display: grid; grid-template-columns: 1fr auto; gap: 2rem; align-items: start;">
<div>

## Aumentando a taxa de entrega, o tempo de ciclo cai:

$$
\Large\textcolor{#02c39a}{\downarrow}\!\text{Tempo de Ciclo} = \frac{\text{WIP}}{\textcolor{#02c39a}{\uparrow}\!\text{Taxa de Entrega (TP)}}
$$

</div>
<div style="text-align: center; padding-top: 0.5rem;">
  <img src="/johnlittle.png" alt="John Little" style="width: 240px; border-radius: 8px;" />
  <p style="font-size: 0.9rem; margin-top: 0.4rem; opacity: 0.7;">John Little</p>
</div>
</div>

---
layout: default
class: little-law-slide
---

# Lei de Little

<div style="display: grid; grid-template-columns: 1fr auto; gap: 2rem; align-items: start;">
<div>

## Reduzindo o WIP, o tempo de ciclo também cai:

$$
\Large\textcolor{#02c39a}{\downarrow}\!\text{Tempo de Ciclo} = \frac{\textcolor{#02c39a}{\downarrow}\!\text{WIP}}{\text{Taxa de Entrega (TP)}}
$$

</div>
<div style="text-align: center; padding-top: 0.5rem;">
  <img src="/johnlittle.png" alt="John Little" style="width: 240px; border-radius: 8px;" />
  <p style="font-size: 0.9rem; margin-top: 0.4rem; opacity: 0.7;">John Little</p>
</div>
</div>

---
layout: default
hide: true
---

# "Stop starting, start finishing"

- A nossa meta não é iniciar trabalho, e sim entregar
- Antes de iniciar um novo trabalho, cheque se você pode terminar algo já em andamento, inclusive itens de colegas
- Um limite estrito de WIP garante que o time foque em terminar o que já começou, ao invés de começar mais coisas.


---
layout: default
---

# Monitore a idade dos itens em andamento

## "Item Age" é há quantos dias um item está em progresso - sem ter terminado.

Todo item novo tem **15% de chance de estourar o SLE de 11 dias**.

Mas um item com 6 dias em andamento já entrou na cauda longa da distribuição - essa chance sobe para mais de **40%**.

Se um item está demorando, investigue:

<div class="grid grid-cols-2 gap-8 mt-2">
<div>

- Tem algum **bloqueador**? Podemos fazer um mutirão?
- O **escopo cresceu** depois que começou?
- Tem alguém **trabalhando nisso agora**?
- **Perdeu prioridade**? Vale a pena cancelar?

</div>
<div class="flex items-center justify-center">
  <img src="/card_age.png" alt="Item age no quadro" style="max-height: 300px; border-radius: 12px; box-shadow: 0 4px 24px rgba(0,0,0,0.25);" />
</div>
</div>

---
layout: default
---

# Controle o tamanho dos itens (Right-Sizing)

## Para cada card novo, faça uma pergunta simples a partir do SLE atual:

<div class="quote-block">
Estamos confiantes de que isso termina abaixo do nosso SLE?
</div>

Se a resposta for hesitante, quebre o card: reavalie o escopo, discuta o que pode ser entregue antes, negocie o que é necessário.

Não precisa estimar com precisão. Só precisa de confiança suficiente.


---
layout: default
---

# Conclusão

- Quando o cliente pede estimativa e velocidade, normalmente o que ele precisa é **previsibilidade e transparência**.
- Para 1 item use percentis de tempo de ciclo, para vários itens use simulação de Monte Carlo.
- Sempre comunique a incerteza: data + confiança.
- Comece pequeno: registre data de início e fim, calcule SLE, torne o trabalho visível.

---
layout: default
---

# Para ver mais

<div class="flex items-center gap-10 mt-4">
  <div class="flex flex-col items-center gap-3">
    <a href="https://actionableagile.com/books/aamfp/" target="_blank" rel="noopener">
      <img src="/vacanti.webp" alt="Actionable Agile Metrics for Predictability - Daniel S. Vacanti" style="height: 384px; border-radius: 8px; box-shadow: 0 4px 24px rgba(0,0,0,0.18);" />
    </a>
  </div>
  <div class="flex flex-col items-center gap-3">
    <a href="https://www.focusedobjective.com/throughput" target="_blank" rel="noopener">
      <img src="/forecaster.png" alt="Simulador avançado (Troy Magennis)" style="height: 384px; border-radius: 8px; box-shadow: 0 4px 24px rgba(0,0,0,0.18);" />
    </a>
  </div>
  <ul style="font-size: 1.7rem; line-height: 1.6; color: var(--secondary);">
    <li style="margin-bottom: 2rem;">Livros e vídeos do Daniel Vacanti<br><a href="https://actionableagile.com" target="_blank" rel="noopener" style="color: var(--teal); font-size: 1.6rem;">actionableagile.com</a></li>
    <li>Simulador avançado (Troy Magennis)<br><a href="https://www.focusedobjective.com/throughput" target="_blank" rel="noopener" style="color: var(--teal); font-size: 1.6rem;">focusedobjective.com/throughput</a></li>
    <li style="margin-top: 2rem; font-weight: 700; font-size: 2rem; color: var(--teal);">Vem falar comigo!</li>
  </ul>
</div>

---
layout: default
footer: false
---

# Obrigado! {.text-center}

<div class="flex justify-center gap-10 mt-3 text-2xl font-medium" style="color: var(--teal);">
  <span style="display: inline-flex; align-items: center; gap: 0.3em;"><img src="/linkedin.svg" alt="LinkedIn" style="height: 1em;" /> <a href="https://www.linkedin.com/in/rodrigobvieira/" target="_blank" rel="noopener" style="color: inherit; text-decoration: none;">rodrigobvieira</a></span>
  <span style="display: inline-flex; align-items: center; gap: 0.3em;"><img src="/mastodon-icon.png" alt="Mastodon" style="height: 1em;" /> <a href="https://pynews.com.br/@rodbv" target="_blank" rel="noopener" style="color: inherit; text-decoration: none;">pynews.com.br/@rodbv</a></span>
</div>

<img src="/qrcode.png" alt="QR Code" class="block mx-auto mt-6 h-auto rounded-2xl shadow-md" style="width: 42%; max-width: 540px; min-width: 220px;" />

<div class="absolute bottom-0 left-0 pb-6 px-10">
  <img src="/vinta_logo.png" alt="Logo da Vinta" class="h-10" />
</div>
