---
theme: seriph
colorSchema: dark
css: ./style.css
title: Quando vai ficar pronto?
info: |
  Talk na Python Sul sobre previsibilidade de entregas com
  métricas de fluxo (Cycle Time, Throughput) e simulação de Monte Carlo.
drawings:
  persist: false
transition: fade
mdc: true
lineNumbers: false
highlighter: shiki
background: '#0d1117'
class: text-center
layout: cover
---

# Quando vai ficar pronto?

Respondendo a pergunta mais difícil do seu cliente **com dados**

<div class="talk-meta">
  Python Sul · 2026 · Rodrigo Vieira
</div>

<!--
Boas-vindas. Pergunta retórica pra começar: quantas vezes essa semana alguém te perguntou isso?
Deixar a pergunta no ar por dois ou três segundos antes de continuar.
-->

---
layout: center
class: text-center
---

<div style="font-size: 2.8rem; font-weight: 800; line-height: 1.2; font-family: 'Manrope', sans-serif">

"Quando isso vai<br>ficar pronto?"

</div>

<v-click>

<div class="mt-8 text-2xl" style="color: var(--brand-text-muted)">

A pergunta que paralisa qualquer dev

</div>

</v-click>

<!--
Pausa. Deixar a plateia reconhecer o sentimento.
Pergunta pra plateia: quem ouviu isso essa semana? Levanta a mão.
-->

---

# O cenário clássico

<div class="speech-bubble mt-6">
  <p>"Essas 15 features que a gente pediu... quando ficam prontas?"</p>
</div>

<v-clicks>

- Silêncio constrangedor 🫠
- Alguém abre o Jira
- *"Bom... temos umas 40 story points ainda..."*
- *"Considerando a velocidade do time... talvez 3 semanas?"*
- Cliente: **"Então 3 semanas. Tô anotando."**
- Você: 😬

</v-clicks>

<!--
Contar isso com energia. Pausa dramática antes de "Então 3 semanas. Tô anotando."
Todo mundo já viveu exatamente esse momento. É quase um trauma coletivo.
-->

---

# O problema com Story Points

Story Points medem **complexidade relativa**, não **tempo**

<v-clicks>

- Servem pra **planejar o sprint** — pra isso são ótimos
- Mas não pra prever datas de entrega
- Velocidade muda semana a semana
- Cada time calibra diferente
- Converter pra horas? Só multiplica o erro

</v-clicks>

<v-click>

<div class="tip-box mt-6">

⚠️ Usar story points pra prever datas é como usar o tamanho da camiseta pra calcular quanto tempo leva pra costurá-la

</div>

</v-click>

<!--
Importante: não tô falando pra jogar story points fora do planning.
Eles continuam sendo úteis. O ponto é que eles não foram feitos pra responder essa pergunta específica.
-->

---

# "Mas a gente usa velocity..."

Velocity é uma média — e médias mentem com dados assim

<v-clicks>

- Se Bill Gates entra num bar, **na média todo mundo ali é milionário**
- Usar velocity × story points = prever com a **média do cycle time**
- Pela definição de média: **você vai errar em ~50% dos casos**
- E como a distribuição de cycle time tem cauda longa, a média fica pra direita da mediana
- Resultado: você erra **mais de 50%** das vezes, sempre subestimando

</v-clicks>

<v-click>

<div class="tip-box mt-4">

Vacanti: *"Using averages for forecasting means you are wrong by definition half the time — and with skewed distributions, worse than half."*

</div>

</v-click>

<!--
Esse é o segundo nível do problema.
Não é só que story points medem complexidade — é que mesmo convertendo velocity pra dias, você usa a média.
E a média em distribuições com cauda longa não representa a maioria dos casos.
Quando o histograma aparecer, vai ficar visual: a média fica bem à direita de onde a maioria das tasks termina.
A analogia do Bill Gates é do próprio Vacanti e é ótima pra fixar o conceito.
-->

---

# A raiz do problema

