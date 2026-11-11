import pytest
from pages.register_page import RegisterPage

@pytest.mark.smoke
@pytest.mark.regression
def test_register_new_user(driver, user_data):
    page = RegisterPage(driver)
    page.open()
    page.register(
        username=user_data["username"],
        password=user_data["password"],
        confirm=user_data["password"],
    )

    assert user_data["username"] in page.get_welcome_title()
    assert "created successfully" in page.get_success_message().lower()