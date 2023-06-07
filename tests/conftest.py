from typing import Callable, cast

import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
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


# Appium

APPIUM_HOST = "localhost"
APPIUM_PORT = "4723"


@pytest.fixture(scope="session")
def appium_service():
    service = AppiumService()
    service.start(
        args=[
            "--address",
            APPIUM_HOST,
            "--port",
            APPIUM_PORT,
        ],
        timeout_ms=20000,
    )
    yield service
    service.stop()


def android_options():
    options = UiAutomator2Options()
    options.platformVersion = "10"
    options.app = "./resources/android.apk"
    options.udid = "emulator-5554"
    caps = dict(autoGrantPermissions=True)
    options.load_capabilities(caps)
    return options


@pytest.fixture(scope="function")
def android_driver():
    appium_server_url = "http://localhost:4723"
    driver = webdriver.Remote(
        command_executor=appium_server_url, options=android_options()
    )
    yield driver
    driver.quit()
