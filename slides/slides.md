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
Boas-vindas rápidas e diretas.
Pergunta de abertura: "Quem aqui ouviu essa pergunta esta semana?".
Conta até dois antes de seguir.
-->

---
layout: center
class: text-center
---

<div style="font-size: 2.8rem; font-weight: 800; line-height: 1.2; font-family: 'Manrope', sans-serif">

"Quando isso vai<br>ficar pronto?"

</div>

<div class="mt-8 text-2xl" style="color: var(--brand-text-muted)">

A pergunta que paralisa qualquer dev

</div>


<!--
Pausa curta para a plateia se reconhecer na cena.
Peça mão levantada para engajar logo no começo.
-->

---

# O cenário clássico

<div class="speech-bubble mt-6">
  <p>"Essas 15 features que a gente pediu... quando ficam prontas?"</p>
</div>


- Silêncio constrangedor
- "Temos 40 story points, talvez 3 semanas?"
- Cliente: **"Então 3 semanas. Tô anotando."**


<!--
Conta quase como uma cena de standup: ritmo e pausa no final.
Segura 1 segundo antes de "Tô anotando" para gerar desconforto proposital.
-->

---

# Roteiro de hoje


Problema com médias e story points

Estimativa vs Forecast

QFP visual para 1 item + QFP probabilístico para backlog



<div class="tip-box mt-6">

O fio condutor é simples: para 1 item, olhe **tempo por item**. Para vários itens, olhe **itens por tempo**.

</div>


<!--
Mostre o mapa da conversa em 10 segundos.
Isso reduz ansiedade de quem não é técnico e prepara a transição para estatística.
-->

---

# O problema com Story Points

Story Points medem **complexidade relativa**, não **tempo**


- Servem para **planejar sprint**, não para prever data de entrega
- Velocidade muda semana a semana e entre times
- Converter points para horas só multiplica erro



<div class="tip-box mt-6">

⚠️ Usar story points pra prever datas é como usar o tamanho da camiseta pra calcular quanto tempo leva pra costurá-la

</div>


<!--
Frase-chave: "Não é anti-story-points; é anti-uso indevido".
Reforce que a crítica é sobre previsão de data, não sobre planejamento de sprint.
-->

---

# "Mas a gente usa velocity..."

Velocity é uma média — e médias mentem com dados assim


- Média não representa bem distribuições com cauda longa
- Velocity × story points vira previsão pela média do cycle time
- Resultado prático: erro frequente e viés de subestimativa


<img src="/cycle_time_histogram.png" class="chart-img" />



<div class="tip-box mt-4">

Em dados com cauda longa, prever por média erra muito e tende a subestimar prazo.

</div>


<!--
Fale "essa é a armadilha da média" e aponte a cauda longa no gráfico.
Evite debate teórico longo: o ponto prático é viés de subestimativa.
Resumo oral: média em cauda longa parece precisa, mas gera promessa otimista.
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

"baseado nos últimos 3 meses, há 85% de chance de levar até 14 dias"

</div>

</div>


<div class="mt-8 text-center" style="color: var(--brand-text-muted)">

A boa notícia? Você já tem os dados. Só não tá usando ainda.

</div>


<!--
Ponto central da talk: não removemos incerteza; damos nome e faixa para ela.
Repita devagar: "estimativa é palpite, forecast é probabilidade".
-->

---

# Essa não é uma ideia nova

<div class="grid grid-cols-2 gap-8 mt-8">

<div class="metric-card">

### Daniel Vacanti

*Actionable Agile Metrics for Predictability* (2015)
*When Will It Be Done?* (2018)

Métricas de fluxo, SLE e previsibilidade

</div>

<div class="metric-card">

### Troy Magennis

*Focused Objective* — simuladores gratuitos

Monte Carlo baseado em throughput,
duas perguntas de forecasting

</div>

</div>


<div class="mt-6 text-center" style="color: var(--brand-text-muted)">

Esta talk aplica o trabalho deles em Python com dados reais

</div>


<!--
Dê crédito em 15 segundos e siga.
Use esta ponte: "vamos pegar essa base e transformar em algo que você roda hoje".
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


<div class="mt-6 text-center" style="color: var(--brand-text-muted)">

Esses três pilares ajudam a enxergar gargalos e melhorar previsibilidade

</div>


<!--
Nesta versão da talk, manter o foco prático nas métricas e no forecasting.
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


```
494 tasks entregues
Cycle time médio: 10.2 dias
```


<!--
Mostre que a barreira técnica é baixa.
Gancho para o próximo slide: "agora vem a parte que a média esconde".
-->

---

# QFP de 1 item: Scatterplot (visual)

Pergunta: "Se eu começar um item hoje, quando ele tende a terminar?"

<img src="/cycle_time_scatterplot.png" class="chart-img" />

