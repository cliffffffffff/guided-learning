#!/usr/bin/env python3
"""Build a small, self-contained skill ZIP using only Python's standard library."""

import argparse
from pathlib import Path
import sys
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo


ROOT = Path(__file__).resolve().parents[1]
# Use the installation guide inside the ZIP so README links do not need intro images.
FILES = {
    "SKILL.md": "SKILL.md",
    "references/teaching-examples.md": "references/teaching-examples.md",
    "references/design-basis.md": "references/design-basis.md",
    "references/fable-writing/SKILL.md": "references/fable-writing/SKILL.md",
    "LICENSE": "LICENSE",
    "agents/openai.yaml": "agents/openai.yaml",
    "assets/icon.svg": "assets/icon.svg",
    "README.md": "INSTALL.md",
}


def build_package(output: Path) -> None:
    payloads = {}
    for archive_name, source_name in FILES.items():
        source = ROOT / source_name
        data = source.read_bytes()
        data.decode("utf-8")
        payloads[archive_name] = data

    if output.exists():
        raise ValueError(f"Output already exists: {output}. Choose a new --output path.")
    if output in {(ROOT / source).resolve() for source in FILES.values()}:
        raise ValueError("Output cannot replace a source file.")
    output.parent.mkdir(parents=True, exist_ok=True)
    # Exclusive creation preserves existing downloads or release artifacts.
    with output.open("xb") as stream:
        with ZipFile(stream, "w", compression=ZIP_DEFLATED) as archive:
            for name, data in sorted(payloads.items()):
                entry = ZipInfo(name, date_time=(2026, 1, 1, 0, 0, 0))
                entry.compress_type = ZIP_DEFLATED
                entry.create_system = 3
                entry.external_attr = 0o100644 << 16
                archive.writestr(entry, data)

    with ZipFile(output) as archive:
        if archive.testzip() is not None or set(archive.namelist()) != set(FILES):
            raise ValueError("ZIP integrity or file manifest check failed.")
        for name, expected in payloads.items():
            if archive.read(name) != expected:
                raise ValueError(f"ZIP content differs from source: {name}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output", type=Path, default=ROOT / "dist" / "guided-learning.zip",
        help="New ZIP path (default: dist/guided-learning.zip; existing files are kept).",
    )
    args = parser.parse_args()
    output = args.output.resolve()
    try:
        build_package(output)
    except (OSError, UnicodeError, ValueError) as error:
        print(f"Packaging failed: {error}", file=sys.stderr)
        return 1
    print(f"Created {output} ({output.stat().st_size:,} bytes, {len(FILES)} files)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
