# Scientific Figure Standards

A portable AI-agent skill/instruction pack for enforcing consistent scientific plotting and map standards across local projects.

This repository works in three modes:

- **Codex Skill**: install under `~/.codex/skills/scientific-figure-standards`.
- **Claude Code Skill**: install under `~/.claude/skills/scientific-figure-standards` or a project `.claude/skills/scientific-figure-standards` folder.
- **OpenCode / AGENTS.md instruction pack**: copy or merge `AGENTS.md` into the target project's instruction file.

The standards preserve a consistent house style for manuscript figures, scientific plots, model-result visualizations, GeoTIFF/raster maps, and publication-ready exports. The examples are not a closed list of supported chart types.

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

## Repository Structure

```text
scientific-figure-standards/
├── SKILL.md                 # Codex / Claude Code skill entrypoint
├── AGENTS.md                # OpenCode / agent instruction entrypoint
├── CLAUDE.md                # Claude Code project-instruction fallback
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

## Install for Codex

Replace `<repo-url>` with this repository's clone URL.

Windows PowerShell:

```powershell
New-Item -ItemType Directory -Force -Path "$env:USERPROFILE\.codex\skills" | Out-Null
git clone <repo-url> "$env:USERPROFILE\.codex\skills\scientific-figure-standards"
```

Update an existing install:

```powershell
cd "$env:USERPROFILE\.codex\skills\scientific-figure-standards"
git pull
```

macOS/Linux:

```bash
mkdir -p ~/.codex/skills
git clone <repo-url> ~/.codex/skills/scientific-figure-standards
```

If your Codex installation uses a custom `CODEX_HOME`, install under `$CODEX_HOME/skills/scientific-figure-standards` instead.

## Install for Claude Code

Claude Code skills are filesystem-based. Install this repository as a user skill:

```bash
mkdir -p ~/.claude/skills
git clone <repo-url> ~/.claude/skills/scientific-figure-standards
```

Or install it only for one project:

```bash
mkdir -p .claude/skills
git clone <repo-url> .claude/skills/scientific-figure-standards
```

Restart Claude Code or start a new session after installing a new top-level skill directory.

## Use with OpenCode

OpenCode reads `AGENTS.md` instructions from a project. To apply these standards to a project, copy or merge this repository's `AGENTS.md` into that project's `AGENTS.md`:

```bash
cp path/to/scientific-figure-standards/AGENTS.md /path/to/your-project/AGENTS.md
```

If the project already has an `AGENTS.md`, merge the plotting section instead of replacing existing project rules.

For a reusable local setup, keep this repository cloned somewhere stable and copy the `AGENTS.md` content into any project where OpenCode should enforce these figure standards.

## References

- `references/visual-standards.md`: scientific figure typography, palettes, axes, legends, exports, and QA.
- `references/map-standards.md`: world/regional map rules, GeoTIFF handling, projections, colorbars, and map color ramps.
- `references/data-standards.md`: data cleaning, unit conversion, model metrics, statistics, and naming standards.
- `references/current-project-style.md`: anonymized house-style examples extracted from prior scientific plotting work.

## Helper Scripts

- `scripts/figure_style.py`: reusable Matplotlib style helpers, color constants, no-text stripping, and save helpers.
- `scripts/map_style.py`: reusable map color ramps, raster cleaning, lon/lat mesh helpers, colorbar text removal, and map saving.

## First-Version Note

This first version intentionally does not define north-arrow or scale-bar standards. Those are reserved for a later update.
