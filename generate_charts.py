"""
Gera os charts para a talk "Quando vai ficar pronto?"
Os charts são salvos em slides/public/ para uso no Slidev.

Uso:
    uv run python generate_charts.py
    # ou: just charts
"""

from pathlib import Path
import random

import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import numpy as np
import pandas as pd

OUTPUT_DIR = Path("slides/public")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
DATA_FILE = Path("data/lead_time_data_clean_2026.csv")

# Paleta Turquoise Harmony para charts
BG = "#ffffff"
BG2 = "#f0f3bd"  # cream
SURFACE = "#e5f5f3"  # teal tint
TEXT = "#032830"  # near-black dark teal
TEXT_MUTED = "#4a8a84"  # muted teal
GRID = "#b2e0db"  # light teal
GREEN = "#02c39a"  # mint-leaf
RED = "#00a896"  # verdigris
MAIN = "#05668d"  # baltic-blue
MC_BAR = "#028090"  # teal


def load_data(clean_cycle_time: bool = True) -> pd.DataFrame:
    df = pd.read_csv(
        DATA_FILE,
        header=None,
        names=["started_at", "finished_at", "cycle_time_days"],
    )
    df["finished_at"] = pd.to_datetime(df["finished_at"])
    df["started_at"] = pd.to_datetime(df["started_at"])
    if clean_cycle_time:
        # Remove apenas registros impossíveis; não remove outliers válidos do fluxo.
        df = df[df["cycle_time_days"] > 0]
    return df


def weekly_throughput(df: pd.DataFrame) -> pd.Series:
    """Return weekly throughput including explicit zero-throughput weeks."""
    semana = df["finished_at"].dt.to_period("W")
    semanas = pd.period_range(semana.min(), semana.max(), freq="W")
    return semana.value_counts().sort_index().reindex(semanas, fill_value=0)


def latest_weekly_throughput(df: pd.DataFrame, weeks: int = 15) -> pd.Series:
    """Retorna throughput semanal das últimas N semanas (inclui semanas zeradas)."""
    return weekly_throughput(df).tail(weeks).astype(int)


def daily_throughput(df: pd.DataFrame) -> pd.Series:
    """Return daily throughput including weekends and explicit zero-throughput days."""
    daily = df["finished_at"].dt.normalize()
    days = pd.date_range(daily.min(), daily.max(), freq="D")
    return daily.value_counts().sort_index().reindex(days, fill_value=0).astype(int)


def latest_daily_throughput(df: pd.DataFrame, weeks: int = 16) -> pd.Series:
    """Retorna throughput diário das últimas N semanas (inclui fins de semana e zeros)."""
    return daily_throughput(df).tail(weeks * 7).astype(int)


def export_latest_daily_throughput_csv(
    df: pd.DataFrame,
    weeks: int = 16,
    csv_path: str = "data/throughput_daily_latest_16w.csv",
    divider: int = 1,
) -> list[int]:
    """Exporta throughput diário das últimas semanas para reuso em simulações."""
    if divider < 1:
        raise ValueError("divider deve ser >= 1")

    throughput = latest_daily_throughput(df, weeks=weeks)
    if divider > 1:
        throughput = np.ceil(throughput / divider).astype(int)

    rows = []
    for day, value in throughput.items():
        rows.append(
            {
                "date": day.date().isoformat(),
                "throughput": int(value),
            }
        )

    pd.DataFrame(rows).to_csv(csv_path, index=False)
    values = [int(v) for v in throughput.tolist()]
    print(f"✓ {csv_path}  ({len(values)} dias, divider={divider})")
    return values


def export_latest_throughput_csv(
    df: pd.DataFrame,
    weeks: int = 15,
    csv_path: str = "data/throughput_latest_15w.csv",
    divider: int = 1,
) -> list[int]:
    """Exporta throughput das últimas semanas para facilitar reuso em simulações."""
    if divider < 1:
        raise ValueError("divider deve ser >= 1")

    throughput = latest_weekly_throughput(df, weeks=weeks)
    if divider > 1:
        throughput = np.ceil(throughput / divider).astype(int)

    rows = []
    for week_period, value in throughput.items():
        rows.append(
            {
                "week_start": week_period.start_time.date().isoformat(),
                "week_end": week_period.end_time.date().isoformat(),
                "throughput": int(value),
            }
        )

    pd.DataFrame(rows).to_csv(csv_path, index=False)
    values = [int(v) for v in throughput.tolist()]
    print(f"✓ {csv_path}  ({len(values)} semanas, divider={divider})")
    return values


def simulate_weeks_to_finish(
    target_cards: int,
    throughput_values: list[int],
    rng: random.Random,
) -> int:
    """Versão didática: sorteia throughput semanal até concluir target_cards."""
    done = 0
    weeks = 0
    while done < target_cards:
        done += rng.choice(throughput_values)
        weeks += 1
    return weeks


def monte_carlo_trace_rows(
    throughput_values: list[int],
    target_cards: int = 50,
    runs: int = 1000,
    seed: int = 42,
) -> list[dict[str, int]]:
    """Gera rastreamento diário por simulação para animação/convergência."""
    rng = random.Random(seed)
    rows: list[dict[str, int]] = []

    for run_id in range(1, runs + 1):
        cumulative_done = 0
        day_num = 0

        while cumulative_done < target_cards:
            day_num += 1
            throughput_picked = rng.choice(throughput_values)
            cumulative_done += throughput_picked

            rows.append(
                {
                    "run_id": run_id,
                    "day_num": day_num,
                    "throughput_picked": throughput_picked,
                    "cumulative_done": cumulative_done,
                }
            )

    return rows


