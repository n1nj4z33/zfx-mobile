from typing import Callable, cast

import pytest
from appium.webdriver.appium_service import AppiumService

from config import settings


def pytest_addoption(parser):
    parser.addoption(
        "--test-service-name", action="store", help="Test service name", required=False
    )


def pytest_bdd_apply_tag(tag: str, function) -> Callable:
    list_splitted_strs = tag.split("(")
    if len(list_splitted_strs) > 1:
        name = list_splitted_strs[0]
        value = list_splitted_strs[1].replace(")", "")
        if "," in value:
            values = value.split(",")
            mark = getattr(pytest.mark, name).with_args(*values)
        else:
            mark = getattr(pytest.mark, name).with_args(value)

    else:
        mark = getattr(pytest.mark, tag)
    marked = mark(function)
    return cast(Callable, marked)


def pytest_configure(config):
    settings.validators.validate()
    config.option.test_service_name = settings.test_service_name


@pytest.fixture(scope="session")
def test_settings():
    return settings


@pytest.fixture(scope="session")
def appium_service():
    service = AppiumService()
    service.start(
        args=[
            "--address",
            settings.appium_host,
            "--port",
            settings.appium_port,
        ],
        timeout_ms=20000,
    )
    yield service
    service.stop()
