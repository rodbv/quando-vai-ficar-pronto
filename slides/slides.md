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
lineNumbers: false
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

