import os.path

from openapi21 import validate_spec_url

root_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..')


def test_validate_spec_url():
    validate_spec_url(
        'file:{}/OpenAPI-Specification-2.1/example/swagger.json'.format(root_path),
        'file:{}/OpenAPI-Specification-2.1/schema.json'.format(root_path)
    )
