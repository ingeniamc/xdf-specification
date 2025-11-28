import os
import xmlschema
import pytest

HERE = os.path.dirname(__file__)
XSD_PATH = os.path.abspath(os.path.join(HERE, '..', 'dictionary.xsd'))


@pytest.fixture(scope='session')
def schema():
    """Provide a shared XMLSchema instance for tests."""
    return xmlschema.XMLSchema(XSD_PATH)

