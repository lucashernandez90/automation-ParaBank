import pytest
from pages.bill_page import BillPage
from config.settings import RegisterData, BillPaymentData

@pytest.mark.smoke
@pytest.mark.regression
def test_bill_payment(driver, registered_user):
    bill = BillPage(driver)

    bill.bill_payment()

    message = bill.get_result_message()

    assert "Bill Payment Complete" in bill.get_result_title()
    assert RegisterData.FIRSTNAME_INPUT in message
    assert str(BillPaymentData.AMOUNT) in message
    assert "was successful" in message