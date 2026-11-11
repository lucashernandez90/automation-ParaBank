import sys
import time
import logging

from pages.base_page import BasePage
from config.locators import TransferFundsLocators
from config.settings import TransferData
from selenium.webdriver.support import expected_conditions as EC

class TransferPage(BasePage):

    def transfer(self, amount=TransferData.AMOUNT):
        self.wait.until(EC.element_to_be_clickable(TransferFundsLocators.TRANSFER_FUND_BUTTON)).click()
        logging.info("button transfer clicked")

        self.wait.until(EC.visibility_of_element_located(TransferFundsLocators.AMOUNT_INPUT)).send_keys(amount)
        logging.info("amount transfered")

        self.wait.until(EC.visibility_of_element_located(TransferFundsLocators.TRANSFER_BUTTON)).click()
        logging.info("button transfered clicked")

    def get_success_transfer_title(self):
        return self.wait.until(EC.visibility_of_element_located(TransferFundsLocators.SUCCESS_TRANSFER_TITLE)).text

    def get_success_transfer_message(self):
        return self.wait.until(EC.visibility_of_element_located(TransferFundsLocators.SUCCESS_TRANSFER_MESSAGE)).text
        


        
        
