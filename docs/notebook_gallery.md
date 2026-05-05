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
- **Want to run on your laptop or in the cloud?** → Look for <a class="tag-link" href="tag-index#tag-platform-laptop"><span class="tag tag-platform">platform:laptop</span></a> or <a class="tag-link" href="tag-index#tag-platform-jetstream2"><span class="tag tag-platform">platform:jetstream2</span></a> notebooks under [Cross-platform / cloud](#cross-platform--cloud-examples).
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
| [`cesm_bias.ipynb`](../notebooks/cesm_bias.ipynb) | Bias-correct CESM2 LENS temperatures using ERA5 | <a class="tag-link" href="tag-index#tag-dataset-cesm"><span class="tag tag-dataset">dataset:cesm</span></a> <a class="tag-link" href="tag-index#tag-dataset-era5"><span class="tag tag-dataset">dataset:era5</span></a> <a class="tag-link" href="tag-index#tag-task-bias-correction"><span class="tag tag-task">task:bias-correction</span></a> <a class="tag-link" href="tag-index#tag-platform-casper"><span class="tag tag-platform">platform:casper</span></a> |
| [`cesm_gmst_ncar.ipynb`](../notebooks/cesm_gmst_ncar.ipynb) | Compute and plot CESM2 LENS GMST anomaly | <a class="tag-link" href="tag-index#tag-dataset-cesm"><span class="tag tag-dataset">dataset:cesm</span></a> <a class="tag-link" href="tag-index#tag-task-visualization"><span class="tag tag-task">task:visualization</span></a> <a class="tag-link" href="tag-index#tag-platform-casper"><span class="tag tag-platform">platform:casper</span></a> |
| [`cesm_oceanheat.ipynb`](../notebooks/cesm_oceanheat.ipynb) | Compute surface ocean heat content from CESM2 LENS | <a class="tag-link" href="tag-index#tag-dataset-cesm"><span class="tag tag-dataset">dataset:cesm</span></a> <a class="tag-link" href="tag-index#tag-task-visualization"><span class="tag tag-task">task:visualization</span></a> <a class="tag-link" href="tag-index#tag-platform-casper"><span class="tag tag-platform">platform:casper</span></a> |
| [`conus404.ipynb`](../notebooks/conus404.ipynb) | Diagnostic plots from CONUS404 | <a class="tag-link" href="tag-index#tag-dataset-conus404"><span class="tag tag-dataset">dataset:conus404</span></a> <a class="tag-link" href="tag-index#tag-task-visualization"><span class="tag tag-task">task:visualization</span></a> <a class="tag-link" href="tag-index#tag-platform-casper"><span class="tag tag-platform">platform:casper</span></a> |
| [`dart-cam6.ipynb`](../notebooks/dart-cam6.ipynb) | Diagnostic plots from the DART/CAM6 reanalysis | <a class="tag-link" href="tag-index#tag-dataset-dart"><span class="tag tag-dataset">dataset:dart</span></a> <a class="tag-link" href="tag-index#tag-task-visualization"><span class="tag tag-task">task:visualization</span></a> <a class="tag-link" href="tag-index#tag-platform-casper"><span class="tag tag-platform">platform:casper</span></a> |
| [`jra_3q.ipynb`](../notebooks/jra_3q.ipynb) | Plots from the JRA-3Q reanalysis | <a class="tag-link" href="tag-index#tag-dataset-jra3q"><span class="tag tag-dataset">dataset:jra3q</span></a> <a class="tag-link" href="tag-index#tag-task-visualization"><span class="tag tag-task">task:visualization</span></a> <a class="tag-link" href="tag-index#tag-platform-casper"><span class="tag tag-platform">platform:casper</span></a> |
| [`eol_era5.ipynb`](../notebooks/eol_era5.ipynb) | ERA5 access via the EOL/NCAR origin | <a class="tag-link" href="tag-index#tag-dataset-era5"><span class="tag tag-dataset">dataset:era5</span></a> <a class="tag-link" href="tag-index#tag-platform-casper"><span class="tag tag-platform">platform:casper</span></a> |
| [`era5_precip.ipynb`](../notebooks/era5_precip.ipynb) | ERA5 precipitation diagnostics | <a class="tag-link" href="tag-index#tag-dataset-era5"><span class="tag tag-dataset">dataset:era5</span></a> <a class="tag-link" href="tag-index#tag-task-visualization"><span class="tag tag-task">task:visualization</span></a> <a class="tag-link" href="tag-index#tag-platform-casper"><span class="tag tag-platform">platform:casper</span></a> |
| [`geocat_climatology.ipynb`](../notebooks/geocat_climatology.ipynb) | Daily-temperature climatology with `geocat-comp` | <a class="tag-link" href="tag-index#tag-dataset-era5"><span class="tag tag-dataset">dataset:era5</span></a> <a class="tag-link" href="tag-index#tag-task-climatology"><span class="tag tag-task">task:climatology</span></a> <a class="tag-link" href="tag-index#tag-platform-casper"><span class="tag tag-platform">platform:casper</span></a> |
| [`hadisst_elnino.ipynb`](../notebooks/hadisst_elnino.ipynb) | El Niño diagnostics from HadISST | <a class="tag-link" href="tag-index#tag-dataset-hadisst"><span class="tag tag-dataset">dataset:hadisst</span></a> <a class="tag-link" href="tag-index#tag-task-visualization"><span class="tag tag-task">task:visualization</span></a> <a class="tag-link" href="tag-index#tag-platform-casper"><span class="tag tag-platform">platform:casper</span></a> |
| [`jja_heatindex.ipynb`](../notebooks/jja_heatindex.ipynb) | JJA heat-index calculation | <a class="tag-link" href="tag-index#tag-task-visualization"><span class="tag tag-task">task:visualization</span></a> <a class="tag-link" href="tag-index#tag-platform-casper"><span class="tag tag-platform">platform:casper</span></a> |
| [`na_cordex.ipynb`](../notebooks/na_cordex.ipynb) | NA-CORDEX diagnostic plots | <a class="tag-link" href="tag-index#tag-dataset-na-cordex"><span class="tag tag-dataset">dataset:na-cordex</span></a> <a class="tag-link" href="tag-index#tag-task-visualization"><span class="tag tag-task">task:visualization</span></a> <a class="tag-link" href="tag-index#tag-platform-casper"><span class="tag tag-platform">platform:casper</span></a> |
| [`saag.ipynb`](../notebooks/saag.ipynb) | SAAG dataset diagnostics | <a class="tag-link" href="tag-index#tag-task-visualization"><span class="tag tag-task">task:visualization</span></a> <a class="tag-link" href="tag-index#tag-platform-casper"><span class="tag tag-platform">platform:casper</span></a> |
| [`uxarray_test.ipynb`](../notebooks/uxarray_test.ipynb) | Unstructured-grid access via UXarray | <a class="tag-link" href="tag-index#tag-task-visualization"><span class="tag tag-task">task:visualization</span></a> <a class="tag-link" href="tag-index#tag-platform-casper"><span class="tag tag-platform">platform:casper</span></a> |

## AWS Open Data

Notebooks that stream from the OSDF AWS open-data origin.

| Notebook | Description | Tags |
|---|---|---|
| [`cmip6_gmst_zarr.ipynb`](../notebooks/cmip6_gmst_zarr.ipynb) | Multi-model GMST from CMIP6 zarr (~27 GCMs), compared to HadCRUT5 | <a class="tag-link" href="tag-index#tag-dataset-cmip6"><span class="tag tag-dataset">dataset:cmip6</span></a> <a class="tag-link" href="tag-index#tag-access-zarr"><span class="tag tag-access">access:zarr</span></a> <a class="tag-link" href="tag-index#tag-task-visualization"><span class="tag tag-task">task:visualization</span></a> |
| [`cmip6_ecs.ipynb`](../notebooks/cmip6_ecs.ipynb) | Equilibrium Climate Sensitivity from CMIP6 | <a class="tag-link" href="tag-index#tag-dataset-cmip6"><span class="tag tag-dataset">dataset:cmip6</span></a> <a class="tag-link" href="tag-index#tag-task-ecs"><span class="tag tag-task">task:ecs</span></a> |
| [`cmip6_bias_correction.ipynb`](../notebooks/cmip6_bias_correction.ipynb) | Bias-correct CMIP6 output | <a class="tag-link" href="tag-index#tag-dataset-cmip6"><span class="tag tag-dataset">dataset:cmip6</span></a> <a class="tag-link" href="tag-index#tag-task-bias-correction"><span class="tag tag-task">task:bias-correction</span></a> |
| [`cmip6_precipitation.ipynb`](../notebooks/cmip6_precipitation.ipynb) | CMIP6 precipitation diagnostics | <a class="tag-link" href="tag-index#tag-dataset-cmip6"><span class="tag tag-dataset">dataset:cmip6</span></a> <a class="tag-link" href="tag-index#tag-task-visualization"><span class="tag tag-task">task:visualization</span></a> |
| [`hrrr_aws.ipynb`](../notebooks/hrrr_aws.ipynb) | Stream HRRR data from AWS | <a class="tag-link" href="tag-index#tag-dataset-hrrr"><span class="tag tag-dataset">dataset:hrrr</span></a> <a class="tag-link" href="tag-index#tag-origin-aws"><span class="tag tag-origin">origin:aws</span></a> |
| [`simple_aws_example.ipynb`](../notebooks/simple_aws_example.ipynb) | Minimal AWS-origin example — good first notebook | <a class="tag-link" href="tag-index#tag-origin-aws"><span class="tag tag-origin">origin:aws</span></a> <a class="tag-link" href="tag-index#tag-level-beginner"><span class="tag tag-level">level:beginner</span></a> |

## Cross-platform / cloud examples

Notebooks demonstrating execution outside Casper.

| Notebook | Description | Tags |
|---|---|---|
| [`cesm_osdf_stampede3.ipynb`](../notebooks/cesm_osdf_stampede3.ipynb) | Bias-correction workflow on TACC Stampede3 | <a class="tag-link" href="tag-index#tag-platform-stampede3"><span class="tag tag-platform">platform:stampede3</span></a> <a class="tag-link" href="tag-index#tag-dataset-cesm"><span class="tag tag-dataset">dataset:cesm</span></a> <a class="tag-link" href="tag-index#tag-task-bias-correction"><span class="tag tag-task">task:bias-correction</span></a> |
| [`jetstream_intro.ipynb`](../notebooks/jetstream_intro.ipynb) | Introduction to running on Jetstream2 | <a class="tag-link" href="tag-index#tag-platform-jetstream2"><span class="tag tag-platform">platform:jetstream2</span></a> <a class="tag-link" href="tag-index#tag-level-beginner"><span class="tag tag-level">level:beginner</span></a> |
| [`jetstream_cesm_oceanheat.ipynb`](../notebooks/jetstream_cesm_oceanheat.ipynb) | Ocean-heat workflow on Jetstream2 | <a class="tag-link" href="tag-index#tag-platform-jetstream2"><span class="tag tag-platform">platform:jetstream2</span></a> <a class="tag-link" href="tag-index#tag-dataset-cesm"><span class="tag tag-dataset">dataset:cesm</span></a> |
| [`jetstream_cmip6_gmst.ipynb`](../notebooks/jetstream_cmip6_gmst.ipynb) | CMIP6 GMST on Jetstream2 | <a class="tag-link" href="tag-index#tag-platform-jetstream2"><span class="tag tag-platform">platform:jetstream2</span></a> <a class="tag-link" href="tag-index#tag-dataset-cmip6"><span class="tag tag-dataset">dataset:cmip6</span></a> |

## Benchmarks

Notebooks that measure data-access throughput from various OSDF origins.

| Notebook | Description | Tags |
|---|---|---|
| [`ndc_workflows/aws_benchmark.ipynb`](../notebooks/ndc_workflows/aws_benchmark.ipynb) | Benchmark CESM2 LENS access from AWS origin | <a class="tag-link" href="tag-index#tag-task-benchmark"><span class="tag tag-task">task:benchmark</span></a> <a class="tag-link" href="tag-index#tag-origin-aws"><span class="tag tag-origin">origin:aws</span></a> |
| [`ndc_workflows/ncar_benchmark.ipynb`](../notebooks/ndc_workflows/ncar_benchmark.ipynb) | Benchmark NCAR-origin access (DART) | <a class="tag-link" href="tag-index#tag-task-benchmark"><span class="tag tag-task">task:benchmark</span></a> <a class="tag-link" href="tag-index#tag-origin-ncar-data-origin"><span class="tag tag-origin">origin:ncar-data-origin</span></a> |
| [`ndc_workflows/ncar_benchmark_simple.ipynb`](../notebooks/ndc_workflows/ncar_benchmark_simple.ipynb) | Simplified NCAR benchmark | <a class="tag-link" href="tag-index#tag-task-benchmark"><span class="tag tag-task">task:benchmark</span></a> <a class="tag-link" href="tag-index#tag-level-beginner"><span class="tag tag-level">level:beginner</span></a> |
| [`ndc_workflows/ncar_benchmark_ap40.ipynb`](../notebooks/ndc_workflows/ncar_benchmark_ap40.ipynb) | NCAR-origin benchmark via OSPool AP40 | <a class="tag-link" href="tag-index#tag-task-benchmark"><span class="tag tag-task">task:benchmark</span></a> <a class="tag-link" href="tag-index#tag-platform-ospool"><span class="tag tag-platform">platform:ospool</span></a> |

## Machine-learning workflows

| Notebook | Description | Tags |
|---|---|---|
| [`ml_workflows/nino3.4_index.ipynb`](../notebooks/ml_workflows/nino3.4_index.ipynb) | Logistic-regression Niño 3.4 prediction from SST | <a class="tag-link" href="tag-index#tag-task-ml"><span class="tag tag-task">task:ml</span></a> <a class="tag-link" href="tag-index#tag-dataset-hadisst"><span class="tag tag-dataset">dataset:hadisst</span></a> |

## NDC pathfinder workflows

Notebooks developed under the [National Discovery Cloud Pathfinder](https://ndc-pathfinders.org/)
initiative. Most run on a laptop without HPC access.

| Notebook | Description | Tags |
|---|---|---|
| [`ndc_workflows/sonar_ai.ipynb`](../notebooks/ndc_workflows/sonar_ai.ipynb) | Plot echograms from NOAA SONAR data | <a class="tag-link" href="tag-index#tag-dataset-sonar"><span class="tag tag-dataset">dataset:sonar</span></a> <a class="tag-link" href="tag-index#tag-origin-aws"><span class="tag tag-origin">origin:aws</span></a> |
| [`ndc_workflows/pycogss_spectral_change.ipynb`](../notebooks/ndc_workflows/pycogss_spectral_change.ipynb) | Spectral change from Sentinel-2 imagery | <a class="tag-link" href="tag-index#tag-dataset-sentinel2"><span class="tag tag-dataset">dataset:sentinel2</span></a> <a class="tag-link" href="tag-index#tag-origin-aws"><span class="tag tag-origin">origin:aws</span></a> |
| [`ndc_workflows/envistor_test_ap40.ipynb`](../notebooks/ndc_workflows/envistor_test_ap40.ipynb) | Envistor test via OSPool AP40 | <a class="tag-link" href="tag-index#tag-platform-ospool"><span class="tag tag-platform">platform:ospool</span></a> |

## Scripts (non-notebook)

| Script | Description |
|---|---|
| [`scripts/ospool_example/`](../scripts/ospool_example/) | Submit OSDF benchmarks to OSPool via HTCondor |
