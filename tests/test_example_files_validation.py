import os
import pytest

HERE = os.path.dirname(__file__)
RESOURCES_DIR = os.path.abspath(os.path.join(HERE, "..", "example_files"))


def collect_example_files():
    """Return a list of XML files under the resources directory (recursive)."""
    if not os.path.isdir(RESOURCES_DIR):
        return []
    matches = []
    for root, dirs, files in os.walk(RESOURCES_DIR):
        for fn in files:
            matches.append(os.path.join(root, fn))
    assert len(matches) > 0, "No example files found in resources directory."
    return matches


EXAMPLE_FILES = collect_example_files()


@pytest.mark.parametrize("example_path", EXAMPLE_FILES)
def test_example_file_valid(schema, example_path):
    """Validate each example XML file against the schema."""
    assert schema.is_valid(example_path), (
        f"{example_path} is not valid: {schema.errors}"
    )


