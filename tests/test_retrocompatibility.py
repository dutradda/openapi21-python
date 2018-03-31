from openapi21 import validate_spec_url


def test_retrocompatibility_petstore_separate():
    assert validate_spec_url(
        'OpenAPI-Specification-Official/examples/v2.0/yaml/'
        'petstore-separate/spec/swagger.yaml'
    )


def test_retrocompatibility_petstore():
    assert validate_spec_url(
        'OpenAPI-Specification-Official/examples/v2.0/yaml/petstore.yaml'
    )


def test_retrocompatibility_petstore_expanded():
    assert validate_spec_url(
        'OpenAPI-Specification-Official/examples/'
        'v2.0/yaml/petstore-expanded.yaml'
    )


def test_retrocompatibility_petstore_minimal():
    assert validate_spec_url(
        'OpenAPI-Specification-Official/examples/'
        'v2.0/yaml/petstore-minimal.yaml'
    )


def test_retrocompatibility_petstore_simple():
    assert validate_spec_url(
        'OpenAPI-Specification-Official/examples/'
        'v2.0/yaml/petstore-simple.yaml'
    )


def test_retrocompatibility_petstore_with_external_docs():
    assert validate_spec_url(
        'OpenAPI-Specification-Official/examples/'
        'v2.0/yaml/petstore-with-external-docs.yaml'
    )


def test_retrocompatibility_uber():
    assert validate_spec_url(
        'OpenAPI-Specification-Official/examples/v2.0/yaml/uber.yaml'
    )


def test_retrocompatibility_api_with_examples():
    assert validate_spec_url(
        'OpenAPI-Specification-Official/examples/'
        'v2.0/yaml/api-with-examples.yaml'
    )
