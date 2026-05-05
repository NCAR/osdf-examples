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

## Find a notebook

- **Have NCAR HPC access (Casper/Derecho)?** → Check the [NCAR Data Origin](#ncar-data-origin) and [NCAR GDEX](#ncar-gdex) sections.
- **Want to run on your laptop or in the cloud?** → Look for `platform:laptop` or `platform:jetstream2` notebooks under [Cross-platform / cloud](#cross-platform--cloud-examples).
- **Looking for ML examples?** → See [Machine learning](#machine-learning-workflows).
- **Comparing OSDF performance?** → See [Benchmarks](#benchmarks).

---

## NCAR Data Origin

Notebooks that stream data from NCAR's OSDF origin (CESM2 LENS, ERA5, JRA-3Q,
DART, CONUS404, etc.).

| Notebook | Description | Tags |
|---|---|---|
| [`cesm_bias.ipynb`](../notebooks/cesm_bias.ipynb) | Bias-correct CESM2 LENS temperatures using ERA5 | `dataset:cesm` `dataset:era5` `task:bias-correction` `platform:casper` |
| [`cesm_gmst_ncar.ipynb`](../notebooks/cesm_gmst_ncar.ipynb) | Compute and plot CESM2 LENS GMST anomaly | `dataset:cesm` `task:visualization` `platform:casper` |
| [`cesm_oceanheat.ipynb`](../notebooks/cesm_oceanheat.ipynb) | Compute surface ocean heat content from CESM2 LENS | `dataset:cesm` `task:visualization` `platform:casper` |
| [`conus404.ipynb`](../notebooks/conus404.ipynb) | Diagnostic plots from CONUS404 | `dataset:conus404` `task:visualization` `platform:casper` |
| [`dart-cam6.ipynb`](../notebooks/dart-cam6.ipynb) | Diagnostic plots from the DART/CAM6 reanalysis | `dataset:dart` `task:visualization` `platform:casper` |
| [`jra_3q.ipynb`](../notebooks/jra_3q.ipynb) | Plots from the JRA-3Q reanalysis | `dataset:jra3q` `task:visualization` `platform:casper` |
| [`eol_era5.ipynb`](../notebooks/eol_era5.ipynb) | ERA5 access via the EOL/NCAR origin | `dataset:era5` `platform:casper` |
| [`era5_precip.ipynb`](../notebooks/era5_precip.ipynb) | ERA5 precipitation diagnostics | `dataset:era5` `task:visualization` `platform:casper` |
| [`geocat_climatology.ipynb`](../notebooks/geocat_climatology.ipynb) | Daily-temperature climatology with `geocat-comp` | `dataset:era5` `task:climatology` `platform:casper` |
| [`hadisst_elnino.ipynb`](../notebooks/hadisst_elnino.ipynb) | El Niño diagnostics from HadISST | `dataset:hadisst` `task:visualization` `platform:casper` |
| [`jja_heatindex.ipynb`](../notebooks/jja_heatindex.ipynb) | JJA heat-index calculation | `task:visualization` `platform:casper` |
| [`na_cordex.ipynb`](../notebooks/na_cordex.ipynb) | NA-CORDEX diagnostic plots | `dataset:na-cordex` `task:visualization` `platform:casper` |
| [`saag.ipynb`](../notebooks/saag.ipynb) | SAAG dataset diagnostics | `task:visualization` `platform:casper` |
| [`uxarray_test.ipynb`](../notebooks/uxarray_test.ipynb) | Unstructured-grid access via UXarray | `task:visualization` `platform:casper` |

## NCAR GDEX

Datasets hosted on NCAR's [Geoscience Data Exchange](https://gdex.ucar.edu/).
The GDEX origin overlaps the NCAR Data Origin in practice; notebooks listed
above that read NA-CORDEX, CONUS404, SAAG, or HadISST also count as GDEX
workflows.

## AWS Open Data

Notebooks that stream from the OSDF AWS open-data origin.

| Notebook | Description | Tags |
|---|---|---|
| [`cmip6_gmst_zarr.ipynb`](../notebooks/cmip6_gmst_zarr.ipynb) | Multi-model GMST from CMIP6 zarr (~27 GCMs), compared to HadCRUT5 | `dataset:cmip6` `access:zarr` `task:visualization` |
| [`cmip6_ecs.ipynb`](../notebooks/cmip6_ecs.ipynb) | Equilibrium Climate Sensitivity from CMIP6 | `dataset:cmip6` `task:ecs` |
| [`cmip6_bias_correction.ipynb`](../notebooks/cmip6_bias_correction.ipynb) | Bias-correct CMIP6 output | `dataset:cmip6` `task:bias-correction` |
| [`cmip6_precipitation.ipynb`](../notebooks/cmip6_precipitation.ipynb) | CMIP6 precipitation diagnostics | `dataset:cmip6` `task:visualization` |
| [`hrrr_aws.ipynb`](../notebooks/hrrr_aws.ipynb) | Stream HRRR data from AWS | `dataset:hrrr` `origin:aws` |
| [`simple_aws_example.ipynb`](../notebooks/simple_aws_example.ipynb) | Minimal AWS-origin example — good first notebook | `origin:aws` `level:beginner` |

## Cross-platform / cloud examples

Notebooks demonstrating execution outside Casper.

| Notebook | Description | Tags |
|---|---|---|
| [`cesm_osdf_stampede3.ipynb`](../notebooks/cesm_osdf_stampede3.ipynb) | Bias-correction workflow on TACC Stampede3 | `platform:stampede3` `dataset:cesm` `task:bias-correction` |
| [`jetstream_intro.ipynb`](../notebooks/jetstream_intro.ipynb) | Introduction to running on Jetstream2 | `platform:jetstream2` `level:beginner` |
| [`jetstream_cesm_oceanheat.ipynb`](../notebooks/jetstream_cesm_oceanheat.ipynb) | Ocean-heat workflow on Jetstream2 | `platform:jetstream2` `dataset:cesm` |
| [`jetstream_cmip6_gmst.ipynb`](../notebooks/jetstream_cmip6_gmst.ipynb) | CMIP6 GMST on Jetstream2 | `platform:jetstream2` `dataset:cmip6` |

## Benchmarks

Notebooks that measure data-access throughput from various OSDF origins.

| Notebook | Description | Tags |
|---|---|---|
| [`ndc_workflows/aws_benchmark.ipynb`](../notebooks/ndc_workflows/aws_benchmark.ipynb) | Benchmark CESM2 LENS access from AWS origin | `task:benchmark` `origin:aws` |
| [`ndc_workflows/ncar_benchmark.ipynb`](../notebooks/ndc_workflows/ncar_benchmark.ipynb) | Benchmark NCAR-origin access (DART) | `task:benchmark` `origin:ncar-data-origin` |
| [`ndc_workflows/ncar_benchmark_simple.ipynb`](../notebooks/ndc_workflows/ncar_benchmark_simple.ipynb) | Simplified NCAR benchmark | `task:benchmark` `level:beginner` |
| [`ndc_workflows/ncar_benchmark_ap40.ipynb`](../notebooks/ndc_workflows/ncar_benchmark_ap40.ipynb) | NCAR-origin benchmark via OSPool AP40 | `task:benchmark` `platform:ospool` |

## Machine-learning workflows

| Notebook | Description | Tags |
|---|---|---|
| [`ml_workflows/nino3.4_index.ipynb`](../notebooks/ml_workflows/nino3.4_index.ipynb) | Logistic-regression Niño 3.4 prediction from SST | `task:ml` `dataset:hadisst` |

## NDC pathfinder workflows

Notebooks developed under the [National Discovery Cloud Pathfinder](https://ndc-pathfinders.org/)
initiative. Most run on a laptop without HPC access.

| Notebook | Description | Tags |
|---|---|---|
| [`ndc_workflows/sonar_ai.ipynb`](../notebooks/ndc_workflows/sonar_ai.ipynb) | Plot echograms from NOAA SONAR data | `dataset:sonar` `origin:aws` |
| [`ndc_workflows/pycogss_spectral_change.ipynb`](../notebooks/ndc_workflows/pycogss_spectral_change.ipynb) | Spectral change from Sentinel-2 imagery | `dataset:sentinel2` `origin:aws` |
| [`ndc_workflows/envistor_test_ap40.ipynb`](../notebooks/ndc_workflows/envistor_test_ap40.ipynb) | Envistor test via OSPool AP40 | `platform:ospool` |

## Scripts (non-notebook)

| Script | Description |
|---|---|
| [`scripts/ospool_example/`](../scripts/ospool_example/) | Submit OSDF benchmarks to OSPool via HTCondor |
