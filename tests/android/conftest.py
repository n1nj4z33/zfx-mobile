import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options

from config import settings


def options():
    options = UiAutomator2Options()
    options.platformVersion = settings.platform_version
    options.app = settings.app
    options.udid = settings.udid
    caps = dict(autoGrantPermissions=True)
    options.load_capabilities(caps)
    return options


@pytest.fixture(scope="function")
def driver():
    appium_server_url = f"http://{settings.appium_host}:{settings.appium_port}"
    driver = webdriver.Remote(command_executor=appium_server_url, options=options())
    yield driver
    driver.quit()
