import pytest

from config import settings


def pytest_addoption(parser):
    parser.addoption(
        "--test-service-name", action="store", help="Test service name", required=False
    )


def pytest_configure(config):
    settings.validators.validate()
    config.option.test_service_name = settings.test_service_name


@pytest.fixture(scope="session")
def test_settings():
    return settings
