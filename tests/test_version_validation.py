import lxml.etree as ET
import os
import xmlschema
import pytest

HERE = os.path.dirname(__file__)
XSD_PATH = os.path.join(HERE, "..", "dictionary.xsd")

VALID_VERSIONS = [
    "3.0",
    "3.1",
    "3.2",
    "3.12",
    "3.1.2",
]

INVALID_VERSIONS = [
    "3",  # minor required
    "2.9",  # lower major version not allowed
    "4.0",  # higher major version not allowed
    "3.0-alpha",  # pre-release not allowed
    "3.a",  # non-numeric minor
]


@pytest.fixture(scope='module')
def schema():
    return xmlschema.XMLSchema(os.path.join(os.path.dirname(HERE), 'dictionary.xsd'))


def make_xml(version_text):
    return f'''<?xml version="1.0"?>
<IngeniaDictionary>
  <Header>
    <Version>{version_text}</Version>
    <DefaultLanguage>en</DefaultLanguage>
  </Header>
  <Body>
    <Categories>
      <Category id="CAT1">
        <Labels>
          <Label lang="en">cat</Label>
        </Labels>
      </Category>
    </Categories>
    <Devices>
    </Devices>
  </Body>
  <DriveImage></DriveImage>
</IngeniaDictionary>'''


@pytest.mark.parametrize('v', VALID_VERSIONS)
def test_valid_versions(schema, v):
    xml = make_xml(v)
    assert schema.is_valid(xml), f'{v} should be valid: {schema.errors}'


@pytest.mark.parametrize('v', INVALID_VERSIONS)
def test_invalid_versions(schema, v):
    xml = make_xml(v)
    assert not schema.is_valid(xml), f'{v} should be invalid: {schema.errors}'
