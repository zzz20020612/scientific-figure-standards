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

Install by cloning this repository into your Codex skills directory. On Windows PowerShell:

```powershell
New-Item -ItemType Directory -Force -Path "$env:USERPROFILE\.codex\skills" | Out-Null
git clone https://github.com/zzz20020612/scientific-figure-standards.git "$env:USERPROFILE\.codex\skills\scientific-figure-standards"
```

If the target folder already exists, update it instead:

```powershell
cd "$env:USERPROFILE\.codex\skills\scientific-figure-standards"
git pull
```

On macOS/Linux:

```bash
mkdir -p ~/.codex/skills
git clone https://github.com/zzz20020612/scientific-figure-standards.git ~/.codex/skills/scientific-figure-standards
```

If your Codex installation uses a custom `CODEX_HOME`, install under `$CODEX_HOME/skills/scientific-figure-standards` instead of `~/.codex/skills/scientific-figure-standards`.

After installation, restart Codex or start a new session so the skill metadata can be discovered.

## First-Version Note

This first version intentionally does not define north-arrow or scale-bar standards. Those are reserved for a later update.
