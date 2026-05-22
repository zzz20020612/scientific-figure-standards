---
name: scientific-figure-standards
description: >-
  Global hard standards for the user's scientific figures, manuscript plots,
  maps, GeoTIFF/raster visualizations, model-result charts, SHAP/ML figures,
  and submission-ready publication exports. Use whenever Codex creates, revises, reviews,
  audits, or writes code for any plotting or map task in any local project.
  Enforce the user's house style first: English figure text by default,
  text/no-text version gate, Arial-based SCI style, user color systems,
  map color ramps, data-cleaning transparency, and output QA.
---

# Scientific Figure Standards

Use this skill for every local project when the task involves drawing, plotting, mapping, figure code, chart review, publication-ready exports, or visual standards. Treat these rules as hard defaults, not suggestions.

## First Gate

Before writing or editing plotting code, establish:

1. Output version: ask whether the user wants `with_text`, `no_text`, or both, unless already stated.
2. Figure purpose: exploratory, manuscript, presentation, supplement, or submission.
3. Figure logic: for formal scientific figures, identify the one-sentence claim or the role of the plot.
4. Data and transformations: identify units, missing values, nodata, negative values, normalization, log transforms, clipping, and uncertainty/statistics.
5. Submission output formats: default to PNG 300 dpi, TIFF 300 dpi, and PDF unless the user specifies otherwise.

Default no-text version: keep every text object and its layout reservation, but make text invisible/transparent. Do not delete labels, tick labels, legend text, colorbar labels, annotations, or map graticule labels if deleting them would change spacing. Retain axes/spines, tick marks, colorbar shape, legend swatches/symbols, and graphical structure unless the user requests a more minimal version.

## Load References

- Read `references/visual-standards.md` for any scientific plot or manuscript figure.
- Read `references/submission-standards.md` for final manuscript, journal, thesis, or publication-ready figures.
- Read `references/map-standards.md` for maps, GeoTIFF, raster, gridded, CRS, or Cartopy work.
- Read `references/data-standards.md` when plotting data that needs unit conversion, missing-value handling, model metrics, statistics, or raster preprocessing.
- Read `references/current-project-style.md` when reproducing the user's established local style or extracting constants from the source project.
- Read `references/template-guide.md` when a requested figure resembles an existing house-style pattern.

Use `templates/` first for exact house-style replication, then `scripts/figure_style.py` and `scripts/map_style.py` as lower-level implementation assets. Copy or import them as appropriate for the project.

## Non-Negotiable Defaults

- Use English figure text by default.
- Use Arial first, with Helvetica and DejaVu Sans fallbacks.
- Use a white background.
- Preserve the user's clean SCI style: restrained colors, clear hierarchy, no decorative effects.
- Use complete axes/spines by default for ordinary scientific plots. Do not adopt frameless Nature-style axes unless explicitly requested or required by a target journal.
- Do not use random colors, rainbow colormaps, default matplotlib colors, or over-saturated palettes when a user palette applies.
- For submission figures, export PNG at 300 dpi, TIFF at 300 dpi, and PDF by default.
- Do not generate SVG by default. Add SVG only when explicitly requested or required by the target journal.
- Use `bbox_inches="tight"` and `facecolor="white"` for saved figures.
- Set `svg.fonttype = "none"` and `pdf.fonttype = 42` before vector export.
- Close figures after saving in scripts that generate batches.

## Template-First Replication

When the task resembles an existing template, start from the template rather than re-creating style from prose:

- `templates/scatter_regression.py` for observed-vs-predicted train/test plots.
- `templates/scenario_bar.py` for scenario reduction-efficiency bars.
- `templates/cumulative_distribution.py` for ranked cumulative contribution curves.
- `templates/broken_axis_bar.py` for skewed bar charts requiring a visible broken axis.
- `templates/shap_swarm.py` for SHAP swarm plus mean absolute SHAP bars.
- `templates/global_raster_map.py` for global GeoTIFF/raster maps.

Only write a new plot from scratch when no template fits. If a new figure type will recur, add a new template.

## Version Rules

`with_text`:
- Keep axis labels, units, tick labels, legends, colorbar labels, panel labels, and necessary annotations.
- Avoid large in-plot titles for manuscript figures unless the user asks; captions usually carry the title.

`no_text`:
- Make axis labels, tick labels, titles, legend text, colorbar labels, panel labels, and annotation text invisible/transparent while preserving their original layout positions.
- Keep axis lines, tick marks, legend swatches/symbols, colorbar body/outline, and core graphical marks.
- Generate the same text objects as `with_text` first, then hide them. Do not skip label creation in the no-text branch.
- Generate no-text outputs from code, not by screenshot cropping.

When both versions are requested, save separate files with `_with_text` and `_no_text` suffixes.

## Scientific Logic Rules

For formal research figures, borrow the rigor of a submission workflow while preserving the user's style:

- Start from the figure's claim or role, not a favorite chart template.
- In multi-panel figures, every panel must answer a unique scientific question.
- Use panel labels `a`, `b`, `c`, ... without parentheses for multi-panel submission figures.
- Keep figure typography from the user's current code/templates by default; do not automatically shrink fonts to generic journal small-font sizes.
- Avoid large in-plot titles for submission figures; captions or manuscript text should carry titles and long explanations.
- Give primary evidence the clearest visual position; make controls and robustness panels visually quieter.
- Keep method/category colors consistent across all panels and all related figures.
- Document or encode `n`, error bars, uncertainty, metric definitions, train/validation/test split, seeds/folds, or statistical tests when they are part of the claim.
- Use direct labels or shared legends when repeated legends waste space.

## Map Rules

- World maps default to Robinson projection with longitude/latitude data drawn through PlateCarree.
- World maps must show graticule labels on the left edge and bottom edge in `with_text` outputs.
- World-map longitude ticks default to `[-90, 0, 90]`; latitude ticks default to `[90, 60, 30, 0, -30, -60, -90]`.
- Use concise graticule styling from the user's code: gray dashed gridlines, linewidth about 0.5, alpha about 0.5, labels not rotated, label size about 10.
- In `no_text` world maps, still create the same left/bottom graticule labels and make them transparent; never disable `draw_labels` just because the version is no-text.
- Regional maps inherit the concise left/bottom graticule style when graticules are needed, but choose sparse ticks from the regional extent instead of using world-map tick values.
- Regional maps do not default to Robinson. Respect the data CRS and task; common lon/lat regional plots use EPSG:4326 / PlateCarree.
- Use the user's global map ramp for emission, variation, risk, rate, or intensity rasters unless the variable semantics require another palette.
- First version does not define north arrow or scale bar standards. Treat those as future extensions and ask the user if needed.

## QA Before Final

Before claiming a figure is complete, verify:

- Requested version(s) were generated.
- Text language, font, size, and units are correct.
- No Chinese mojibake or accidental default font appears in figure text.
- Palette matches the user's standards or the deviation is justified.
- Axes, spines, ticks, labels, legends, colorbars, and annotations do not overlap data.
- Raster/map preprocessing handles nodata, NaN, inf, negative values, units, and transforms explicitly.
- DPI and output formats match the purpose.
- Submission outputs include PNG 300 dpi, TIFF 300 dpi, and PDF unless the user requested a different set.
