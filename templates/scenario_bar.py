"""House-style scenario bar template."""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Patch

from scripts.figure_style import SCENARIO_COLORS, apply_house_style, save_figure, strip_text_for_no_text


def plot_scenario_bar(
    scenarios,
    values,
    scenario_types,
    *,
    output_base: str | Path = "scenario_bar",
    version: str = "with_text",
    ylabel: str = "Reduction Efficiency (%)",
    legend_labels=("Single-factor scenario", "Multi-factor scenario", "Comprehensive Integration Scenarios"),
    formats=("png",),
    dpi: int = 600,
):
    apply_house_style(base_font_size=12, complete_spines=True)
    fig, ax = plt.subplots(figsize=(9, 6))

    bar_colors = [SCENARIO_COLORS[int(t) - 1] for t in scenario_types]
    bars = ax.bar(scenarios, values, color=bar_colors, width=0.55, alpha=1)

    label_fontsize = 20
    for bar in bars:
        height = bar.get_height()
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            height + 1,
            f"{height:g}%",
            ha="center",
            va="bottom",
            fontsize=label_fontsize,
            color="black",
        )
    ax.set_ylabel(ylabel, fontsize=20, labelpad=10)
    ax.tick_params(axis="both", which="major", labelsize=label_fontsize, length=4, width=1, colors="black", rotation=90)
    legend_elements = [Patch(facecolor=SCENARIO_COLORS[i], label=legend_labels[i]) for i in range(min(3, len(legend_labels)))]
    ax.legend(handles=legend_elements, loc="upper left", fontsize=20, frameon=False)
    if version != "with_text":
        strip_text_for_no_text(fig)

    ax.set_ylim(0, max(max(values) * 1.35, 1))
    for spine in ax.spines.values():
        spine.set_visible(True)
        spine.set_linewidth(1)
    ax.grid(False)

    saved = save_figure(fig, output_base, version=version, formats=formats, dpi=dpi)
    plt.close(fig)
    return fig, saved
