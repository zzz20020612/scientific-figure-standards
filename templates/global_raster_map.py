"""House-style global raster map template."""

from __future__ import annotations

from pathlib import Path

import cartopy.crs as ccrs
import cartopy.feature as cfeature
import matplotlib.pyplot as plt

from scripts.map_style import global_continuous_cmap, lonlat_mesh, read_clean_raster, remove_colorbar_text, save_map


def plot_global_raster_map(
    tiff_path: str | Path,
    *,
    output_base: str | Path | None = None,
    version: str = "with_text",
    colorbar_label: str = "",
    vmin=None,
    vmax=None,
    formats=("png",),
    dpi: int = 600,
    mask_negative: bool = False,
):
    data, meta = read_clean_raster(tiff_path, mask_negative=mask_negative)
    bounds = meta["bounds"]
    lon_grid, lat_grid = lonlat_mesh(bounds, meta["height"], meta["width"])

    fig = plt.figure(figsize=(14, 8))
    ax = plt.axes(projection=ccrs.Robinson())
    ax.set_global()
    ax.add_feature(cfeature.COASTLINE, linewidth=0.5, color="black", alpha=0.7)

    label_color = "black" if version == "with_text" else (0, 0, 0, 0)
    gl = ax.gridlines(
        draw_labels={"bottom": "x", "left": "y"},
        linewidth=0.5,
        color="gray",
        alpha=0.5,
        linestyle="--",
        xlocs=[-90, 0, 90],
        ylocs=[90, 60, 30, 0, -30, -60, -90],
    )
    gl.rotate_labels = False
    gl.labels_style = {"rotation": 0, "size": 10, "color": label_color}
    gl.xlabel_style = {"size": 10, "color": label_color}
    gl.ylabel_style = {"size": 10, "color": label_color}

    im = ax.pcolormesh(
        lon_grid,
        lat_grid,
        data,
        transform=ccrs.PlateCarree(),
        cmap=global_continuous_cmap(),
        shading="auto",
        vmin=vmin,
        vmax=vmax,
    )
    cbar = plt.colorbar(im, ax=ax, orientation="horizontal", pad=0.05, shrink=0.8, aspect=50, format="%.2f")
    cbar.set_label(colorbar_label, fontsize=15)
    if version != "with_text":
        remove_colorbar_text(cbar)

    plt.tight_layout()
    if output_base is None:
        output_base = Path(tiff_path).with_suffix("")
    saved = save_map(fig, output_base, version=version, formats=formats, dpi=dpi)
    plt.close(fig)
    return fig, saved
