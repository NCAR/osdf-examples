---
title: Notebook Gallery
author: OSDF-Examples contributors
date: 2026-05-05
---

# Notebook Gallery

Browse all notebooks in this collection, grouped by **data origin** (the OSDF
origin a notebook streams from). Each entry shows a short description and the
key tags so you can spot relevant ones at a glance.

For the tag taxonomy and conventions, see [CONTRIBUTING.md](../CONTRIBUTING.md#tag-taxonomy).
For background on OSDF and PelicanFS, see Project Pythia's
[OSDF Cookbook](https://projectpythia.org/osdf-cookbook/).

> **Note on `platform:` tags.** Most notebooks default to a Dask
> `LocalCluster` (with PBS/Slurm options for HPC users), so they should run
> on a laptop with no changes other than a cluster-switch toggle. The
> `platform:` tag documents where the notebook was *verified*, not the only
> place it can run.

## Find a notebook

- **Have NCAR HPC access (Casper/Derecho)?** → Check the [GDEX / NCAR Data Origin](#gdex--ncar-data-origin) section — these stream from NCAR's GDEX origin.
- **Want to run on your laptop or in the cloud?** → Look for <span class="tag tag-platform">platform:laptop</span> or <span class="tag tag-platform">platform:jetstream2</span> notebooks under [Cross-platform / cloud](#cross-platform--cloud-examples).
- **Looking for ML examples?** → See [Machine learning](#machine-learning-workflows).
- **Comparing OSDF performance?** → See [Benchmarks](#benchmarks).

---

## GDEX / NCAR Data Origin

Notebooks that stream data from NCAR's OSDF origin — i.e. NCAR's
[Geoscience Data Exchange (GDEX)](https://gdex.ucar.edu/) — covering CESM2
LENS, ERA5, JRA-3Q, DART, CONUS404, NA-CORDEX, SAAG, HadISST, and more. All
of these run on Casper.

| Notebook | Description | Tags |
|---|---|---|
| [`cesm_bias.ipynb`](../notebooks/cesm_bias.ipynb) | Bias-correct CESM2 LENS temperatures using ERA5 | <span class="tag tag-dataset">dataset:cesm</span> <span class="tag tag-dataset">dataset:era5</span> <span class="tag tag-task">task:bias-correction</span> <span class="tag tag-platform">platform:casper</span> |
| [`cesm_gmst_ncar.ipynb`](../notebooks/cesm_gmst_ncar.ipynb) | Compute and plot CESM2 LENS GMST anomaly | <span class="tag tag-dataset">dataset:cesm</span> <span class="tag tag-task">task:visualization</span> <span class="tag tag-platform">platform:casper</span> |
| [`cesm_oceanheat.ipynb`](../notebooks/cesm_oceanheat.ipynb) | Compute surface ocean heat content from CESM2 LENS | <span class="tag tag-dataset">dataset:cesm</span> <span class="tag tag-task">task:visualization</span> <span class="tag tag-platform">platform:casper</span> |
| [`conus404.ipynb`](../notebooks/conus404.ipynb) | Diagnostic plots from CONUS404 | <span class="tag tag-dataset">dataset:conus404</span> <span class="tag tag-task">task:visualization</span> <span class="tag tag-platform">platform:casper</span> |
| [`dart-cam6.ipynb`](../notebooks/dart-cam6.ipynb) | Diagnostic plots from the DART/CAM6 reanalysis | <span class="tag tag-dataset">dataset:dart</span> <span class="tag tag-task">task:visualization</span> <span class="tag tag-platform">platform:casper</span> |
| [`jra_3q.ipynb`](../notebooks/jra_3q.ipynb) | Plots from the JRA-3Q reanalysis | <span class="tag tag-dataset">dataset:jra3q</span> <span class="tag tag-task">task:visualization</span> <span class="tag tag-platform">platform:casper</span> |
| [`eol_era5.ipynb`](../notebooks/eol_era5.ipynb) | ERA5 access via the EOL/NCAR origin | <span class="tag tag-dataset">dataset:era5</span> <span class="tag tag-platform">platform:casper</span> |
| [`era5_precip.ipynb`](../notebooks/era5_precip.ipynb) | ERA5 precipitation diagnostics | <span class="tag tag-dataset">dataset:era5</span> <span class="tag tag-task">task:visualization</span> <span class="tag tag-platform">platform:casper</span> |
| [`geocat_climatology.ipynb`](../notebooks/geocat_climatology.ipynb) | Daily-temperature climatology with `geocat-comp` | <span class="tag tag-dataset">dataset:era5</span> <span class="tag tag-task">task:climatology</span> <span class="tag tag-platform">platform:casper</span> |
| [`hadisst_elnino.ipynb`](../notebooks/hadisst_elnino.ipynb) | El Niño diagnostics from HadISST | <span class="tag tag-dataset">dataset:hadisst</span> <span class="tag tag-task">task:visualization</span> <span class="tag tag-platform">platform:casper</span> |
| [`jja_heatindex.ipynb`](../notebooks/jja_heatindex.ipynb) | JJA heat-index calculation | <span class="tag tag-task">task:visualization</span> <span class="tag tag-platform">platform:casper</span> |
| [`na_cordex.ipynb`](../notebooks/na_cordex.ipynb) | NA-CORDEX diagnostic plots | <span class="tag tag-dataset">dataset:na-cordex</span> <span class="tag tag-task">task:visualization</span> <span class="tag tag-platform">platform:casper</span> |
| [`saag.ipynb`](../notebooks/saag.ipynb) | SAAG dataset diagnostics | <span class="tag tag-task">task:visualization</span> <span class="tag tag-platform">platform:casper</span> |
| [`uxarray_test.ipynb`](../notebooks/uxarray_test.ipynb) | Unstructured-grid access via UXarray | <span class="tag tag-task">task:visualization</span> <span class="tag tag-platform">platform:casper</span> |

## AWS Open Data

Notebooks that stream from the OSDF AWS open-data origin.

| Notebook | Description | Tags |
|---|---|---|
| [`cmip6_gmst_zarr.ipynb`](../notebooks/cmip6_gmst_zarr.ipynb) | Multi-model GMST from CMIP6 zarr (~27 GCMs), compared to HadCRUT5 | <span class="tag tag-dataset">dataset:cmip6</span> <span class="tag tag-access">access:zarr</span> <span class="tag tag-task">task:visualization</span> |
| [`cmip6_ecs.ipynb`](../notebooks/cmip6_ecs.ipynb) | Equilibrium Climate Sensitivity from CMIP6 | <span class="tag tag-dataset">dataset:cmip6</span> <span class="tag tag-task">task:ecs</span> |
| [`cmip6_bias_correction.ipynb`](../notebooks/cmip6_bias_correction.ipynb) | Bias-correct CMIP6 output | <span class="tag tag-dataset">dataset:cmip6</span> <span class="tag tag-task">task:bias-correction</span> |
| [`cmip6_precipitation.ipynb`](../notebooks/cmip6_precipitation.ipynb) | CMIP6 precipitation diagnostics | <span class="tag tag-dataset">dataset:cmip6</span> <span class="tag tag-task">task:visualization</span> |
| [`hrrr_aws.ipynb`](../notebooks/hrrr_aws.ipynb) | Stream HRRR data from AWS | <span class="tag tag-dataset">dataset:hrrr</span> <span class="tag tag-origin">origin:aws</span> |
| [`simple_aws_example.ipynb`](../notebooks/simple_aws_example.ipynb) | Minimal AWS-origin example — good first notebook | <span class="tag tag-origin">origin:aws</span> <span class="tag tag-level">level:beginner</span> |

## Cross-platform / cloud examples

Notebooks demonstrating execution outside Casper.

| Notebook | Description | Tags |
|---|---|---|
| [`cesm_osdf_stampede3.ipynb`](../notebooks/cesm_osdf_stampede3.ipynb) | Bias-correction workflow on TACC Stampede3 | <span class="tag tag-platform">platform:stampede3</span> <span class="tag tag-dataset">dataset:cesm</span> <span class="tag tag-task">task:bias-correction</span> |
| [`jetstream_intro.ipynb`](../notebooks/jetstream_intro.ipynb) | Introduction to running on Jetstream2 | <span class="tag tag-platform">platform:jetstream2</span> <span class="tag tag-level">level:beginner</span> |
| [`jetstream_cesm_oceanheat.ipynb`](../notebooks/jetstream_cesm_oceanheat.ipynb) | Ocean-heat workflow on Jetstream2 | <span class="tag tag-platform">platform:jetstream2</span> <span class="tag tag-dataset">dataset:cesm</span> |
| [`jetstream_cmip6_gmst.ipynb`](../notebooks/jetstream_cmip6_gmst.ipynb) | CMIP6 GMST on Jetstream2 | <span class="tag tag-platform">platform:jetstream2</span> <span class="tag tag-dataset">dataset:cmip6</span> |

## Benchmarks

Notebooks that measure data-access throughput from various OSDF origins.

| Notebook | Description | Tags |
|---|---|---|
| [`ndc_workflows/aws_benchmark.ipynb`](../notebooks/ndc_workflows/aws_benchmark.ipynb) | Benchmark CESM2 LENS access from AWS origin | <span class="tag tag-task">task:benchmark</span> <span class="tag tag-origin">origin:aws</span> |
| [`ndc_workflows/ncar_benchmark.ipynb`](../notebooks/ndc_workflows/ncar_benchmark.ipynb) | Benchmark NCAR-origin access (DART) | <span class="tag tag-task">task:benchmark</span> <span class="tag tag-origin">origin:ncar-data-origin</span> |
| [`ndc_workflows/ncar_benchmark_simple.ipynb`](../notebooks/ndc_workflows/ncar_benchmark_simple.ipynb) | Simplified NCAR benchmark | <span class="tag tag-task">task:benchmark</span> <span class="tag tag-level">level:beginner</span> |
| [`ndc_workflows/ncar_benchmark_ap40.ipynb`](../notebooks/ndc_workflows/ncar_benchmark_ap40.ipynb) | NCAR-origin benchmark via OSPool AP40 | <span class="tag tag-task">task:benchmark</span> <span class="tag tag-platform">platform:ospool</span> |

## Machine-learning workflows

| Notebook | Description | Tags |
|---|---|---|
| [`ml_workflows/nino3.4_index.ipynb`](../notebooks/ml_workflows/nino3.4_index.ipynb) | Logistic-regression Niño 3.4 prediction from SST | <span class="tag tag-task">task:ml</span> <span class="tag tag-dataset">dataset:hadisst</span> |

## NDC pathfinder workflows

Notebooks developed under the [National Discovery Cloud Pathfinder](https://ndc-pathfinders.org/)
initiative. Most run on a laptop without HPC access.

| Notebook | Description | Tags |
|---|---|---|
| [`ndc_workflows/sonar_ai.ipynb`](../notebooks/ndc_workflows/sonar_ai.ipynb) | Plot echograms from NOAA SONAR data | <span class="tag tag-dataset">dataset:sonar</span> <span class="tag tag-origin">origin:aws</span> |
| [`ndc_workflows/pycogss_spectral_change.ipynb`](../notebooks/ndc_workflows/pycogss_spectral_change.ipynb) | Spectral change from Sentinel-2 imagery | <span class="tag tag-dataset">dataset:sentinel2</span> <span class="tag tag-origin">origin:aws</span> |
| [`ndc_workflows/envistor_test_ap40.ipynb`](../notebooks/ndc_workflows/envistor_test_ap40.ipynb) | Envistor test via OSPool AP40 | <span class="tag tag-platform">platform:ospool</span> |

## Scripts (non-notebook)

| Script | Description |
|---|---|
| [`scripts/ospool_example/`](../scripts/ospool_example/) | Submit OSDF benchmarks to OSPool via HTCondor |
