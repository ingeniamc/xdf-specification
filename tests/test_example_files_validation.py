from pathlib import Path
import pytest

from tests.conftest import EXAMPLE_FILES_DIR


def collect_example_files():
    """Return a list of XML files under the resources directory (recursive)."""
    example_dir = Path(EXAMPLE_FILES_DIR)
    matches = [str(p) for p in example_dir.rglob('*') if p.is_file()]
    assert len(matches) > 0, "No example files found in resources directory."
    return matches


EXAMPLE_FILES = collect_example_files()


@pytest.mark.parametrize("example_path", EXAMPLE_FILES)
def test_example_file_valid(schema, example_path):
    """Validate each example XML file against the schema."""
    assert schema.is_valid(example_path), (
        f"{example_path} is not valid: {schema.errors}"
    )
