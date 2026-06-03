# Contributing to OSDF-Examples

Thanks for your interest in contributing! Notebooks that demonstrate streaming
Earth System Science data via OSDF/PelicanFS are welcome from anyone — you do
**not** need an NCAR HPC account. Workflows that run on a laptop, on a public
cloud, or on any HPC system are all in scope.

## Workflow

1. Fork the repository.
2. Create a branch: `git checkout -b example/<short-description>`.
3. Add your notebook under `notebooks/` (or an appropriate subfolder).
4. Add an entry to `myst.yml` so it appears in the Jupyter Book.
5. Open a pull request describing the dataset, origin, and compute platform
   used.

## Notebook conventions

### Frontmatter and visible tag line

Every notebook needs **two cells at the top**:

1. A title cell — a markdown cell containing only the YAML frontmatter
   (title, author, tags) and the H1 heading. The frontmatter `tags` feed
   MyST's search/categorization.
2. A separate markdown cell with a visible **Tags:** line. This must be its
   own cell — MyST treats anything else in the title cell as title metadata
   and strips it from the rendered page, so an inline tag line in the same
   cell as the heading will not appear.

**Cell 1 (title cell):**

```yaml
---
title: Bias-correct CESM2 LENS temperature data
author: Your Name
tags:
  - origin:ncar-posix
  - origin:ncar-object-store
  - platform:casper
  - dataset:cesm
  - dataset:era5
  - task:bias-correction
  - level:intermediate
---
# Bias-correct CESM2 LENS temperature data using ERA5 reanalysis
```

**Cell 2 (tag line, separate cell)** — wrap each tag in an `<a class="tag-link">`
anchor pointing at the matching section of the auto-generated
[Tag Index](docs/tag_index.md), with an inner `<span>` carrying the
`tag tag-<facet>` classes (where `<facet>` is one of `origin`, `platform`,
`dataset`, `task`, `level`). The script handles all of this for you, so just
add a row to `NOTEBOOKS` and re-run `tag_notebooks.py`. The rendered cell
looks like:

```html
<a class="tag-link" href="tag-index#tag-origin-ncar-posix"><span class="tag tag-origin">origin:ncar-posix</span></a> <a class="tag-link" href="tag-index#tag-origin-ncar-object-store"><span class="tag tag-origin">origin:ncar-object-store</span></a> <a class="tag-link" href="tag-index#tag-platform-casper"><span class="tag tag-platform">platform:casper</span></a> ...
```

(MyST passes inline HTML through; the Pandoc-style `[text]{.class}` shorthand
is *not* parsed by jupyter-book v2.0, so use the verbose HTML form.)

Keep the two tag lists in sync — the visible line should mirror the
frontmatter exactly. The
[`scripts/maintenance/tag_notebooks.py`](scripts/maintenance/tag_notebooks.py)
helper in this repo can apply both cells in one go from a small per-notebook
mapping; add an entry there when you contribute a new notebook.

### Tag taxonomy

Tags use a `facet:value` scheme so users can filter on any axis. Always pick
from the lists below — invent a new value only when none of the existing ones
fit, and please mention the addition in your PR.

| Facet | Allowed values |
|-------|----------------|
| `origin:`   | `aws`, `ncar-posix`, `ncar-object-store` |
| `platform:` | `casper`, `stampede3`, `jetstream2`, `ospool`, `laptop` |
| `dataset:`  | `cesm`, `cmip6`, `era5`, `conus404`, `na-cordex`, `hrrr`, `dart`, `jra3q`, `hadisst`, `sentinel2`, `sonar` |
| `task:`     | `bias-correction`, `climatology`, `ml`, `benchmark`, `visualization`, `ecs` |
| `level:`    | `beginner`, `intermediate`, `advanced` |

NCAR runs two OSDF origins. Use `origin:ncar-posix` for any notebook that
streams from `osdf:///ncar/gdex/...` (POSIX storage; some older notebooks use
the previous name `osdf:///ncar/rda/...` — that's the same origin). Use
`origin:ncar-object-store` for notebooks that stream from
`osdf:///ncar-gdex/...` (NCAR's object storage, currently called Boreas).

A notebook can carry multiple `origin:` or `dataset:` tags — list every origin
or dataset it actually touches.

**About `platform:` tags.** The repository's goal is that every notebook
can run on a user's own machine via a Dask **`LocalCluster`** (with PBS/Slurm
options available for users on HPC). The `platform:` tag therefore documents
**where the notebook has been verified to run** — *not* the only place it
can run. A notebook tagged `platform:casper` was tested on NCAR Casper using
a PBS cluster; the same notebook should still work locally by flipping the
cluster switch in the notebook (e.g. `USE_PBS_SCHEDULER = False`). Use a
single `platform:` value reflecting the platform where the notebook was
verified — there's no need to also tag `platform:laptop` just because the
LocalCluster path exists.

### Required intro section

After the frontmatter, include a short info section so a reader who lands on
the notebook directly can tell at a glance whether it's relevant:

- **What this does** — one or two sentences.
- **Data origin(s)** — which OSDF origin(s) the notebook streams from.
- **Compute platform** — where the notebook was tested.
- **Prerequisites** — any credentials, accounts, or HPC allocations needed.
- **Approximate runtime** and **data volume** — rough order of magnitude.

If a notebook requires NCAR HPC access (Casper/Derecho) or any other
non-public resource, say so in this section so external readers aren't
surprised.

### Other guidelines

- Clear notebook outputs that contain large embedded data before committing
  (`jupyter nbconvert --clear-output --inplace your_notebook.ipynb`).
- Avoid hard-coded paths to user-private storage; use environment variables
  or call them out in the prerequisites.
- Keep cell outputs that visualize results — those are the value of the
  example.

## Reporting issues

Bugs, broken links, environment problems, and suggestions all belong in
[GitHub Issues](https://github.com/NCAR/osdf-examples/issues).