def export_monte_carlo_trace_csv(
    throughput_values: list[int],
    target_cards: int = 50,
    runs: int = 1000,
    seed: int = 42,
    csv_path: str = "data/monte_carlo_trace_daily_10k.csv",
) -> None:
    rows = monte_carlo_trace_rows(
        throughput_values=throughput_values,
        target_cards=target_cards,
        runs=runs,
        seed=seed,
    )
    pd.DataFrame(rows).to_csv(csv_path, index=False)
    print(f"✓ {csv_path}  ({runs} simulações)")


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
    p85 = float(ct.quantile(0.85))

    ax.hist(ct_plot, bins=30, color=GREEN, edgecolor=BG, alpha=0.85)
    ax.axvspan(0, p85, color=GREEN, alpha=0.16, zorder=0)
    # Escala log melhora leitura quando alguns bins concentram muitos casos.
    ax.set_yscale("log")

    for pct, color, label in [
        (0.50, GREEN, "P50"),
        (0.85, MAIN, "P85"),
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
    ax.legend(fontsize=11, facecolor=SURFACE, labelcolor=TEXT, edgecolor=GRID)
    for spine in ax.spines.values():
        spine.set_color(GRID)

    fig.tight_layout()
    out = OUTPUT_DIR / "cycle_time_histogram.png"
    fig.savefig(out, dpi=150, bbox_inches="tight", facecolor=BG)
    plt.close(fig)
    print(f"✓ {out}")


def fig_normal_distribution_reference(
    mean_days: float = 10.0,
    median_days: float = 10.0,
    std_days: float = 4.0,
) -> None:
    """Curva normal de referência em dias para ilustrar média e mediana coincidentes."""
    # Eixo simétrico em torno da média, começando em x=0.
    x_min = 0.0
    x_max = 2 * mean_days
    x = np.linspace(x_min, x_max, 800)
    y = (1 / (std_days * np.sqrt(2 * np.pi))) * np.exp(
        -0.5 * ((x - mean_days) / std_days) ** 2
    )
    # Força a curva a tocar y=0 nas extremidades para efeito visual didático.
    y[0] = 0.0
    y[-1] = 0.0

    fig, ax = plt.subplots(figsize=(11, 5), facecolor=BG)
    ax.set_facecolor(BG)

    one_sigma_low = max(0.0, mean_days - std_days)
    one_sigma_high = min(x_max, mean_days + std_days)
    sigma_mask = (x >= one_sigma_low) & (x <= one_sigma_high)

    ax.fill_between(x, y, color=MAIN, alpha=0.12)
    ax.fill_between(x[sigma_mask], y[sigma_mask], color=GREEN, alpha=0.24)
    ax.plot(x, y, color=MAIN, linewidth=3)

    ax.axvline(
        mean_days,
        color=MAIN,
        linewidth=2.2,
        linestyle="--",
        label=f"Média: {mean_days:.0f} dias",
    )
    ax.axvspan(
        one_sigma_low,
        one_sigma_high,
        color=GREEN,
        alpha=0.08,
        label=f"Faixa central: {one_sigma_low:.0f}-{one_sigma_high:.0f} dias",
    )

    ax.set_title(
        "Como nosso cérebro pensa em estimativas", color=TEXT, fontsize=14, pad=12
    )
    ax.set_xlabel("Dias", color=TEXT_MUTED)
    ax.set_ylabel("Densidade", color=TEXT_MUTED)
    ax.set_xlim(x_min, x_max)
    ax.set_xticks(np.arange(int(x_min), int(x_max) + 1, 2))
    ax.tick_params(colors=TEXT_MUTED)
    ax.grid(axis="y", color=GRID, linestyle=":", linewidth=0.9)
    ax.legend(
        fontsize=15.5,
        facecolor=BG,
        labelcolor=TEXT,
        edgecolor=GRID,
        borderpad=1.0,
        labelspacing=0.8,
        handlelength=2.4,
        handletextpad=0.9,
        loc="upper right",
    )
    for spine in ax.spines.values():
        spine.set_color(GRID)

    fig.tight_layout()
    out = OUTPUT_DIR / "normal_distribution_curve.png"
    fig.savefig(out, dpi=150, bbox_inches="tight", facecolor=BG)
    plt.close(fig)
    print(f"✓ {out}")


def fig_skewed_distribution_reference(
    df: pd.DataFrame, max_percentile_for_plot: float = 99.0
) -> None:
    """Curva assimétrica à direita usando lead time real (cycle_time_days)."""
    sample = df["cycle_time_days"].to_numpy(dtype=float)
    sample = sample[sample > 0]

    p50 = float(np.percentile(sample, 50))
    p75 = float(np.percentile(sample, 75))
    p85 = float(np.percentile(sample, 85))
    p95 = float(np.percentile(sample, 95))

    x_max = int(np.ceil(np.percentile(sample, max_percentile_for_plot)))
    x_max = max(x_max, int(np.ceil(p95 * 1.1)), 20)
    bins = np.arange(0.5, x_max + 1.5, 1.0)
    sample_plot = sample[sample <= x_max]
    hist, edges = np.histogram(sample_plot, bins=bins, density=True)
    centers = (edges[:-1] + edges[1:]) / 2
    sigma_k = 1.4
    radius = int(np.ceil(4 * sigma_k))
    kernel_x = np.arange(-radius, radius + 1)
    kernel = np.exp(-0.5 * (kernel_x / sigma_k) ** 2)
    kernel /= kernel.sum()
    smooth = np.convolve(hist, kernel, mode="same")

    fig, ax = plt.subplots(figsize=(11, 5), facecolor=BG)
    ax.set_facecolor(BG)

    ax.fill_between(centers, smooth, color=MAIN, alpha=0.12)
    ax.plot(centers, smooth, color=MAIN, linewidth=3)

    ax.axvline(
        p50,
        color=GREEN,
        linewidth=2.2,
        linestyle="--",
        label=f"Mediana (P50): {p50:.0f} dias",
    )
    ax.axvline(
        p75,
        color=TEXT_MUTED,
        linewidth=1.8,
        linestyle=":",
        label=f"P75: {p75:.0f} dias",
    )
    ax.axvline(
        p85, color=MAIN, linewidth=2.0, linestyle="--", label=f"P85: {p85:.0f} dias"
    )
    ax.axvline(
        p95, color=RED, linewidth=2.2, linestyle="-", label=f"P95: {p95:.0f} dias"
    )

    ax.set_title(
        "Lead time real: distribuição assimétrica", color=TEXT, fontsize=14, pad=12
    )
    ax.set_xlabel("Dias", color=TEXT_MUTED)
    ax.set_ylabel("Densidade", color=TEXT_MUTED)
    ax.set_xlim(0, x_max)
    ax.tick_params(colors=TEXT_MUTED)
    ax.grid(axis="y", color=GRID, linestyle=":", linewidth=0.9)
    ax.legend(
        fontsize=14.5,
        facecolor=BG,
        labelcolor=TEXT,
        edgecolor=GRID,
        borderpad=1.0,
        labelspacing=0.8,
        handlelength=2.4,
        handletextpad=0.9,
        loc="upper right",
    )
    for spine in ax.spines.values():
        spine.set_color(GRID)

    fig.tight_layout()
    out = OUTPUT_DIR / "skewed_distribution_curve.png"
    fig.savefig(out, dpi=150, bbox_inches="tight", facecolor=BG)
    plt.close(fig)
    print(
        f"✓ {out}  (dados reais n={len(sample)} P50={p50:.0f} P75={p75:.0f} P85={p85:.0f} P95={p95:.0f} dias)"
    )


def airport_trip_minutes() -> np.ndarray:
    """Série sintética de 50 viagens ao aeroporto com cauda longa e menos empates."""
    minutes = np.array(
        [
            29.0,
            29.4,
            29.9,
            30.3,
            30.8,
            31.0,
            31.2,
            31.4,
            31.6,
            31.8,
            32.0,
            32.1,
            32.2,
            32.3,
            32.4,
            32.5,
            32.55,
            32.6,
            32.65,
            32.7,
            32.72,
            32.74,
            32.76,
            32.78,
            32.8,
            33.2,
            33.3,
            33.5,
            33.8,
            34.2,
            34.7,
            35.3,
            36.0,
            37.0,
            38.2,
            39.8,
            41.5,
            44.0,
            47.0,
            50.5,
            54.0,
            58.5,
            63.0,
            70.0,
            89.0,
            99.0,
            101.0,
            104.5,
            108.0,
            111.0,
        ],
        dtype=float,
    )
    return minutes


def fig_airport_travel_time_distribution() -> None:
    minutes = airport_trip_minutes()
    p50 = float(np.percentile(minutes, 50))
    p70 = float(np.percentile(minutes, 70))
    p80 = float(np.percentile(minutes, 80))
    p90 = float(np.percentile(minutes, 90))
    p95 = float(np.percentile(minutes, 95))

    bin_edges = [
        27,
        31,
        35,
        39,
        43,
        47,
        51,
        55,
        59,
        63,
        67,
        71,
        75,
        79,
        83,
        87,
        91,
        95,
        99,
        103,
        107,
        111,
        115,
    ]
    weights = np.ones_like(minutes, dtype=float) / len(minutes)
    hist, edges = np.histogram(minutes, bins=bin_edges, weights=weights)
    centers = (edges[:-1] + edges[1:]) / 2

    sigma_bins = 1.35
    radius = int(np.ceil(4 * sigma_bins))
    kernel_x = np.arange(-radius, radius + 1)
    kernel = np.exp(-0.5 * (kernel_x / sigma_bins) ** 2)
    kernel /= kernel.sum()
    smooth = np.convolve(hist, kernel, mode="same")
    y_max = smooth.max() * 1.22

    fig, ax = plt.subplots(figsize=(11.5, 5.6), facecolor=BG)
    ax.set_facecolor(BG)

    ax.fill_between(centers, smooth, color=MAIN, alpha=0.12)
    ax.fill_between(
        centers,
        smooth,
        where=(centers >= p90).tolist(),
        color=RED,
        alpha=0.22,
        interpolate=True,
    )
    ax.plot(centers, smooth, color=MAIN, linewidth=3)

    ax.axvline(
        p50,
        color=GREEN,
        linewidth=2.4,
        linestyle="--",
        label=f"P50: {p50:.0f} min",
    )
    ax.axvline(
        p70,
        color=GREEN,
        linewidth=1.7,
        linestyle=":",
        alpha=0.75,
        label=f"P70: {p70:.0f} min",
    )
    ax.axvline(
        p80,
        color=MAIN,
        linewidth=2.0,
        linestyle="--",
        alpha=0.8,
        label=f"P80: {p80:.0f} min",
    )
    ax.axvline(
        p90,
        color=RED,
        linewidth=2.6,
        label=f"P90: {p90:.0f} min",
    )
    ax.axvline(
        minutes.min(),
        color=TEXT_MUTED,
        linewidth=1.6,
        linestyle=":",
        label=f"Mínimo: {minutes.min()} min",
    )

    ax.set_title(
        "Tempo até o aeroporto: distribuição assimétrica à direita",
        color=TEXT,
        fontsize=14,
        pad=12,
    )
    ax.set_xlabel("Minutos", color=TEXT_MUTED)
    ax.set_ylabel("Densidade relativa", color=TEXT_MUTED)
    ax.set_xlim(27, 114)
    ax.set_ylim(-0.004, y_max)
    ax.set_xticks([29, 33, 45, 60, 75, 90, 105])
    ax.tick_params(colors=TEXT_MUTED)
    ax.grid(axis="y", color=GRID, linestyle=":", linewidth=0.9)
    ax.legend(
        fontsize=14.5,
        facecolor=BG,
        labelcolor=TEXT,
        edgecolor=GRID,
        borderpad=0.92,
        labelspacing=0.76,
        handlelength=2.25,
        handletextpad=0.8,
        loc="upper right",
    )
    for spine in ax.spines.values():
        spine.set_color(GRID)

    fig.tight_layout()
    out = OUTPUT_DIR / "airport_travel_time_distribution.png"
    fig.savefig(out, dpi=150, bbox_inches="tight", facecolor=BG)
    plt.close(fig)
    print(
        f"✓ {out}  (min={minutes.min():.0f} P50={p50:.0f} P90={p90:.0f} P95={p95:.0f} min)"
    )


def fig_airport_travel_time_histogram() -> None:
    minutes = airport_trip_minutes()
    p50 = float(np.percentile(minutes, 50))
    p70 = float(np.percentile(minutes, 70))
    p80 = float(np.percentile(minutes, 80))
    p90 = float(np.percentile(minutes, 90))

    bin_edges = [
        27,
        32,
        37,
        42,
        47,
        52,
        57,
        62,
        67,
        72,
        77,
        82,
        87,
        92,
        97,
        102,
        107,
        112,
        117,
    ]
    fig, ax = plt.subplots(figsize=(11.5, 5.6), facecolor=BG)
    ax.set_facecolor(BG)

    ax.hist(
        minutes,
        bins=bin_edges,
        color=MAIN,
        alpha=0.18,
        edgecolor=MAIN,
        linewidth=1.2,
        rwidth=0.86,
    )

    ax.axvline(
        p50,
        color=GREEN,
        linewidth=2.4,
        linestyle="--",
        label=f"P50: {p50:.0f} min",
    )
    ax.axvline(
        p70,
        color=GREEN,
        linewidth=1.7,
        linestyle=":",
        alpha=0.75,
        label=f"P70: {p70:.0f} min",
    )
    ax.axvline(
        p80,
        color=MAIN,
        linewidth=2.0,
        linestyle="--",
        alpha=0.8,
        label=f"P80: {p80:.0f} min",
    )
    ax.axvline(
        p90,
        color=RED,
        linewidth=2.6,
        label=f"P90: {p90:.0f} min",
    )
    ax.axvline(
        minutes.min(),
        color=TEXT_MUTED,
        linewidth=1.6,
        linestyle=":",
        label=f"Mínimo: {minutes.min()} min",
    )

    ax.set_title(
        "Tempo até o aeroporto: histograma de frequência",
        color=TEXT,
        fontsize=14,
        pad=12,
    )
    ax.set_xlabel("Minutos", color=TEXT_MUTED)
    ax.set_ylabel("Quantidade", color=TEXT_MUTED)
    ax.set_xlim(27, 117)
    ax.set_xticks([29, 33, 45, 60, 75, 90, 105])
    ax.yaxis.set_major_locator(mticker.MaxNLocator(integer=True))
    ax.tick_params(colors=TEXT_MUTED)
    ax.grid(axis="y", color=GRID, linestyle=":", linewidth=0.9)
    ax.legend(
        fontsize=14.5,
        facecolor=BG,
        labelcolor=TEXT,
        edgecolor=GRID,
        borderpad=0.92,
        labelspacing=0.76,
        handlelength=2.25,
        handletextpad=0.8,
        loc="upper right",
    )
    for spine in ax.spines.values():
        spine.set_color(GRID)

    fig.tight_layout()
    out = OUTPUT_DIR / "airport_travel_time_histogram.png"
    fig.savefig(out, dpi=150, bbox_inches="tight", facecolor=BG)
    plt.close(fig)
    print(f"✓ {out}  (min={minutes.min():.0f} P50={p50:.0f} P90={p90:.0f} min)")


def fig_airport_travel_time_cdf() -> None:
    minutes = airport_trip_minutes()
    sorted_minutes = np.sort(minutes)
    cumulative = np.arange(1, len(sorted_minutes) + 1) / len(sorted_minutes)

    p50 = float(np.percentile(minutes, 50))
    p70 = float(np.percentile(minutes, 70))
    p80 = float(np.percentile(minutes, 80))
    p90 = float(np.percentile(minutes, 90))

    fig, ax = plt.subplots(figsize=(11.5, 5.6), facecolor=BG)
    ax.set_facecolor(BG)

    ax.step(
        sorted_minutes,
        cumulative,
        where="post",
        color=MAIN,
        linewidth=3,
    )
    ax.fill_between(sorted_minutes, cumulative, step="post", color=MAIN, alpha=0.10)

    for percentile, color, label, linestyle, linewidth in [
        (0.50, GREEN, f"P50: {p50:.0f} min", "--", 2.4),
        (0.70, GREEN, f"P70: {p70:.0f} min", ":", 1.7),
        (0.80, MAIN, f"P80: {p80:.0f} min", "--", 2.0),
        (0.90, RED, f"P90: {p90:.0f} min", "-", 2.6),
    ]:
        ax.axvline(
            float(np.percentile(minutes, percentile * 100)),
            color=color,
            linewidth=linewidth,
            linestyle=linestyle,
            alpha=0.9 if percentile < 0.9 else 1.0,
            label=label,
        )
        ax.axhline(
            percentile,
            color=color,
            linewidth=1.1,
            linestyle=":",
            alpha=0.18,
        )

    ax.axvline(
        minutes.min(),
        color=TEXT_MUTED,
        linewidth=1.6,
        linestyle=":",
        label=f"Mínimo: {minutes.min():.0f} min",
    )

    ax.set_title(
        "Tempo até o aeroporto: distribuição acumulada (CDF)",
        color=TEXT,
        fontsize=14,
        pad=12,
    )
    ax.set_xlabel("Minutos", color=TEXT_MUTED)
    ax.set_ylabel("Percentual acumulado", color=TEXT_MUTED)
    ax.set_xlim(27, 117)
    ax.set_ylim(0, 1.02)
    ax.set_xticks([29, 33, 45, 60, 75, 90, 105])
    ax.yaxis.set_major_formatter(mticker.PercentFormatter(1.0, decimals=0))
    ax.tick_params(colors=TEXT_MUTED)
    ax.grid(color=GRID, linestyle=":", linewidth=0.9)
    ax.legend(
        fontsize=14.5,
        facecolor=BG,
        labelcolor=TEXT,
        edgecolor=GRID,
        borderpad=0.92,
        labelspacing=0.76,
        handlelength=2.25,
        handletextpad=0.8,
        loc="lower right",
    )
    for spine in ax.spines.values():
        spine.set_color(GRID)

    fig.tight_layout()
    out = OUTPUT_DIR / "airport_travel_time_cdf.png"
    fig.savefig(out, dpi=150, bbox_inches="tight", facecolor=BG)
    plt.close(fig)
    print(f"✓ {out}  (P50={p50:.0f} P90={p90:.0f} min)")


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
        (0.50, GREEN, "P50"),
        (0.85, MAIN, "P85"),
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
    ax.legend(fontsize=11, facecolor=SURFACE, labelcolor=TEXT, edgecolor=GRID)
    for spine in ax.spines.values():
        spine.set_color(GRID)

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
        color=MAIN,
        linewidth=2,
        linestyle="--",
        label=f"Média: {media:.1f} tasks/semana",
    )

    ax.set_title("Throughput Semanal", color=TEXT, fontsize=14, pad=12)
    ax.set_xlabel("Semanas (mais antigas → mais recentes)", color=TEXT_MUTED)
    ax.set_ylabel("Tarefas entregues", color=TEXT_MUTED)
    ax.set_xticks([])
    ax.tick_params(colors=TEXT_MUTED)
    ax.legend(fontsize=11, facecolor=SURFACE, labelcolor=TEXT, edgecolor=GRID)
    for spine in ax.spines.values():
        spine.set_color(GRID)

    fig.tight_layout()
    out = OUTPUT_DIR / "throughput_weekly.png"
    fig.savefig(out, dpi=150, bbox_inches="tight", facecolor=BG)
    plt.close(fig)
    print(f"✓ {out}")


