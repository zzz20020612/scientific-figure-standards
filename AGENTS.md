# Scientific Figure Standards

Use these instructions whenever this project involves scientific plotting, manuscript figures, model-result charts, maps, GeoTIFF/raster visualization, or publication exports.

## Required First Question

Before creating or editing any figure, ask which output version is required unless already specified:

- `with_text`: keep labels, units, tick labels, legends, colorbar labels, panel labels, and necessary annotations.
- `no_text`: keep the same text objects and layout positions as `with_text`, but make text invisible/transparent. Do not delete labels, tick labels, legends, colorbar labels, panel labels, annotations, or map graticule labels if deletion changes spacing.
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
- For world maps, show left-edge latitude labels and bottom-edge longitude labels; default ticks are `xlocs=[-90, 0, 90]` and `ylocs=[90, 60, 30, 0, -30, -60, -90]`, with unrotated size-10 labels.
- For no-text maps, keep those graticule labels as transparent placeholders.
- For submission figures, export PNG at 300 dpi, TIFF at 300 dpi, and PDF by default.
- Do not generate SVG by default unless explicitly requested or required by the target journal.
- Use panel labels `a`, `b`, `c` without parentheses for multi-panel submission figures.
- Use `bbox_inches="tight"` and `facecolor="white"` for saved figures.
- Set `svg.fonttype = "none"` and `pdf.fonttype = 42` before vector export.

## Required References

When this repository is available, consult these files before implementing substantial plotting work:

- `references/template-guide.md` for template selection.
- `references/submission-standards.md` for final manuscript, journal, thesis, or publication-ready outputs.
- `references/visual-standards.md` for scientific plot style and QA.
- `references/map-standards.md` for maps, CRS, GeoTIFF, and colorbar rules.
- `references/data-standards.md` for unit conversion, missing data, model metrics, and statistics.
- `references/current-project-style.md` for extracted house-style examples.

Use `scripts/figure_style.py` and `scripts/map_style.py` when writing lower-level Python plotting code.

## QA Before Completion

Verify requested version(s), font, language, units, palette, dpi, output format, data transformations, no-text transparent placeholders, world-map left/bottom graticule labels, and absence of overlap before claiming a figure is complete.
