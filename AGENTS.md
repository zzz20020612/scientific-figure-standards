# Scientific Figure Standards

Use these instructions whenever this project involves scientific plotting, manuscript figures, model-result charts, maps, GeoTIFF/raster visualization, or publication exports.

## Required First Question

Before creating or editing any figure, ask which output version is required unless already specified:

- `with_text`: keep labels, units, tick labels, legends, colorbar labels, panel labels, and necessary annotations.
- `no_text`: remove all visible text while preserving axes/spines, tick marks, colorbar body, legend swatches/symbols, and graphical structure.
- `both`: generate separate `_with_text` and `_no_text` outputs.

## Template-First Rule

When the requested figure resembles an existing pattern, start from `templates/` rather than re-creating the style from prose:

- `scatter_regression.py`
- `scenario_bar.py`
- `cumulative_distribution.py`
- `broken_axis_bar.py`
- `shap_swarm.py`
- `global_raster_map.py`

## Hard Defaults

- Use English figure text by default.
- Use Arial first, with Helvetica and DejaVu Sans as fallbacks.
- Use a white background.
- Use complete axes/spines by default for ordinary scientific plots.
- Use restrained, publication-style palettes; do not use rainbow, random, or default matplotlib colors when a house palette applies.
- Save raster outputs at 300 dpi minimum; use 600 dpi for final figures, maps, dense panels, or submission-like outputs.
- Use `bbox_inches="tight"` and `facecolor="white"` for saved figures.
- Set `svg.fonttype = "none"` and `pdf.fonttype = 42` before vector export.

## Required References

When this repository is available, consult these files before implementing substantial plotting work:

- `references/template-guide.md` for template selection.
- `references/visual-standards.md` for scientific plot style and QA.
- `references/map-standards.md` for maps, CRS, GeoTIFF, and colorbar rules.
- `references/data-standards.md` for unit conversion, missing data, model metrics, and statistics.
- `references/current-project-style.md` for extracted house-style examples.

Use `scripts/figure_style.py` and `scripts/map_style.py` when writing lower-level Python plotting code.

## QA Before Completion

Verify requested version(s), font, language, units, palette, dpi, output format, data transformations, no-text text removal, and absence of overlap before claiming a figure is complete.