def fig_cycle_time_scatterplot(df: pd.DataFrame) -> None:
    """Lead Time Scatterplot com dados reais e linhas de P50/P85."""
    import matplotlib.dates as mdates

    ct = df["cycle_time_days"]
    dates = df["finished_at"]

    plot_bg = "#ffffff"
    text_main = "#0f172a"
    text_muted = "#475569"
    grid = "#cbd5e1"
    point = "#16a34a"

    fig, ax = plt.subplots(figsize=(13, 5), facecolor=plot_bg)
    ax.set_facecolor(plot_bg)

    ax.scatter(dates, ct, color=point, alpha=0.45, s=20, zorder=3)

    for pct, color, label in [
        (0.50, GREEN, f"P50: {ct.quantile(0.50):.0f} dias"),
        (0.85, MAIN, f"P85: {ct.quantile(0.85):.0f} dias"),
    ]:
        val = ct.quantile(pct)
        ax.axhline(
            val, color=color, linewidth=1.5, linestyle="--", label=label, alpha=0.9
        )

    ax.set_title(
        "Lead Time Scatterplot (dados reais de 2026)",
        color=text_main,
        fontsize=14,
        pad=12,
    )
    ax.set_xlabel("Data de entrega", color=text_muted)
    ax.set_ylabel("Lead time (dias)", color=text_muted)
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


