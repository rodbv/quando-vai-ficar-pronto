---
theme: seriph
colorSchema: dark
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
background: '#0b1f1a'
layout: cover

---

# Quando vai ficar pronto?

Respondendo a pergunta mais importante do cliente.

<div class="talk-meta">
  Python Sul · 2026 · Rodrigo Vieira
</div>

---
layout: image
image: /trampo.png
backgroundSize: contain
---

---
layout: default
---

# Como sair dessa armadilha?

<div class="h-[72%] flex flex-col justify-center space-y-10 text-left">
  <div>
    <h3 class="text-2xl">Estimativa</h3>
    <div class="mt-4 text-[2.1rem] leading-tight">
      "Acho que dá dia 8 de junho"
    </div>
    <div class="mt-5 text-lg leading-relaxed opacity-85">
      Estimativa é palpite pontual.
    </div>
  </div>

  <div>
    <h3 class="text-2xl">Previsão</h3>
    <div class="mt-4 text-[2.1rem] leading-tight">
      "Temos 50% de confiança de entregar até dia 8 de junho, e 90% de confiança até dia 20."
    </div>
    <div class="mt-5 text-lg leading-relaxed opacity-85">
      Previsão tem dois elementos: uma faixa de datas com percentual de confiança.
    </div>
  </div>
</div>

---
layout: default
---

# Mas como fazer uma previsão?

<div class="h-[70%] flex flex-col justify-center items-start text-left">
  <ul class="text-left space-y-4 text-2xl leading-tight">
    <li>Jogo nos búzios?</li>
    <li>Claude?</li>
    <li>3 horas de reunião?</li>
  </ul>
</div>

---
layout: default
---

# Na verdade só juntar um dado que você provavelmente já tem:

<div class="h-[72%] flex flex-col justify-center">
  <ul class="text-left space-y-2 text-xl">
    <li>Data de início da tarefa</li>
    <li>Data de fim da tarefa</li>
  </ul>

  <div class="mt-6">
    <table>
      <thead>
        <tr>
          <th>INICIO</th>
          <th>FIM</th>
          <th>DIAS</th>
        </tr>
      </thead>
      <tbody>
        <tr><td>03/06/2026</td><td>08/06/2026</td><td>6</td></tr>
        <tr><td>04/06/2026</td><td>04/06/2026</td><td>1</td></tr>
        <tr><td>05/06/2026</td><td>07/06/2026</td><td>3</td></tr>
        <tr><td>14/06/2026</td><td>19/06/2026</td><td>5</td></tr>
      </tbody>
    </table>
  </div>
</div>


---
layout: default
---

# Prevendo 1 item: Scatterplot

<div class="h-[98%] mt-3 w-full overflow-hidden">
  <img src="/cycle_time_scatterplot.png" alt="Scatterplot de cycle time" class="h-full w-full object-contain" />
</div>

---
layout: default
---

# Mas eu não quero fazer esse treco


| INICIO     | FIM        | DIAS | P   |
| ---------- | ---------- | ---- | --- |
| 01/06/2026 | 01/06/2026 | 1    |     |
| 02/06/2026 | 03/06/2026 | 2    |     |
| 03/06/2026 | 04/06/2026 | 2    |     |
| 04/06/2026 | 06/06/2026 | 3    |     |
| 05/06/2026 | 08/06/2026 | 4    | 50  |
| 06/06/2026 | 09/06/2026 | 4    |     |
| 07/06/2026 | 10/06/2026 | 4    | 70  |
| 08/06/2026 | 12/06/2026 | 5    |     |
| 09/06/2026 | 14/06/2026 | 6    | 90  |
| 10/06/2026 | 20/06/2026 | 11   |     |

---
layout: default
---

# Mas eu quero usar Python

<div class="text-2xl">

```python {lines:true}
dias = sorted(row["dias"] for row in tarefas)

def percentil(dados, p):
    return dados[int(len(dados) * p / 100) - 1]

p50 = percentil(dias, 50)   # 5 dias
p85 = percentil(dias, 85)   # 14 dias
p95 = percentil(dias, 95)   # 31 dias
```

</div>

<style>
.slidev-code code, .slidev-code pre {
  font-size: 1.6rem !important;
  line-height: 1.6 !important;
}
</style>

---

# Monte Carlo em Python puro

<div class="text-[1.8rem] leading-tight">

```python {lines:true}
import csv, random

throughput = []
with open("data/throughput_latest_15w.csv") as f:
  for row in csv.DictReader(f):
    throughput.append(int(row["throughput"]))

def semanas_para_80_cards(tp):
  feitas, semanas = 0, 0
  while feitas < 80:
    feitas += random.choice(tp)
    semanas += 1
  return semanas

random.seed(42)
print(semanas_para_80_cards(throughput))
```

</div>

---

# Rastreando 1000 simulações para GIF

<div class="text-[1.45rem] leading-tight">

```python {lines:true}
import csv, random

rows = []
rng = random.Random(42)

for run_id in range(1, 1001):
  done, week_num = 0, 0
  while done < 80:
    week_num += 1
    picked = rng.choice(throughput)
    done += picked
    rows.append([run_id, week_num, picked, done])

with open("data/monte_carlo_trace_1k.csv", "w", newline="") as f:
  w = csv.writer(f)
  w.writerow(["run_id", "week_num", "throughput_picked", "cumulative_done"])
  w.writerows(rows)
```

</div>

---

# O que você já ganha com isso?


<div class="mt-20 text-2xl">

Agora o seu time já tem um SLE (Service Level Expectaction)


## Para qualquer tarefa, o time leva 14 dias para entregar, com 85% de confiança 

(agora para de ficar pedindo estimativa e deixa a gente trabalhar...)
</div>