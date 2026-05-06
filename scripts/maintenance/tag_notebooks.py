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
#
# Origin tag values reflect the OSDF namespace each notebook actually streams
# from:
#   * origin:ncar-posix         -> osdf:///ncar/gdex/...  (POSIX storage; some
#                                                          older notebooks use
#                                                          osdf:///ncar/rda/...
#                                                          which is the same
#                                                          origin under its
#                                                          previous name)
#   * origin:ncar-object-store  -> osdf:///ncar-gdex/...  (NCAR object storage,
#                                                          currently called
#                                                          Boreas)
#   * origin:aws                -> osdf:///aws-opendata/...
NOTEBOOKS = {
    # NCAR HPC workflows on Casper
    "notebooks/cesm_bias.ipynb": (
        "Bias-correct CESM2 LENS temperature data",
        ["origin:ncar-posix", "origin:ncar-object-store", "platform:casper",
         "dataset:cesm", "dataset:era5", "task:bias-correction",
         "level:intermediate"],
    ),
    "notebooks/cesm_gmst_ncar.ipynb": (
        "CESM2 LENS Global Mean Surface Temperature anomaly",
        ["origin:ncar-posix", "platform:casper",
         "dataset:cesm", "task:visualization",
         "level:intermediate"],
    ),
    "notebooks/cesm_oceanheat.ipynb": (
        "CESM2 LENS surface ocean heat content",
        ["origin:ncar-posix", "platform:casper",
         "dataset:cesm", "task:visualization",
         "level:intermediate"],
    ),
    "notebooks/conus404.ipynb": (
        "CONUS404 diagnostic plots",
        ["origin:ncar-posix", "platform:casper",
         "dataset:conus404", "task:visualization",
         "level:intermediate"],
    ),
    "notebooks/dart-cam6.ipynb": (
        "DART/CAM6 reanalysis diagnostics",
        ["origin:ncar-posix", "origin:ncar-object-store", "platform:casper",
         "dataset:dart", "task:visualization",
         "level:intermediate"],
    ),
    "notebooks/eol_era5.ipynb": (
        "ERA5 access via the EOL/NCAR origin",
        ["origin:ncar-posix", "platform:casper",
         "dataset:era5", "task:visualization",
         "level:intermediate"],
    ),
    "notebooks/era5_precip.ipynb": (
        "ERA5 precipitation diagnostics",
        ["origin:ncar-posix", "platform:casper",
         "dataset:era5", "task:visualization",
         "level:intermediate"],
    ),
    "notebooks/geocat_climatology.ipynb": (
        "Daily-temperature climatology with geocat-comp",
        ["origin:ncar-posix", "platform:casper",
         "dataset:era5", "task:climatology",
         "level:intermediate"],
    ),
    "notebooks/hadisst_elnino.ipynb": (
        "El Niño diagnostics from HadISST",
        ["origin:ncar-posix", "platform:casper",
         "dataset:hadisst", "task:visualization",
         "level:intermediate"],
    ),
    "notebooks/jja_heatindex.ipynb": (
        "JJA heat-index calculation",
        ["origin:ncar-posix", "platform:casper",
         "dataset:era5", "task:visualization",
         "level:intermediate"],
    ),
    "notebooks/jra_3q.ipynb": (
        "JRA-3Q reanalysis diagnostics",
        ["origin:ncar-posix", "platform:casper",
         "dataset:jra3q", "task:visualization",
         "level:intermediate"],
    ),
    "notebooks/na_cordex.ipynb": (
        "NA-CORDEX diagnostic plots",
        ["origin:ncar-posix", "origin:ncar-object-store", "platform:casper",
         "dataset:na-cordex", "task:visualization",
         "level:intermediate"],
    ),
    "notebooks/saag.ipynb": (
        "SAAG dataset diagnostics",
        ["origin:ncar-posix", "platform:casper",
         "dataset:saag", "task:visualization",
         "level:intermediate"],
    ),
    "notebooks/uxarray_test.ipynb": (
        "Unstructured-grid access via UXarray",
        ["origin:ncar-posix", "platform:casper",
         "task:visualization",
         "level:advanced"],
    ),
    # AWS Open Data
    "notebooks/cmip6_gmst_zarr.ipynb": (
        "Multi-model GMST from CMIP6 zarr (~27 GCMs)",
        ["origin:aws", "origin:ncar-posix", "origin:ncar-object-store",
         "platform:casper",
         "dataset:cmip6", "task:visualization",
         "level:intermediate"],
    ),
    "notebooks/cmip6_ecs.ipynb": (
        "Equilibrium Climate Sensitivity from CMIP6",
        ["origin:aws", "platform:casper",
         "dataset:cmip6", "task:ecs",
         "level:advanced"],
    ),
    "notebooks/cmip6_bias_correction.ipynb": (
        "Bias-correct CMIP6 model output",
        ["origin:aws", "platform:casper",
         "dataset:cmip6", "task:bias-correction",
         "level:intermediate"],
    ),
    "notebooks/cmip6_precipitation.ipynb": (
        "CMIP6 precipitation diagnostics",
        ["origin:aws", "platform:casper",
         "dataset:cmip6", "task:visualization",
         "level:intermediate"],
    ),
    "notebooks/hrrr_aws.ipynb": (
        "Stream HRRR data from AWS",
        ["origin:aws", "platform:casper",
         "dataset:hrrr", "task:visualization",
         "level:intermediate"],
    ),
    "notebooks/simple_aws_example.ipynb": (
        "A simple AWS Open Data example",
        ["origin:aws", "platform:laptop",
         "dataset:cmip6",
         "level:beginner"],
    ),
    # ML
    "notebooks/ml_workflows/nino3.4_index.ipynb": (
        "Forecasting Nino 3.4 indices using regression",
        ["origin:ncar-posix", "platform:casper",
         "dataset:hadisst", "task:ml",
         "level:intermediate"],
    ),
    # Other compute platforms
    "notebooks/cesm_osdf_stampede3.ipynb": (
        "Bias-correction workflow on TACC Stampede3",
        ["origin:ncar-posix", "origin:ncar-object-store", "platform:stampede3",
         "dataset:cesm", "dataset:era5", "task:bias-correction",
         "level:advanced"],
    ),
    "notebooks/jetstream_intro.ipynb": (
        "Introduction to running on Jetstream2",
        ["platform:jetstream2",
         "level:beginner"],
    ),
    "notebooks/jetstream_cesm_oceanheat.ipynb": (
        "Ocean-heat workflow on Jetstream2",
        ["origin:ncar-posix", "platform:jetstream2",
         "dataset:cesm", "task:visualization",
         "level:intermediate"],
    ),
    "notebooks/jetstream_cmip6_gmst.ipynb": (
        "CMIP6 GMST on Jetstream2",
        ["origin:aws", "origin:ncar-posix", "platform:jetstream2",
         "dataset:cmip6", "task:visualization",
         "level:intermediate"],
    ),
    # NDC / benchmarks
    "notebooks/ndc_workflows/aws_benchmark.ipynb": (
        "Benchmark CESM2 LENS access from AWS origin",
        ["origin:aws", "platform:casper",
         "dataset:cesm", "task:benchmark",
         "level:intermediate"],
    ),
    "notebooks/ndc_workflows/ncar_benchmark.ipynb": (
        "Benchmark NCAR-origin access (DART)",
        ["origin:aws", "origin:ncar-posix", "platform:casper",
         "dataset:dart", "task:benchmark",
         "level:intermediate"],
    ),
    "notebooks/ndc_workflows/ncar_benchmark_simple.ipynb": (
        "Simplified NCAR-origin benchmark",
        ["origin:ncar-posix", "platform:laptop",
         "task:benchmark",
         "level:beginner"],
    ),
    "notebooks/ndc_workflows/ncar_benchmark_ap40.ipynb": (
        "NCAR-origin benchmark via OSPool AP40",
        ["origin:ncar-posix", "platform:ospool",
         "task:benchmark",
         "level:advanced"],
    ),
    "notebooks/ndc_workflows/envistor_test_ap40.ipynb": (
        "Envistor test via OSPool AP40",
        ["platform:ospool", "task:benchmark",
         "level:advanced"],
    ),
    "notebooks/ndc_workflows/sonar_ai.ipynb": (
        "Plot echograms from NOAA SONAR data",
        ["origin:aws", "platform:laptop",
         "dataset:sonar", "task:visualization",
         "level:intermediate"],
    ),
    "notebooks/ndc_workflows/pycogss_spectral_change.ipynb": (
        "Spectral change from Sentinel-2 imagery",
        ["origin:aws", "platform:laptop",
         "dataset:sentinel2", "task:visualization",
         "level:intermediate"],
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


FACET_ORDER = ["origin", "platform", "dataset", "task", "level"]
FACET_TITLES = {
    "origin":   "Data origin",
    "platform": "Compute platform (tested on)",
    "dataset":  "Dataset",
    "task":     "Task",
    "level":    "Difficulty level",
}


def tag_anchor(tag: str) -> str:
    """Anchor id used on tag-index for a given tag (e.g. tag-origin-aws)."""
    facet, value = tag.split(":", 1)
    return f"tag-{facet}-{value}"


def render_chip(tag: str) -> str:
    """Render one tag as a colored, clickable pill linking to the index.

    Uses inline HTML because MyST/jupyter-book v2.0 doesn't parse
    Pandoc-style `[text]{.class}` attributes, but passes raw HTML through.
    """
    facet = tag.split(":", 1)[0]
    return (
        f'<a class="tag-link" href="tag-index#{tag_anchor(tag)}">'
        f'<span class="tag tag-{facet}">{tag}</span>'
        f'</a>'
    )


def make_tag_cell(tags: list[str]) -> dict:
    """Build the visible tag-line cell — a row of clickable colored pills."""
    inline = " ".join(render_chip(t) for t in tags)
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
    "**Tags:**",                  # original code-span format
    "[origin:",                   # bracketed-attr format (MyST didn't parse)
    "[platform:",
    '<span class="tag',           # earlier HTML-span format (no anchor)
    '<a class="tag-link"',        # current anchor-wrapped HTML-span format
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


def write_tag_index() -> None:
    """Write docs/tag_index.md — the inverse map (tag → notebooks)."""
    # Build {facet: {value: [(rel_path, title), ...]}}
    inverse: dict[str, dict[str, list[tuple[str, str]]]] = {f: {} for f in FACET_ORDER}
    for rel_path, (title, tags) in NOTEBOOKS.items():
        if not (REPO / rel_path).exists():
            continue
        for tag in tags:
            facet, value = tag.split(":", 1)
            inverse.setdefault(facet, {}).setdefault(value, []).append((rel_path, title))

    out: list[str] = [
        "---",
        "title: Tag Index",
        "description: Find notebooks by tag — every tag pill on the site links here.",
        "---",
        "",
        "# Tag Index",
        "",
        "Every colored pill on a notebook page or in the gallery is a link to a",
        "section on this page. Click a tag anywhere on the site to jump straight",
        "to the list of notebooks that share it.",
        "",
        "You can also reach this index by typing a tag value (e.g. `platform:casper`)",
        "into the search bar at the top of the page.",
        "",
    ]

    for facet in FACET_ORDER:
        values = inverse.get(facet, {})
        if not values:
            continue
        out.append(f"## {FACET_TITLES[facet]}")
        out.append("")
        for value in sorted(values):
            anchor = f"tag-{facet}-{value}"
            tag = f"{facet}:{value}"
            chip = (
                f'<span class="tag tag-{facet}">{tag}</span>'
            )
            out.append(f"({anchor})=")
            out.append(f"### {chip}")
            out.append("")
            for rel_path, title in sorted(values[value], key=lambda x: x[1].lower()):
                out.append(f"- [`{Path(rel_path).name}`](../{rel_path}) — {title}")
            out.append("")

    (REPO / "docs" / "tag_index.md").write_text("\n".join(out) + "\n")
    print(f"wrote docs/tag_index.md ({sum(len(v) for v in inverse.values())} unique tag values)")


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
    write_tag_index()
    print()
    print(f"updated: {counts['updated']}")
    print(f"missing: {counts['missing']}")


if __name__ == "__main__":
    main()
