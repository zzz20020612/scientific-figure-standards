"""House-style train/test scatter-regression template.

Expected data columns:
- actual_col: observed values
- predicted_col: predicted values
- dataset_col: values such as "Train" and "Test"
"""

from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.metrics import mean_squared_error, r2_score

from scripts.figure_style import DATASET_COLORS, apply_house_style, save_figure, strip_text_for_no_text


def plot_scatter_regression(
    data: pd.DataFrame,
    *,
    actual_col: str,
    predicted_col: str,
    dataset_col: str = "Dataset",
    variable_label: str = "Variable",
    output_base: str | Path = "scatter_regression",
    version: str = "with_text",
    formats=("png",),
    dpi: int = 600,
):
    apply_house_style(base_font_size=12, complete_spines=True)

    g = sns.jointplot(
        data=data,
        x=actual_col,
        y=predicted_col,
        hue=dataset_col,
        height=10,
        palette=DATASET_COLORS,
        kind="scatter",
        s=100,
        ratio=3,
        space=0,
    )
    ax = g.ax_joint

    for spine in ax.spines.values():
        spine.set_visible(True)
        spine.set_linewidth(1.0)

    g.plot_marginals(sns.histplot, kde=True, color="gray", alpha=0.3, bins=10, fill=True)

    for name, color in DATASET_COLORS.items():
        subset = data[data[dataset_col] == name]
        if not subset.empty:
            sns.regplot(
                data=subset,
                x=actual_col,
                y=predicted_col,
                scatter=False,
                ax=ax,
                color=color,
                ci=95,
                line_kws={"linewidth": 2},
            )

    max_val = max(data[actual_col].max(), data[predicted_col].max()) * 1.1
    ax.plot([0, max_val], [0, max_val], "k--", alpha=0.5)
    ax.set_xlim(0, max_val)
    ax.set_ylim(0, max_val)

    if version == "with_text":
        ax.set_xlabel(f"Obs {variable_label} Load Fraction", fontsize=25)
        ax.set_ylabel(f"Pred {variable_label} Load Fraction", fontsize=25)
        ax.tick_params(axis="both", labelsize=25)

        handles, labels = ax.get_legend_handles_labels()
        if handles:
            legends = []
            for name, loc in (("Train", "upper left"), ("Test", "lower right")):
                subset = data[data[dataset_col] == name]
                if subset.empty:
                    continue
                r2 = r2_score(subset[actual_col], subset[predicted_col])
                rmse = np.sqrt(mean_squared_error(subset[actual_col], subset[predicted_col]))
                handle = handles[labels.index(name)] if name in labels else handles[0]
                legend = ax.legend(
                    [handle],
                    [f"{'Training data' if name == 'Train' else 'Test data'}\nR2 = {r2:.2f}\nRMSE = {rmse:.3f}"],
                    fontsize=25,
                    loc=loc,
                    frameon=True,
                    facecolor="lightgray",
                )
                legends.append(legend)
            if legends:
                ax.add_artist(legends[0])
    else:
        strip_text_for_no_text(g.fig)

    g.fig.subplots_adjust(hspace=0, wspace=0)
    saved = save_figure(g.fig, output_base, version=version, formats=formats, dpi=dpi)
    return g.fig, saved
