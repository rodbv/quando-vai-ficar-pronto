"""
Gera os charts para a talk "Quando vai ficar pronto?"
Os charts são salvos em slides/public/ para uso no Slidev.

Uso:
    uv run python generate_charts.py
    # ou: just charts
"""

from pathlib import Path

import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import numpy as np
import pandas as pd

OUTPUT_DIR = Path("slides/public")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Paleta dark
BG = "#0d1117"
BG2 = "#161b22"
SURFACE = "#21262d"
TEXT = "#e6edf3"
TEXT_MUTED = "#8b949e"
GREEN = "#3fb950"
AMBER = "#e3b341"
BLUE = "#58a6ff"
RED = "#f85149"


def load_data() -> pd.DataFrame:
    df = pd.read_csv(
        "data/lead_time_data.csv",
        header=None,
        names=["started_at", "finished_at", "cycle_time_days"],
    )
    df["finished_at"] = pd.to_datetime(df["finished_at"])
    df["started_at"] = pd.to_datetime(df["started_at"])
    # Remove apenas registros impossíveis; não remove outliers válidos do fluxo.
    df = df[df["cycle_time_days"] > 0]
    return df


def weekly_throughput(df: pd.DataFrame) -> pd.Series:
    """Return weekly throughput including explicit zero-throughput weeks."""
    semana = df["finished_at"].dt.to_period("W")
    semanas = pd.period_range(semana.min(), semana.max(), freq="W")
    return semana.value_counts().sort_index().reindex(semanas, fill_value=0)


def print_stats(df: pd.DataFrame) -> None:
    ct = df["cycle_time_days"]
    throughput = weekly_throughput(df)

    print(f"\n{'=' * 52}")
    print(f"Total de tasks:  {len(df)}")
    print(
        f"Período:         {df['finished_at'].min().date()} → {df['finished_at'].max().date()}"
    )
    print(f"\nCycle Time (dias):")
    print(f"  Média:   {ct.mean():.1f}")
    print(f"  P50:     {ct.quantile(0.50):.0f}")
    print(f"  P70:     {ct.quantile(0.70):.0f}")
    print(f"  P85:     {ct.quantile(0.85):.0f}")
    print(f"  P95:     {ct.quantile(0.95):.0f}")
    print(f"\nThroughput semanal:")
    print(f"  Médio:   {throughput.mean():.1f} tasks/semana")
    print(f"  Mín:     {throughput.min()} tasks/semana")
    print(f"  Máx:     {throughput.max()} tasks/semana")
    print(f"{'=' * 52}\n")


def fig_cycle_time_histogram(df: pd.DataFrame) -> None:
    ct = df["cycle_time_days"]

    fig, ax = plt.subplots(figsize=(11, 5), facecolor=BG)
    ax.set_facecolor(BG)

    # Cap em 60 dias pra não distorcer visualmente pelos outliers
    ct_plot = ct[ct <= 60]

    ax.hist(ct_plot, bins=30, color=GREEN, edgecolor=BG, alpha=0.85)
    # Escala log melhora leitura quando alguns bins concentram muitos casos.
    ax.set_yscale("log")

    for pct, color, label in [
        (0.50, BLUE, "P50"),
        (0.85, AMBER, "P85"),
        (0.95, RED, "P95"),
    ]:
        val = ct.quantile(pct)
        ax.axvline(
            val,
            color=color,
            linewidth=2,
            linestyle="--",
            label=f"{label}: {val:.0f} dias",
        )

    ax.set_title("Distribuição do Cycle Time", color=TEXT, fontsize=14, pad=12)
    ax.set_xlabel("Dias", color=TEXT_MUTED)
    ax.set_ylabel("Número de tarefas (escala log)", color=TEXT_MUTED)
    ax.tick_params(colors=TEXT_MUTED)
    ax.legend(fontsize=11, facecolor=SURFACE, labelcolor=TEXT, edgecolor=SURFACE)
    for spine in ax.spines.values():
        spine.set_color("#30363d")

    fig.tight_layout()
    out = OUTPUT_DIR / "cycle_time_histogram.png"
    fig.savefig(out, dpi=150, bbox_inches="tight", facecolor=BG)
    plt.close(fig)
    print(f"✓ {out}")


