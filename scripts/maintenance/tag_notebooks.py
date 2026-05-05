#!/usr/bin/env python3
"""Apply faceted tags to every notebook in osdf-examples.

For each notebook:
1. Replace the first markdown cell with a YAML frontmatter block + H1 only.
2. Insert (or update) a second markdown cell with a visible "**Tags:**" line.

The visible tag line MUST be in a separate cell — MyST treats the title cell
as title metadata and strips trailing content.
"""
from __future__ import annotations
import json
import sys
import uuid
from pathlib import Path

REPO = Path("/Users/harshah/osdf_examples/.claude/worktrees/naughty-robinson-7a1fa6")

# (relative path) -> (title, tags)
NOTEBOOKS = {
    # GDEX / NCAR data origin (Casper)
    "notebooks/cesm_bias.ipynb": (
        "Bias-correct CESM2 LENS temperature data",
        ["origin:aws", "origin:ncar-data-origin", "platform:casper",
         "dataset:cesm", "dataset:era5", "task:bias-correction",
         "access:pelicanfs", "access:intake-esm", "level:intermediate"],
    ),
    "notebooks/cesm_gmst_ncar.ipynb": (
        "CESM2 LENS Global Mean Surface Temperature anomaly",
        ["origin:ncar-data-origin", "platform:casper",
         "dataset:cesm", "task:visualization",
         "access:pelicanfs", "access:intake-esm", "level:intermediate"],
    ),
    "notebooks/cesm_oceanheat.ipynb": (
        "CESM2 LENS surface ocean heat content",
        ["origin:ncar-data-origin", "platform:casper",
         "dataset:cesm", "task:visualization",
         "access:pelicanfs", "access:intake-esm", "level:intermediate"],
    ),
    "notebooks/conus404.ipynb": (
        "CONUS404 diagnostic plots",
        ["origin:ncar-data-origin", "platform:casper",
         "dataset:conus404", "task:visualization",
         "access:pelicanfs", "level:intermediate"],
    ),
    "notebooks/dart-cam6.ipynb": (
        "DART/CAM6 reanalysis diagnostics",
        ["origin:ncar-data-origin", "platform:casper",
         "dataset:dart", "task:visualization",
         "access:pelicanfs", "level:intermediate"],
    ),
    "notebooks/eol_era5.ipynb": (
        "ERA5 access via the EOL/NCAR origin",
        ["origin:ncar-data-origin", "platform:casper",
         "dataset:era5", "task:visualization",
         "access:pelicanfs", "level:intermediate"],
    ),
    "notebooks/era5_precip.ipynb": (
        "ERA5 precipitation diagnostics",
        ["origin:ncar-data-origin", "platform:casper",
         "dataset:era5", "task:visualization",
         "access:pelicanfs", "level:intermediate"],
    ),
    "notebooks/geocat_climatology.ipynb": (
        "Daily-temperature climatology with geocat-comp",
        ["origin:ncar-data-origin", "platform:casper",
         "dataset:era5", "task:climatology",
         "access:pelicanfs", "level:intermediate"],
    ),
    "notebooks/hadisst_elnino.ipynb": (
        "El Niño diagnostics from HadISST",
        ["origin:ncar-data-origin", "platform:casper",
         "dataset:hadisst", "task:visualization",
         "access:pelicanfs", "level:intermediate"],
    ),
    "notebooks/jja_heatindex.ipynb": (
        "JJA heat-index calculation",
        ["origin:ncar-data-origin", "platform:casper",
         "dataset:era5", "task:visualization",
         "access:pelicanfs", "level:intermediate"],
    ),
    "notebooks/jra_3q.ipynb": (
        "JRA-3Q reanalysis diagnostics",
        ["origin:ncar-data-origin", "platform:casper",
         "dataset:jra3q", "task:visualization",
         "access:pelicanfs", "level:intermediate"],
    ),
    "notebooks/na_cordex.ipynb": (
        "NA-CORDEX diagnostic plots",
        ["origin:ncar-data-origin", "platform:casper",
         "dataset:na-cordex", "task:visualization",
         "access:pelicanfs", "level:intermediate"],
    ),
    "notebooks/saag.ipynb": (
        "SAAG dataset diagnostics",
        ["origin:ncar-data-origin", "platform:casper",
         "dataset:saag", "task:visualization",
         "access:pelicanfs", "level:intermediate"],
    ),
    "notebooks/uxarray_test.ipynb": (
        "Unstructured-grid access via UXarray",
        ["origin:ncar-data-origin", "platform:casper",
         "task:visualization",
         "access:pelicanfs", "level:advanced"],
    ),
    # AWS Open Data
    "notebooks/cmip6_gmst_zarr.ipynb": (
        "Multi-model GMST from CMIP6 zarr (~27 GCMs)",
        ["origin:aws", "platform:casper",
         "dataset:cmip6", "task:visualization",
         "access:pelicanfs", "access:zarr", "level:intermediate"],
    ),
    "notebooks/cmip6_ecs.ipynb": (
        "Equilibrium Climate Sensitivity from CMIP6",
        ["origin:aws", "platform:casper",
         "dataset:cmip6", "task:ecs",
         "access:pelicanfs", "access:zarr", "level:advanced"],
    ),
    "notebooks/cmip6_bias_correction.ipynb": (
        "Bias-correct CMIP6 model output",
        ["origin:aws", "platform:casper",
         "dataset:cmip6", "task:bias-correction",
         "access:pelicanfs", "access:zarr", "level:intermediate"],
    ),
    "notebooks/cmip6_precipitation.ipynb": (
        "CMIP6 precipitation diagnostics",
        ["origin:aws", "platform:casper",
         "dataset:cmip6", "task:visualization",
         "access:pelicanfs", "access:zarr", "level:intermediate"],
    ),
    "notebooks/hrrr_aws.ipynb": (
        "Stream HRRR data from AWS",
        ["origin:aws", "platform:casper",
         "dataset:hrrr", "task:visualization",
         "access:pelicanfs", "access:zarr", "level:intermediate"],
    ),
    "notebooks/simple_aws_example.ipynb": (
        "A simple AWS Open Data example",
        ["origin:aws", "platform:laptop",
         "dataset:cmip6",
         "access:pelicanfs", "access:zarr", "level:beginner"],
    ),
    # ML
    "notebooks/ml_workflows/nino3.4_index.ipynb": (
        "Forecasting Nino 3.4 indices using regression",
        ["origin:ncar-data-origin", "platform:casper",
         "dataset:hadisst", "task:ml",
         "access:pelicanfs", "level:intermediate"],
    ),
    # Other compute platforms
    "notebooks/cesm_osdf_stampede3.ipynb": (
        "Bias-correction workflow on TACC Stampede3",
        ["origin:aws", "origin:ncar-data-origin", "platform:stampede3",
         "dataset:cesm", "dataset:era5", "task:bias-correction",
         "access:pelicanfs", "access:intake-esm", "level:advanced"],
    ),
    "notebooks/jetstream_intro.ipynb": (
        "Introduction to running on Jetstream2",
        ["platform:jetstream2",
         "access:pelicanfs", "level:beginner"],
    ),
    "notebooks/jetstream_cesm_oceanheat.ipynb": (
        "Ocean-heat workflow on Jetstream2",
        ["origin:ncar-data-origin", "platform:jetstream2",
         "dataset:cesm", "task:visualization",
         "access:pelicanfs", "access:intake-esm", "level:intermediate"],
    ),
    "notebooks/jetstream_cmip6_gmst.ipynb": (
        "CMIP6 GMST on Jetstream2",
        ["origin:aws", "platform:jetstream2",
         "dataset:cmip6", "task:visualization",
         "access:pelicanfs", "access:zarr", "level:intermediate"],
    ),
    # NDC / benchmarks
    "notebooks/ndc_workflows/aws_benchmark.ipynb": (
        "Benchmark CESM2 LENS access from AWS origin",
        ["origin:aws", "platform:casper",
         "dataset:cesm", "task:benchmark",
         "access:pelicanfs", "access:zarr", "level:intermediate"],
    ),
    "notebooks/ndc_workflows/ncar_benchmark.ipynb": (
        "Benchmark NCAR-origin access (DART)",
        ["origin:ncar-data-origin", "platform:casper",
         "dataset:dart", "task:benchmark",
         "access:pelicanfs", "level:intermediate"],
    ),
    "notebooks/ndc_workflows/ncar_benchmark_simple.ipynb": (
        "Simplified NCAR-origin benchmark",
        ["origin:ncar-data-origin", "platform:laptop",
         "task:benchmark",
         "access:pelicanfs", "level:beginner"],
    ),
    "notebooks/ndc_workflows/ncar_benchmark_ap40.ipynb": (
        "NCAR-origin benchmark via OSPool AP40",
        ["origin:ncar-data-origin", "platform:ospool",
         "task:benchmark",
         "access:pelicanfs", "level:advanced"],
    ),
    "notebooks/ndc_workflows/envistor_test_ap40.ipynb": (
        "Envistor test via OSPool AP40",
        ["platform:ospool", "task:benchmark",
         "access:pelicanfs", "level:advanced"],
    ),
    "notebooks/ndc_workflows/sonar_ai.ipynb": (
        "Plot echograms from NOAA SONAR data",
        ["origin:aws", "platform:laptop",
         "dataset:sonar", "task:visualization",
         "access:pelicanfs", "level:intermediate"],
    ),
    "notebooks/ndc_workflows/pycogss_spectral_change.ipynb": (
        "Spectral change from Sentinel-2 imagery",
        ["origin:aws", "platform:laptop",
         "dataset:sentinel2", "task:visualization",
         "access:pelicanfs", "level:intermediate"],
    ),
}