def reasonable_x_axis_max(values: np.ndarray, minimum: int = 10, step: int = 10) -> int:
    """Escolhe limite de eixo X legível sem ser dominado por outliers extremos."""
    if len(values) == 0:
        return minimum

    p95 = float(np.percentile(values, 95))
    p99 = float(np.percentile(values, 99))
    candidate = max(p99, p95 * 1.1, float(minimum))
    rounded = int(np.ceil(candidate / step) * step)
    return max(minimum, rounded)


def fig_monte_carlo(
    df: pd.DataFrame,
    n_items: int = 20,
    throughput_values: np.ndarray | None = None,
    unit_label: str = "semanas",
    output: str = "monte_carlo_resultado.png",
    x_axis_max: int | None = None,
) -> tuple[float, float, float]:
    throughput = (
        throughput_values
        if throughput_values is not None
        else weekly_throughput(df).values
    )

    simulacao = monte_carlo_quando(throughput, n_items)

    p50 = np.percentile(simulacao, 50)
    p85 = np.percentile(simulacao, 85)
    p95 = np.percentile(simulacao, 95)
    x_max = x_axis_max if x_axis_max is not None else reasonable_x_axis_max(simulacao)

    fig, ax = plt.subplots(figsize=(11, 5), facecolor=BG)
    ax.set_facecolor(BG)

    bins = range(int(simulacao.min()), int(simulacao.max()) + 2)
    ax.hist(simulacao, bins=bins, color=MC_BAR, edgecolor=BG, alpha=0.9, align="left")

    ax.axvline(
        p50,
        color=GREEN,
        linewidth=2,
        linestyle="--",
        label=f"P50: {p50:.0f} {unit_label}",
    )
    ax.axvline(
        p85,
        color=MAIN,
        linewidth=2.5,
        label=f"P85: {p85:.0f} {unit_label}  ← use este",
    )
    ax.axvline(
        p95,
        color=RED,
        linewidth=2,
        linestyle="--",
        label=f"P95: {p95:.0f} {unit_label}",
    )

    ax.set_title(
        f"Monte Carlo: quando entregamos {n_items} cards?",
        color=TEXT,
        fontsize=14,
        pad=12,
    )
    ax.set_xlabel(unit_label.capitalize(), color=TEXT_MUTED)
    ax.set_ylabel("Frequência (10.000 simulações)", color=TEXT_MUTED)
    ax.set_xlim(1, x_max)
    ax.xaxis.set_major_locator(mticker.MaxNLocator(integer=True))
    ax.tick_params(colors=TEXT_MUTED)
    ax.legend(fontsize=11, facecolor=SURFACE, labelcolor=TEXT, edgecolor=GRID)
    for spine in ax.spines.values():
        spine.set_color(GRID)

    fig.tight_layout()
    out = OUTPUT_DIR / output
    fig.savefig(out, dpi=150, bbox_inches="tight", facecolor=BG)
    plt.close(fig)
    print(f"✓ {out}  (P50={p50:.0f} P85={p85:.0f} P95={p95:.0f} {unit_label})")
    return p50, p85, p95