<div class="text-center my-10">
<div style="font-size: 2.8rem; font-weight: 800; font-family: 'Manrope', sans-serif">
  <span style="color: var(--brand-red)">Estimativa</span>
  <span class="mx-6" style="color: var(--brand-text-muted)">≠</span>
  <span style="color: var(--brand-green)">Previsão</span>
</div>
</div>

<div class="grid grid-cols-2 gap-8">

<div class="p-5 rounded-lg" style="border: 1px solid var(--brand-red); background: var(--brand-red-dim)">

**Estimativa**

"acho que leva uns 5 dias"

</div>

<div class="p-5 rounded-lg" style="border: 1px solid var(--brand-green); background: var(--brand-green-dim)">

**Previsão**

"baseado nos últimos 3 meses, há 85% de chance de levar até 16 dias"

</div>

</div>

<v-click>

<div class="mt-8 text-center" style="color: var(--brand-text-muted)">

A boa notícia? Você já tem os dados. Só não tá usando ainda.

</div>

</v-click>

<!--
Esse é o ponto central da talk. A previsão não elimina a incerteza — ela a quantifica honestamente.
Guardem isso: estimativa é chute, previsão é probabilidade.
-->

---

# Essa não é uma ideia nova

<div class="grid grid-cols-2 gap-8 mt-8">

<div class="metric-card">

### Daniel Vacanti

*Actionable Agile Metrics for Predictability* (2015)
*When Will It Be Done?* (2018)

Métricas de fluxo, Little's Law, SLE

</div>

<div class="metric-card">

### Troy Magennis

*Focused Objective* — simuladores gratuitos

Monte Carlo baseado em throughput,
duas perguntas de forecasting

</div>

</div>

<v-click>

<div class="mt-6 text-center" style="color: var(--brand-text-muted)">

Esta talk aplica o trabalho deles em Python com dados reais

</div>

</v-click>

<!--
Dar crédito explícito. Vacanti é A referência em métricas de fluxo para software.
Magennis popularizou o Monte Carlo baseado em throughput pra times ágeis.
O que a gente vai ver aqui é a aplicação prática do trabalho deles.
-->

---
layout: section
---

# Métricas de Fluxo

Cycle Time, Throughput e WIP

<!--
Seção 2. Apresentar o que vem aí: duas métricas simples que mudam como a gente responde.
-->

---

# Três pilares de fluxo (Vacanti)

<div class="grid grid-cols-3 gap-5 mt-8">

<div class="metric-card">

### Cycle Time

Quanto tempo uma tarefa leva do início ao fim

*Do "em andamento" ao "done"*

</div>

<div class="metric-card">

### Throughput

Quantas tarefas são entregues por semana

*O ritmo real da equipe*

</div>

<div class="metric-card">

### WIP

Work In Progress — quantas tarefas estão ativas ao mesmo tempo

*O que está em andamento agora*

</div>

</div>

<v-click>

<div class="mt-6 text-center" style="color: var(--brand-text-muted)">

Esses três pilares se conectam por uma lei fundamental

</div>

</v-click>

<!--
Vacanti usa esses três como o triângulo de métricas de fluxo.
WIP é especialmente importante: alto WIP = cycle time longo (vai ficar claro no próximo slide).
O triângulo é: se você controla dois, o terceiro é calculável.
-->

---

# Little's Law

<div class="text-center my-10">
<div style="font-size: 2.8rem; font-weight: 700; font-family: 'JetBrains Mono', monospace">
  CT = WIP / Throughput
</div>
</div>

<v-clicks>

- **WIP alto + throughput constante** → cycle time sobe
- **Quer entregar mais rápido?** Reduza o WIP — não acelere o time
- É uma lei matemática, não uma sugestão
- Funciona pra fila de banco, restaurante, e squad de desenvolvimento

</v-clicks>

<v-click>

<div class="tip-box mt-4">

*"Stop starting, start finishing"* — o slogan do Kanban tem base matemática

</div>

</v-click>

<!--
Little's Law foi provada em 1961 por John Little. Vale pra qualquer sistema de fila.
Implicação prática: puxar mais tasks em paralelo não acelera entrega — aumenta cycle time.
Isso é contra-intuitivo pra muita gente. Deixar a afirmação pousar antes de continuar.
-->

