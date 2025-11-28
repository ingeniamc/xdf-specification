import pytest


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


def make_xml(version_text):
    return f"""<?xml version="1.0"?>
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
</IngeniaDictionary>"""


@pytest.mark.parametrize("version", VALID_VERSIONS)
def test_valid_versions(schema, version: str):
    xml = make_xml(version)
    assert schema.is_valid(xml), f"{version} should be valid: {schema.errors}"


@pytest.mark.parametrize("version", INVALID_VERSIONS)
def test_invalid_versions(schema, version: str):
    xml = make_xml(version)
    assert not schema.is_valid(xml), f"{version} should be invalid: {schema.errors}"
