import sys
import time
import logging

from pages.base_page import BasePage
from config.locators import LoginLocators
from config.settings import RegisterData
from selenium.webdriver.support import expected_conditions as EC

class LoginPage(BasePage):
    
    def login(self, username= RegisterData.USERNAME_INPUT, password= RegisterData.PASSWORD_INPUT):

        self.wait.until(EC.element_to_be_clickable(LoginLocators.USERNAME)).send_keys(username)
        self.wait.until(EC.element_to_be_clickable(LoginLocators.PASSWORD)).send_keys(password)
        logging.info("filled username and password")

        self.wait.until(EC.element_to_be_clickable(LoginLocators.LOGIN_BUTTON)).click()
        logging.info("clicked login button")

        time.sleep(2)

    