---

# Cycle Time: do dado ao número

```python
import pandas as pd

# Exportou do Jira/ClickUp/Trello? Adapte as colunas aqui
df = pd.read_csv(
    "lead_time_data.csv",
    header=None,
    names=["started_at", "finished_at", "cycle_time_days"],
)

df = df[df["cycle_time_days"] > 0]  # remove anomalias de dados

print(f"{len(df)} tasks entregues")
print(f"Cycle time médio: {df['cycle_time_days'].mean():.1f} dias")
```

<v-click>

```
494 tasks entregues
Cycle time médio: 10.2 dias
```

</v-click>

<!--
Simples assim. Você exporta os dados, carrega no pandas, tem o número em 5 linhas.
Mas a média sozinha está escondendo uma coisa importante — vamos ver o quê.
-->

---

# A distribuição importa mais que a média

<img src="/cycle_time_histogram.png" class="chart-img" />

<!--
Apontar a cauda longa no histograma.
A maioria das tasks termina em 1-7 dias, mas outliers puxam a média pra cima.
"Média de 10.2 dias" — lembra do Bill Gates? É exatamente isso acontecendo aqui.
A linha azul (P50) fica bem à esquerda da média. Quem prevê com a média sempre subestima.
-->

---

# Cycle Time Scatterplot

Vacanti prefere esse gráfico: cada ponto é uma tarefa real

<img src="/cycle_time_scatterplot.png" class="chart-img" />

<!--
Vantagem do scatterplot sobre o histograma: você vê QUANDO os outliers aconteceram.
"Aquela semana com tarefas de 45 dias — o que estava acontecendo ali?"
Você consegue correlacionar com eventos do projeto (lançamento, mudança de time, etc).
As linhas horizontais são os percentis — elas mostram o SLE visualmente.
-->

---

# SLE — Service Level Expectation

Termo de Vacanti: uma promessa baseada em percentil histórico

```python
ct = df["cycle_time_days"]

for p in [50, 70, 85, 95]:
    print(f"  SLE {p}%: ≤ {ct.quantile(p / 100):.0f} dias")
```

<v-click>

```
  SLE 50%: ≤ 5 dias
  SLE 70%: ≤ 8 dias
  SLE 85%: ≤ 14 dias   ← ponto de partida recomendado
  SLE 95%: ≤ 31 dias
```

</v-click>

<v-click>

<div class="tip-box mt-4">

**"85% das tasks ficam prontas em até 14 dias"** — isso é uma SLE. Não é promessa, é probabilidade com nome.

</div>

</v-click>

<!--
SLE = Service Level Expectation, conceito de Vacanti.
É a resposta padrão que você dá quando alguém pergunta "quanto tempo leva uma task?"
"Nossa SLE é 14 dias no P85" — qualquer PO ou cliente entende.
A diferença pro SLA tradicional: você não promete que TODO item vai caber, você define a probabilidade.
-->

---

# Item Age: WIP que envelhece

Outro conceito de Vacanti — para gerenciar itens **em andamento**

<v-clicks>

- Cycle Time mede tarefas **concluídas**
- **Item Age** mede tarefas em andamento: há quantos dias essa task começou?
- Item com age acima do P50 da SLE? Atenção redobrada — risco aumentando
- Item com age acima do P85? Já está na cauda longa — precisa de intervenção

</v-clicks>

<v-click>

<div class="tip-box mt-4">

**Standup de fluxo:** em vez de "o que fiz ontem?", pergunte *"qual o item mais velho em andamento?"*

</div>

</v-click>

<!--
Item Age é a aplicação proativa do Cycle Time.
Em vez de esperar o item terminar pra ver que demorou muito, você monitora enquanto ainda dá pra agir.
Exemplo: "essa task está há 18 dias em andamento, nossa SLE é 14 dias no P85 — o que está travando?"
Isso é o que Vacanti chama de gerenciar pelo processo, não pelo resultado.
-->

