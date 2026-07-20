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
        self.wait.until(EC.visibility_of_element_located(TransferFundsLocators.AMOUNT_INPUT)).send_keys(amount)
        self.wait.until(EC.visibility_of_element_located(TransferFundsLocators.TRANSFER_BUTTON)).click()
        


        
        
