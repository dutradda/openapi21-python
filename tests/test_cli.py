import os.path

import pytest

TESTS_ROOT = os.path.dirname(os.path.realpath(__file__))


@pytest.fixture
def args_mock(monkeypatch):
    argv = []
    monkeypatch.setattr('sys.argv', argv)
    return argv


def test_success_validation(args_mock):
    args_mock.extend([
        'openapi21-cli',
        'file:{}/fixtures/validation_spec/swagger.json'.format(TESTS_ROOT)
    ])
    from openapi21 import cli
    assert cli.main() == 0


def test_success_validation_two_specs(args_mock):
    args_mock.extend([
        'openapi21-cli',
        'file:{}/fixtures/validation_spec/swagger.json'.format(TESTS_ROOT),
        'OpenAPI-Specification-2.1/example/swagger.json'
    ])
    from openapi21 import cli
    assert cli.main() == 0


def test_success_validation_silent(args_mock):
    args_mock.extend([
        'openapi21-cli',
        'file:{}/fixtures/validation_spec/swagger.json'.format(TESTS_ROOT),
        '-t'
    ])
    from openapi21 import cli
    assert cli.main() == 0


def test_fail_validation(args_mock):
    args_mock.extend([
        'openapi21-cli',
        'file:{}/fixtures/failing_specs/examples_error.json'
        .format(TESTS_ROOT)
    ])
    from openapi21 import cli
    assert cli.main() == 1


def test_fail_validation_show_all(args_mock):
    args_mock.extend([
        'openapi21-cli',
        'file:{}/fixtures/failing_specs/examples_error.json'
        .format(TESTS_ROOT), '-a'
    ])
    from openapi21 import cli
    assert cli.main() == 1


def test_fail_validation_stop_on_fail(args_mock):
    args_mock.extend([
        'openapi21-cli',
        'file:{}/fixtures/failing_specs/examples_error.json'
        .format(TESTS_ROOT), '-f'
    ])
    from openapi21 import cli
    assert cli.main() == 1
