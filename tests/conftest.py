from pathlib import Path
import xmlschema
import pytest


HERE = Path(__file__).parent
REPO_PATH = HERE / '..'
XSD_PATH = REPO_PATH / 'dictionary.xsd'
EXAMPLE_FILES_DIR = REPO_PATH / 'example_files'


@pytest.fixture(scope='session')
def schema():
    """Provide a shared XMLSchema instance for tests."""
    return xmlschema.XMLSchema(XSD_PATH)

