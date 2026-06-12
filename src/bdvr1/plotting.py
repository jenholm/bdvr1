"""Reproduce paper figures."""

from __future__ import annotations

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from scipy.stats import spearmanr

from bdvr1.config import OUTPUT_FIGURES, RANDOM_SEED

# Non-interactive backend for script use
matplotlib.use("Agg")

PLOT_STYLE = {
    "font.family": "sans-serif",
    "font.size": 10,
    "axes.titlesize": 12,
    "axes.labelsize": 11,
    "figure.dpi": 180,
    "savefig.dpi": 180,
    "savefig.bbox": "tight",
}


def _apply_style():
    plt.rcParams.update(PLOT_STYLE)


def _minmax(x: np.ndarray) -> np.ndarray:
    x = np.asarray(x, dtype=float)
    xmin, xmax = np.nanmin(x), np.nanmax(x)
    if xmax == xmin:
        return np.zeros_like(x)
    return (x - xmin) / (xmax - xmin)


def plot_cross_survey_quartiles(
    sparc_df,
    xgass_df,
    sparc_score_col: str = "sparc_demographic_proxy",
    xgass_score_col: str = "xgass_coherence_proxy",
    sparc_residual_col: str = "btfr_abs_residual",
    xgass_residual_col: str = "btfr_abs_residual",
    save: bool = True,
):
    _apply_style()
    fig, axes = plt.subplots(1, 2, figsize=(9, 4.5))

    for ax, df, score_col, res_col, title in [
        (axes[0], sparc_df, sparc_score_col, sparc_residual_col, "SPARC"),
        (axes[1], xgass_df, xgass_score_col, xgass_residual_col, "xGASS"),
    ]:
        valid = df[[score_col, res_col]].dropna()
        C = valid[score_col].to_numpy()
        R = valid[res_col].to_numpy()
        order = np.argsort(C)
        n = len(order)
        qsize = n // 4
        colors = ["tab:blue", "tab:cyan", "tab:orange", "tab:red"]
        for i, (label, color) in enumerate(zip(["Q1", "Q2", "Q3", "Q4"], colors)):
            lo = i * qsize
            hi = (i + 1) * qsize if i < 3 else n
            idx = order[lo:hi]
            ax.scatter(
                C[idx], R[idx],
                c=color, label=label, s=18, alpha=0.7, edgecolors="none",
            )
        ax.set_xlabel("Organization proxy")
        ax.set_ylabel("|BTFR residual| (dex)")
        ax.set_title(title)
        ax.legend(fontsize=8, title="Quartile")
        ax.grid(alpha=0.15)

    fig.tight_layout()
    if save:
        OUTPUT_FIGURES.mkdir(parents=True, exist_ok=True)
        fig.savefig(OUTPUT_FIGURES / "fig1_cross_survey_quartiles.png")
    plt.close(fig)


def plot_xgass_velocity_variants(
    xgass_df,
    vels: dict[str, str] | None = None,
    score_col: str = "xgass_coherence_proxy",
    save: bool = True,
):
    _apply_style()
    if vels is None:
        vels = {"Vflat (W50/2)": "Vflat", "Mbar-based logV": "logVflat"}
    fig, axes = plt.subplots(1, len(vels), figsize=(9, 4.5))
    if len(vels) == 1:
        axes = [axes]

    valid = xgass_df[[score_col]].dropna()
    C = valid[score_col].to_numpy()

    for ax, (label, vel_col) in zip(axes, vels.items()):
        if vel_col in xgass_df.columns:
            V = xgass_df.loc[valid.index, vel_col].to_numpy()
        else:
            V = np.full(len(valid), np.nan)
        ax.scatter(C, V, s=12, alpha=0.6, c="steelblue", edgecolors="none")
        rho, p = spearmanr(C[~np.isnan(V)], V[~np.isnan(V)])
        ax.set_xlabel("Coherence proxy")
        ax.set_ylabel(label)
        ax.set_title(f"{label}\nrho={rho:.3f}")
        ax.grid(alpha=0.15)

    fig.tight_layout()
    if save:
        OUTPUT_FIGURES.mkdir(parents=True, exist_ok=True)
        fig.savefig(OUTPUT_FIGURES / "fig2_xgass_velocity_variants.png")
    plt.close(fig)


