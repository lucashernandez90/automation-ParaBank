import sys
import time
import logging

from pages.base_page import BasePage
from config.locators import OpenNewAccountLocators
from selenium.webdriver.support import expected_conditions as EC

class NewAccountPage(BasePage):

    def open_account(self):
        self.wait.until(EC.element_to_be_clickable(OpenNewAccountLocators.LINK_NEW_ACCOUNT)).click()
        logging.info("link new account clicked")

        # self.wait.until(EC.element_to_be_clickable(OpenNewAccountLocators.OPTION_SAVINGS)).click()
        # logging.info("selected savings account")

        self.wait.until(EC.element_to_be_clickable(OpenNewAccountLocators.OPTION_CHECKING)).click()
        logging.info("selected savings account")

        self.wait.until(EC.element_to_be_clickable(OpenNewAccountLocators.NEW_ACCOUNT_BUTTON)).click()
        logging.info("clicked on the button creat account")

        time.sleep(10)