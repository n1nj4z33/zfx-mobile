from pytest_bdd import scenario

# pylint: disable=wildcard-import, unused-wildcard-import
from steps.android import *

# pylint: enable=wildcard-import, unused-wildcard-import


@scenario("android.feature", "Android Scenario")
def test_android(test_settings, appium_service, driver):
    print(appium_service)
    assert test_settings is not None
    assert "API Demos" == android_step_given(driver)
    assert "API Demos" == android_step_when(driver)
    assert "API Demos" == android_step_then(driver)
