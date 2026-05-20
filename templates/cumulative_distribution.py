"""House-style cumulative pollution distribution template."""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from scripts.figure_style import POLLUTANT_COLORS, apply_house_style, save_figure, strip_text_for_no_text


def plot_cumulative_distribution(
    series_by_label,
    *,
    output_base: str | Path = "cumulative_distribution",
    version: str = "with_text",
    xlabel: str = "Cumulative area percentage (%)",
    ylabel: str = "Cumulative Pollution Percentage (%)",
    formats=("png",),
    dpi: int = 300,
):
    """Plot sorted cumulative contribution curves.

    `series_by_label` maps labels such as WW/COD/TN/TP to 1-D positive arrays.
    """
    apply_house_style(base_font_size=12, complete_spines=True)
    fig, ax = plt.subplots(figsize=(8, 7))

    for label, values in series_by_label.items():
        arr = np.asarray(values, dtype=float)
        valid = arr[np.isfinite(arr) & (arr > 0)]
        if valid.size == 0:
            continue
        sorted_values = np.sort(valid)[::-1]
        cumulative = np.cumsum(sorted_values)
        x = np.arange(1, sorted_values.size + 1) / sorted_values.size * 100
        y = cumulative / cumulative[-1] * 100
        ax.plot(x, y, color=POLLUTANT_COLORS.get(label, "#46788E"), linewidth=2.5, label=label, alpha=1)

    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.set_xticks(np.arange(0, 101, 20))
    ax.set_yticks(np.arange(0, 101, 20))
    ax.tick_params(axis="both", which="both", length=6, labelsize=20)

    if version == "with_text":
        ax.set_xlabel(xlabel, fontsize=20)
        ax.set_ylabel(ylabel, fontsize=20)
        legend = ax.legend(fontsize=18, loc="lower right", framealpha=1, columnspacing=0.8, handlelength=1.5, handletextpad=0.5, borderpad=0.4)
        legend.get_frame().set_facecolor("white")
        legend.get_frame().set_edgecolor("gray")
        legend.get_frame().set_linewidth(0.5)
    else:
        strip_text_for_no_text(fig)

    saved = save_figure(fig, output_base, version=version, formats=formats, dpi=dpi)
    plt.close(fig)
    return fig, saved
