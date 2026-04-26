slides:
    cd slides && npm run dev -- --remote --port 3030

slides-install:
    cd slides && npm install

slides-build:
    cd slides && npm run build

charts:
    uv run python generate_charts.py

# Notebook companion (SLE + Monte Carlo)
notebook-deps:
    uv run python -m pip install -U jupyter nbconvert

notebook:
    uv run python -m notebook --notebook-dir notebook

notebook-exec:
    cd notebook && uv run python -m nbconvert --to notebook --execute --ExecutePreprocessor.timeout=120 --output previsao.executed.ipynb previsao.ipynb