def fig_monte_carlo_animation(
    trace_csv: str = "data/monte_carlo_trace_daily_10k.csv",
    target_cards: int = 50,
    output_spaghetti: str = "01-monte-carlo-spaghetti.gif",
    output_histogram: str = "03-monte-carlo-histogramas.gif",
    x_axis_max: int | None = None,
) -> None:
    """Exporta dois GIFs separados: um de spaghetti e outro de histogramas."""
    import io
    from PIL import Image

    df_trace = pd.read_csv(trace_csv)
    step_col = "day_num" if "day_num" in df_trace.columns else "week_num"
    run_ids = sorted(df_trace["run_id"].unique())
    n_runs = len(run_ids)
    traces = {rid: grp.sort_values(step_col) for rid, grp in df_trace.groupby("run_id")}
    completion = {
        rid: int(grp[step_col].max()) for rid, grp in df_trace.groupby("run_id")
    }
    all_completions = [completion[r] for r in run_ids]
    x_max_weeks = (
        x_axis_max
        if x_axis_max is not None
        else reasonable_x_axis_max(np.array(all_completions))
    )
    y_max_cards = int(df_trace["cumulative_done"].max() * 1.05)
    hist_bins = list(range(1, x_max_weeks + 2))

    def _save_gif(
        images: list,
        durations: list[int],
        output_name: str,
        loop_forever: bool = True,
    ) -> None:
        out = OUTPUT_DIR / output_name
        save_kwargs = {
            "save_all": True,
            "append_images": images[1:],
            "duration": durations,
            "optimize": False,
        }
        if loop_forever:
            save_kwargs["loop"] = 0
        images[0].save(out, **save_kwargs)
        total_s = sum(durations) / 1000
        loop_label = "∞" if loop_forever else "1x"
        print(
            f"✓ {out}  ({len(images)} frames, ~{total_s:.0f}s total, loop={loop_label})"
        )

    def save_frame(
        images: list, durations: list[int], fig: plt.Figure, duration_ms: int
    ) -> None:
        buf = io.BytesIO()
        fig.savefig(buf, format="png", dpi=100, bbox_inches="tight", facecolor=BG)
        plt.close(fig)
        buf.seek(0)
        images.append(Image.open(buf).copy())
        buf.close()
        durations.append(duration_ms)

    def make_ax() -> tuple[plt.Figure, plt.Axes]:
        fig, ax = plt.subplots(figsize=(11, 5.5), facecolor=BG)
        ax.set_facecolor(BG)
        ax.set_xlim(1, x_max_weeks)
        ax.set_xlabel("Dia", color=TEXT_MUTED, fontsize=12)
        ax.tick_params(colors=TEXT_MUTED)
        ax.xaxis.set_major_locator(mticker.MaxNLocator(integer=True))
        for spine in ax.spines.values():
            spine.set_color(GRID)
        return fig, ax

    def draw_target(ax: plt.Axes) -> None:
        ax.axhline(
            target_cards,
            color=MAIN,
            linewidth=2,
            linestyle="--",
            label=f"Meta: {target_cards} cards",
        )

    def spaghetti_axis(ax: plt.Axes) -> None:
        ax.set_ylim(0, y_max_cards)
        ax.set_ylabel("Cards concluídos", color=TEXT_MUTED, fontsize=12)

    # ── GIF 1: SPAGHETTI (direto para N simulações) ──────────────────────────
    spaghetti_images: list = []
    spaghetti_durations: list[int] = []

    print("Spaghetti GIF: fanning out simulations…")
    # milestones + how long to hold each
    milestones = [
        (10, 400),
        (50, 400),
        (200, 500),
        (500, 600),
        (1000, 700),
        (2500, 800),
        (5000, 900),
        (10000, 1000),
    ]
    rng_sub = np.random.default_rng(0)

    for n_visible, hold_ms in milestones:
        n_visible = min(n_visible, n_runs)
        visible_runs = run_ids[:n_visible]

        fig, ax = make_ax()
        spaghetti_axis(ax)
        draw_target(ax)

        # cap dim lines to 300 for performance
        dim_runs = visible_runs[:-1]
        if len(dim_runs) > 300:
            dim_runs = rng_sub.choice(dim_runs, size=300, replace=False).tolist()

        alpha = max(0.03, min(0.18, 12 / n_visible))
        for rid in dim_runs:
            t = traces[rid]
            ax.plot(
                t[step_col],
                t["cumulative_done"],
                color=GREEN,
                alpha=alpha,
                linewidth=0.8,
            )

        # highlight last added run
        t_last = traces[visible_runs[-1]]
        ax.plot(
            t_last[step_col],
            t_last["cumulative_done"],
            color=GREEN,
            alpha=0.9,
            linewidth=2.2,
        )

        ax.set_title(
            f"{n_visible} simulações — futuros possíveis (dias)",
            color=TEXT,
            fontsize=14,
            pad=10,
        )
        ax.legend(fontsize=11, facecolor=SURFACE, labelcolor=TEXT, edgecolor=GRID)
        fig.tight_layout()
        save_frame(spaghetti_images, spaghetti_durations, fig, duration_ms=hold_ms)

    _save_gif(
        spaghetti_images, spaghetti_durations, output_spaghetti, loop_forever=True
    )

    # ── GIF 2: HISTOGRAMAS (fase 3) ──────────────────────────────────────────
    histogram_images: list = []
    histogram_durations: list[int] = []

    print("Histogram GIF: collapsing to histogram with percentile reveals…")
    final_completions = [completion[r] for r in run_ids]
    p50 = float(np.percentile(final_completions, 50))
    p85 = float(np.percentile(final_completions, 85))
    p95 = float(np.percentile(final_completions, 95))

    # Histogram builds up then percentiles appear
    for n_hist in [250, 500, 1000, 2500, 5000, 10000]:
        fig, ax = make_ax()
        ax.set_ylabel("Frequência (simulações)", color=TEXT_MUTED, fontsize=12)
        ax.hist(
            [completion[r] for r in run_ids[:n_hist]],
            bins=hist_bins,
            color=MC_BAR,
            edgecolor=BG,
            alpha=0.9,
            align="left",
        )
        ax.set_title(
            f"Quantos dias para entregar? ({n_hist} simulações)",
            color=TEXT,
            fontsize=14,
            pad=10,
        )
        fig.tight_layout()
        save_frame(histogram_images, histogram_durations, fig, duration_ms=400)

    # reveal P50
    fig, ax = make_ax()
    ax.set_ylabel("Frequência (simulações)", color=TEXT_MUTED, fontsize=12)
    ax.hist(
        final_completions,
        bins=hist_bins,
        color=MC_BAR,
        edgecolor=BG,
        alpha=0.9,
        align="left",
    )
    ax.axvline(
        p50,
        color=GREEN,
        linewidth=2.5,
        linestyle="--",
        label=f"P50: {p50:.0f} dias (50% de chance)",
    )
    ax.set_title("Quantos dias para entregar?", color=TEXT, fontsize=14, pad=10)
    ax.legend(fontsize=12, facecolor=SURFACE, labelcolor=TEXT, edgecolor=GRID)
    fig.tight_layout()
    save_frame(histogram_images, histogram_durations, fig, duration_ms=1000)

    # reveal P85
    fig, ax = make_ax()
    ax.set_ylabel("Frequência (simulações)", color=TEXT_MUTED, fontsize=12)
    ax.hist(
        final_completions,
        bins=hist_bins,
        color=MC_BAR,
        edgecolor=BG,
        alpha=0.9,
        align="left",
    )
    ax.axvline(
        p50, color=GREEN, linewidth=2.5, linestyle="--", label=f"P50: {p50:.0f} dias"
    )
    ax.axvline(p85, color=MAIN, linewidth=3, label=f"P85: {p85:.0f} dias  ← use este")
    ax.set_title("Quantos dias para entregar?", color=TEXT, fontsize=14, pad=10)
    ax.legend(fontsize=12, facecolor=SURFACE, labelcolor=TEXT, edgecolor=GRID)
    fig.tight_layout()
    save_frame(histogram_images, histogram_durations, fig, duration_ms=1000)

    # reveal P95
    fig, ax = make_ax()
    ax.set_ylabel("Frequência (simulações)", color=TEXT_MUTED, fontsize=12)
    ax.hist(
        final_completions,
        bins=hist_bins,
        color=MC_BAR,
        edgecolor=BG,
        alpha=0.9,
        align="left",
    )
    ax.axvline(
        p50, color=GREEN, linewidth=2.5, linestyle="--", label=f"P50: {p50:.0f} dias"
    )
    ax.axvline(p85, color=MAIN, linewidth=3, label=f"P85: {p85:.0f} dias  ← use este")
    ax.axvline(
        p95, color=RED, linewidth=2.5, linestyle="--", label=f"P95: {p95:.0f} dias"
    )
    ax.set_title("Quantos dias para entregar?", color=TEXT, fontsize=14, pad=10)
    ax.legend(fontsize=12, facecolor=SURFACE, labelcolor=TEXT, edgecolor=GRID)
    fig.tight_layout()
    save_frame(histogram_images, histogram_durations, fig, duration_ms=2000)

    _save_gif(
        histogram_images, histogram_durations, output_histogram, loop_forever=False
    )