---

# De "acho que..." pra SLE

<div class="text-center my-8">

<div class="text-2xl mb-6" style="text-decoration: line-through; color: var(--brand-text-muted)">

"Essa task deve levar uns 5 dias"

</div>

<v-click>

<div class="text-2xl font-semibold" style="color: var(--brand-green)">

"Nossa SLE é 14 dias no P85 — 85% das tasks entregam em até 14 dias"

</div>

</v-click>

</div>

<v-click>

<div class="text-center" style="color: var(--brand-text-muted)">

Mesma incerteza. Comunicação muito mais honesta — e rastreável.

</div>

</v-click>

<!--
A mudança de linguagem importa.
"SLE de 14 dias" posiciona você como quem trabalha com dados, não chute.
E é rastreável: depois você pode medir se a SLE foi cumprida — o que alimenta o ciclo de melhoria.
-->

---

# Throughput: o ritmo da equipe

```python
df["finished_at"] = pd.to_datetime(df["finished_at"])
df["semana"] = df["finished_at"].dt.to_period("W")

throughput = df.groupby("semana").size()

print(f"Médio: {throughput.mean():.1f} tasks/semana")
print(f"Mín:   {throughput.min()} tasks/semana")
print(f"Máx:   {throughput.max()} tasks/semana")
```

<v-click>

```
Médio: 14.1 tasks/semana
Mín:   4 tasks/semana
Máx:   27 tasks/semana
```

</v-click>

<!--
A variação é real: mín 4, máx 27. Quase 7x de diferença.
Feriados, bugs críticos, onboarding, dívida técnica...
O time não é uma máquina constante — e é exatamente por isso que simulação funciona melhor que fórmula.
Magennis recomenda pelo menos 10-15 semanas de dados pro Monte Carlo ser confiável.
Com 34 semanas aqui, estamos bem.
-->

---

# Throughput na prática

<img src="/throughput_weekly.png" class="chart-img" />

<!--
Mostrar o gráfico. Apontar as semanas mais fracas (feriados? onboarding?) e as mais fortes.
Perguntar: essa variação é parecida com o projeto de vocês?
A linha tracejada é a média — mas repara que quase nenhuma semana bate exatamente nela.
-->

---

# Por que isso é melhor que story points

<v-clicks>

- Story Points dependem de **calibração subjetiva** do time
- Cycle Time é **objetivo**: data de início → data de fim
- Story Points **variam** entre sprints e entre times
- Throughput captura o ritmo **real**, incluindo interrupções
- Story points → conversão pra horas → estimativa
- Dados históricos → simulação → **probabilidade**

</v-clicks>

<v-click>

<div class="tip-box mt-4">

Não é que story points são ruins. É que eles não foram feitos pra isso.

</div>

</v-click>

<!--
Reforçar: não é anti-ágil, é pró-dados.
Story points continuam úteis pro planejamento de sprint.
Mas pra perguntas de data de entrega, precisamos de outra ferramenta.
-->

---

# Duas perguntas, dois forecasts (Magennis)

<div class="grid grid-cols-2 gap-8 mt-8">

<div class="p-5 rounded-lg" style="border: 1px solid var(--brand-amber); background: var(--brand-amber-dim)">

### "Quando terminamos?"

Tenho N features no backlog.
Quando o time vai entregar todas?

→ Monte Carlo **"quando"**

</div>

<div class="p-5 rounded-lg" style="border: 1px solid var(--brand-blue); background: var(--brand-blue-dim)">

### "Quantas entregamos?"

Temos X semanas até o lançamento.
Quantas features cabem?

→ Monte Carlo **"quantas"**

</div>

</div>

<v-click>

<div class="tip-box mt-6">

Mesma base de dados, mesma simulação — pergunta diferente. Nesta talk: foco no **"quando"**.

</div>

</v-click>

<!--
Troy Magennis deixa claro que são duas perguntas distintas com respostas distintas.
"Quando terminamos 40 features?" é diferente de "quantas features entregamos até 15 de maio?"
Ambas usam o throughput histórico, mas a direção da simulação é invertida.
Vale mencionar que o código muda pouco — boa referência pro dev freelance levar pra casa.
-->

