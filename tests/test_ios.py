from pytest_bdd import scenario

# pylint: disable=wildcard-import, unused-wildcard-import
from steps.ios import *

# pylint: enable=wildcard-import, unused-wildcard-import


@scenario("ios.feature", "iOS Scenario")
def test_ios(test_settings):
    ios_step_given()
    ios_step_when()
    ios_step_then()
    assert test_settings is not None
