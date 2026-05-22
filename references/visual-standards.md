# Visual Standards

Use these standards for all scientific figures unless the user explicitly overrides them.

For exact house-style replication, start from `references/template-guide.md` and the nearest file in `templates/` before applying these prose rules.

For final manuscript, journal, thesis, or publication-ready figures, also read `references/submission-standards.md`.

## Figure Contract

For formal scientific outputs, establish a compact contract before plotting:

```text
Purpose:
Core conclusion or figure role:
Output version: with_text / no_text / both
Final use: manuscript / presentation / supplement / submission
Data transformations:
Statistics or model metrics:
Output formats:
```

Do not force this into a long user-facing form when the task is simple. Infer what is obvious and ask only the missing blocker.

## Typography

- Default text language: English.
- Default font stack: Arial, Helvetica, DejaVu Sans.
- Use `axes.unicode_minus = False`.
- Use mathtext for units such as `kg capita$^{-1}$`, `mol g$^{-1}$ day$^{-1}$`, and `Mean |SHAP Value|`.
- Manuscript figures normally avoid large in-plot titles. Use captions for titles.
- If the user targets a strict journal final-size figure, scale fonts to the final dimensions; otherwise preserve the user's large-readable house style.

Common house-style ranges:

| Element | Default range |
|---|---:|
| Axis labels | 20-25 pt for large standalone plots; 10-14 pt for compact panels |
| Tick labels | 20-25 pt for large standalone plots; 9-12 pt for compact panels |
| Legends | 18-25 pt for large plots; 10-14 pt for compact panels |
| Panel labels | bold `a`, `b`, `c` for submission panels; keep placement consistent |

## Axes, Spines, and Grid

- Default to white background.
- Default to complete axes/spines: top, right, bottom, and left visible.
- Typical spine linewidth: 1.0-1.2.
- Tick direction: outward when practical.
- Tick length: 4-6; tick width about 1.
- Gridlines are off by default. If needed for reading values, use light gray dashed lines with low alpha.
- Do not use seaborn's default despined look as the default house style.

## Palettes

Use fixed palettes whenever the semantic category matches.

Pollutants:

```python
POLLUTANT_COLORS = {
    "WW": "#46788E",
    "water": "#46788E",
    "COD": "#78B7C9",
    "TN": "#F6E093",
    "TP": "#E58B7B",
}
```

Train/test:

```python
DATASET_COLORS = {
    "Train": "#3769b1",
    "Test": "#d6221b",
}
```

Scenario / zone family:

```python
SCENARIO_COLORS = ["#3182bd", "#9ecae1", "#fd8d3c", "#3769b1"]
```

SHAP feature value ramp:

```python
SHAP_RAMP = [
    "#067FB8", "#4C93BD", "#9AC2DB", "#BCD6E5",
    "#FDE6DE", "#F1B4A1", "#E38C7B", "#D26872",
]
```

When a new category has no established user palette, choose a restrained semantic family. Keep related methods or groups in related hues. Reserve red/green mainly for directional gains/losses or signed effects. Never use rainbow or random colors.

## Legends and Labels

- Use legends only when they reduce ambiguity.
- Prefer shared legends or standalone legend exports for multi-panel figures.
- Keep legends away from dense data.
- Legend frames may be white/light gray with thin edges in the user's house style; frameless legends are optional for strict journal style.
- For no-text versions, keep legend text, axis labels, tick labels, colorbar labels, panel labels, and annotations as layout placeholders but make the text invisible/transparent.
- Always create the same text-bearing objects in `no_text` as in `with_text` before hiding text. Do not skip label, legend, or colorbar creation in the no-text branch.
- Avoid clearing strings, removing tick locations, turning off tick labels, or deleting text artists when the user may need the original text positions for later manual composition.

## Figure Types Are Not a Boundary

Existing local examples include scatter/regression, SHAP, bars, broken axes, cumulative distributions, histograms, and per-capita deviation plots. These are examples only. For any new plot type, preserve the same typography, palette discipline, clean borders, output quality, and data-transformation transparency.

## Scientific Rigor

- Scatter/model comparison figures should include reference lines or regression lines when they clarify the claim.
- Model figures should define metrics such as R2/RMSE/NSE and distinguish train/test/validation consistently.
- Bars with uncertainty must define the error bar meaning.
- Distribution plots must define binning, KDE, clipping, log transforms, and thresholds when used.
- Broken axes must include visible break marks; never hide a truncation.
- Multi-panel figures must avoid redundant panels. If a panel only repeats another panel in a different chart type, remove or replace it with a relationship, deviation, or robustness view.

## Exports

- Submission default: PNG at 300 dpi, TIFF at 300 dpi, and PDF.
- Do not generate SVG by default. Add SVG only when explicitly requested or required by the target journal.
- Keep `with_text` and `no_text` output formats identical when both versions are requested.
- Always set:

```python
mpl.rcParams["svg.fonttype"] = "none"
mpl.rcParams["pdf.fonttype"] = 42
```

- Save with `bbox_inches="tight"` and `facecolor="white"`.
- Close batch figures with `plt.close(fig)`.

## Final QA

Check before delivery:

- Correct requested version: with_text, no_text, or both.
- No visible text remains in no-text outputs, while original text positions and spacing are preserved.
- No visible mojibake, accidental Chinese labels, or fallback CJK font unless requested.
- Units match data transformations.
- Colors match the semantic palette.
- Text, legend, markers, and colorbars do not overlap.
- Raster output is not blurry at intended size.
- PNG/TIFF/PDF outputs are present for submission figures unless the user requested a different format set.