def plot_proxy_variant_comparison(
    ablation_results: dict,
    save: bool = True,
):
    _apply_style()
    variants = list(ablation_results.keys())
    rhos = [ablation_results[v].get("spearman_rho", np.nan) for v in variants]
    ratios = [ablation_results[v].get("Q4_Q1_ratio", np.nan) for v in variants]

    fig, axes = plt.subplots(2, 1, figsize=(8, 6))

    colors = ["tab:blue" if r > 0 else "tab:red" for r in rhos]
    axes[0].barh(variants, rhos, color=colors, alpha=0.7)
    axes[0].axvline(0, color="black", linewidth=0.8)
    axes[0].set_xlabel("Spearman rho")
    axes[0].set_title("Proxy variant vs |BTFR residual|")

    axes[1].barh(variants, ratios, color="tab:orange", alpha=0.7)
    axes[1].axvline(1, color="black", linestyle="--", linewidth=0.8)
    axes[1].set_xlabel("Q4/Q1 scatter ratio")
    axes[1].set_title("Q4/Q1 ratio by variant")

    fig.tight_layout()
    if save:
        OUTPUT_FIGURES.mkdir(parents=True, exist_ok=True)
        fig.savefig(OUTPUT_FIGURES / "fig3_proxy_variant_comparison.png")
    plt.close(fig)


def plot_mass_bin_quartiles(
    xgass_df,
    score_col: str = "xgass_coherence_proxy",
    mass_col: str = "logMbar",
    residual_col: str = "btfr_abs_residual",
    save: bool = True,
):
    _apply_style()
    valid = xgass_df[[score_col, mass_col, residual_col]].dropna()
    C = valid[score_col].to_numpy()
    M = valid[mass_col].to_numpy()
    R = valid[residual_col].to_numpy()

    mass_bins = np.linspace(np.nanpercentile(M, 10), np.nanpercentile(M, 90), 5)
    n_bins = len(mass_bins) - 1

    fig, axes = plt.subplots(1, n_bins, figsize=(4 * n_bins, 4))
    if n_bins == 1:
        axes = [axes]

    for i, ax in enumerate(axes):
        lo, hi = mass_bins[i], mass_bins[i + 1]
        mask = (M >= lo) & (M < hi)
        if np.sum(mask) < 4:
            ax.set_title(f"M bin {i+1}\n(no data)")
            continue
        C_bin = C[mask]
        R_bin = R[mask]
        order = np.argsort(C_bin)
        qsize = len(order) // 4
        colors = ["tab:blue", "tab:cyan", "tab:orange", "tab:red"]
        for j, (label, color) in enumerate(zip(["Q1", "Q2", "Q3", "Q4"], colors)):
            lo_j = j * qsize
            hi_j = (j + 1) * qsize if j < 3 else len(order)
            idx = order[lo_j:hi_j]
            ax.scatter(
                C_bin[idx], R_bin[idx],
                c=color, label=label if i == n_bins - 1 else None,
                s=15, alpha=0.6, edgecolors="none",
            )
        ax.set_xlabel("Proxy")
        ax.set_ylabel("|Residual|")
        ax.set_title(f"M bin [{lo:.2f}, {hi:.2f}]")
        ax.grid(alpha=0.15)

    fig.legend(fontsize=8, loc="upper right")
    fig.tight_layout()
    if save:
        OUTPUT_FIGURES.mkdir(parents=True, exist_ok=True)
        fig.savefig(OUTPUT_FIGURES / "fig4_mass_bin_quartiles.png")
    plt.close(fig)


def plot_q4_q1_summary(
    summary_data: dict,
    save: bool = True,
):
    _apply_style()
    labels = list(summary_data.keys())
    ratios = [summary_data[k].get("Q4_Q1_ratio", np.nan) for k in labels]
    ci_lows = [summary_data[k].get("ratio_ci_95", [np.nan, np.nan])[0] for k in labels]
    ci_highs = [summary_data[k].get("ratio_ci_95", [np.nan, np.nan])[1] for k in labels]

    fig, ax = plt.subplots(figsize=(7, 4.5))
    xpos = np.arange(len(labels))
    ax.bar(xpos, ratios, color="tab:purple", alpha=0.7, yerr=[
        [r - cl if np.isfinite(cl) else 0 for r, cl in zip(ratios, ci_lows)],
        [ch - r if np.isfinite(ch) else 0 for r, ch in zip(ratios, ci_highs)],
    ], capsize=4)
    ax.axhline(1, color="black", linestyle="--", linewidth=0.8, label="Q4/Q1 = 1")
    ax.set_xticks(xpos)
    ax.set_xticklabels(labels, rotation=30, ha="right")
    ax.set_ylabel("Q4/Q1 scatter ratio")
    ax.set_title("Q4/Q1 ratio summary with 95% CI")
    ax.legend()
    ax.grid(alpha=0.15, axis="y")

    fig.tight_layout()
    if save:
        OUTPUT_FIGURES.mkdir(parents=True, exist_ok=True)
        fig.savefig(OUTPUT_FIGURES / "fig5_q4_q1_ratio_summary.png")
    plt.close(fig)
