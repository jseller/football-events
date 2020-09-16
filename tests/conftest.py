
import os

import pytest

from football.app import create_app
from football.config import TestConfig


def pytest_logger_config(logger_config):
    logger_config.add_loggers(['test'], stdout_level='info')
    logger_config.set_log_option_default('test')


@pytest.fixture(scope='module')
def app():
    """An application for the tests."""
    os.environ['FLASK_ENV'] = 'testing'
    _app = create_app(TestConfig)
    ctx = _app.test_request_context()
    ctx.push()
    yield _app
    ctx.pop()
