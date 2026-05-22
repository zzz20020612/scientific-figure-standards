# Submission Standards

Use this reference for final manuscript, journal, thesis, or publication-ready figures. These are submission-grade defaults, not exploratory plotting rules.

## Priority

For every submission figure:

1. Preserve the user's existing code/template style for typography, palettes, map appearance, legends, colorbars, and layout.
2. Enforce submission quality for outputs, data handling, no-text placeholders, CRS correctness, units, and reproducibility from code.
3. If existing code conflicts with scientific correctness or submission quality, fix the risk while preserving the visual style as much as possible.

Do not redesign a figure just to match a generic journal aesthetic. The user's style remains the visual source of truth.

## Required First Gate

Before creating or editing a submission figure, ask for the output version unless already specified:

- `with_text`
- `no_text`
- `both`

For `no_text`, keep text objects and layout positions, then make text transparent. Do not delete labels, ticks, colorbar text, legend text, annotations, panel labels, or map graticule labels.

## Figure Size

Use journal-common final widths unless the target journal gives exact requirements:

- Single column: about 85 mm wide.
- 1.5 columns: about 120-140 mm wide.
- Double column: about 170-180 mm wide.
- Full page: keep height under about 220-240 mm.

Use millimeter-to-inch conversion in code when final physical size matters:

```python
def mm_to_inch(mm):
    return mm / 25.4
```

Do not use these dimensions as an excuse to shrink the user's typography automatically.

## Typography

- Keep font sizes from the user's current code/templates by default.
- Do not automatically convert figures to tiny journal-style fonts such as 7-8 pt.
- Only change font sizes when the user explicitly asks for a target journal's final-size layout or when overlap/cropping makes the figure unusable.
- Use English figure text by default.
- Avoid large in-plot titles for submission figures. Put titles, interpretation, and long explanations in the caption or manuscript text.

## Outputs

Default submission output formats:

- PNG at 300 dpi.
- TIFF at 300 dpi.
- PDF as a faithful submission/archive version.

Do not generate SVG by default. Add SVG only when the user explicitly asks for editable vector output or the target journal requires it.

For `both`, generate the same format set for `with_text` and `no_text`. The two versions must preserve the same canvas size, bounding box behavior, panel positions, map extent, colorbar placement, and graphical structure.

## No Extra Metadata Files

Do not create sidecar metadata, notes, or JSON files by default.

Keep scientific traceability in code and summarize important transformations or caveats in the final response when needed. Do not put long method descriptions into the figure itself.

## Panel Labels

For multi-panel submission figures:

- Use `a`, `b`, `c`, ... without parentheses.
- Place labels consistently near the upper-left of each panel unless the panel geometry makes another nearby placement cleaner.
- Use bold labels.
- Keep label size consistent with the user's current style.
- In `no_text`, keep panel labels as transparent placeholders.
- Prefer shared legends or shared colorbars when that matches the existing style and reduces repetition.

## Scientific Content Without Visual Clutter

Submission standards require scientific correctness, but not visual over-explanation.

- Keep statistical definitions, CRS choices, nodata handling, and transformations in code and final notes, not as long in-figure text.
- Put only necessary reader-facing elements in the figure: axis labels, units, concise legends, colorbar labels, panel labels, and essential annotations.
- Preserve the user's existing legend and colorbar style unless it obscures data, creates ambiguity, or breaks submission readability.

## Data and Statistical QA

Before exporting:

- Confirm units match plotted transformations.
- Confirm log, normalization, clipping, percentile stretching, aggregation, or standardization are explicit in code.
- Confirm model metrics and train/test/validation splits are correctly computed when shown.
- Confirm error bars have a known meaning when shown.
- Confirm broken axes are visibly marked.
- Confirm color semantics match the variable type.

These checks do not require adding extra text to the figure.

## Map QA

For submission maps:

- Follow the user's existing map code for style, including coastline, boundaries, colorbar, graticules, and palette.
- World maps default to Robinson; lon/lat raster data uses `PlateCarree()` as the data transform.
- Regional lon/lat maps default to EPSG:4326 / PlateCarree unless a better display projection is required.
- Area, distance, buffer, and density calculations must not be performed directly in EPSG:4326. Use a suitable projected CRS for calculations.
- Read nodata from source rasters and mask nodata, NaN, and inf before plotting.
- Do not map nodata, NaN, inf, or non-study areas as valid low values.
- Follow the source project's handling for negative values, log transforms, clipping, and percentile stretching, then correct any submission-risk behavior.

World-map graticules remain a hard standard:

- Bottom longitude labels: `xlocs=[-90, 0, 90]`.
- Left latitude labels: `ylocs=[90, 60, 30, 0, -30, -60, -90]`.
- No top/right labels by default.
- Unrotated labels, size about 10 in the user's current map style.
- `no_text` keeps these labels as transparent placeholders.