---
layout: section
---

# Simulação de Monte Carlo

Do passado pro futuro em 50 linhas de Python

<!--
Seção 3. Apresentar como as duas métricas anteriores se combinam numa simulação.
-->

---
layout: center
---

# "Monte Carlo... parece coisa de físico nuclear"

<v-click>

<div class="text-2xl mt-6" style="color: var(--brand-text-muted)">

Na verdade é só sortear muito

</div>

</v-click>

<!--
Quebrar o gelo. Monte Carlo tem nome grandioso mas a ideia é simples demais.
-->

---

# A intuição por trás

Você quer saber: **quando 40 features novas ficam prontas?**

<v-clicks>

- Você tem o histórico de **centenas de semanas** reais de entrega
- Sorteia aleatoriamente o throughput de cada semana
- Conta quantas semanas até completar 40 tarefas
- Repete isso **10.000 vezes**
- Olha a distribuição dos resultados

</v-clicks>

<v-click>

<div class="tip-box mt-4">

"Dado que o passado é o melhor previsor que temos, o que aconteceria em 10 mil cenários possíveis?"

</div>

</v-click>

<!--
Ponto-chave: não inventamos nada. Só reamostramos do que JÁ aconteceu.
Se o time teve semanas de 4 e semanas de 42, a simulação vai refletir isso.
-->

---

# Setup: o que você precisa

```bash
pip install pandas numpy matplotlib
```

<v-click>

<div class="mt-10 text-center text-xl" style="color: var(--brand-text-muted)">

Só isso. Sem ML, sem modelo complexo, sem dependência de nuvem.

</div>

</v-click>

<!--
Intencionalmente simples.
Qualquer dev pode rodar isso hoje no próprio projeto.
Se quiser testar agora mesmo: Google Colab, zero instalação.
-->

---

# Carregando e preparando os dados

```python
import pandas as pd
import numpy as np

# Exportou do Jira/ClickUp/Trello? Adapte as colunas aqui
df = pd.read_csv(
    "lead_time_data.csv",
    header=None,
    names=["started_at", "finished_at", "cycle_time_days"],
)
df["finished_at"] = pd.to_datetime(df["finished_at"])
df = df[df["cycle_time_days"] > 0]  # remove anomalias de dados

# Throughput por semana — base da simulação
df["semana"] = df["finished_at"].dt.to_period("W")
throughput_historico = df.groupby("semana").size().values
```

<!--
Destacar que adaptar pra outros sistemas é trivial — só mudar os nomes das colunas.
O filtro cycle_time > 0 é importante: dados reais têm sujeira (tasks reabertas, etc).
-->

---

# A simulação

```python
def monte_carlo_quando(throughput, n_items, n_sim=10_000, seed=42):
    """
    Pergunta: quantas semanas pra entregar n_items?

    Sorteia semanas do histórico real até acumular n_items entregues.
    Repete n_sim vezes e retorna a distribuição de semanas.
    """
    rng = np.random.default_rng(seed)
    resultados = []

    for _ in range(n_sim):
        entregues, semanas = 0, 0
        while entregues < n_items:
            entregues += rng.choice(throughput)  # sorteia uma semana do passado
            semanas += 1
        resultados.append(semanas)

    return np.array(resultados)

simulacao = monte_carlo_quando(throughput_historico, n_items=40)
```

<!--
Ir linha a linha.
O loop é o coração: sorteia uma semana, acumula entregas, conta semanas.
10.000 execuções rodam em menos de 1 segundo no laptop de qualquer um.
seed=42 garante resultados reproduzíveis entre apresentações.
-->

---

# Interpretando os resultados

```python
p50 = np.percentile(simulacao, 50)
p85 = np.percentile(simulacao, 85)
p95 = np.percentile(simulacao, 95)

print("40 features entregues em:")
print(f"  50% dos cenários:   {p50:.0f} semanas")
print(f"  85% dos cenários:   {p85:.0f} semanas  ← use esse")
print(f"  95% dos cenários:   {p95:.0f} semanas")
```

