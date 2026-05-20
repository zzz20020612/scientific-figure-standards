# Scientific Figure Standards for Claude Code

This repository can be used as a Claude Code skill by installing the whole folder under `~/.claude/skills/scientific-figure-standards` or `.claude/skills/scientific-figure-standards` in a project.

If Claude Code loads this file as project instructions instead of as a skill, follow the same standards in `SKILL.md`.

Core behavior:

- For any plotting, map, GeoTIFF/raster, model-result chart, manuscript figure, or publication-export task, use the standards in `SKILL.md`.
- Ask whether output should be `with_text`, `no_text`, or both unless already specified.
- For house-style replication, start from `references/template-guide.md` and the nearest file in `templates/`.
- Read `references/visual-standards.md`, `references/map-standards.md`, and `references/data-standards.md` when relevant.
- Prefer the helper scripts in `scripts/figure_style.py` and `scripts/map_style.py` for Python plotting work.
- Preserve the user's house style first; only switch to strict journal/Nature-style variants when explicitly requested.