def make_title_cell(title: str, tags: list[str], heading: str) -> dict:
    """Build a markdown cell with frontmatter + H1."""
    src_lines = ["---\n", f"title: {title}\n", "author: Harsha R. Hampapura\n", "tags:\n"]
    for t in tags:
        src_lines.append(f"  - {t}\n")
    src_lines.append("---\n")
    src_lines.append(f"# {heading}")
    return {
        "cell_type": "markdown",
        "id": str(uuid.uuid4())[:8],
        "metadata": {},
        "source": src_lines,
    }


def make_tag_cell(tags: list[str]) -> dict:
    """Build the visible tag line cell as inline HTML span elements.

    Renders each tag as `<span class="tag tag-origin">origin:aws</span>` so
    it can be styled as a pill badge by `custom.css`. Pandoc-style
    `[text]{.class}` attributes are not parsed by MyST/jupyter-book v2.0,
    but inline HTML is passed through unchanged.
    """
    chips = []
    for t in tags:
        facet = t.split(":", 1)[0]
        chips.append(f'<span class="tag tag-{facet}">{t}</span>')
    inline = " ".join(chips)
    return {
        "cell_type": "markdown",
        "id": str(uuid.uuid4())[:8],
        "metadata": {},
        "source": [inline],
    }


def find_existing_h1(nb: dict) -> str | None:
    """Find the first H1 anywhere in the notebook to use as visible heading."""
    for cell in nb["cells"]:
        if cell["cell_type"] != "markdown":
            continue
        src = "".join(cell["source"]) if isinstance(cell["source"], list) else cell["source"]
        for line in src.splitlines():
            line = line.strip()
            if line.startswith("# ") and not line.startswith("##"):
                return line[2:].strip()
    return None


