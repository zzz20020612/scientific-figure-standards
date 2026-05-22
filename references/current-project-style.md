# Current Project Style

This reference summarizes an anonymized source-project style snapshot from prior environmental modeling, raster processing, and manuscript-figure work. Use it as the house-style evidence base, not as a closed list of supported plot types.

## Source Areas Studied

The style snapshot was extracted from representative scripts covering:

- ERA5-Land download and NetCDF-to-GeoTIFF conversion.
- HWSD Excel joins and raster layer exports.
- A core hierarchical pollution allocation model and its paper figures.
- Curated manuscript-figure scripts.
- Global CH4 raster map scripts.

The original source snapshot was not a Git repository, so no commit history was available.

## Core Visual Identity

- Python / matplotlib / seaborn / cartopy.
- White background.
- Arial-first typography.
- Large, readable standalone figures.
- Complete plot borders are common and should remain the default.
- Clean PNG output is common; submission outputs now default to PNG 300 dpi, TIFF 300 dpi, and PDF.
- Figure text is usually English even when source-code comments are not.
- Avoid decorative visual effects.

## Fixed Palettes

Pollutant palette:

```python
["#46788E", "#78B7C9", "#F6E093", "#E58B7B"]
```

Train/test:

```python
{"Train": "#3769b1", "Test": "#d6221b"}
```

Scenario/zone:

```python
["#3182bd", "#9ecae1", "#fd8d3c", "#3769b1"]
```

SHAP ramp:

```python
["#067FB8", "#4C93BD", "#9AC2DB", "#BCD6E5", "#FDE6DE", "#F1B4A1", "#E38C7B", "#D26872"]
```

World map ramp:

```python
["#015D55", "#52928A", "#79B0A1", "#CCD9CF", "#FFE4E1", "#FFA07A", "#FF6347", "#8B0000"]
```

## Existing Figure Patterns

Use these as samples:

- Scatter/regression: seaborn jointplot, train/test colors, marginal hist/KDE, diagonal 1:1 reference, R2/RMSE in legends.
- Scenario bars: colored scenario families, vertical x labels, value labels above bars, complete box, no grid.
- SHAP swarm: custom blue-to-red ramp, small rasterized scatter points, mean absolute SHAP bars on a top twin axis, side colorbar.
- SHAP pies: pollutant/feature color palette, separate legend export, white background.
- Cumulative pollution distributions: pollutant colors, 0-100 axes, clean legend, 300 dpi.
- Broken-axis top-5 bars: visible break marks, large labels, pollutant colors, 300 dpi.
- Per-capita deviation bars: sorted bars, reference range background, red baseline, zone colors, complete box.
- Correlation histograms: minimal labels, complete box, large tick labels, white background.

These patterns are examples. For new figure types, preserve the same house rules.

## Core Model Context

The representative model context is a hierarchical spatial allocation workflow:

- input raster features include nightlight, hotel, basestation, and building variables;
- raster outputs are aggregated to township via `scatter_add_`;
- township outputs are mapped to wastewater plants via a township-to-plant matrix;
- pollution variables are WW/water, COD, TN, and TP;
- training uses MSE plus a native-pollution constraint;
- outputs include CSV comparisons and GeoTIFF predictions.

When plotting comparable model results, be explicit about whether values are normalized fractions, absolute loads, or rescaled raster predictions.

## Encoding Caution

Legacy source files can display mojibake in comments/strings depending on terminal decoding. Preserve original source encodings when editing legacy files and avoid introducing mojibake into figure text.
