---
brand: python-brasil
colorSchema: auto
theme: none
title: When will it be done?
author: Rodrigo Vieira
lang: en
info: |
  Talk from Python Brasil 2026 about delivery predictability with
  flow metrics and simulation.
fonts:
  sans: Roboto
  serif: Cascadia Mono
  mono: Cascadia Mono
  weights: '400,700'
transition: fade
mdc: true
lineNumbers: true
canvasWidth: 1280
aspectRatio: 16/9
routerMode: hash
layout: cover

---


# When will it<br>be done?

Answering the customer's most important question.

<a class="lang-link" href="https://rodbv.github.io/quando-vai-ficar-pronto/" lang="pt-BR">Versão em português</a>

---
layout: default
---


# About me

<ul style="font-size: 2.2rem; line-height: 1.5; margin-bottom: 1.5rem;">
    <li>Henrique's dad</li>
    <li>Senior Software Engineer at Loadsmart</li>
    <li>Contributor to Django and other open source projects</li>
    <li>Co-organizer of Python Floripa</li>
</ul>

<img src="/pyfln.png" alt="Python Floripa" style="height: 265px; border-radius: 16px; box-shadow: 0 4px 24px rgba(11, 26, 82, 0.15); margin-left: 2.8rem;" />

<div class="flex flex-col items-end gap-8" style="position: absolute; right: 3.2rem; bottom: 2.5rem;">
  <img src="/python-floripa-claro.png" alt="Python Floripa logo" class="dark:hidden" style="height: 48px;" />
  <img src="/python-floripa-escuro.png" alt="Python Floripa logo" class="hidden dark:block" style="height: 48px;" />
  <img src="/loadsmart_logo.png" alt="Loadsmart logo" style="height: 48px;" />
</div>

---
layout: full
class: quadrinho
---

<div class="cartoon-pane cartoon-en pane-tl" role="img" aria-label="Comic, panel 1: the team discusses estimates"></div>

---
layout: full
class: quadrinho
---

<div class="cartoon-pane cartoon-en pane-tr" role="img" aria-label="Comic, panel 2: the manager reports to leadership"></div>

---
layout: full
class: quadrinho
---

<div class="cartoon-pane cartoon-en pane-bl" role="img" aria-label="Comic, panel 3: an executive presents the date to the board"></div>

---
layout: full
class: quadrinho
---

<div class="cartoon-pane cartoon-en pane-br" role="img" aria-label="Comic, panel 4: a developer reads an email and panics"></div>
---
layout: default
---

# How do we get out of this trap?

## We want to stop giving estimates that turn into promises from one person or one team...

- "I think it will take about 4 or 5 days."

## ...and start giving forecasts based on data

- "Based on our recent deliveries, we are 85% confident that we will finish in 11 calendar days."


---
layout: default
---



# What we'll cover today

<ol style="font-size: 2.9rem; line-height: 1.5; margin-left: 2.2rem;">
    <li style="margin-bottom: 1.1rem; font-size: 2.2rem;">Estimates vs. forecasts: how they differ</li>
    <li style="margin-bottom: 1.1rem; font-size: 2.2rem;">How to forecast the delivery of 1 item</li>
    <li style="margin-bottom: 1.1rem; font-size: 2.2rem;">How to forecast the delivery of many items</li>
    <li style="font-size: 2.2rem;">How to deliver faster, the right way</li>
</ol>

<p style="position: absolute; bottom: 3.5rem; left: 2.8rem; right: 2.8rem; font-size: 1.35rem; color: var(--accent); opacity: 0.75;">
  You'll find all the code, links and references at the end, in a QR code.
</p>


---
layout: default
---

# What is an estimate?

<div class="flex justify-center mt-6">
  <img src="/bug.png" alt="Two bugs: on the left a guess, on the right an estimate, which is the same bug in a suit" class="h-auto rounded-xl" style="max-height: 340px; margin-bottom: 0.4rem;" />
</div>