def fig_normal_distribution_reference(
    mean_days: float = 5.0, median_days: float = 5.0, std_days: float = 1.6
) -> None:
    """Curva normal de referência com média/mediana fixadas em 5 dias."""
    x = np.linspace(0, 12, 600)
    y = (1 / (std_days * np.sqrt(2 * np.pi))) * np.exp(
        -0.5 * ((x - mean_days) / std_days) ** 2
    )

    fig, ax = plt.subplots(figsize=(11, 5), facecolor=BG)
    ax.set_facecolor(BG)

    ax.plot(x, y, color=GREEN, linewidth=3)
    ax.fill_between(x, y, color=GREEN, alpha=0.22)

    ax.axvline(
        mean_days,
        color=BLUE,
        linewidth=2.2,
        linestyle="--",
        label=f"Média: {mean_days:.0f} dias",
    )
    ax.axvline(
        median_days,
        color=AMBER,
        linewidth=2.2,
        linestyle=":",
        label=f"Mediana: {median_days:.0f} dias",
    )

    ax.set_title("Distribuição Normal (referência)", color=TEXT, fontsize=14, pad=12)
    ax.set_xlabel("Dias", color=TEXT_MUTED)
    ax.set_ylabel("Densidade", color=TEXT_MUTED)
    ax.set_xlim(0, 12)
    ax.tick_params(colors=TEXT_MUTED)
    ax.legend(fontsize=11, facecolor=SURFACE, labelcolor=TEXT, edgecolor=SURFACE)
    for spine in ax.spines.values():
        spine.set_color("#30363d")

    fig.tight_layout()
    out = OUTPUT_DIR / "normal_distribution_curve.png"
    fig.savefig(out, dpi=150, bbox_inches="tight", facecolor=BG)
    plt.close(fig)
    print(f"✓ {out}")


def fig_cycle_time_distribution_curve(df: pd.DataFrame) -> None:
    """Curva suavizada da distribuição real de cycle time (sem barras)."""
    ct = df["cycle_time_days"].to_numpy(dtype=float)

    # Exibe até o P99 para manter legibilidade sem perder a forma principal.
    x_max = int(np.ceil(np.percentile(ct, 99)))
    x_max = max(x_max, 15)
    bins = np.arange(0.5, x_max + 1.5, 1.0)

    hist, edges = np.histogram(ct, bins=bins, density=True)
    centers = (edges[:-1] + edges[1:]) / 2

    sigma_bins = 1.3
    radius = int(np.ceil(4 * sigma_bins))
    kernel_x = np.arange(-radius, radius + 1)
    kernel = np.exp(-0.5 * (kernel_x / sigma_bins) ** 2)
    kernel /= kernel.sum()
    smooth = np.convolve(hist, kernel, mode="same")

    fig, ax = plt.subplots(figsize=(11, 5), facecolor=BG)
    ax.set_facecolor(BG)

    ax.plot(centers, smooth, color=GREEN, linewidth=3)
    ax.fill_between(centers, smooth, color=GREEN, alpha=0.22)

    for pct, color, label in [
        (0.50, BLUE, "P50"),
        (0.85, AMBER, "P85"),
        (0.95, RED, "P95"),
    ]:
        val = np.percentile(ct, pct * 100)
        if val <= x_max:
            ax.axvline(
                val,
                color=color,
                linewidth=2,
                linestyle="--",
                label=f"{label}: {val:.0f} dias",
            )

    ax.set_title(
        "Distribuição Real do Cycle Time (curva suave)", color=TEXT, fontsize=14, pad=12
    )
    ax.set_xlabel("Dias", color=TEXT_MUTED)
    ax.set_ylabel("Densidade", color=TEXT_MUTED)
    ax.set_xlim(0, x_max)
    ax.tick_params(colors=TEXT_MUTED)
    ax.legend(fontsize=11, facecolor=SURFACE, labelcolor=TEXT, edgecolor=SURFACE)
    for spine in ax.spines.values():
        spine.set_color("#30363d")

    fig.tight_layout()
    out = OUTPUT_DIR / "cycle_time_distribution_curve.png"
    fig.savefig(out, dpi=150, bbox_inches="tight", facecolor=BG)
    plt.close(fig)
    print(f"✓ {out}")


