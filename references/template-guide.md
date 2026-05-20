# Template Guide

Use templates when the user asks for a figure that resembles the established house style. Templates are the preferred starting point for replication; prose standards are the fallback for new chart types.

## Available Templates

| Template | Use when | House-style anchors |
|---|---|---|
| `templates/scatter_regression.py` | Train/test model comparison or observed-vs-predicted plots | jointplot, train/test colors, marginal hist/KDE, 1:1 line, R2/RMSE legends, 600 dpi |
| `templates/scenario_bar.py` | Scenario or grouped reduction-efficiency bars | 9x6 figure, blue/orange scenario family, complete border, vertical x labels, value labels |
| `templates/cumulative_distribution.py` | Ranked cumulative contribution/distribution curves | 8x7 figure, pollutant palette, 0-100 axes, lower-right legend |
| `templates/broken_axis_bar.py` | Top-contribution or heavily skewed bar charts | 8x8 broken axis, visible break marks, pollutant palette |
| `templates/shap_swarm.py` | SHAP beeswarm-style feature effect figure | blue-red SHAP ramp, rasterized small points, mean absolute SHAP twin-axis bars |
| `templates/global_raster_map.py` | Global GeoTIFF/raster maps | Robinson projection, PlateCarree data transform, coastlines, gridlines, horizontal colorbar, global map ramp |

## How to Use

1. Pick the closest template.
2. Copy it into the target project or import it from the cloned skill directory.
3. Adapt only data loading, labels, units, and variable-specific limits.
4. Preserve the template's style constants unless the user explicitly requests a deviation.
5. Generate requested `with_text`, `no_text`, or both versions.

## New Figure Types

When no template matches:

- Follow `references/visual-standards.md`.
- Reuse constants from `scripts/figure_style.py`.
- Match the closest existing template's typography, legend, save, and version-handling logic.
- If the new figure type will recur, add a new template instead of writing one-off code repeatedly.

## Replication Priority

For exact house-style replication, prefer this order:

1. Existing template.
2. Helper scripts plus visual/map/data references.
3. Prose-only standards.
