from pytest_bdd import scenario

# pylint: disable=wildcard-import, unused-wildcard-import
from steps.ios import *

# pylint: enable=wildcard-import, unused-wildcard-import


@scenario("ios.feature", "iOS Scenario")
def test_ios(test_settings, appium_service, driver):
    ios_step_given(driver)
    ios_step_when(driver)
    ios_step_then(driver)
    assert test_settings is not None
