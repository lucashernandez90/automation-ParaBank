import pytest
from pages.new_account_page import NewAccountPage


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.parametrize("account_type", ["CHECKING", "SAVINGS"])
def test_new_account(driver, registered_user, account_type):
    new_account = NewAccountPage(driver)

    new_account.open_account(account_type)

    assert "Account Opened" in new_account.get_success_new_account_title()
    assert "your account is now open" in new_account.get_success_new_account_message().lower()
    assert new_account.get_new_account_id().isdigit()