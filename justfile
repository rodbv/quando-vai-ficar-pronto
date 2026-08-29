default: run

# Alias para abrir o notebook principal
nb: notebook-open
slides:
    cd slides && npm run dev -- --remote --port 3030

slides-install:
    cd slides && npm install

slides-build:
    cd slides && npm run build

just-build: slides-install slides-build

run: slides-install slides-build slides

charts:
    uv run python generate_charts.py

# Notebook companion (SLE + Monte Carlo)
notebook-deps:
    uv run python -m pip install -U jupyter nbconvert


# Abre direto o notebook principal
notebook-open:
    uv run jupyter notebook notebook/previsao.ipynb

notebook:
    uv run python -m notebook --notebook-dir notebook

notebook-exec:
    cd notebook && uv run python -m nbconvert --to notebook --execute --ExecutePreprocessor.timeout=120 --output previsao.executed.ipynb previsao.ipynb