<p style="text-align: center; font-size: 1rem; color: var(--muted); margin: 0 0 1rem;">Left: a guess. Right: an estimate, which is a guess in a suit.</p>

<h3 style="text-align: center;">We can't avoid estimates completely, but we can use fewer of them and stop stacking one estimate on top of another.</h3>

---
layout: default
class: definition-slide
---

# What is a forecast?

## A **forecast** is a statement about the future, based on historical data, that gives the probability of a specific outcome.


**A forecast has two parts:**

- **A date (or a range of dates)** for the result
- **A level of confidence** (for example, an 85% chance)

**Examples:**

- "We are 85% confident that we will deliver **this item** by **May 11**."
- "We are 85% confident that we will finish **at least** **12 items** by **May 20**."

---
layout: default
---

# Why do our estimates always seem too low?

## Our brain (and our optimism) assumes a normal distribution

<img src="/normal_distribution_curve.en.png" alt="Reference normal distribution curve" style="width: 92%; max-height: 72%; object-fit: contain; display: block; margin: 1.2rem auto 0;" />

---
layout: default
---

# Our kind of work has a "long tail"

## Surprises are more likely to **delay** delivery than to speed it up.

<img src="/skewed_distribution_curve.en.png" alt="Real lead time distribution with a long tail" style="width: 92%; max-height: 72%; object-fit: contain; display: block; margin: 1.2rem auto 0;" />

---
layout: default
---

# How can we forecast without estimation meetings?

## You only need two things for each work item:

- The start date
- The end date

| Start | End |
|---|---|
| 2026-03-03 | 2026-03-03 |
| 2026-03-03 | 2026-03-06 |
| 2026-03-04 | 2026-03-08 |
| 2026-03-05 | 2026-03-09 |
| 2026-03-06 | 2026-03-11 |
| 2026-03-07 | 2026-03-10 |
| 2026-03-10 | 2026-03-15 |
| 2026-03-12 | 2026-03-18 |


---
layout: default
---

# How can we forecast without estimation meetings?

## From these dates, we calculate how many days each item took (the "cycle time").

| Start | End | Days |
|---|---|---|
| 2026-03-03 | 2026-03-03 | 1 |
| 2026-03-03 | 2026-03-06 | 4 |
| 2026-03-04 | 2026-03-08 | 5 |
| 2026-03-05 | 2026-03-09 | 5 |
| 2026-03-06 | 2026-03-11 | 6 |
| 2026-03-07 | 2026-03-10 | 4 |
| 2026-03-10 | 2026-03-15 | 6 |
| 2026-03-12 | 2026-03-18 | 7 |



---
layout: default
class: full-height-img-slide
hide: true
---

# Lead time distribution

## The area to the left of 11 days holds 85% of the items

<img src="/cycle_time_histogram.en.png" alt="Lead time histogram with the 85th percentile highlighted" style="width: 95%; max-height: 68%; object-fit: contain; display: block; margin: 1rem auto 0;" />


---
layout: default
class: full-height-img-slide
---

# Now we can forecast 1 item


## Recent data shows that we finish 85% of our items in 11 days or less.

<img src="/cycle_time_scatterplot.en.png" alt="Scatterplot of real lead times with P50 and P85 lines" style="width: 95%; max-height: 68%; object-fit: contain; display: block; margin: 1rem auto 0;" />



---
layout: default
class: full-height-img-slide
---

# Let the spreadsheet do the math

<img class="slide-full-img" src="/excel-p85.png" alt="Spreadsheet with the formula for the 85th percentile" />

---
layout: default
class: code-slide
---

# Or even better: Python

```python
import math
import numpy as np

lead_times = load_days_csv()

def percentile(data: list[int], p: float) -> int:
        return math.ceil(np.percentile(data, p))

print(percentile(lead_times, 85)) # 11

```

---
layout: default
---

# Now we have our SLE (Service Level Expectation)


## Based on recent data, our SLE is 11 days with 85% confidence.

**This means that 85% of our work items finish in 11 days or less.**

