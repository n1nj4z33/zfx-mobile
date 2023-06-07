from pytest_bdd import given, then, when


@given("ios_step_given")
def ios_step_given(driver):
    print("ios_step_given")
    print(driver)


@when("ios_step_when")
def ios_step_when(driver):
    print("ios_step_when")
    print(driver)


@then("ios_step_then")
def ios_step_then(driver):
    print("ios_step_then")
    print(driver)