TAG_CELL_MARKERS = (
    "**Tags:**",            # original code-span format
    "[origin:",             # bracketed-attr format (MyST didn't parse)
    "[platform:",
    '<span class="tag',     # current HTML-span format
)


def is_tag_cell(cell: dict) -> bool:
    """Detect a previously-generated tag-line cell in any past format."""
    if cell["cell_type"] != "markdown":
        return False
    src = "".join(cell["source"]) if isinstance(cell["source"], list) else cell["source"]
    s = src.strip()
    return any(s.startswith(m) for m in TAG_CELL_MARKERS)


def process(rel_path: str, title: str, tags: list[str]) -> str:
    path = REPO / rel_path
    nb = json.loads(path.read_text())

    # Pick a heading: prefer existing H1 in notebook (so we don't change the
    # visible title text), else fall back to title from the mapping.
    heading = find_existing_h1(nb) or title

    new_first = make_title_cell(title, tags, heading)
    new_second = make_tag_cell(tags)

    # Drop any prior tag-line cells (in any past format) so this script is
    # idempotent across format migrations.
    nb["cells"] = [c for i, c in enumerate(nb["cells"]) if not (i > 0 and is_tag_cell(c))]

    nb["cells"][0] = new_first
    nb["cells"].insert(1, new_second)

    path.write_text(json.dumps(nb, indent=1, ensure_ascii=False))
    return "updated"


def main():
    counts = {"updated": 0, "missing": 0}
    for rel_path, (title, tags) in NOTEBOOKS.items():
        full = REPO / rel_path
        if not full.exists():
            print(f"MISSING: {rel_path}")
            counts["missing"] += 1
            continue
        action = process(rel_path, title, tags)
        counts[action] += 1
        print(f"{action}: {rel_path}")
    print()
    print(f"updated: {counts['updated']}")
    print(f"missing: {counts['missing']}")


if __name__ == "__main__":
    main()