<p>
This number comes from our recent data, so it already includes everything we usually leave out of an estimate:
</p>

- Interruptions
- Context switching
- Meetings
- Multitasking
- Less productive days
- ...and everything else that happens in real life.

---
layout: default
---

# Forecasting many items: the Monte Carlo method

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 2rem; margin-top: 1rem;">
  <div style="display: flex; align-items: center; justify-content: center;">
    <img src="/mcs.png" alt="The Monte Carlo method" style="width: 90%;" />
  </div>
  <div>
    <ul style="font-size: 1.5rem; line-height: 2.4rem;">
      <li>Created by Ulam, von Neumann and Metropolis at <strong>Los Alamos</strong> (1946 to 1947), as part of the US nuclear program</li>
      <li>Main idea: use <strong>random sampling</strong> for problems with no analytical solution. We can't calculate every possibility, but enough random samples <strong>converge on the right answer</strong>.</li>
    </ul>
  </div>
</div>

---
layout: default
---

# Forecasting a project with many items


### From the same data, we calculate our **daily delivery rate** (*throughput*, TP).


| Date | Items delivered (daily TP) |
|---|---|
| 2026-03-03 | 1 |
| 2026-03-04 | 0 |
| 2026-03-05 | 1 |
| 2026-03-06 | 3 |
| 2026-03-07 | 2 |
| ... | ... |
| 2026-04-14 | 2 |

---
layout: default
---

# Running 1 Monte Carlo simulation for 50 items

###  We draw random daily TP values from this history until we reach 50 items. One run looks like this:


| Day | Items delivered | Remaining |
|---|---|---|
| 1 | 0 | 50 |
| 2 | 1 | 49 |
| 3 | 0 | 49 |
| 4 | 2 | 47 |
| 5 | 0 | 47 |
| 6 | 1 | 46 |
| ... | ... | ... |
| 23 | 1 | 0 |

This first run took 23 days.

---
layout: default
---

# Step 1: the simulate_delivery function (1 run)

```python
import random

tp_history = load_tp_csv()  # [1, 0, 1, 3, 2, 0, 0, ..., 2]

def simulate_delivery(num_items: int, history: list[int]) -> int:
    remaining = num_items
    days = 0

    while remaining > 0:
        days += 1
        remaining -= random.choice(history)

    return days

simulate_delivery(50, tp_history) # e.g. 23
```

---
layout: default
---

# Step 2: 10,000 simulations + percentiles with NumPy

```python
import numpy as np

results = [simulate_delivery(50, tp_history) for _ in range(10_000)]
# [23, 27, 21, 25, 30, 24, 22, 26, 28, 24, ..., 25]

p50, p85, p95 = np.percentile(results, [50, 85, 95])

print(f"P50={p50:.0f}  P85={p85:.0f}  P95={p95:.0f} days")
# P50=24  P85=30  P95=34 days
```

So now we can say: we are 85% confident that we will deliver the 50 items in 30 days or less. We are 95% confident that we will deliver them in 34 days or less.

No guesswork, no estimation meeting: just real data and a simulation.


---
layout: default
class: full-height-img-slide
---

# Result: 10,000 Monte Carlo simulations

## Distribution of the results, with confidence percentiles

<img src="/monte_carlo_resultado_daily.en.png" alt="Histogram of 10,000 Monte Carlo simulations with P50, P85 and P95 lines" style="width: 96%; max-height: 72%; object-fit: contain; display: block; margin: 1rem auto 0;" />


---
layout: default
---

# Simulating deliveries up to a deadline

## For each day until the deadline, we pick a random TP from the history and add up the delivered items:

| Day | Random TP | Delivered (total) |
|---|---|---|
| 1 | 1 | 1 |
| 2 | 0 | 1 |
| 3 | 2 | 3 |
| 4 | 1 | 4 |
| 5 | 0 | 4 |
| 6 | 3 | 7 |
| ... | ... | ... |
| N | 1 | 26 |

This simulation delivered **26 items** by the deadline.

---
layout: default
---

