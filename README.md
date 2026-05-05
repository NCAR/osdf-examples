# OSDF-Examples

[![Jupyter Book](https://img.shields.io/badge/jupyter--book-live-blue?logo=jupyter)](https://ncar.github.io/osdf-examples/)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.16863133.svg)](https://doi.org/10.5281/zenodo.16863133)
[![Python](https://img.shields.io/badge/python-3.10%2B-blue?logo=python)](https://www.python.org/)
[![PelicanFS](https://img.shields.io/badge/built%20with-PelicanFS-orange)](https://github.com/PelicanPlatform/pelicanfs)

A collection of Jupyter notebooks that stream Earth System Science data from
[Open Science Data Federation (OSDF)](https://osg-htc.org/services/osdf.html)
origins using [PelicanFS](https://github.com/PelicanPlatform/pelicanfs), and
run analysis on a variety of HPC and cloud platforms.

**Browse the rendered book:** https://ncar.github.io/osdf-examples/

**New to OSDF or PelicanFS?** Project Pythia's
[OSDF Cookbook](https://projectpythia.org/osdf-cookbook/) is the recommended
introduction — its first chapters cover the OSDF concept and PelicanFS in
depth. For background on how NCAR integrated OSDF with its data
infrastructure, see
[*Integration of OSDF with NCAR's data infrastructure: Interim Project Report*](https://gdex.ucar.edu/documents/24/Interim_Project_Report_OSDF.pdf)
(Oct 2025).

## Quick Start

```bash
git clone https://github.com/NCAR/osdf-examples.git
cd osdf-examples
python -m venv .venv && source .venv/bin/activate    # or use conda
pip install -r requirements.txt
jupyter lab
```

New here? Start with [`notebooks/simple_aws_example.ipynb`](notebooks/simple_aws_example.ipynb)
(runs on a laptop, no credentials required).

## What's inside

The repository is organized by **data origin** — the OSDF origin a notebook
streams data from. Each notebook also indicates the **compute platform** it
was tested on. Browse the [Notebook Gallery](docs/notebook_gallery.md) for the
full, tagged list.

### Data origins
- **GDEX / NCAR Data Origin** — datasets streamed from NCAR's OSDF origin,
  which is NCAR's [Geoscience Data Exchange (GDEX)](https://gdex.ucar.edu/).
  Covers CESM2 LENS, ERA5, JRA-3Q, DART, CONUS404, NA-CORDEX, SAAG, HadISST,
  and more.
- **AWS Open Data** — CESM2 LENS, CMIP6 zarr (~27 GCMs), HRRR, NOAA SONAR,
  Sentinel-2 streamed via the AWS open-data origin.
- **Cross-origin workflows** — examples that combine two or more origins
  (e.g. bias-correcting a CESM AWS dataset against an NCAR ERA5 dataset).

### Compute platforms covered
NCAR Casper · TACC Stampede3 · Indiana Jetstream2 · OSPool · laptop

> Most notebooks are designed to run on a user's own machine via a Dask
> `LocalCluster`. The compute-platform mentions and `platform:` tags
> indicate where each notebook was *verified* (e.g. via PBS on Casper),
> not the only place it can run — flip the cluster switch in the notebook
> to use a `LocalCluster` instead.

### Workflow types
Bias correction · climatology · ML (logistic-regression Niño 3.4 prediction) ·
benchmarking · diagnostic visualization · equilibrium climate sensitivity.

## Finding a notebook

Each notebook is tagged in its frontmatter with a faceted scheme so you can
filter by axis instead of guessing keywords:

| Facet | Examples |
|-------|----------|
| `origin:`   | `aws`, `ncar-data-origin`, `ncar-gdex` |
| `platform:` | `casper`, `stampede3`, `jetstream2`, `ospool`, `laptop` |
| `dataset:`  | `cesm`, `cmip6`, `era5`, `conus404`, `na-cordex`, `hrrr`, `dart`, `jra3q`, `hadisst` |
| `task:`     | `bias-correction`, `climatology`, `ml`, `benchmark`, `visualization`, `ecs` |
| `access:`   | `pelicanfs`, `intake-esm`, `zarr` |
| `level:`    | `beginner`, `intermediate`, `advanced` |

The rendered Jupyter Book exposes these tags as filters. See the [Notebook
Gallery](docs/notebook_gallery.md) for a tagged index, or
[CONTRIBUTING.md](CONTRIBUTING.md) for the tag conventions when adding new
notebooks.

## Repository structure

```
docs/         Markdown overviews and the notebook gallery
notebooks/    All workflow notebooks (subfolders for ML and NDC workflows)
scripts/      Non-notebook code (e.g. OSPool batch examples)
myst.yml      Jupyter Book configuration / table of contents
```

## How to contribute

Contributions are welcome from anyone — you do **not** need an NCAR HPC
account. Notebooks that run on a laptop, on the cloud, or on any HPC system
are all in scope, as long as they demonstrate accessing data via OSDF/PelicanFS.

1. Fork the repository.
2. Create a feature branch: `git checkout -b example/my-amazing-example`.
3. Add your notebook with the standard frontmatter and tags (see
   [CONTRIBUTING.md](CONTRIBUTING.md)).
4. Open a pull request describing the dataset, origin, and compute platform.

If you're contributing a workflow that requires NCAR HPC access, please note
that in the notebook so external readers know what to expect.

## Citing

If you use any workflow in this repository, please cite via the DOI badge
above.

## Support

Bug reports and feature requests: please open a [GitHub Issue](https://github.com/NCAR/osdf-examples/issues).
