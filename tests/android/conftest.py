import pytest

from appium import webdriver
from appium.options.android import UiAutomator2Options


def options():
    options = UiAutomator2Options()
    options.platformVersion = "10"
    options.app = "./resources/app.apk"
    options.udid = "emulator-5554"
    caps = dict(autoGrantPermissions=True)
    options.load_capabilities(caps)
    return options


@pytest.fixture(scope="function")
def driver():
    appium_server_url = "http://localhost:4723"
    driver = webdriver.Remote(
        command_executor=appium_server_url, options=options()
    )
    yield driver
    driver.quit()