<!--
Vantagem do scatterplot sobre o histograma: você vê QUANDO os outliers aconteceram.
"Aquela semana com tarefas de 45 dias — o que estava acontecendo ali?"
Você consegue correlacionar com eventos do projeto (lançamento, mudança de time, etc).
As linhas horizontais são os percentis — elas mostram o SLE visualmente.
-->

---

# Transformando visual em forecast de 1 item (SLE)

Termo de Vacanti: uma promessa baseada em percentil histórico

```python
ct = df["cycle_time_days"]

for p in [50, 70, 85, 95]:
    print(f"  SLE {p}%: ≤ {ct.quantile(p / 100):.0f} dias")
```


```
  SLE 50%: ≤ 5 dias
  SLE 70%: ≤ 8 dias
  SLE 85%: ≤ 14 dias   ← ponto de partida recomendado
  SLE 95%: ≤ 31 dias
```



<div class="tip-box mt-4">

**"85% das tasks ficam prontas em até 14 dias"** — isso é uma SLE. Não é promessa, é probabilidade com nome.

</div>


<!--
Frase de bolso para levar para o trabalho: "Nossa SLE atual é 14 dias no P85".
Reforce: SLE não é garantia, é expectativa probabilística explícita.
-->

---

# Item Age: WIP que envelhece

Outro conceito de Vacanti — para gerenciar itens **em andamento**


- Cycle Time mede tarefas **concluídas**
- **Item Age** mede há quantos dias um item em andamento existe
- Passou do P85 da SLE: tratar como risco e intervir



<div class="tip-box mt-4">

**Standup de fluxo:** em vez de "o que fiz ontem?", pergunte *"qual o item mais velho em andamento?"*

</div>


<!--
Este é um slide de gestão diária, não de estatística.
Faça a pergunta em voz alta: "qual item está velho demais e por quê?".
Feche com ação: identificar bloqueio e reduzir risco antes do atraso virar fato.
-->

---

# De "acho que..." pra SLE

<div class="text-center my-8">

<div class="text-2xl mb-6" style="text-decoration: line-through; color: var(--brand-text-muted)">

"Essa task deve levar uns 5 dias"

</div>


<div class="text-2xl font-semibold" style="color: var(--brand-green)">

"Nossa SLE é 14 dias no P85 — 85% das tasks entregam em até 14 dias"

</div>


</div>


<div class="text-center" style="color: var(--brand-text-muted)">

Mesma incerteza. Comunicação muito mais honesta — e rastreável.

</div>


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
semanas = pd.period_range(df["semana"].min(), df["semana"].max(), freq="W")
throughput = df.groupby("semana").size().reindex(semanas, fill_value=0)

print(f"Médio: {throughput.mean():.1f} tasks/semana")
print(f"Mín:   {throughput.min()} tasks/semana")
print(f"Máx:   {throughput.max()} tasks/semana")
```


```
Médio: 14.1 tasks/semana
Mín:   4 tasks/semana
Máx:   27 tasks/semana
```


<!--
A variação é real: mín 4, máx 27. Quase 7x de diferença.
Feriados, bugs críticos, onboarding, dívida técnica...
O time não é uma máquina constante — e é exatamente por isso que simulação funciona melhor que fórmula.
Com 3 meses (~12 semanas) já dá para começar com um forecast útil.
-->

---

# Para muitos itens: cycle time ou throughput?


- Para **1 item**, use distribuição de cycle time
- Para **N itens em paralelo**, o sinal de capacidade está no **throughput por período**
- Monte Carlo para backlog usa throughput semanal (ou diário)



<div class="tip-box mt-6">

Crítica importante: se o tamanho do time mudou muito, o throughput histórico antigo pode não representar o futuro. Nesses casos, use janela recente, segmente por fase ou normalize por FTE.

</div>


<!--
Mensagem curta e firme: 1 item = cycle time; muitos itens = throughput.
Ressalva honesta: se o sistema mudou muito, recorte uma janela mais recente.
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


- Story Points dependem de calibração subjetiva
- Cycle Time e Throughput são dados objetivos do fluxo real
- Dados históricos + simulação geram probabilidade, não chute



<div class="tip-box mt-4">

Não é que story points são ruins. É que eles não foram feitos pra isso.

</div>


<!--
Evite polarização.
Frase útil: "story points para conversa de esforço; throughput/cycle time para conversa de prazo".
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


<div class="tip-box mt-6">

Mesma base de dados, mesma simulação — pergunta diferente. Nesta talk: foco no **"quando"**.

</div>


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

QFP de muitos itens com distribuição de throughput

<!--
Abra esta seção com: "agora junta tudo em um algoritmo simples".
-->

---
layout: center
---

# "Monte Carlo... parece coisa de físico nuclear"


<div class="text-2xl mt-6" style="color: var(--brand-text-muted)">

Na verdade é só sortear muito

</div>


<!--
Quebrar o gelo. Monte Carlo tem nome grandioso mas a ideia é simples demais.
-->

---

# A intuição por trás

Você quer saber: **quando 40 features novas ficam prontas?**


- Sorteia aleatoriamente o throughput das semanas históricas
- Acumula semanas até completar as 40 tarefas
- Repete 10.000 vezes e observa a distribuição



<div class="tip-box mt-4">

"Dado que o passado é o melhor previsor que temos, o que aconteceria em 10 mil cenários possíveis?"

</div>


<!--
Ponto-chave: não inventamos nada. Só reamostramos do que JÁ aconteceu.
Se o time teve semanas de 4 e semanas de 42, a simulação vai refletir isso.
-->

---

# Setup: o que você precisa

```bash
uv sync
# ou: uv add pandas numpy matplotlib
```


<div class="mt-10 text-center text-xl" style="color: var(--brand-text-muted)">

Só isso. Sem ML, sem modelo complexo, sem dependência de nuvem.

</div>


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
df = df[df["cycle_time_days"] > 0]  # remove somente registros inválidos

# Throughput por semana — base da simulação
df["semana"] = df["finished_at"].dt.to_period("W")
semanas = pd.period_range(df["semana"].min(), df["semana"].max(), freq="W")
throughput_historico = df.groupby("semana").size().reindex(semanas, fill_value=0).values
```