def fig_monte_carlo_single_run_gif(
    trace_csv: str = "data/monte_carlo_trace_daily_10k.csv",
    target_cards: int = 50,
    total_seconds: float = 5.0,
    output: str = "00-monte-carlo-simulacao-5s.gif",
    x_axis_max: int | None = None,
) -> None:
    """Gera GIF didático com uma única simulação, controlado para ~5s."""
    import io
    from PIL import Image

    df_trace = pd.read_csv(trace_csv)
    step_col = "day_num" if "day_num" in df_trace.columns else "week_num"
    first_run_id = int(df_trace["run_id"].min())
    t = (
        df_trace[df_trace["run_id"] == first_run_id]
        .sort_values(step_col)
        .reset_index(drop=True)
    )

    weeks = t[step_col].tolist()
    done = t["cumulative_done"].tolist()
    completion = (
        df_trace.groupby("run_id", as_index=False)[step_col].max()[step_col].to_numpy()
    )
    x_max = x_axis_max if x_axis_max is not None else reasonable_x_axis_max(completion)
    y_max = int(df_trace["cumulative_done"].max() * 1.05)

    frame_count = len(weeks)
    step_duration_ms = max(80, int((total_seconds * 1000) / frame_count))

    images: list = []
    durations: list[int] = []

    for step in range(1, frame_count + 1):
        fig, ax = plt.subplots(figsize=(11, 5.5), facecolor=BG)
        ax.set_facecolor(BG)

        ax.plot(weeks[:step], done[:step], color=GREEN, linewidth=2.8, alpha=0.95)
        ax.axhline(
            target_cards,
            color=MAIN,
            linewidth=2,
            linestyle="--",
            label=f"Meta: {target_cards} cards",
        )

        ax.set_xlim(1, x_max)
        ax.set_ylim(0, y_max)
        ax.set_title(
            "Uma simulação Monte Carlo diária (passo a passo)",
            color=TEXT,
            fontsize=14,
            pad=10,
        )
        ax.set_xlabel("Dia", color=TEXT_MUTED)
        ax.set_ylabel("Cards concluídos", color=TEXT_MUTED)
        ax.xaxis.set_major_locator(mticker.MaxNLocator(integer=True))
        ax.tick_params(colors=TEXT_MUTED)
        ax.legend(fontsize=11, facecolor=SURFACE, labelcolor=TEXT, edgecolor=GRID)
        for spine in ax.spines.values():
            spine.set_color(GRID)

        fig.tight_layout()
        buf = io.BytesIO()
        fig.savefig(buf, format="png", dpi=100, bbox_inches="tight", facecolor=BG)
        plt.close(fig)
        buf.seek(0)
        images.append(Image.open(buf).copy())
        buf.close()
        durations.append(step_duration_ms)

    # Fecha em ~5s mesmo após arredondamento.
    durations[-1] += max(0, int(total_seconds * 1000) - sum(durations))

    out = OUTPUT_DIR / output
    images[0].save(
        out,
        save_all=True,
        append_images=images[1:],
        duration=durations,
        loop=0,
        optimize=False,
    )
    total_s = sum(durations) / 1000
    print(f"✓ {out}  ({len(images)} frames, ~{total_s:.1f}s total, loop=∞)")