def fig_throughput_weekly(df: pd.DataFrame) -> None:
    throughput = weekly_throughput(df)

    fig, ax = plt.subplots(figsize=(13, 4), facecolor=BG)
    ax.set_facecolor(BG)

    ax.bar(
        range(len(throughput)), throughput.values, color=GREEN, alpha=0.8, edgecolor=BG
    )
    media = throughput.mean()
    ax.axhline(
        media,
        color=AMBER,
        linewidth=2,
        linestyle="--",
        label=f"Média: {media:.1f} tasks/semana",
    )

    ax.set_title("Throughput Semanal", color=TEXT, fontsize=14, pad=12)
    ax.set_xlabel("Semanas (mais antigas → mais recentes)", color=TEXT_MUTED)
    ax.set_ylabel("Tarefas entregues", color=TEXT_MUTED)
    ax.set_xticks([])
    ax.tick_params(colors=TEXT_MUTED)
    ax.legend(fontsize=11, facecolor=SURFACE, labelcolor=TEXT, edgecolor=SURFACE)
    for spine in ax.spines.values():
        spine.set_color("#30363d")

    fig.tight_layout()
    out = OUTPUT_DIR / "throughput_weekly.png"
    fig.savefig(out, dpi=150, bbox_inches="tight", facecolor=BG)
    plt.close(fig)
    print(f"✓ {out}")


def fig_cycle_time_scatterplot(df: pd.DataFrame) -> None:
    """Cycle Time Scatterplot — visualização preferida por Vacanti."""
    import matplotlib.dates as mdates

    max_date = df["finished_at"].max()
    cutoff_date = max_date - pd.DateOffset(months=3)
    df_plot = df[df["finished_at"] >= cutoff_date].copy()

    ct = df_plot["cycle_time_days"]
    dates = df_plot["finished_at"]

    plot_bg = "#ffffff"
    text_main = "#0f172a"
    text_muted = "#475569"
    grid = "#cbd5e1"
    point = "#16a34a"

    fig, ax = plt.subplots(figsize=(13, 5), facecolor=plot_bg)
    ax.set_facecolor(plot_bg)

    ax.scatter(dates, ct, color=point, alpha=0.45, s=20, zorder=3)

    for pct, color, label in [
        (0.50, BLUE, f"P50: {ct.quantile(0.50):.0f} dias"),
        (0.85, AMBER, f"P85: {ct.quantile(0.85):.0f} dias"),
        (0.95, RED, f"P95: {ct.quantile(0.95):.0f} dias"),
    ]:
        val = ct.quantile(pct)
        ax.axhline(
            val, color=color, linewidth=1.5, linestyle="--", label=label, alpha=0.9
        )

    ax.set_yscale("log")
    ax.yaxis.set_major_locator(mticker.FixedLocator([1, 10, 100]))
    ax.yaxis.set_major_formatter(
        mticker.FuncFormatter(
            lambda value, _: (
                "1 dia"
                if value == 1
                else f"{int(value)} dias" if value in (1, 10, 100) else ""
            )
        )
    )
    ax.set_title(
        "Cycle Time Scatterplot (últimos 3 meses)",
        color=text_main,
        fontsize=14,
        pad=12,
    )
    ax.set_xlabel("Data de entrega", color=text_muted)
    ax.set_ylabel("Cycle Time (dias, escala log)", color=text_muted)
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%b/%y"))
    ax.xaxis.set_major_locator(mdates.MonthLocator())
    ax.tick_params(colors=text_muted, axis="both")
    ax.tick_params(axis="x", rotation=30)
    ax.grid(axis="y", which="both", color=grid, linestyle=":", linewidth=0.9)
    ax.legend(
        fontsize=10,
        facecolor=plot_bg,
        labelcolor=text_main,
        edgecolor=grid,
    )
    for spine in ax.spines.values():
        spine.set_color(grid)

    fig.tight_layout()
    out = OUTPUT_DIR / "cycle_time_scatterplot.png"
    fig.savefig(out, dpi=150, bbox_inches="tight", facecolor=plot_bg)
    plt.close(fig)
    print(f"✓ {out}")


