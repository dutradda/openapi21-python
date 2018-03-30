from openapi21 import validate_spec_url


def test_retrocompatibility_petstore_separate():
    validate_spec_url(
        'OpenAPI-Specification-Official/examples/v2.0/yaml/'
        'petstore-separate/spec/swagger.yaml'
    )


def test_retrocompatibility_petstore():
    validate_spec_url(
        'OpenAPI-Specification-Official/examples/v2.0/yaml/petstore.yaml'
    )


def test_retrocompatibility_petstore_expanded():
    validate_spec_url(
        'OpenAPI-Specification-Official/examples/'
        'v2.0/yaml/petstore-expanded.yaml'
    )


def test_retrocompatibility_petstore_minimal():
    validate_spec_url(
        'OpenAPI-Specification-Official/examples/'
        'v2.0/yaml/petstore-minimal.yaml'
    )


def test_retrocompatibility_petstore_simple():
    validate_spec_url(
        'OpenAPI-Specification-Official/examples/'
        'v2.0/yaml/petstore-simple.yaml'
    )


def test_retrocompatibility_petstore_with_external_docs():
    validate_spec_url(
        'OpenAPI-Specification-Official/examples/'
        'v2.0/yaml/petstore-with-external-docs.yaml'
    )


def test_retrocompatibility_uber():
    validate_spec_url(
        'OpenAPI-Specification-Official/examples/v2.0/yaml/uber.yaml'
    )


def test_retrocompatibility_api_with_examples():
    validate_spec_url(
        'OpenAPI-Specification-Official/examples/'
        'v2.0/yaml/api-with-examples.yaml'
    )