def fig_monte_carlo_histogram_100_runs(
    trace_csv: str = "data/monte_carlo_trace_daily_10k.csv",
    runs: int = 100,
    target_cards: int = 50,
    output: str = "03-monte-carlo-histograma-100-runs.png",
    x_axis_max: int | None = None,
) -> None:
    """Gera histograma de semanas para concluir N cards com as primeiras 100 simulações."""
    df_trace = pd.read_csv(trace_csv)

    step_col = "day_num" if "day_num" in df_trace.columns else "week_num"
    completion = (
        df_trace[df_trace["run_id"] <= runs]
        .groupby("run_id", as_index=False)[step_col]
        .max()
    )
    completion_weeks = completion[step_col].astype(int).to_numpy()
    x_max = (
        x_axis_max
        if x_axis_max is not None
        else reasonable_x_axis_max(completion_weeks)
    )

    p50 = float(np.percentile(completion_weeks, 50))
    p85 = float(np.percentile(completion_weeks, 85))
    p95 = float(np.percentile(completion_weeks, 95))

    fig, ax = plt.subplots(figsize=(11, 5), facecolor=BG)
    ax.set_facecolor(BG)

    bins = range(int(completion_weeks.min()), int(completion_weeks.max()) + 2)
    ax.hist(
        completion_weeks,
        bins=bins,
        color=MC_BAR,
        edgecolor=BG,
        alpha=0.9,
        align="left",
    )
    ax.axvline(
        p50,
        color=GREEN,
        linewidth=2,
        linestyle="--",
        label=f"P50: {p50:.0f} dias",
    )
    ax.axvline(
        p85,
        color=MAIN,
        linewidth=2.5,
        label=f"P85: {p85:.0f} dias",
    )
    ax.axvline(
        p95,
        color=RED,
        linewidth=2,
        linestyle="--",
        label=f"P95: {p95:.0f} dias",
    )

    ax.set_title(
        f"Monte Carlo (100 simulações): dias para concluir {target_cards} cards",
        color=TEXT,
        fontsize=14,
        pad=12,
    )
    ax.set_xlabel("Dias", color=TEXT_MUTED)
    ax.set_ylabel("Frequência", color=TEXT_MUTED)
    ax.set_xlim(1, x_max)
    ax.xaxis.set_major_locator(mticker.MaxNLocator(integer=True))
    ax.tick_params(colors=TEXT_MUTED)
    ax.legend(fontsize=11, facecolor=SURFACE, labelcolor=TEXT, edgecolor=GRID)
    for spine in ax.spines.values():
        spine.set_color(GRID)

    fig.tight_layout()
    out = OUTPUT_DIR / output
    fig.savefig(out, dpi=150, bbox_inches="tight", facecolor=BG)
    plt.close(fig)
    print(f"✓ {out}  (runs={len(completion_weeks)} P85={p85:.0f} dias)")


