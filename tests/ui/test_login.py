import pytest
from pages.login_page import LoginPage

@pytest.mark.smoke
@pytest.mark.regression
def test_login_with_created_user(driver, registered_user):
    login = LoginPage(driver)

    login.logout()
    login.login(registered_user["username"], registered_user["password"])

    assert login.is_logged_in()