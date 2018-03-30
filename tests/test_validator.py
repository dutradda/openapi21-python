import os.path

from openapi21 import OPENAPI21_PATH, validate_spec_url

TESTS_ROOT = os.path.dirname(os.path.realpath(__file__))


def test_validate_spec_url_scheme():
    validate_spec_url(
        'file:{}/fixtures/validation_spec/swagger.json'.format(TESTS_ROOT)
    )


def test_validate_spec_url_absolute():
    validate_spec_url(
        '{}/fixtures/validation_spec/swagger.json'.format(TESTS_ROOT)
    )


def test_validate_spec_url_absolute_with_schema_url():
    validate_spec_url(
        'file:{}/fixtures/validation_spec/swagger.json'.format(TESTS_ROOT),
        schema_url='file:{}/spec/schema.json'.format(OPENAPI21_PATH)
    )


def test_validate_spec_url_relative():
    validate_spec_url(
        'OpenAPI-Specification-2.1/example/swagger.json'
    )


def test_validate_spec_url_relative_with_schema_url():
    validate_spec_url(
        'OpenAPI-Specification-2.1/example/swagger.json',
        schema_url='file:{}/spec/schema.json'.format(OPENAPI21_PATH)
    )


def test_validate_spec_url_with_base_path():
    validate_spec_url(
        '../OpenAPI-Specification-2.1/example/swagger.json',
        spec_url_base_path=TESTS_ROOT
    )