# Step 2: 10,000 simulations of "how many items by day X?"

```python
def simulate_items(deadline: date, history: list[int]) -> int:
    delivered = 0
    for _ in range((deadline - date.today()).days):
        delivered += random.choice(history)
    return delivered

results = [simulate_items(date(2026, 6, 1), tp_history) for _ in range(10_000)]
p15, p50, p85 = np.percentile(results, [15, 50, 85])

print(f"P15={p15:.0f}  P50={p50:.0f}  P85={p85:.0f} items")
# P15=59  P50=72  P85=86 items
```

Here, a higher percentile means more items. So the number with the highest confidence is the lowest one: we are **85% confident** that we will deliver at least **59 items** by June 1, 2026.

---
layout: default
class: full-height-img-slide
---

# Result: 10,000 simulations of "how many items by June 1?"

## The shaded area shows that 85% of the simulations deliver P15 items **or more**

<img src="/monte_carlo_itens.en.png" alt="Histogram of 10,000 simulations of how many items are done by the deadline, with P15 highlighted as the safe forecast" style="width: 96%; max-height: 64%; object-fit: contain; display: block; margin: 1rem auto 0;" />

---
layout: default
---

# What if the team needs to deliver faster?

## What we do **not** want:

- Cherry-pick the data, remove outliers, or look for reasons to exclude data.
- Ask the team to "try harder", "focus" or "avoid interruptions".
- Use the 50th percentile: by definition, you'll be wrong half the time.

<div class="m16"></div>

## What we **should** do:

- Make the flow of work visible, and manage it

---
layout: default
class: full-height-img-slide
---

# Make the work visible

<img class="slide-full-img" src="/trello-kanban.png" alt="Kanban board with columns and work cards" />

---
layout: default
class: little-law-slide
---

# Limit work in progress (WIP)

## WIP (Work In Progress) is the number of items that are in progress at the same time.

A WIP limit reduces cycle time. It makes us finish work before we start new work (less multitasking).

<div class="quote-block">
Stop starting, start finishing!
</div>

---
layout: default
class: little-law-slide
---

# Little's Law

<div style="display: grid; grid-template-columns: 1fr auto; gap: 2rem; align-items: start;">
<div>

## It connects cycle time, WIP and the delivery rate (throughput):

$$
\Large\text{ Cycle Time} = \frac{\text{WIP}}{\text{ Delivery Rate (TP)}}
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

# Little's Law

<div style="display: grid; grid-template-columns: 1fr auto; gap: 2rem; align-items: start;">
<div>

## When the delivery rate goes up, cycle time goes down:

$$
\Large\downarrow\!\text{Cycle Time} = \frac{\text{WIP}}{\uparrow\!\text{Delivery Rate (TP)}}
$$

This is the intuitive approach: if we finish items faster, each item takes less time.

In practice, it usually turns into asking the team to "try harder", which is on the list of what we do **not** want.

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

# Little's Law

<div style="display: grid; grid-template-columns: 1fr auto; gap: 2rem; align-items: start;">
<div>

## When WIP goes down, cycle time also goes down:

$$
\Large\downarrow\!\text{Cycle Time} = \frac{\downarrow\!\text{WIP}}{\text{Delivery Rate (TP)}}
$$

This is the lever that the team controls: start fewer items at the same time.

With the same delivery rate, each item waits less and finishes sooner. Nobody needs to work harder.

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

- Our goal is to deliver work, not to start it
- Before you start new work, check if you can finish something that is already in progress, including your colleagues' items
- A strict WIP limit makes the team finish what it already started, instead of starting more things.


---
layout: default
class: compacto
---

# Watch the age of items in progress

## "Item Age" is the number of days that an item has been in progress, without being finished.

Every new item has a **15% chance of going over the SLE of 11 days**.

But an item that has been in progress for 6 days is already in the long tail of the distribution. Its chance goes up to more than **40%**.

If an item is taking a long time, investigate:

<div class="grid grid-cols-2 gap-8 mt-2">
<div>

