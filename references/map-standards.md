# Map Standards

Use this reference for maps, GeoTIFFs, rasters, gridded environmental data, CRS decisions, global maps, and regional spatial visualizations.

For global raster maps, start from `templates/global_raster_map.py` unless the task requires a substantially different cartographic layout.

## Version Gate

Maps follow the same version rule as all figures:

- Ask whether to generate `with_text`, `no_text`, or both unless already stated.
- `no_text` removes all visible text but keeps map geometry, coastlines/boundaries, gridline strokes, colorbar body, legend swatches, and graphical structure.

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
- horizontal colorbar, `pad=0.05`, `shrink=0.8`, `aspect=50`
- white background
- `tight_layout()` before saving
- PNG at 300 or 600 dpi depending on final use

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

- Remove colorbar labels and tick labels.
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
- No-text version contains no labels, tick labels, titles, or annotations.
