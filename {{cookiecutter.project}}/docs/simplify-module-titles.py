from pathlib import Path

# pylint: disable=invalid-name
def simplify_file_modules(f: Path):
    text = f.read_text()

    new_text = ""
    for line in text.splitlines():
        if line.endswith(" module"):
            line = line.rsplit(".", 1)[-1].replace(" module", "", 1)

        new_text += f"{line}\n"

    f.write_text(new_text)


if __name__ == "__main__":
    source_dir = Path(__file__).parent / "source"

    for file in source_dir.glob("*.rst"):
        if file.name in ("index.rst", "modules.rst"):
            continue

        simplify_file_modules(file)
