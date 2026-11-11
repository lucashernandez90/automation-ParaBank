import pytest
from pages.update_page import UpdatePage 

@pytest.mark.smoke
@pytest.mark.regression

def test_update_account(driver, registered_user):
    update_account = UpdatePage(driver)

    update_account.update()

    assert "Profile Updated" in update_account.get_sucess_update_title()
    assert "updated address and phone number" in update_account.get_sucess_update_message()