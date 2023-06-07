from pytest_bdd import scenario

from steps import login


@scenario("login.feature", "Login Scenario")
def test_template(test_settings):
    login.login_step_given()
    login.login_step_when()
    login.login_step_then()
    assert test_settings is not None
