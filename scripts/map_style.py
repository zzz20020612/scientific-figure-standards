"""Reusable map helpers for the user's scientific figure standards."""

from __future__ import annotations

from pathlib import Path
from typing import Iterable

import numpy as np
import rasterio
import matplotlib.pyplot as plt
from matplotlib.colors import BoundaryNorm, LinearSegmentedColormap, ListedColormap


GLOBAL_MAP_RAMP = [
    "#015D55",
    "#52928A",
    "#79B0A1",
    "#CCD9CF",
    "#FFE4E1",
    "#FFA07A",
    "#FF6347",
    "#8B0000",
]


def global_continuous_cmap(name: str = "user_global_continuous", n: int = 256):
    return LinearSegmentedColormap.from_list(name, GLOBAL_MAP_RAMP, N=n)


def global_classified_cmap(boundaries):
    cmap = ListedColormap(GLOBAL_MAP_RAMP)
    norm = BoundaryNorm(boundaries, cmap.N)
    return cmap, norm


def read_clean_raster(path: str | Path, *, mask_negative: bool = False):
    """Read a single-band raster and return clean data plus source metadata."""
    with rasterio.open(path) as src:
        data = src.read(1)
        meta = {
            "bounds": src.bounds,
            "crs": src.crs,
            "transform": src.transform,
            "nodata": src.nodata,
            "height": src.height,
            "width": src.width,
            "profile": src.profile.copy(),
        }
    nodata = meta["nodata"]
    clean = np.where(np.isnan(data) | np.isinf(data), np.nan, data)
    if nodata is not None:
        clean = np.where(data == nodata, np.nan, clean)
    if mask_negative:
        clean = np.where(clean < 0, np.nan, clean)
    return clean, meta


def lonlat_mesh(bounds, height: int, width: int):
    lon_min, lat_min, lon_max, lat_max = bounds
    lons = np.linspace(lon_min, lon_max, width)
    lats = np.linspace(lat_max, lat_min, height)
    return np.meshgrid(lons, lats)


def remove_colorbar_text(cbar) -> None:
    """Hide colorbar text while preserving tick positions and label space."""
    for label in (cbar.ax.xaxis.label, cbar.ax.yaxis.label):
        label.set_alpha(0)
        label.set_color((0, 0, 0, 0))
    for text in cbar.ax.get_xticklabels() + cbar.ax.get_yticklabels():
        text.set_alpha(0)
        text.set_color((0, 0, 0, 0))
    for text in cbar.ax.texts:
        text.set_alpha(0)
        text.set_color((0, 0, 0, 0))


def save_map(fig, output_base: str | Path, *, version: str, formats: Iterable[str] = ("png",), dpi: int = 600):
    output_base = Path(output_base)
    output_base.parent.mkdir(parents=True, exist_ok=True)
    saved = []
    for ext in formats:
        path = output_base.with_name(f"{output_base.name}_{version}.{ext.lstrip('.')}")
        kwargs = {"bbox_inches": "tight", "facecolor": "white"}
        if ext.lower() in {"png", "jpg", "jpeg", "tif", "tiff"}:
            kwargs["dpi"] = dpi
        fig.savefig(path, **kwargs)
        saved.append(path)
    return saved
