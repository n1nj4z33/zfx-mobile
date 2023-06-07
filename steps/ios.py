from pytest_bdd import given, then, when


@given("ios_step_given")
def ios_step_given(driver):
    print("ios_step_given")


@when("ios_step_when")
def ios_step_when(driver):
    print("ios_step_when")


@then("ios_step_then")
def ios_step_then(driver):
    print("ios_step_then")
