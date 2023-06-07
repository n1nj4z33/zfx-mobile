from pytest_bdd import given, then, when


@given("login_step_given")
def login_step_given():
    print("login_step_given")


@when("login_step_when")
def login_step_when():
    print("login_step_when")


@then("login_step_then")
def login_step_then():
    print("login_step_then")
