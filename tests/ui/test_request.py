import pytest
from pages.request_page import RequestPage

@pytest.mark.smoke
@pytest.mark.regression
def test_request_loan(driver, registered_user):
    request = RequestPage(driver)

    request.request_loan()

    assert "Loan Request Processed" in request.get_success_loan_title()
    assert request.get_loan_status() == "Approved"
    assert "Congratulations" in request.get_success_loan_message()