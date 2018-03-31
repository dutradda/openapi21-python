import json
import os.path

from swagger_spec_validator3.validator20 import validate_spec as ssv_validate_spec

from openapi21 import validate_spec_url

TESTS_ROOT = os.path.dirname(os.path.realpath(__file__))


def test_resolver_derefered_with_store_spec():
    resolver = validate_spec_url(
        'OpenAPI-Specification-2.1/example/swagger.json'
    )
    spec_derefered_expected = json.load(
        open(os.path.join(TESTS_ROOT, 'fixtures/derefed_specs/store_example.json'))
    )
    assert resolver.spec_derefered == spec_derefered_expected


def test_resolver_derefered_with_validation_spec():
    resolver = validate_spec_url(
        'tests/fixtures/validation_spec/swagger.json'
    )
    spec_derefered_expected = json.load(
        open(os.path.join(TESTS_ROOT, 'fixtures/derefed_specs/validation_spec.json'))
    )
    assert resolver.spec_derefered == spec_derefered_expected


def test_resolver_derefered_with_validation_petstore_separate_spec():
    resolver = validate_spec_url(
        'OpenAPI-Specification-Official/examples/v2.0/yaml/'
        'petstore-separate/spec/swagger.yaml'
    )
    ssv_validate_spec(resolver.spec_derefered)
    spec_derefered_expected = json.load(
        open(os.path.join(TESTS_ROOT, 'fixtures/derefed_specs/petstore-separate.json'))
    )
    assert resolver.spec_derefered == spec_derefered_expected


def test_resolver_derefered_with_validation_petstore_spec():
    resolver = validate_spec_url(
        'OpenAPI-Specification-Official/examples/v2.0/yaml/petstore.yaml'
    )
    ssv_validate_spec(resolver.spec_derefered)
    spec_derefered_expected = json.load(
        open(os.path.join(TESTS_ROOT, 'fixtures/derefed_specs/petstore.json'))
    )
    assert resolver.spec_derefered == spec_derefered_expected


def test_resolver_derefered_with_validation_petstore_expanded_spec():
    resolver = validate_spec_url(
        'OpenAPI-Specification-Official/examples/'
        'v2.0/yaml/petstore-expanded.yaml'
    )
    ssv_validate_spec(resolver.spec_derefered)
    spec_derefered_expected = json.load(
        open(os.path.join(TESTS_ROOT, 'fixtures/derefed_specs/petstore-expanded.json'))
    )
    assert resolver.spec_derefered == spec_derefered_expected


def test_resolver_derefered_with_validation_petstore_minimal_spec():
    resolver = validate_spec_url(
        'OpenAPI-Specification-Official/examples/'
        'v2.0/yaml/petstore-minimal.yaml'
    )
    ssv_validate_spec(resolver.spec_derefered)
    spec_derefered_expected = json.load(
        open(os.path.join(TESTS_ROOT, 'fixtures/derefed_specs/petstore-minimal.json'))
    )
    assert resolver.spec_derefered == spec_derefered_expected


def test_resolver_derefered_with_validation_petstore_simple_spec():
    resolver = validate_spec_url(
        'OpenAPI-Specification-Official/examples/'
        'v2.0/yaml/petstore-simple.yaml'
    )
    ssv_validate_spec(resolver.spec_derefered)
    spec_derefered_expected = json.load(
        open(os.path.join(TESTS_ROOT, 'fixtures/derefed_specs/petstore-simple.json'))
    )
    assert resolver.spec_derefered == spec_derefered_expected


def test_resolver_derefered_with_validation_petstore_with_external_docs_spec():
    resolver = validate_spec_url(
        'OpenAPI-Specification-Official/examples/'
        'v2.0/yaml/petstore-with-external-docs.yaml'
    )
    ssv_validate_spec(resolver.spec_derefered)
    spec_derefered_expected = json.load(
        open(os.path.join(TESTS_ROOT, 'fixtures/derefed_specs/petstore-with-external-docs.json'))
    )
    assert resolver.spec_derefered == spec_derefered_expected


def test_resolver_derefered_with_validation_uber_spec():
    resolver = validate_spec_url(
        'OpenAPI-Specification-Official/examples/v2.0/yaml/uber.yaml'
    )
    ssv_validate_spec(resolver.spec_derefered)
    spec_derefered_expected = json.load(
        open(os.path.join(TESTS_ROOT, 'fixtures/derefed_specs/uber.json'))
    )
    assert resolver.spec_derefered == spec_derefered_expected


def test_resolver_derefered_with_validation_api_with_examples_spec():
    resolver = validate_spec_url(
        'OpenAPI-Specification-Official/examples/'
        'v2.0/yaml/api-with-examples.yaml'
    )
    ssv_validate_spec(resolver.spec_derefered)
    spec_derefered_expected = json.load(
        open(os.path.join(TESTS_ROOT, 'fixtures/derefed_specs/api-with-examples.json'))
    )
    assert resolver.spec_derefered == spec_derefered_expected