<div class="tip-box mt-4">

Não "higienize" a variabilidade real: doença, férias, incidentes e itens muito longos também fazem parte do futuro. Limpe apenas erro de dado (ex.: data inválida), não eventos reais do sistema.
Se houve semana com zero entrega, mantenha zero no histórico (não remova da série).

</div>

<!--
Detalhe importante: este preparo de dados já evita um erro comum de forecast otimista.
Não apague semanas ruins nem outliers reais do processo.
Limpeza é só para erro de registro, não para "embelezar" histórico.
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
Em geral, 10.000 execuções rodam rapidamente em máquina comum (normalmente em segundos).
seed=42 garante resultados reproduzíveis entre apresentações.
Essa reamostragem preserva eventos raros (atrasos longos, semanas ruins), que são parte real do risco.
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


```
40 features entregues em:
  50% dos cenários:   3 semanas
  85% dos cenários:   4 semanas  ← use esse
  95% dos cenários:   5 semanas
```


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
Apontar: a distribuição não é normal; cauda à direita é esperada em software.
A linha laranja (P85) é o compromisso padrão para conversa externa.
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

"Rodei uma simulação com os últimos 3 meses de dados reais. Com 85% de confiança, essas 40 features ficam prontas em 4 semanas. Se quiser 95%, são 5 semanas."

</div>

<!--
Contraste direto.
O "depois" é mais curto, mais confiante, e mais honesto sobre incerteza.
Não é arrogância — é profissionalismo com dados.
-->

---

# O que muda na conversa


- Você troca chute por opções com probabilidade
- O cliente entende incerteza como parte normal de software
- A negociação vira escopo vs prazo com dados


<!--
Use esta frase para negociação: "mais confiança custa escopo ou prazo".
O objetivo não é vencer discussão; é tornar trade-off explícito.
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


- Vai acontecer: P85 ainda implica 15% de chance de erro
- Quando errar, use os dados para explicar a causa
- Atualize a simulação com dados novos e recalcule o forecast



<div class="tip-box mt-6">

A confiança do cliente não vem de nunca errar. Vem de ser transparente quando erra.

</div>


<!--
Aqui vale desacelerar: erro não invalida o método; erro é parte da distribuição.
Mostre maturidade: explique causa, atualize dados, publique novo forecast.
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


**1. Exporte os dados**

Jira, ClickUp, Trello, Linear... todos têm export de CSV com datas de início e fim de cada tarefa

**2. Calcule os percentis**

São 10 linhas de Python. Você já viu aqui.

**3. Rode uma simulação**

Use o código desta talk como template. Adapte pro seu CSV.


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
  (flow metrics, SLE, forecasting)

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


**Registre datas de início e fim** de cada tarefa — esse é o único dado que você precisa

Story points **não preveem datas** — tudo bem, não é pra isso que servem

Cycle Time e Throughput **são dados que você já tem** no seu Jira

Monte Carlo **é sorteio em escala** — 50 linhas de Python, sem ML

Falar em **percentis** é mais honesto do que "acho que"


<!--
Recap em ritmo mais lento, como fechamento de história.
Cada linha deve soar como "takeaway" que a pessoa leva para segunda-feira.
-->

---
layout: center
class: text-center
---

# Quando vai ficar pronto?


<div class="text-3xl mt-8 font-semibold" style="color: var(--brand-green)">

"Com 85% de confiança: em até 4 semanas."

</div>



<div class="mt-12" style="color: var(--brand-text-muted)">

Obrigado!

`github.com/rodrigo/quando-vai-ficar-pronto`

</div>


<!--
Encerrar com a resposta pra pergunta do título.
Pausar depois de "Com 85% de confiança" — deixar a plateia processar o contraste com o início.
Aguardar antes de abrir pra perguntas.
-->
