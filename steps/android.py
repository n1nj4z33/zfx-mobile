from appium.webdriver.common.appiumby import AppiumBy
from pytest_bdd import given, then, when


@given("android_step_given")
def android_step_given(driver):
    print("android_step_given")
    element = driver.find_element(
        by=AppiumBy.XPATH, value="//android.widget.TextView"
    )
    return element.get_attribute("text")


@when("android_step_when")
def android_step_when(driver):
    print("android_step_when")
    element = driver.find_element(
        by=AppiumBy.XPATH, value="//android.widget.TextView"
    )
    return element.get_attribute("text")


@then("android_step_then")
def android_step_then(driver):
    print("android_step_then")
    element = driver.find_element(
        by=AppiumBy.XPATH, value="//android.widget.TextView"
    )
    return element.get_attribute("text")
