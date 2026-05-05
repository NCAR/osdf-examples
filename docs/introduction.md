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
interesting calculation or visualization.

:::{warning} Important Notice
This Jupyter Book is under active development. Set up your Python environment
using the `requirements.txt` file before running any of the notebooks. Please
open an issue on the associated GitHub repository to report bugs or suggest
improvements.
:::

## A short primer on OSDF and PelicanFS

If accessing scientific data still feels like "download a giant archive, then
analyze it locally," OSDF is the alternative. The
[Open Science Data Federation](https://osg-htc.org/services/osdf.html) is an
NSF-funded content-distribution layer for science: it sits in front of
existing repositories and streams data over HTTPS to wherever your code is
running.

Two pieces of jargon worth knowing:

- **Origin** — a server that connects an existing data repository to the
  federation. For example, NCAR runs on-prem OSDF origins that expose
  datasets from [GDEX](https://gdex.ucar.edu) (NCAR's Geoscience Data
  Exchange — 17 PB across 1600+ datasets on POSIX storage). The origin is a
  separate piece of hardware that talks to GDEX's storage; the two are
  co-located but conceptually distinct.
- **Cache** — a server that holds temporary copies of frequently-requested
  objects close to where computation happens. For instance, NCAR also runs
  an on-prem cache so Casper/Derecho users get fast access to data from
  *any* OSDF origin (not just NCAR's).

You don't have to think about origins and caches when you read data — the
Pelican packages handle this transparently. In this repository, we use the
Pelican Python client **PelicanFS**, an
[FSSpec](https://filesystem-spec.readthedocs.io/) implementation, which
plugs into anything that already speaks FSSpec: `xarray`, `intake`,
`intake-esm`, `pandas`. The two URL schemes you'll see throughout this book:

| Scheme | Format | Used for |
|---|---|---|
| `osdf` | `osdf:///<namespace-path>` | OSDF data — note the **three** slashes |
| `pelican` | `pelican://<federation-host>/<namespace-path>` | Other Pelican federations |

Common namespaces in this book:

- `osdf:///ncar/gdex/<dataset_id>` — NCAR/GDEX datasets via the NCAR origin.
- `osdf:///aws-opendata/us-west-2/...` and `.../us-west-1/...` — AWS Open
  Data (CMIP6, CESM2 LENS, HRRR, etc.) via the AWS origin.

A typical xarray + zarr call looks like:

```python
import xarray as xr
ds = xr.open_zarr("osdf:///aws-opendata/us-west-2/cmip6-pds/.../...")
```

For a deeper introduction with executable examples, see Project Pythia's
[**OSDF Cookbook**](https://projectpythia.org/osdf-cookbook/) — its first
chapters cover the OSDF concept and PelicanFS usage in detail. To learn how
NCAR integrated OSDF with its data infrastructure, see
[*Integration of OSDF with NCAR's data infrastructure: Interim Project Report*](https://gdex.ucar.edu/documents/24/Interim_Project_Report_OSDF.pdf)
(Oct 2025).

## Find a notebook

The collection is organized by **data origin** rather than a fixed list of
notebooks, so it scales as new examples are added. Use whichever entry point
matches what you have:

- **You have NCAR HPC access (Casper/Derecho).** Browse the GDEX / NCAR Data
  Origin section — those notebooks stream GDEX data through NCAR's on-prem
  OSDF origin and run on Casper.
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

**A note on `platform:` tags.** Most notebooks are designed to run on a
user's own machine via a Dask `LocalCluster`, and only opt into PBS/Slurm
when a flag is set. The `platform:` tag therefore documents **where the
notebook has been verified to run**, not the only place it can run. A
notebook tagged `platform:casper` was tested on Casper using PBS; flip the
cluster switch in the notebook (e.g. `USE_PBS_SCHEDULER = False`) and the
same notebook runs locally.

For the full taxonomy and conventions, see [CONTRIBUTING.md](../CONTRIBUTING.md#tag-taxonomy).

## How is the repository organized?

This repository is organized into sections based mostly on the data origins
from which the data is accessed and the computational platforms used to
execute the notebooks.

- **NCAR HPC workflows (Casper)** — notebooks executed on NCAR's HPC system.
    - GDEX / NCAR Data Origin — GDEX data streamed via NCAR's on-prem OSDF
      origin.
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
