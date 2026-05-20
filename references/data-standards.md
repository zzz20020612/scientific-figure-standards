# Data and Model Standards

Use this reference when the figure depends on preprocessing, units, statistics, model outputs, or raster transformations.

## General Data Transparency

Every plotted transformation must be explicit in code:

- unit conversion
- normalization
- log transform
- percentile stretch
- clipping
- filtering thresholds
- NaN/nodata/inf handling
- negative-value handling
- aggregation level

Do not only change axis labels to imply a transformation.

## Raster and GeoTIFF Data

For raster figures and maps:

1. Read data with rasterio or another geospatial reader that preserves bounds, CRS, transform, and nodata.
2. Create a clean data array:

```python
clean = np.where((data == nodata) | np.isnan(data) | np.isinf(data), np.nan, data)
```

3. For nonnegative environmental variables, mask or clip negative values deliberately:

```python
clean = np.where(clean < 0, np.nan, clean)
```

4. Preserve geospatial metadata on output GeoTIFFs.
5. Use LZW compression when writing GeoTIFF unless there is a reason not to.

## Pollution Variable Naming

Use stable labels:

- `WW`
- `COD`
- `TN`
- `TP`

If source code uses `water`, map it visually to `WW` when presenting figures.

## Model Figures

When plotting model results:

- distinguish train, validation, and test sets clearly;
- use the fixed train/test colors from the visual standards;
- report metric definitions when shown in the figure;
- include R2/RMSE/NSE or other metrics only if computed from the correct split;
- do not mix normalized fractions and absolute loads without explicit labels;
- keep seed/fold/split information available for formal outputs.

Minimum model metadata for formal figures:

```text
train/validation/test split:
number of seeds or folds:
metric definition:
confidence interval or variability definition:
baseline definition:
source data:
```

## Statistics

For quantitative scientific panels, capture or infer:

```text
n definition:
biological or spatial replicates:
technical replicates:
center statistic:
spread or interval:
test:
multiple-comparison correction:
p-value display:
source data:
```

Do not add significance marks unless the test and comparison are known.

## Output Naming

Filenames should encode what matters:

```text
<variable>_<year-or-scenario>_<plot-or-map-type>_<with_text|no_text>.<ext>
```

For batch outputs, keep names sortable and stable.