def fig_monte_carlo_itens(
    throughput_values: np.ndarray,
    prazo_dias: int = 34,
    n_sim: int = 10_000,
    seed: int = 42,
    output: str = "monte_carlo_itens.png",
) -> tuple[float, float, float]:
    """Histograma de 'quantos itens entregamos até o prazo?'
    Usa P15 como estimativa conservadora (85% das simulações entregam >= P15 itens).
    """
    rng = np.random.default_rng(seed)
    resultados = np.array(
        [
            int(rng.choice(throughput_values, size=prazo_dias).sum())
            for _ in range(n_sim)
        ]
    )

    p15 = float(np.percentile(resultados, 15))
    p50 = float(np.percentile(resultados, 50))
    p85 = float(np.percentile(resultados, 85))

    fig, ax = plt.subplots(figsize=(11, 5), facecolor=BG)
    ax.set_facecolor(BG)

    bins = range(int(resultados.min()), int(resultados.max()) + 2)
    ax.hist(resultados, bins=bins, color=MC_BAR, edgecolor=BG, alpha=0.9, align="left")

    # Shade area to the right of P15 to show "85% das simulações"
    ax.axvspan(p15, resultados.max() + 1, color=GREEN, alpha=0.10, zorder=0)

    ax.axvline(
        p15,
        color=MAIN,
        linewidth=2.5,
        linestyle="--",
        label=f"P15: {p15:.0f} itens  ← use este",
    )
    ax.axvline(
        p50,
        color=GREEN,
        linewidth=2,
        linestyle="--",
        label=f"P50: {p50:.0f} itens",
    )
    ax.axvline(
        p85,
        color=RED,
        linewidth=2,
        linestyle="--",
        label=f"P85: {p85:.0f} itens  (só 15% chegam aqui)",
    )

    ax.set_title(
        f"Monte Carlo: quantos itens entregamos em {prazo_dias} dias?",
        color=TEXT,
        fontsize=14,
        pad=12,
    )
    ax.set_xlabel("Itens entregues", color=TEXT_MUTED)
    ax.set_ylabel("Frequência (10.000 simulações)", color=TEXT_MUTED)
    ax.xaxis.set_major_locator(mticker.MaxNLocator(integer=True))
    ax.tick_params(colors=TEXT_MUTED)
    ax.legend(fontsize=11, facecolor=SURFACE, labelcolor=TEXT, edgecolor=GRID)
    for spine in ax.spines.values():
        spine.set_color(GRID)

    fig.tight_layout()
    out = OUTPUT_DIR / output
    fig.savefig(out, dpi=150, bbox_inches="tight", facecolor=BG)
    plt.close(fig)
    print(f"✓ {out}  (P15={p15:.0f} P50={p50:.0f} P85={p85:.0f} itens)")
    return p15, p50, p85


if __name__ == "__main__":
    df = load_data()
    df_tp = load_data(clean_cycle_time=False)
    print_stats(df)

    throughput_daily_latest_16w = export_latest_daily_throughput_csv(
        df_tp,
        weeks=16,
        csv_path="data/throughput_daily_latest_16w.csv",
        divider=1,
    )
    sample_days = simulate_weeks_to_finish(
        target_cards=50,
        throughput_values=throughput_daily_latest_16w,
        rng=random.Random(42),
    )
    print(f"Exemplo didático (run único): 50 cards em {sample_days} dias")
    export_monte_carlo_trace_csv(
        throughput_values=throughput_daily_latest_16w,
        target_cards=50,
        runs=10_000,
        seed=42,
        csv_path="data/monte_carlo_trace_daily_10k.csv",
    )

    fig_normal_distribution_reference(mean_days=10, median_days=10)
    fig_skewed_distribution_reference(df)
    fig_cycle_time_distribution_curve(df)
    fig_cycle_time_histogram(df)
    fig_cycle_time_scatterplot(df)
    fig_throughput_weekly(df)
    fig_monte_carlo(
        df,
        n_items=50,
        throughput_values=np.array(throughput_daily_latest_16w),
        unit_label="dias",
        output="monte_carlo_resultado_daily.png",
    )
    fig_monte_carlo_animation(
        trace_csv="data/monte_carlo_trace_daily_10k.csv",
        target_cards=50,
        output_spaghetti="01-monte-carlo-spaghetti-daily.gif",
        output_histogram="03-monte-carlo-histogramas-daily.gif",
    )
    fig_monte_carlo_single_run_gif(
        trace_csv="data/monte_carlo_trace_daily_10k.csv",
        target_cards=50,
        output="00-monte-carlo-simulacao-5s-daily.gif",
    )
    fig_monte_carlo_histogram_100_runs(
        trace_csv="data/monte_carlo_trace_daily_10k.csv",
        target_cards=50,
        output="02-monte-carlo-histograma-100-runs-daily.png",
    )
    fig_monte_carlo_itens(
        throughput_values=np.array(throughput_daily_latest_16w),
        prazo_dias=34,
        output="monte_carlo_itens.png",
    )
    print("\nCharts salvos em slides/public/")
    print("Rode 'just slides' para ver a apresentação.")
