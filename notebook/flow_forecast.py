from __future__ import annotations

import math
import random
from pathlib import Path
from typing import Iterable, Sequence

import numpy as np
import pandas as pd


def read_items_csv(
    path: str | Path,
    *,
    started_col: str = "started_at",
    finished_col: str = "finished_at",
) -> pd.DataFrame:
    # Header não importa: sempre ler como "sem header" e pegar as 2 primeiras colunas.
    # Se existir header, ele vira uma linha (e cai no dropna após parse).
    df = pd.read_csv(
        path,
        header=None,
        names=[started_col, finished_col],
        usecols=[0, 1],
    )

    df = df.copy()
    # CSV pode misturar date e datetime; parse robusto e depois ignora hora (normalize).
    df[started_col] = pd.to_datetime(df[started_col], errors="coerce", format="mixed")
    df[finished_col] = pd.to_datetime(df[finished_col], errors="coerce", format="mixed")

    df = df.dropna(subset=[started_col, finished_col])
    df[started_col] = df[started_col].dt.normalize()
    df[finished_col] = df[finished_col].dt.normalize()

    invalid = df[df[finished_col] < df[started_col]]
    if not invalid.empty:
        examples = invalid[[started_col, finished_col]].head(5)
        raise ValueError(
            "CSV inválido: encontrou item com finished_at < started_at. "
            f"Exemplos:\n{examples.to_string(index=False)}"
        )

    return df


def add_cycle_time_days(
    df: pd.DataFrame,
    *,
    started_col: str = "started_at",
    finished_col: str = "finished_at",
    out_col: str = "cycle_time_days",
) -> pd.DataFrame:
    started = pd.to_datetime(df[started_col]).dt.normalize()
    finished = pd.to_datetime(df[finished_col]).dt.normalize()
    return df.assign(**{out_col: (finished - started).dt.days + 1})


def cycle_time_days_values(
    df: pd.DataFrame,
    *,
    started_col: str = "started_at",
    finished_col: str = "finished_at",
) -> np.ndarray:
    tmp = add_cycle_time_days(
        df, started_col=started_col, finished_col=finished_col, out_col="cycle_time_days"
    )
    values = tmp["cycle_time_days"].to_numpy(dtype=float)
    values = values[np.isfinite(values)]
    values = values[values > 0]
    return values.astype(int)


def percentile(values: Sequence[int] | np.ndarray, p: float) -> int:
    if len(values) == 0:
        raise ValueError("percentile: values vazio")
    return int(math.ceil(float(np.percentile(np.asarray(values), p))))


def sle_days(values: Sequence[int] | np.ndarray, *, confidence: float = 0.85) -> int:
    return percentile(values, confidence * 100)


def daily_throughput(
    df: pd.DataFrame,
    *,
    finished_col: str = "finished_at",
) -> np.ndarray:
    finished = pd.to_datetime(df[finished_col]).dt.normalize()
    finished = finished.dropna()
    if finished.empty:
        raise ValueError("daily_throughput: sem finished_at válido")

    days = pd.date_range(finished.min(), finished.max(), freq="D")
    series = finished.value_counts().sort_index().reindex(days, fill_value=0).astype(int)
    return series.to_numpy(dtype=int)


def simulate_days_to_finish(
    n_items: int,
    daily_tp: Sequence[int] | np.ndarray,
    *,
    rng: random.Random | None = None,
) -> int:
    if n_items < 0:
        raise ValueError("n_items deve ser >= 0")
    tp = list(int(x) for x in daily_tp)
    if len(tp) == 0:
        raise ValueError("daily_tp vazio")

    rng = rng or random.Random()
    remaining = n_items
    days = 0
    while remaining > 0:
        days += 1
        remaining -= rng.choice(tp)
    return days


def monte_carlo_days_to_finish(
    n_items: int,
    daily_tp: Sequence[int] | np.ndarray,
    *,
    runs: int = 10_000,
    seed: int = 42,
) -> np.ndarray:
    if runs < 1:
        raise ValueError("runs deve ser >= 1")
    if n_items < 0:
        raise ValueError("n_items deve ser >= 0")

    tp = np.asarray(daily_tp, dtype=int)
    if tp.size == 0:
        raise ValueError("daily_tp vazio")

    rng = np.random.default_rng(seed)
    out = np.empty(runs, dtype=int)
    for i in range(runs):
        done = 0
        days = 0
        while done < n_items:
            done += int(rng.choice(tp))
            days += 1
        out[i] = days
    return out


def simulate_items_in_days(
    n_days: int,
    daily_tp: Sequence[int] | np.ndarray,
    *,
    rng: random.Random | None = None,
) -> int:
    if n_days < 0:
        raise ValueError("n_days deve ser >= 0")
    tp = list(int(x) for x in daily_tp)
    if len(tp) == 0:
        raise ValueError("daily_tp vazio")

    rng = rng or random.Random()
    delivered = 0
    for _ in range(n_days):
        delivered += rng.choice(tp)
    return delivered


def monte_carlo_items_in_days(
    n_days: int,
    daily_tp: Sequence[int] | np.ndarray,
    *,
    runs: int = 10_000,
    seed: int = 42,
) -> np.ndarray:
    if runs < 1:
        raise ValueError("runs deve ser >= 1")
    if n_days < 0:
        raise ValueError("n_days deve ser >= 0")

    tp = np.asarray(daily_tp, dtype=int)
    if tp.size == 0:
        raise ValueError("daily_tp vazio")

    rng = np.random.default_rng(seed)
    out = np.empty(runs, dtype=int)
    for i in range(runs):
        out[i] = int(rng.choice(tp, size=n_days, replace=True).sum())
    return out


def percentiles_from_sim(sim: Sequence[int] | np.ndarray, ps: Iterable[int] = (50, 85, 95)) -> dict[int, float]:
    arr = np.asarray(sim, dtype=float)
    if arr.size == 0:
        raise ValueError("sim vazio")
    ps_list = list(ps)
    vals = np.percentile(arr, ps_list)
    return {int(p): float(v) for p, v in zip(ps_list, vals, strict=True)}

