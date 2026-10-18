---
brand: python-floripa
colorSchema: auto
theme: none
title: Como parar de perder tempo estimando prazo de entrega
author: Rodrigo Vieira
lang: pt-BR
info: |
  Palestra relâmpago na Python Floripa sobre previsão de entregas
  com tempo de ciclo e simulação de Monte Carlo.
fonts:
  sans: Poppins,Roboto
  mono: JetBrains Mono
  weights: '400,700,800'
layout: cover
transition: fade
---

# Como parar de perder tempo estimando prazo de entrega

Previsões com os dados que o seu time já tem

**Rodrigo Vieira** · Loadsmart

<!--
- 3 minutos no total. Uns 15 segundos por slide.
-->

---
layout: full
class: quadrinho
---

<div class="cartoon-pane pane-tl" role="img" aria-label="Quadrinho, painel 1: o time discute estimativas cheias de condições e alguém arrisca 5 ou 6 semanas"></div>

<!--
- O time chuta "5, 6 semanas, mas vai ser puxado", cheio de "se".
-->

---
layout: full
class: quadrinho
---

<div class="cartoon-pane pane-tr" role="img" aria-label="Quadrinho, painel 2: a gestora diz para a liderança que o time consegue em 5 semanas"></div>

<!--
- Na reunião de liderança, o "5 ou 6, se tudo der certo" vira "5 semanas".
-->

---
layout: full
class: quadrinho
---

<div class="cartoon-pane pane-bl" role="img" aria-label="Quadrinho, painel 3: no board, o diretor promete o projeto pronto em 5 semanas, dia 8 de junho"></div>

<!--
- No board, "5 semanas" vira uma data: 8 de junho.
-->

---
layout: full
class: quadrinho
---

<div class="cartoon-pane pane-br" role="img" aria-label="Quadrinho, painel 4: no dia seguinte, a desenvolvedora recebe o email da demo para clientes em 8 de junho e se assusta"></div>

<!--
- No dia seguinte, o chute virou demo para cliente.
-->

---

# Para 1 item: anote início e fim

| Início | Fim | Dias |
|---|---|---|
| 03/03 | 03/03 | 1 |
| 03/03 | 06/03 | 4 |
| 04/03 | 08/03 | 5 |
| 06/03 | 11/03 | 6 |
| 12/03 | 18/03 | 7 |

<p class="muted">Os dias de cada item já incluem reuniões, bloqueios e interrupções.</p>

<!--
- Só duas datas por item. O tempo de ciclo sai da subtração.
- Esse número carrega o "mundo real" que a estimativa esquece.
-->

---
class: grafico
---

# 85% dos itens terminam em <mark>11 dias</mark> ou menos

<img src="/cycle_time_scatterplot.png" alt="Scatterplot do tempo de ciclo de cerca de 200 itens reais de 2026, com a linha do P50 em 4 dias e a do P85 em 11 dias" />

<!--
- Cada ponto é um item entregue. A linha de cima é o P85.
- A previsão tem data e confiança: "85% de chance de terminar em 11 dias ou menos".
-->

---

# Para N itens: sorteie o histórico

```python
historico = entregas_por_dia()  # [1, 0, 1, 3, 2, 0, ...]

def simula(itens: int) -> int:
    dias = 0
    while itens > 0:
        dias += 1
        itens -= random.choice(historico)
    return dias

resultados = [simula(50) for _ in range(10_000)]
np.percentile(resultados, 85)  # 30
```

<!--
- O histórico é quantos itens o time entregou em cada dia.
- Cada simulação sorteia um dia do histórico até acabarem os itens.
- Isso é Monte Carlo: 10 mil simulações e um percentil.
-->

---
class: grafico
---

# 85% de confiança: <mark>50 itens em 30 dias</mark> ou menos

<img src="/monte_carlo_resultado_daily.png" alt="Histograma de 10 mil simulações de Monte Carlo para 50 itens, com P50 em 24 dias, P85 em 30 dias e P95 em 34 dias" />

<!--
- Cada barra conta quantas simulações terminaram naquele dia.
- Nada de P50: com ele, você erra metade das vezes.
- Sem reunião de estimativa: só as datas de início e fim.
-->

---
layout: two-cols
---

# A palestra completa

**Quando vai ficar pronto?**

Slides, notebook e referências no QR code

<p class="muted">linkedin.com/in/rodrigobvieira<br>pynews.com.br/@rodbv</p>

::right::

<div class="flex flex-col items-center justify-center h-full">
  <img src="/qrcode.png" alt="QR code para github.com/rodbv/quando-vai-ficar-pronto" class="qr" />
  <p class="qr-legenda">github.com/rodbv/quando-vai-ficar-pronto</p>
</div>

<!--
- A versão completa mostra como acelerar entregas: limite de WIP, idade dos itens e Lei de Little.
-->
