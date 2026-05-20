---
name: scientific-figure-standards
description: >-
  Global hard standards for the user's scientific figures, manuscript plots,
  maps, GeoTIFF/raster visualizations, model-result charts, SHAP/ML figures,
  and publication exports. Use whenever Codex creates, revises, reviews,
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
5. Output formats: default to PNG; add SVG for formal scientific figures; add PDF/TIFF for submission-style outputs.

Default no-text version: remove all visible text, but retain axes/spines, tick marks, colorbar shape, legend swatches/symbols, and graphical structure unless the user requests a more minimal version.

## Load References

- Read `references/visual-standards.md` for any scientific plot or manuscript figure.
- Read `references/map-standards.md` for maps, GeoTIFF, raster, gridded, CRS, or Cartopy work.
- Read `references/data-standards.md` when plotting data that needs unit conversion, missing-value handling, model metrics, statistics, or raster preprocessing.
- Read `references/current-project-style.md` when reproducing the user's established local style or extracting constants from the source project.

Use `scripts/figure_style.py` and `scripts/map_style.py` as implementation assets when writing Python plotting code. Copy or import them as appropriate for the project.

## Non-Negotiable Defaults

- Use English figure text by default.
- Use Arial first, with Helvetica and DejaVu Sans fallbacks.
- Use a white background.
- Preserve the user's clean SCI style: restrained colors, clear hierarchy, no decorative effects.
- Use complete axes/spines by default for ordinary scientific plots. Do not adopt frameless Nature-style axes unless explicitly requested or required by a target journal.
- Do not use random colors, rainbow colormaps, default matplotlib colors, or over-saturated palettes when a user palette applies.
- Save raster outputs at 300 dpi minimum; use 600 dpi for final figures, maps, dense panels, or submission-like outputs.
- Use `bbox_inches="tight"` and `facecolor="white"` for saved figures.
- Set `svg.fonttype = "none"` and `pdf.fonttype = 42` before vector export.
- Close figures after saving in scripts that generate batches.

## Version Rules

`with_text`:
- Keep axis labels, units, tick labels, legends, colorbar labels, panel labels, and necessary annotations.
- Avoid large in-plot titles for manuscript figures unless the user asks; captions usually carry the title.

`no_text`:
- Remove axis labels, tick labels, titles, legend text, colorbar labels, and annotation text.
- Keep axis lines, tick marks, legend swatches/symbols, colorbar body/outline, and core graphical marks.
- Generate no-text outputs from code, not by screenshot cropping.

When both versions are requested, save separate files with `_with_text` and `_no_text` suffixes.

## Scientific Logic Rules

For formal research figures, borrow the rigor of a submission workflow while preserving the user's style:

- Start from the figure's claim or role, not a favorite chart template.
- In multi-panel figures, every panel must answer a unique scientific question.
- Give primary evidence the clearest visual position; make controls and robustness panels visually quieter.
- Keep method/category colors consistent across all panels and all related figures.
- Document or encode `n`, error bars, uncertainty, metric definitions, train/validation/test split, seeds/folds, or statistical tests when they are part of the claim.
- Use direct labels or shared legends when repeated legends waste space.

## Map Rules

- World maps default to Robinson projection with longitude/latitude data drawn through PlateCarree.
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
- SVG/PDF text remains editable when vector output is required.
