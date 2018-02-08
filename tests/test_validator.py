import os.path

from openapi21 import OPENAPI21_PATH, validate_spec_url


def test_validate_spec_url():
    validate_spec_url(
        'file:{}/example/swagger.json'.format(OPENAPI21_PATH)
    )
