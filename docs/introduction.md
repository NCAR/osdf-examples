---
title: Introduction
author:  Harsha R. Hampapura
date: 2026-1-28
---

# Introduction

Welcome to the **OSDF Examples** repository! This repository provides example
notebooks and scripts that demonstrate how to access data via the Open Science
Data Federation ([OSDF](https://osg-htc.org/services/osdf.html)) using
[PelicanFS](https://github.com/PelicanPlatform/pelicanfs). All the notebooks
show how to stream geoscience data into your workflows and perform an
interesting calculation or visualization. To learn more about OSDF and
Pelican, see the [OSDF cookbook](https://projectpythia.org/osdf-cookbook/).

:::{warning} Important Notice
This Jupyter Book is under active development. Set up your Python environment
using the `requirements.txt` file before running any of the notebooks. Please
open an issue on the associated GitHub repository to report bugs or suggest
improvements.
:::

## Find a notebook

The collection is organized by **data origin** rather than a fixed list of
notebooks, so it scales as new examples are added. Use whichever entry point
matches what you have:

- **You have NCAR HPC access (Casper/Derecho).** Browse the NCAR Data Origin
  and NCAR GDEX sections — most workflows there assume Casper.
- **You want to run on a laptop or in the cloud.** Look for notebooks tagged
  `platform:laptop` or `platform:jetstream2`. The
  [NDC Pathfinder](./ndc_workflows.md) workflows are a good starting point.
- **You want to compare OSDF performance.** See the benchmark notebooks under
  the NDC section.
- **Brand new and just want to see something work.** Open
  [`simple_aws_example.ipynb`](../notebooks/simple_aws_example.ipynb).

The full tagged index lives in the [Notebook Gallery](./notebook_gallery.md).

## How notebooks are tagged

Every notebook carries a faceted set of tags in its frontmatter so users can
filter by axis (compute platform, data origin, dataset, task, level). The
facets are:

| Facet | Examples |
|-------|----------|
| `origin:`   | `aws`, `ncar-data-origin`, `ncar-gdex` |
| `platform:` | `casper`, `stampede3`, `jetstream2`, `ospool`, `laptop` |
| `dataset:`  | `cesm`, `cmip6`, `era5`, `conus404`, `na-cordex`, `hrrr`, `dart`, `jra3q`, `hadisst` |
| `task:`     | `bias-correction`, `climatology`, `ml`, `benchmark`, `visualization`, `ecs` |
| `access:`   | `pelicanfs`, `intake-esm`, `zarr` |
| `level:`    | `beginner`, `intermediate`, `advanced` |

For the full taxonomy and conventions, see [CONTRIBUTING.md](../CONTRIBUTING.md#tag-taxonomy).

## How is the repository organized?

This repository is organized into sections based mostly on the data origins
from which the data is accessed and the computational platforms used to
execute the notebooks.

- **NCAR GDEX workflows** — workflows executed on NCAR's HPC system Casper.
    - NCAR Data Origin — data streamed from NCAR's OSDF origin.
    - Other Data Origins — data streamed from origins like AWS Open Data.
    - ML Workflows — machine-learning workflows.
- **Other Computational Platforms** — workflows executed on other HPC and
  cloud computing platforms.
- **NDC Workflows** — workflows developed as part of the
  National Discovery Cloud (NDC) Pathfinder initiative.
- **Scripts** — Python scripts and any content that is not a Jupyter notebook.

### Access methods
Some notebooks use intake/intake-ESM catalogs in conjunction with PelicanFS
to stream data. Others use PelicanFS directly to load data into xarray.

## Repository structure
- **`docs/`** — introductory markdown files for each section and the notebook gallery.
- **`notebooks/`** — all computational workflows archived as Jupyter notebooks.
- **`scripts/`** — Python scripts and any content that is not a Jupyter notebook.
