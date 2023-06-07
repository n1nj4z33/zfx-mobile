from pytest_bdd import given, then, when


@given("ios_step_given")
def ios_step_given():
    print("ios_step_given")


@when("ios_step_when")
def ios_step_when():
    print("ios_step_when")


@then("ios_step_then")
def ios_step_then():
    print("ios_step_then")
