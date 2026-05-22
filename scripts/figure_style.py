"""Reusable house style helpers for scientific figures.

Copy or import this module in local projects when applying the user's figure
standards. Keep functions small and explicit so project scripts can adapt them.
"""

from __future__ import annotations

from pathlib import Path
from typing import Iterable, Mapping

import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap


POLLUTANT_COLORS: Mapping[str, str] = {
    "WW": "#46788E",
    "water": "#46788E",
    "COD": "#78B7C9",
    "TN": "#F6E093",
    "TP": "#E58B7B",
}

DATASET_COLORS: Mapping[str, str] = {
    "Train": "#3769b1",
    "Test": "#d6221b",
}

SCENARIO_COLORS = ["#3182bd", "#9ecae1", "#fd8d3c", "#3769b1"]

SHAP_RAMP = [
    "#067FB8",
    "#4C93BD",
    "#9AC2DB",
    "#BCD6E5",
    "#FDE6DE",
    "#F1B4A1",
    "#E38C7B",
    "#D26872",
]


def apply_house_style(base_font_size: float = 12, complete_spines: bool = True) -> None:
    """Apply the user's default scientific-figure style."""
    mpl.rcParams.update(
        {
            "font.family": "sans-serif",
            "font.sans-serif": ["Arial", "Helvetica", "DejaVu Sans"],
            "font.size": base_font_size,
            "axes.linewidth": 1.0,
            "axes.unicode_minus": False,
            "axes.spines.left": True,
            "axes.spines.bottom": True,
            "axes.spines.top": complete_spines,
            "axes.spines.right": complete_spines,
            "figure.facecolor": "white",
            "axes.facecolor": "white",
            "savefig.facecolor": "white",
            "svg.fonttype": "none",
            "pdf.fonttype": 42,
        }
    )


def make_shap_cmap(name: str = "user_shap_diverging", n: int = 1500) -> LinearSegmentedColormap:
    return LinearSegmentedColormap.from_list(name, SHAP_RAMP, N=n)


def style_axes(ax, *, complete_spines: bool = True, grid: bool = False) -> None:
    for side in ("left", "bottom", "top", "right"):
        ax.spines[side].set_visible(complete_spines or side in ("left", "bottom"))
        ax.spines[side].set_linewidth(1.0)
    ax.tick_params(axis="both", which="major", direction="out", length=4, width=1)
    ax.grid(grid, linestyle="--", linewidth=0.5, alpha=0.5, color="gray")


def _make_text_invisible(text) -> None:
    """Hide text without changing its layout reservation."""
    text.set_alpha(0)
    text.set_color((0, 0, 0, 0))


def hide_text_preserve_layout(fig) -> None:
    """Hide visible text while preserving text objects, padding, and layout."""
    for ax in fig.axes:
        _make_text_invisible(ax.title)
        _make_text_invisible(ax.xaxis.label)
        _make_text_invisible(ax.yaxis.label)
        for text in ax.get_xticklabels() + ax.get_yticklabels():
            _make_text_invisible(text)
        legend = ax.get_legend()
        if legend is not None:
            for text in legend.get_texts():
                _make_text_invisible(text)
            _make_text_invisible(legend.get_title())
        for text in ax.texts:
            _make_text_invisible(text)
    for text in fig.texts:
        _make_text_invisible(text)


def strip_text_for_no_text(fig) -> None:
    """Backward-compatible alias for the no-text layout-preserving standard."""
    hide_text_preserve_layout(fig)


def save_figure(
    fig,
    output_base: str | Path,
    *,
    version: str = "with_text",
    formats: Iterable[str] = ("png",),
    dpi: int = 300,
    tight: bool = True,
) -> list[Path]:
    """Save a figure with house defaults and a version suffix."""
    output_base = Path(output_base)
    output_base.parent.mkdir(parents=True, exist_ok=True)
    suffix = f"_{version}" if version in {"with_text", "no_text"} else ""
    saved: list[Path] = []
    for ext in formats:
        path = output_base.with_name(f"{output_base.name}{suffix}.{ext.lstrip('.')}")
        kwargs = {"bbox_inches": "tight"} if tight else {}
        if ext.lower() in {"png", "jpg", "jpeg", "tif", "tiff"}:
            kwargs["dpi"] = dpi
        fig.savefig(path, facecolor="white", **kwargs)
        saved.append(path)
    return saved
