from appium.webdriver.common.appiumby import AppiumBy
from pytest_bdd import given, then, when


@given("android_step_given")
def android_step_given(android_driver):
    print("android_step_given")
    element = android_driver.find_element(
        by=AppiumBy.XPATH, value="//android.widget.TextView"
    )
    return element.get_attribute("text")


@when("android_step_when")
def android_step_when(android_driver):
    print("android_step_when")
    element = android_driver.find_element(
        by=AppiumBy.XPATH, value="//android.widget.TextView"
    )
    return element.get_attribute("text")


@then("android_step_then")
def android_step_then(android_driver):
    print("android_step_then")
    element = android_driver.find_element(
        by=AppiumBy.XPATH, value="//android.widget.TextView"
    )
    return element.get_attribute("text")
