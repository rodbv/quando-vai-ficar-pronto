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

## Deploy

O deploy é feito automaticamente para o GitHub Pages via GitHub Actions. O conteúdo publicado está em `gh-pages`.

## Estrutura
- `slides/` — Projeto Slidev (Markdown, CSS, assets)
- `data/` — Dados reais para simulação e gráficos
- `generate_charts.py` — Script para gerar gráficos
- `justfile` — Atalhos para build e automação

## Licença
MIT. Veja o arquivo LICENSE.
