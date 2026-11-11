import pytest
from pages.transfer_page import TransferPage

@pytest.mark.smoke
@pytest.mark.regression

def test_transfer(driver, registered_user):
    transfer = TransferPage(driver)

    transfer.transfer()

    message = transfer.get_success_transfer_message()

    assert "Transfer Complete!" in transfer.get_success_transfer_title()
    assert "has been transferred" in message