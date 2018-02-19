import os.path

import pytest
from jsonschema.exceptions import ValidationError
from openapi21 import OPENAPI21_PATH, validate_spec_url

TESTS_ROOT = os.path.dirname(os.path.realpath(__file__))


def test_validate_spec_url_with_invalid_base_path():
    with pytest.raises(ValueError) as exc_info:
        validate_spec_url(
            '',
            spec_url_base_path='..'
        )
    expected = ("The 'base_path' must be an absolute path",)
    assert exc_info.value.args == expected


def test_validate_spec_url_with_invalid_parameters_examples():
    with pytest.raises(ValidationError) as exc_info:
        validate_spec_url(
            '{}/fixtures/failing_specs/examples_error.json'.format(TESTS_ROOT)
        )
    expected = ("{'name': 'test', 'in': 'body', 'schema': {}, 'example': {}, "
                "'examples': {}} is not valid under any of the given schemas")
    assert exc_info.value.message == expected

