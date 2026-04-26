# Quando vai ficar pronto?

Slides e materiais da palestra apresentada na Python Sul 2026, sobre previsibilidade de entregas com métricas de fluxo e simulação Monte Carlo.

## Slides

Acesse os slides online:
https://rodbv.github.io/quando-vai-ficar-pronto/

Ou rode localmente:

```sh
cd slides
npm install
npm run dev
```

## Geração de gráficos

Os gráficos usados nos slides são gerados a partir dos dados reais em `data/`:

```sh
just charts
# ou
uv run python generate_charts.py
```

## Notebook (SLE + Monte Carlo)

Para experimentar com os conceitos (SLE para 1 item, Monte Carlo para N itens), veja `notebook/`:
- `notebook/previsao.ipynb` — notebook companion dos slides
- `notebook/flow_forecast.py` — helpers do notebook (não compartilhado com `generate_charts.py`)

### CSV mínimo esperado

Um CSV com pelo menos estas colunas:
- `started_at`: data ou datetime (hora é ignorada)
- `finished_at`: data ou datetime (hora é ignorada)

Throughput sempre por dia (inclui fins de semana + zeros no intervalo).

### Rodar

Abra o `.ipynb` no Cursor e execute as células, ou rode Jupyter no ambiente do projeto:

```sh
uv run python -m pip install -U jupyter
uv run python -m notebook
```

## Deploy

O deploy é feito automaticamente para o GitHub Pages via GitHub Actions. O conteúdo publicado está em `gh-pages`.

## Estrutura
- `slides/` — Projeto Slidev (Markdown, CSS, assets)
- `data/` — Dados reais para simulação e gráficos
- `generate_charts.py` — Script para gerar gráficos
- `notebook/` — Notebook + helpers (SLE + Monte Carlo)
- `justfile` — Atalhos para build e automação

## Licença
MIT. Veja o arquivo LICENSE.
