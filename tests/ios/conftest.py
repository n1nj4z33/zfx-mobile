import pytest

from appium import webdriver
from appium.options.ios import XCUITestOptions

def options():
    options = XCUITestOptions()
    options.platformVersion = "13.4"
    options.app = "./resources/app.zip"
    options.udid = "0AD3AE13-D5B1-4653-8B07-7680800D1FE4"
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