import sys
import time
import logging

from pages.base_page import BasePage
from config.locators import RegisterLocators
from config.settings import RegisterData
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

class RegisterPage(BasePage):

    def open(self):
        self.driver.get(RegisterData.URL_SITE)

    def register(self, firstname=RegisterData.FIRSTNAME_INPUT, lastname= RegisterData.LASTNAME_INPUT, address=RegisterData.ADDRESS_INPUT,city= RegisterData.CITY_INPUT,state= RegisterData.STATE_INPUT, 
                 zipcode= RegisterData.ZIP_CODE_INPUT, phone= RegisterData.PHONE_INPUT, ssn= RegisterData.SSN_INPUT, 
                 username= RegisterData.USERNAME_INPUT, password=RegisterData.PASSWORD_INPUT, confirm= RegisterData.CONFIRM_INPUT):
        
        self.wait.until(EC.element_to_be_clickable(RegisterLocators.REGISTER_LINK)).click()
        
        self.wait.until(EC.visibility_of_element_located(RegisterLocators.FIRSTNAME_INPUT)).send_keys(firstname)
        self.wait.until(EC.visibility_of_element_located(RegisterLocators.LASTNAME_INPUT)).send_keys(lastname)
        self.wait.until(EC.visibility_of_element_located(RegisterLocators.ADDRESS_INPUT)).send_keys(address)
        self.wait.until(EC.visibility_of_element_located(RegisterLocators.CITY_INPUT)).send_keys(city)
        self.wait.until(EC.visibility_of_element_located(RegisterLocators.STATE_INPUT)).send_keys(state)
        self.wait.until(EC.visibility_of_element_located(RegisterLocators.ZIP_CODE_INPUT)).send_keys(zipcode)
        self.wait.until(EC.visibility_of_element_located(RegisterLocators.PHONE_INPUT)).send_keys(phone)
        self.wait.until(EC.visibility_of_element_located(RegisterLocators.SSN_INPUT)).send_keys(ssn)

        self.wait.until(EC.visibility_of_element_located(RegisterLocators.USERNAME_INPUT)).send_keys(username)
        self.wait.until(EC.visibility_of_element_located(RegisterLocators.PASSWORD_INPUT)).send_keys(password)
        self.wait.until(EC.visibility_of_element_located(RegisterLocators.CONFIRM_INPUT)).send_keys(confirm)

        self.wait.until(EC.element_to_be_clickable(RegisterLocators.REGISTER_BUTTON)).click()
    
        logging.info("register camps filled")

        time.sleep(5)

    def username_already_exists(self, timeout=3):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(RegisterLocators.USERNAME_ERROR)
            )
            return "already exists" in element.text.lower()
        except TimeoutException:
            return False