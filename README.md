# Scientific Figure Standards

A global Codex skill for enforcing consistent scientific plotting and map standards across local projects.

This skill captures a house style for manuscript figures, scientific plots, model-result visualizations, GeoTIFF/raster maps, and publication-ready exports. It is designed to preserve a consistent visual language rather than only providing examples for a few chart types.

## What It Enforces

- Ask whether each output should be `with_text`, `no_text`, or both before plotting.
- Use English figure text by default.
- Use an Arial-first, white-background, high-DPI scientific style.
- Preserve complete axes/spines by default for ordinary scientific plots.
- Use fixed house palettes for pollutants, train/test splits, scenarios, SHAP values, and global maps.
- Apply explicit data handling for nodata, NaN, inf, negative values, unit conversion, log transforms, clipping, and normalization.
- Use Robinson projection by default for world maps, while respecting CRS for regional maps.
- Add SVG/PDF editable-text export rules for formal scientific figures.
- Run final QA for fonts, units, palettes, overlap, version correctness, and output quality.

## Skill Structure

```text
scientific-figure-standards/
├── SKILL.md
├── agents/
│   └── openai.yaml
├── references/
│   ├── current-project-style.md
│   ├── data-standards.md
│   ├── map-standards.md
│   └── visual-standards.md
└── scripts/
    ├── figure_style.py
    └── map_style.py
```

## References

- `references/visual-standards.md`: scientific figure typography, palettes, axes, legends, exports, and QA.
- `references/map-standards.md`: world/regional map rules, GeoTIFF handling, projections, colorbars, and map color ramps.
- `references/data-standards.md`: data cleaning, unit conversion, model metrics, statistics, and naming standards.
- `references/current-project-style.md`: style extracted from the source local project and used as house-style evidence.

## Helper Scripts

- `scripts/figure_style.py`: reusable Matplotlib style helpers, color constants, no-text stripping, and save helpers.
- `scripts/map_style.py`: reusable map color ramps, raster cleaning, lon/lat mesh helpers, colorbar text removal, and map saving.

## Installation

Place this folder under your Codex skills directory:

```text
C:\Users\86188\.codex\skills\scientific-figure-standards
```

Codex can then discover and use the skill whenever a task involves scientific plotting, map drawing, raster visualization, manuscript figures, or publication exports.

## First-Version Note

This first version intentionally does not define north-arrow or scale-bar standards. Those are reserved for a later update.
