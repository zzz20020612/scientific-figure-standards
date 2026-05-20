# Current Project Style

This reference summarizes style extracted from `D:\代码合集` as of 2026-05-20. Use it as the house-style evidence base, not as a closed list of supported plot types.

## Project Areas Studied

- `ERA5数据下载`: ERA5-Land download and NetCDF to GeoTIFF conversion.
- `HWSD数据下载`: HWSD Excel joins and raster layer exports.
- `论文模型及绘图`: core hierarchical pollution allocation model and paper plots.
- `绘图代码\论文插图`: duplicated/curated paper-figure scripts.
- `绘图代码\地图`: global CH4 raster map scripts.

The source folder is not a Git repository, so no commit history was available.

## Core Visual Identity

- Python / matplotlib / seaborn / cartopy.
- White background.
- Arial-first typography.
- Large, readable standalone figures.
- Complete plot borders are common and should remain the default.
- Clean high-DPI PNG output is common; formal outputs should now add SVG.
- Figure text is usually English even when code comments are Chinese.
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

- Scatter/regression: seaborn jointplot, train/test colors, marginal hist/KDE, diagonal 1:1 reference, R2/RMSE in legends, 600 dpi.
- Scenario bars: colored scenario families, vertical x labels, value labels above bars, complete box, no grid, 600 dpi.
- SHAP swarm: custom blue-to-red ramp, small rasterized scatter points, mean absolute SHAP bars on a top twin axis, side colorbar.
- SHAP pies: pollutant/feature color palette, separate legend export, white background.
- Cumulative pollution distributions: pollutant colors, 0-100 axes, clean legend, 300 dpi.
- Broken-axis top-5 bars: visible break marks, large labels, pollutant colors, 300 dpi.
- Per-capita deviation bars: sorted bars, reference range background, red baseline, zone colors, complete box.
- Correlation histograms: minimal labels, complete box, large tick labels, white background.

These patterns are examples. For new figure types, preserve the same house rules.

## Core Model Context

The core model is a hierarchical spatial allocation workflow:

- input raster features include nightlight, hotel, basestation, and building variables;
- raster outputs are aggregated to township via `scatter_add_`;
- township outputs are mapped to wastewater plants via a township-to-plant matrix;
- pollution variables are WW/water, COD, TN, and TP;
- training uses MSE plus a native-pollution constraint;
- outputs include CSV comparisons and GeoTIFF predictions.

When plotting model results, be explicit about whether values are normalized fractions, absolute loads, or rescaled raster predictions.

## Encoding Caution

Some source files display mojibake in comments/strings depending on terminal decoding. Preserve original source encodings when editing legacy files and avoid introducing new mojibake into figure text.
