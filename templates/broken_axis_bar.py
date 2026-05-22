"""House-style broken-axis contribution bar template."""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from scripts.figure_style import POLLUTANT_COLORS, apply_house_style, save_figure, strip_text_for_no_text


def plot_broken_axis_bar(
    labels,
    percentages,
    annotations=None,
    *,
    break_point: float = 55,
    output_base: str | Path = "broken_axis_bar",
    version: str = "with_text",
    formats=("png", "tiff", "pdf"),
    dpi: int = 300,
):
    apply_house_style(base_font_size=12, complete_spines=True)
    fig, (ax_top, ax_bottom) = plt.subplots(2, 1, figsize=(8, 8), gridspec_kw={"height_ratios": [7, 1], "hspace": 0.03})

    x_pos = np.arange(len(labels))
    colors = [POLLUTANT_COLORS.get(label, "#46788E") for label in labels]
    percentages = np.asarray(percentages, dtype=float)
    annotations = annotations if annotations is not None else [None] * len(labels)

    bars_top = ax_top.bar(x_pos, percentages, color=colors, alpha=1)
    ax_bottom.bar(x_pos, percentages, color=colors, alpha=1)

    max_percentage = float(np.nanmax(percentages)) if percentages.size else break_point
    ax_top.set_ylim(break_point, max_percentage * 1.1)
    ax_bottom.set_ylim(0, break_point)
    ax_top.set_xticks([])
    ax_bottom.set_xticks([])
    ax_top.tick_params(axis="y", labelsize=40)
    ax_bottom.tick_params(axis="y", labelsize=40)

    for bar, label in zip(bars_top, annotations):
        if label:
            ax_top.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + max_percentage * 0.05, str(label), ha="center", va="bottom", fontsize=30, fontweight="bold")
    if version != "with_text":
        strip_text_for_no_text(fig)

    d = 0.010
    kwargs = dict(transform=ax_top.transAxes, color="k", clip_on=False)
    ax_top.plot((-d, +d), (-d, +d), **kwargs)
    ax_top.plot((1 - d, 1 + d), (-d, +d), **kwargs)
    kwargs.update(transform=ax_bottom.transAxes)
    ax_bottom.plot((-d, +d), (1 - d, 1 + d), **kwargs)
    ax_bottom.plot((1 - d, 1 + d), (1 - d, 1 + d), **kwargs)

    saved = save_figure(fig, output_base, version=version, formats=formats, dpi=dpi)
    plt.close(fig)
    return fig, saved