- Is there a **blocker**? Can several people work on it together?
- Did the **scope grow** after the work started?
- Is someone **working on it right now**?
- Did it **lose priority**? Should we cancel it?

</div>
<div class="flex items-center justify-center">
  <img src="/card_age.png" alt="Item age on the board" style="max-height: 300px; border-radius: 12px; box-shadow: 0 4px 24px rgba(0,0,0,0.25);" />
</div>
</div>

---
layout: default
---

# Control the size of items (right-sizing)

## For each new card, ask one question, based on the current SLE:

<div class="quote-block">
Are we confident that this will finish within our SLE?
</div>

If the team hesitates, split the card: review the scope, discuss what you can deliver first, and negotiate what is necessary.

You do not need a precise estimate. You need enough confidence.


---
layout: default
---

# Conclusion

- When customers ask for estimates and speed, they usually need **predictability and transparency**.
- For 1 item, use cycle time percentiles. For many items, use a Monte Carlo simulation.
- Always communicate the uncertainty: a date and a confidence level.
- Start small: record the start and end dates, calculate your SLE, and make the work visible.

---
layout: default
---

# Learn more

<div class="flex items-center gap-10 mt-4">
  <div class="flex flex-col items-center gap-3">
    <a href="https://actionableagile.com/books/aamfp/" target="_blank" rel="noopener">
      <img src="/vacanti.webp" alt="Actionable Agile Metrics for Predictability, by Daniel S. Vacanti" style="height: 384px; border-radius: 8px; box-shadow: 0 4px 24px rgba(0,0,0,0.18);" />
    </a>
  </div>
  <div class="flex flex-col items-center gap-3">
    <a href="https://www.focusedobjective.com/throughput" target="_blank" rel="noopener">
      <img src="/forecaster.png" alt="Advanced forecasting simulator (Troy Magennis)" style="height: 384px; border-radius: 8px; box-shadow: 0 4px 24px rgba(0,0,0,0.18);" />
    </a>
  </div>
  <ul style="font-size: 1.7rem; line-height: 1.6; color: var(--text);">
    <li style="margin-bottom: 2rem;">Books and videos by Daniel Vacanti<br><a href="https://actionableagile.com" target="_blank" rel="noopener" style="color: var(--accent); font-size: 1.6rem;">actionableagile.com</a></li>
    <li>Advanced simulator (Troy Magennis)<br><a href="https://www.focusedobjective.com/throughput" target="_blank" rel="noopener" style="color: var(--accent); font-size: 1.6rem;">focusedobjective.com/throughput</a></li>
    <li style="margin-top: 2rem; font-weight: 700; font-size: 2rem; color: var(--accent);">Let's talk!</li>
  </ul>
</div>

---
layout: default
semRodape: true
---

# Thank you! {.text-center}

<div class="flex justify-center gap-10 mt-3 text-2xl font-medium" style="color: var(--accent);">
  <span style="display: inline-flex; align-items: center; gap: 0.3em;"><img src="/linkedin.svg" alt="LinkedIn" style="height: 1em;" /> <a href="https://www.linkedin.com/in/rodrigobvieira/" target="_blank" rel="noopener" style="color: inherit; text-decoration: none;">rodrigobvieira</a></span>
  <span style="display: inline-flex; align-items: center; gap: 0.3em;"><img src="/mastodon-icon.png" alt="Mastodon" style="height: 1em;" /> <a href="https://pynews.com.br/@rodbv" target="_blank" rel="noopener" style="color: inherit; text-decoration: none;">pynews.com.br/@rodbv</a></span>
</div>

<img src="/qrcode.png" alt="QR code that links to the talk repository on GitHub" class="block mx-auto mt-6 h-auto rounded-2xl shadow-md" style="width: 42%; max-width: 540px; min-width: 220px;" />

<div class="absolute bottom-0 left-0 pb-6 px-10">
  <img src="/loadsmart_logo.png" alt="Loadsmart logo" class="h-10" />
</div>
