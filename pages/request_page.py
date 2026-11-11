import sys
import time
import logging

from pages.base_page import BasePage
from config.settings import LoanData
from config.locators import RequestLoanLocators
from selenium.webdriver.support import expected_conditions as EC

class RequestPage(BasePage):

    def request_loan(self, loan= LoanData.LOAN_AMMOUNT, downPayment= LoanData.DOWN_PAYMENT):

        self.wait.until(EC.element_to_be_clickable(RequestLoanLocators.LINK_REQUEST_LOAN)).click()
        logging.info("link request loan clicked")

        self.wait.until(EC.visibility_of_element_located(RequestLoanLocators.INPUT_LOAN_AMOUNT)).send_keys(loan)
        self.wait.until(EC.visibility_of_element_located(RequestLoanLocators.INPUT_DOWN_PAYMENT)).send_keys(downPayment)
        logging.info("filled blanks")
        
        self.wait.until(EC.element_to_be_clickable(RequestLoanLocators.BUTTON_APPLY_LOAN)).click()
        logging.info("button appply clicked")

    def get_success_loan_title(self):
        return self.wait.until(EC.visibility_of_element_located(RequestLoanLocators.SUCCESS_LOAN_TITLE)).text

    def get_success_loan_message(self):
        return self.wait.until(EC.visibility_of_element_located(RequestLoanLocators.SUCCESS_LOAN_MESSAGE)).text

    def get_loan_status(self):
        return self.wait.until(EC.visibility_of_element_located(RequestLoanLocators.LOAN_STATUS)).text