def monte_carlo_quando(
    throughput: np.ndarray,
    n_items: int,
    n_sim: int = 10_000,
    seed: int = 42,
) -> np.ndarray:
    """Simula quantas semanas para entregar n_items."""
    rng = np.random.default_rng(seed)
    resultados = []
    for _ in range(n_sim):
        entregues, semanas = 0, 0
        while entregues < n_items:
            entregues += rng.choice(throughput)
            semanas += 1
        resultados.append(semanas)
    return np.array(resultados)


def fig_monte_carlo(df: pd.DataFrame, n_items: int = 20) -> tuple[float, float, float]:
    throughput = weekly_throughput(df).values

    simulacao = monte_carlo_quando(throughput, n_items)

    p50 = np.percentile(simulacao, 50)
    p85 = np.percentile(simulacao, 85)
    p95 = np.percentile(simulacao, 95)

    fig, ax = plt.subplots(figsize=(11, 5), facecolor=BG)
    ax.set_facecolor(BG)

    bins = range(int(simulacao.min()), int(simulacao.max()) + 2)
    ax.hist(simulacao, bins=bins, color=GREEN, edgecolor=BG, alpha=0.85, align="left")

    ax.axvline(
        p50, color=BLUE, linewidth=2, linestyle="--", label=f"P50: {p50:.0f} semanas"
    )
    ax.axvline(
        p85, color=AMBER, linewidth=2.5, label=f"P85: {p85:.0f} semanas  ← use este"
    )
    ax.axvline(
        p95, color=RED, linewidth=2, linestyle="--", label=f"P95: {p95:.0f} semanas"
    )

    ax.set_title(
        f"Monte Carlo: quando entregamos {n_items} features?",
        color=TEXT,
        fontsize=14,
        pad=12,
    )
    ax.set_xlabel("Semanas", color=TEXT_MUTED)
    ax.set_ylabel("Frequência (10.000 simulações)", color=TEXT_MUTED)
    ax.xaxis.set_major_locator(mticker.MaxNLocator(integer=True))
    ax.tick_params(colors=TEXT_MUTED)
    ax.legend(fontsize=11, facecolor=SURFACE, labelcolor=TEXT, edgecolor=SURFACE)
    for spine in ax.spines.values():
        spine.set_color("#30363d")

    fig.tight_layout()
    out = OUTPUT_DIR / "monte_carlo_resultado.png"
    fig.savefig(out, dpi=150, bbox_inches="tight", facecolor=BG)
    plt.close(fig)
    print(f"✓ {out}  (P50={p50:.0f} P85={p85:.0f} P95={p95:.0f} semanas)")
    return p50, p85, p95


if __name__ == "__main__":
    df = load_data()
    print_stats(df)
    fig_normal_distribution_reference(mean_days=5, median_days=5)
    fig_cycle_time_distribution_curve(df)
    fig_cycle_time_histogram(df)
    fig_cycle_time_scatterplot(df)
    fig_throughput_weekly(df)
    fig_monte_carlo(df, n_items=40)
    print("\nCharts salvos em slides/public/")
    print("Rode 'just slides' para ver a apresentação.")