<v-click>

```
40 features entregues em:
  50% dos cenários:   3 semanas
  85% dos cenários:   4 semanas  ← use esse
  95% dos cenários:   5 semanas
```

</v-click>

<!--
Por que 85% e não 100%? Porque 100% incluiria o pior cenário absoluto — seria excessivamente conservador.
85% é o equilíbrio entre ser honesto (não subestimar) e prático.
Pra projetos críticos ou contratos com multa, use 95%.
-->

---

# O resultado visualmente

<img src="/monte_carlo_resultado.png" class="chart-img" />

<!--
Deixar o chart falar por si só por alguns segundos.
Apontar: a distribuição não é uma curva normal — tem cauda à direita.
Isso é característico de projetos de software.
A linha laranja (P85) é onde você committa com o cliente.
-->

---
layout: section
---

# Apresentando ao cliente

Como transformar número em conversa

<!--
Seção 4. Saber calcular é metade do caminho — saber comunicar é a outra metade.
-->

---
layout: two-cols
---

# Antes

<div class="before-card">

"Bom, a gente tem umas 80 story points, nossa velocidade tá em torno de 20 por sprint, então... uns 4 sprints? Talvez 6 semanas? Depende de vários fatores..."

</div>

::right::

# Depois

<div class="after-card">

"Rodei uma simulação com os últimos 8 meses de dados reais. Com 85% de confiança, essas 40 features ficam prontas em 4 semanas. Se quiser 95%, são 5 semanas."

</div>

<!--
Contraste direto.
O "depois" é mais curto, mais confiante, e mais honesto sobre incerteza.
Não é arrogância — é profissionalismo com dados.
-->

---

# O que muda na conversa

<v-clicks>

- Você para de **adivinhar** e começa a apresentar **opções com probabilidade**
- O cliente entende que existe **incerteza natural** — e isso é normal em software
- Vocês podem **negociar com dados**: "quer 95%? Reduz o escopo em 3 features"
- O histórico de entregas vira **ativo da relação**, não arquivo morto no Jira

</v-clicks>

<!--
Ponto-chave: você não elimina incerteza, você a quantifica.
Isso abre espaço pra negociações baseadas em dados, não em intuição.
"Quer mais confiança? O preço é escopo ou prazo" — essa conversa fica muito mais fácil.
-->

---

# Qual percentil usar?

<div class="grid grid-cols-3 gap-4 mt-8">

<div class="p-5 text-center rounded-lg" style="border: 1px solid var(--brand-blue); background: var(--brand-blue-dim)">

**P50**

Cenário otimista

Use pra motivar o time internamente

</div>

<div class="p-5 text-center rounded-lg" style="border: 1px solid var(--brand-amber); background: var(--brand-amber-dim)">

**P85**

Cenário realista

Use pra compromissos com cliente

</div>

<div class="p-5 text-center rounded-lg" style="border: 1px solid var(--brand-red); background: var(--brand-red-dim)">

**P95**

Cenário conservador

Use pra datas críticas ou contratos

</div>

</div>

<!--
Esse framework de três cenários é muito útil na prática.
Dá ao cliente a opção de escolher o nível de risco que quer assumir.
"Você quer 85% ou 95% de confiança?" é uma conversa muito diferente de "acho que 3 semanas".
-->

---

# E quando você erra?

<v-clicks>

- E vai acontecer — isso é esperado. P85 significa 15% de erro.
- Quando você erra, você **já tem os dados pra explicar por quê**
- "O throughput caiu pra 4 essa semana por um bug crítico, o histórico é 19"
- E você pode **atualizar a simulação** com os dados novos

</v-clicks>

<v-click>

<div class="tip-box mt-6">

A confiança do cliente não vem de nunca errar. Vem de ser transparente quando erra.

</div>

</v-click>

<!--
Esse ponto é especialmente importante pra gestores na plateia.
Monte Carlo não é uma promessa — é uma comunicação honesta de probabilidades.
E quando você erra com dados, você tem a narrativa, não só o resultado.
-->

