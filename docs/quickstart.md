---
title: Quick Start
author: Harsha R. Hampapura
---

# Quick Start

Get from zero to a working `osdf://` data read in a few minutes, then branch into
the rest of the collection. This page uses **ERA5** (NCAR GDEX dataset
[`d633000`](https://gdex.ucar.edu/datasets/d633000/)) as a single running example
so you can see every access pattern against the same data.

:::{admonition} Written for PelicanFS 1.3.1
:class: important
This guide was written with **PelicanFS 1.3.1** in mind and **will evolve** as
PelicanFS changes — option names, defaults, and cache behavior may differ in
other versions. Always cross-check against the current
[PelicanFS documentation](https://docs.pelicanplatform.org/) and the
[PelicanFS repository](https://github.com/PelicanPlatform/pelicanfs).
:::

## 1. Why OSDF?

If accessing scientific data still means "download a giant archive, then analyze
it locally," OSDF is the alternative: it **streams** data over HTTPS to wherever
your code runs — a laptop, a cloud VM, or an HPC node — so you read only the
bytes you actually use. In this repository you access OSDF through
[**PelicanFS**](https://github.com/PelicanPlatform/pelicanfs), an
[FSSpec](https://filesystem-spec.readthedocs.io/) client, so `xarray`, `intake`,
and `pandas` all work unchanged.

## 2. Set up — pick one path

**Fastest (laptop, minimal deps).** Just enough to run the first read below:

```bash
pip install pelicanfs xarray zarr dask aiohttp
```

**Full repository (all notebooks).** Clone and build the pinned environment:

```bash
git clone https://github.com/NCAR/osdf-examples.git
cd osdf-examples
conda env create -n osdf -f environment.yml
conda activate osdf
jupyter lab
```

**One-click Binder.** *Coming soon* — a launch-in-your-browser badge is in the
works with the NCAR CIRRUS team. Until then, use one of the two paths above.

## 3. Your first OSDF read

Open ERA5 2-metre temperature straight from OSDF. The store is opened *lazily*,
so this returns in seconds without downloading the full archive:

```python
import xarray as xr

ds = xr.open_zarr("osdf:///ncar/gdex/d633000/e5.oper.an.sfc.zarr/e5.oper.an.sfc.2t.zarr")
ds          # a lazy xarray.Dataset — metadata now, bytes on demand
```

Pull a single value to prove data really flows over OSDF:

```python
ds["VAR_2T"].isel(time=0, latitude=360, longitude=720).values   # one point, streamed on demand
```

:::{tip}
Note the **three** slashes in `osdf:///`. `osdf://path` (two slashes) is silently
wrong — the leading slash is part of the namespace path.
:::

## 4. What just happened?

You asked a Pelican **director** for `ncar/gdex/d633000/...`; it pointed PelicanFS
at a nearby **cache** (or the **origin** — the server that exposes GDEX data to
the federation), and only the chunks you touched were transferred. You don't have
to manage any of this — but when you *want* control (a slow cache, a bad cache),
the options in [§5](#sec-patterns) give it to you. For the full concept primer,
see the [Introduction](introduction.md).

(sec-patterns)=
## 5. PelicanFS access patterns (with ERA5)

### Zarr vs NetCDF

PelicanFS is format-agnostic — anything FSSpec can read works. **Zarr** stores
open directly by URL:

```python
ds = xr.open_zarr("osdf:///ncar/gdex/d633000/e5.oper.an.sfc.zarr/e5.oper.an.sfc.2t.zarr")
```

**NetCDF** files are opened through a PelicanFS file handle (HDF5/NetCDF needs a
seekable file object, so hand `xr.open_dataset` an open handle rather than a URL):

```python
from pelicanfs.core import OSDFFileSystem

fs = OSDFFileSystem()
# One month of hourly ERA5 2-m temperature — a ~1.1 GB raw NetCDF file under d633000.
nc_path = "osdf:///ncar/gdex/d633000/e5.oper.an.sfc/202501/e5.oper.an.sfc.128_167_2t.ll025sc.2025010100_2025013123.nc"
with fs.open(nc_path, "rb") as f:
    ds_nc = xr.open_dataset(f, engine="h5netcdf")   # header now; variable data on demand
```

Opening reads only the file header, so it returns quickly despite the ~1 GB size —
variable data streams in as you slice. For *many* NetCDF files at once, a kerchunk
reference (below) is far more efficient than opening each one over HTTP.

### Generic read (no options)

The everyday form — no extra arguments. The director rotates among healthy
caches for you:

```python
ds = xr.open_zarr("osdf:///ncar/gdex/d633000/e5.oper.an.sfc.zarr/e5.oper.an.sfc.2t.zarr")
```

Reach for the options below only when the default path is slow or a cache is
misbehaving.

### Director-aware URL (without PelicanFS)

Because OSDF is just HTTPS, you can read *without* PelicanFS by handing the
**director** URL straight to any HTTPS-aware reader — the director issues an
HTTP redirect to a cache:

```python
# Plain HTTPS via the director — no pelicanfs scheme, no cache/failover control.
ds = xr.open_zarr("https://osdf-director.osg-htc.org/ncar/gdex/d633000/e5.oper.an.sfc.zarr/e5.oper.an.sfc.2t.zarr")
```

This is handy for a quick one-off, but you lose PelicanFS features — cache
failover, `direct_reads`, and `preferred_caches` below. Prefer the `osdf:///`
scheme for real workflows.

### `direct_reads` — go straight to the origin

Bypass the cache layer entirely and read from the origin. Useful when you're
close to the origin, or when a cache is serving bad data. For a **Zarr** open the
option rides in `storage_options`:

```python
ds = xr.open_zarr(
    "osdf:///ncar/gdex/d633000/e5.oper.an.sfc.zarr/e5.oper.an.sfc.2t.zarr",
    storage_options={"direct_reads": True},
)
```

### `preferred_caches` — pin the caches you trust

Try specific caches first. Keep the `"+"` sentinel so the director's own caches
remain as a fallback (**without `"+"` there is no fallback** — a single bad or
mistyped host raises `NoAvailableSource`):

```python
ds = xr.open_zarr(
    "osdf:///ncar/gdex/d633000/e5.oper.an.sfc.zarr/e5.oper.an.sfc.2t.zarr",
    storage_options={"preferred_caches": ["https://a-good-cache.example.org:8443", "+"]},
)
```

### kerchunk references (virtual Zarr over NetCDF)

kerchunk exposes a pile of NetCDF files as one virtual Zarr store via a small
reference file, opened through the `osdf` **remote protocol**. Cache-control
options ride in `remote_options` (not `storage_options`) here:

```python
ds = xr.open_dataset(
    "https://data.gdex.ucar.edu/d633000/kerchunk/<era5-reference>.parq",  # confirm exact reference name
    engine="kerchunk",
    storage_options={
        "remote_protocol": "osdf",
        "remote_options": {"direct_reads": True},   # or {"preferred_caches": [...]}
    },
)
```

A complete, working kerchunk-over-OSDF example (JRA-3Q) lives in
[`jja_heatindex.ipynb`](../notebooks/jja_heatindex.ipynb); ERA5 references open
the same way.

## 6. Common errors and fixes

| Symptom | Likely cause | Fix |
|---|---|---|
| `FileNotFoundError` / nothing resolves | `osdf://path` — **two** slashes | use `osdf:///path` (three) |
| `NoAvailableSource` | no working cache — a pinned/mistyped host, or `preferred_caches` with no `"+"` fallback | check the host; add `"+"`; drop bad entries |
| `ReferenceNotReachable` / `ConnectionError` | too many concurrent range reads (kerchunk fan-out) overwhelm a cache | reduce concurrency (fewer Dask workers / lower `zarr` `async.concurrency`), retry, or `direct_reads` |
| `zlib: incorrect header check` / `ContentLengthError`, every retry | a **cache serving corrupt bytes** | `direct_reads=True` (origin) or pin a good cache via `preferred_caches` |
| kerchunk data won't materialize / silently re-reads | `.load()`/`.compute()` return lazy Dask on this stack | pull `.values` / `np.asarray(...)` to force true NumPy |
| `MergeError: conflicting values for 'utc_date'` | merging ERA5 surface stores with a differing scalar coord | sub-select variables before merge, or `xr.merge(..., compat="override")` |

## 7. Find your next notebook

- **By origin / platform / dataset:** browse the [Notebook Gallery](notebook_gallery.md)
  or search any tag with the book's search bar (`/`) — see the [Tag Index](tag_index.md).
- **A fuller ERA5 workflow:** [`eol_era5.ipynb`](../notebooks/eol_era5.ipynb) and
  the multi-dataset [`jja_heatindex.ipynb`](../notebooks/jja_heatindex.ipynb)
  (ERA5 + JRA-3Q, kerchunk, `direct_reads`).
- **Brand new, just want it to work:** [`simple_aws_example.ipynb`](../notebooks/simple_aws_example.ipynb).

## 8. Go deeper

- [PelicanFS documentation](https://docs.pelicanplatform.org/) and
  [repository](https://github.com/PelicanPlatform/pelicanfs) — the source of truth
  for options and behavior.
- [Project Pythia OSDF Cookbook](https://projectpythia.org/osdf-cookbook/) — the
  concept-first tutorial across multiple science domains.
- [GDEX examples](https://ncar.github.io/gdex-examples/) — more NCAR/GDEX workflows.
- [Contributing](../CONTRIBUTING.md) — add your own example.
