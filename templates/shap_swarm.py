"""House-style SHAP swarm + mean absolute SHAP bar template."""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from scripts.figure_style import apply_house_style, make_shap_cmap, save_figure, strip_text_for_no_text


def plot_shap_swarm(
    shap_data: pd.DataFrame,
    *,
    feature_col: str = "Feature",
    shap_col: str = "SHAP Value",
    value_col: str = "Feature Value",
    output_base: str | Path = "shap_swarm",
    version: str = "with_text",
    sample_size_per_feature: int = 15500,
    formats=("png", "tiff", "pdf"),
    dpi: int = 300,
):
    apply_house_style(base_font_size=10, complete_spines=True)
    custom_cmap = make_shap_cmap()

    feature_names = shap_data[feature_col].unique().tolist()
    sampled = []
    for feature in feature_names:
        feature_data = shap_data[shap_data[feature_col] == feature]
        if len(feature_data) > sample_size_per_feature:
            sampled.append(feature_data.sample(sample_size_per_feature, random_state=42))
        else:
            sampled.append(feature_data)
    sampled_data = pd.concat(sampled)

    importance = {
        feature: np.abs(sampled_data.loc[sampled_data[feature_col] == feature, shap_col]).mean()
        for feature in feature_names
    }
    sorted_features = sorted(importance.items(), key=lambda item: item[1], reverse=True)
    sorted_feature_names = [item[0] for item in sorted_features]
    sorted_importance = [item[1] for item in sorted_features]

    fig, ax = plt.subplots(figsize=(7, len(feature_names) * 0.8), dpi=dpi)
    bar_color = "#B0C4DE"

    for i, feature in enumerate(sorted_feature_names):
        feature_data = sampled_data[sampled_data[feature_col] == feature]
        shap_values = feature_data[shap_col].to_numpy()
        feature_values = feature_data[value_col].to_numpy()
        if np.nanmax(feature_values) > np.nanmin(feature_values):
            norm_values = (feature_values - np.nanmin(feature_values)) / (np.nanmax(feature_values) - np.nanmin(feature_values))
        else:
            norm_values = np.zeros_like(feature_values)
        order = np.argsort(norm_values)
        np.random.seed(42)
        y_jitter = np.random.normal(0, 0.08, size=len(order))
        x_jitter = np.random.normal(0, 0.008, size=len(order))
        ax.scatter(
            shap_values[order] + x_jitter,
            np.ones(len(order)) * i + y_jitter,
            c=norm_values[order],
            cmap=custom_cmap,
            s=3,
            alpha=0.7,
            edgecolor="none",
            rasterized=True,
        )

    ax.set_yticks(range(len(sorted_feature_names)))
    ax.set_yticklabels(sorted_feature_names)
    ax.set_xlabel("SHAP Value", fontsize=11)

    ax2 = ax.twiny()
    bars = ax2.barh(range(len(sorted_feature_names)), sorted_importance, color=bar_color, alpha=0.3, height=0.6, edgecolor="none")

    for bar, value in zip(bars, sorted_importance):
        ax2.text(max(sorted_importance) * 0.02, bar.get_y() + bar.get_height() / 2, f"{value:.3f}", va="center", ha="left", fontsize=8, color="black")
    ax2.set_xlabel("Mean |SHAP Value|", fontsize=10, color=bar_color)
    ax2.tick_params(axis="x", labelsize=9, colors=bar_color)
    fig.subplots_adjust(left=0.25, right=0.82)
    cax = fig.add_axes([0.85, 0.2, 0.025, 0.6])
    cbar = fig.colorbar(plt.cm.ScalarMappable(cmap=custom_cmap), cax=cax)
    cbar.set_label("Feature Value", fontsize=10)
    cbar.ax.tick_params(labelsize=9)
    cbar.outline.set_visible(False)

    for spine_name, spine in ax.spines.items():
        spine.set_visible(spine_name != "top")
        spine.set_linewidth(0.1 if spine_name != "top" else 0)
    for spine in ax2.spines.values():
        spine.set_visible(True)
        spine.set_linewidth(0.5)

    if version != "with_text":
        strip_text_for_no_text(fig)

    saved = save_figure(fig, output_base, version=version, formats=formats, dpi=dpi)
    plt.close(fig)
    return fig, saved