---

# Como melhorar a previsibilidade

Dois rituais que mudam o jogo (Vacanti)

<div class="grid grid-cols-2 gap-8 mt-8">

<div class="metric-card">

### Standup de fluxo

Foco em **queue time** e **Item Age**

*"Qual o item mais velho em andamento? O que está bloqueando?"*

Não "o que fiz ontem" — mas **o que está travado**

</div>

<div class="metric-card">

### Retro de previsibilidade

Foco no **scatterplot** e na evolução do histograma

*"Estamos reduzindo nosso P85? O cycle time médio está caindo?"*

Medir melhoria com os mesmos dados

</div>

</div>

<!--
Esses dois rituais vêm diretamente de Vacanti.
Standup: o foco muda do passado (o que fiz) pro presente (o que está travado).
Retro: em vez de "como foi o sprint?", você olha se as métricas de fluxo estão melhorando.
São mudanças pequenas de pergunta — com impacto grande na previsibilidade do time.
-->

---
layout: section
---

# Como começar hoje

3 passos práticos

---

# 3 passos pra começar hoje

<v-clicks>

**1. Exporte os dados**

Jira, ClickUp, Trello, Linear... todos têm export de CSV com datas de início e fim de cada tarefa

**2. Calcule os percentis**

São 10 linhas de Python. Você já viu aqui.

**3. Rode uma simulação**

Use o código desta talk como template. Adapte pro seu CSV.

</v-clicks>

<!--
Intencionalmente simples. Três passos, qualquer um consegue hoje.
O maior obstáculo costuma ser o passo 1 — conseguir os dados em formato usável.
No Jira: Reports > Cycle Time. No ClickUp: export de tasks com datas de status.
-->

---

# Ferramentas e referências

<div class="grid grid-cols-2 gap-6 mt-4">

<div>

**Pra rodar hoje:**

- `pandas` + `numpy` + `matplotlib`
- Google Colab (zero instalação)
- Código: `github.com/rodrigo/quando-vai-ficar-pronto`

</div>

<div>

**Leitura obrigatória:**

- **Daniel Vacanti** — *Actionable Agile Metrics for Predictability* e *When Will It Be Done?*
  (flow metrics, SLE, Little's Law)

- **Troy Magennis** — focusedobjective.com
  (simuladores Excel/Sheets gratuitos, sem código)

</div>

</div>

<!--
Detalhe importante sobre Magennis: ele disponibiliza simuladores prontos no focusedobjective.com.
Pra quem não quer escrever código, é uma ótima entrada.
O livro do Vacanti é denso mas é A referência. O segundo livro ("When Will It Be Done?") é mais acessível.
-->

---
layout: center
class: text-center
---

# Resumindo

<v-clicks>

**Registre datas de início e fim** de cada tarefa — esse é o único dado que você precisa

Story points **não preveem datas** — tudo bem, não é pra isso que servem

Cycle Time e Throughput **são dados que você já tem** no seu Jira

Monte Carlo **é sorteio em escala** — 50 linhas de Python, sem ML

Falar em **percentis** é mais honesto do que "acho que"

</v-clicks>

<!--
Recap rápido. Cada ponto deve ressoar com algo que foi visto na talk.
Dar tempo pra cada ponto aparecer e processar antes de avançar.
-->

---
layout: center
class: text-center
---

# Quando vai ficar pronto?

<v-click>

<div class="text-3xl mt-8 font-semibold" style="color: var(--brand-green)">

"Com 85% de confiança: em até 4 semanas."

</div>

</v-click>

<v-click>

<div class="mt-12" style="color: var(--brand-text-muted)">

Obrigado!

`github.com/rodrigo/quando-vai-ficar-pronto`

</div>

</v-click>

<!--
Encerrar com a resposta pra pergunta do título.
Pausar depois de "Com 85% de confiança" — deixar a plateia processar o contraste com o início.
Aguardar antes de abrir pra perguntas.
-->
