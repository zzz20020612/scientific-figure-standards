# Map Standards

Use this reference for maps, GeoTIFFs, rasters, gridded environmental data, CRS decisions, global maps, and regional spatial visualizations.

For global raster maps, start from `templates/global_raster_map.py` unless the task requires a substantially different cartographic layout.

## Version Gate

Maps follow the same version rule as all figures:

- Ask whether to generate `with_text`, `no_text`, or both unless already stated.
- `no_text` makes text invisible/transparent while preserving text objects, label padding, tick positions, colorbar label space, graticule label space, map geometry, coastlines/boundaries, gridline strokes, colorbar body, legend swatches, and graphical structure.

## Projection Rules

- World maps default to Robinson projection.
- World lon/lat raster data is drawn with `transform=ccrs.PlateCarree()`.
- Regional maps do not default to Robinson.
- For regional lon/lat data, prefer EPSG:4326 / PlateCarree unless there is a clear analytical or cartographic reason to use a projected CRS.
- For administrative boundaries, watersheds, and local study areas, respect the data CRS and map purpose.

Do not force a global decorative projection onto a local or regional map.

## House World Map Style

Current user world-map style:

- `figsize=(14, 8)`
- Robinson projection
- global extent
- black coastline, linewidth about 0.5, alpha about 0.7
- gray dashed gridlines, linewidth about 0.5, alpha about 0.5
- longitude labels on the bottom edge only, with `xlocs=[-90, 0, 90]`
- latitude labels on the left edge only, with `ylocs=[90, 60, 30, 0, -30, -60, -90]`
- no top/right graticule labels by default
- `rotate_labels=False`
- graticule label size about 10, following the user's original code
- horizontal colorbar, `pad=0.05`, `shrink=0.8`, `aspect=50`
- white background
- `tight_layout()` before saving
- PNG at 300 or 600 dpi depending on final use

Canonical world-map graticule code:

```python
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
gl.labels_style = {"rotation": 0, "size": 10}
gl.xlabel_style = {"size": 10}
gl.ylabel_style = {"size": 10}
```

For no-text world maps, still use `draw_labels={"bottom": "x", "left": "y"}` and the same tick locations. Hide label text by transparent color/alpha; do not omit labels, clear strings, or remove tick locations.

## Regional Graticules

For regional maps that need graticules:

- Use left-edge latitude labels and bottom-edge longitude labels.
- Keep top/right labels off unless the user explicitly asks.
- Keep labels sparse, usually 3-5 major ticks per axis.
- Use extent-aware tick values instead of world-map defaults.
- Keep gridlines light gray, dashed, linewidth about 0.5, alpha about 0.5.
- Keep labels unrotated and visually quiet; start from size 10 and reduce only for compact panels.

## Global Map Color Ramp

Use this ramp for global emission, rate, intensity, coefficient of variation, risk, and similar continuous or ordered variables unless the variable semantics require a different palette:

```python
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
```

Continuous data:

```python
LinearSegmentedColormap.from_list("user_global_continuous", GLOBAL_MAP_RAMP, N=256)
```

Classified data:

```python
ListedColormap(GLOBAL_MAP_RAMP)
BoundaryNorm(boundaries, ncolors=8)
```

## Raster Cleaning

Before mapping rasters:

- Read nodata from the source file.
- Convert nodata, NaN, and inf to `np.nan`.
- Decide how to treat negative values based on the variable. For pollution/emission/rate variables, negative values are usually invalid and should be masked or clipped.
- Document unit conversions in code, not only in labels.
- If using log10, protect zero and negative values explicitly.
- If clipping/stretching, state percentile or fixed bounds.

## Colorbar Rules

With-text maps:

- Include clear colorbar labels and units.
- Use readable tick labels.
- Use concise scientific notation when values are extreme.

No-text maps:

- Keep colorbar labels and tick labels as objects, but make them invisible/transparent.
- Do not call `set_ticks([])`, `set_ticklabels([])`, `NullLocator`, or `NullFormatter` solely to make a no-text version, because those change the layout and remove the user's future text-placement guide.
- Keep the colorbar body and outline unless the user requests a fully minimal map.

## North Arrow and Scale Bar

First version intentionally does not define north-arrow or scale-bar standards. Treat them as a future extension. If a task needs them, ask the user for the desired convention or wait for the updated skill.

## QA

Check:

- Projection matches map scale and purpose.
- Data transform matches CRS.
- Nodata/missing areas are not miscolored as real data.
- Colorbar bounds match the intended transformation.
- Coastline/boundary strokes do not dominate the raster.
- No-text version contains no visible labels, tick labels, titles, or annotations, but preserves their positions for later manual composition.
