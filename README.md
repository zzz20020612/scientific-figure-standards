# Scientific Figure Standards

A portable AI-agent skill/instruction pack for enforcing consistent scientific plotting and map standards across local projects.

This repository works in three modes:

- **Codex Skill**: install under `~/.codex/skills/scientific-figure-standards`.
- **Claude Code Skill**: install under `~/.claude/skills/scientific-figure-standards` or a project `.claude/skills/scientific-figure-standards` folder.
- **OpenCode / AGENTS.md instruction pack**: copy or merge `AGENTS.md` into the target project's instruction file.

The standards preserve a consistent house style for manuscript figures, scientific plots, model-result visualizations, GeoTIFF/raster maps, and publication-ready exports. The examples are not a closed list of supported chart types.

## Version and License

Current version: `0.3.0`

License: MIT. You may freely use, copy, modify, distribute, and adapt this project.

## What It Enforces

- Ask whether each output should be `with_text`, `no_text`, or both before plotting.
- Treat `no_text` as transparent text placeholders that preserve layout, not as deleted labels.
- Use English figure text by default.
- Use an Arial-first, white-background, high-DPI scientific style.
- Preserve complete axes/spines by default for ordinary scientific plots.
- Use fixed house palettes for pollutants, train/test splits, scenarios, SHAP values, and global maps.
- Apply explicit data handling for nodata, NaN, inf, negative values, unit conversion, log transforms, clipping, and normalization.
- Use Robinson projection by default for world maps, while respecting CRS for regional maps.
- Require concise left-edge latitude and bottom-edge longitude labels on world maps.
- Add SVG/PDF editable-text export rules for formal scientific figures.
- Use template files first when a requested figure matches an existing house-style pattern.
- Run final QA for fonts, units, palettes, overlap, version correctness, and output quality.

## Template-First Replication

For exact house-style replication, start from the nearest template:

- `templates/scatter_regression.py`
- `templates/scenario_bar.py`
- `templates/cumulative_distribution.py`
- `templates/broken_axis_bar.py`
- `templates/shap_swarm.py`
- `templates/global_raster_map.py`

Use prose standards only when no template matches.

## Repository Structure

```text
scientific-figure-standards/
├── SKILL.md
├── AGENTS.md
├── CLAUDE.md
├── CHANGELOG.md
├── LICENSE
├── VERSION
├── agents/
├── references/
├── scripts/
└── templates/
```

## Install for Codex

Replace `<repo-url>` with this repository's clone URL.

```bash
mkdir -p ~/.codex/skills
git clone <repo-url> ~/.codex/skills/scientific-figure-standards
```

On Windows PowerShell:

```powershell
New-Item -ItemType Directory -Force -Path "$env:USERPROFILE\.codex\skills" | Out-Null
git clone <repo-url> "$env:USERPROFILE\.codex\skills\scientific-figure-standards"
```

## Install for Claude Code

```bash
mkdir -p ~/.claude/skills
git clone <repo-url> ~/.claude/skills/scientific-figure-standards
```

Or install it only for one project:

```bash
mkdir -p .claude/skills
git clone <repo-url> .claude/skills/scientific-figure-standards
```

## Use with OpenCode

Copy or merge this repository's `AGENTS.md` into the target project's `AGENTS.md`.

## First-Version Note

This project still intentionally leaves north-arrow and scale-bar standards for a later update.
