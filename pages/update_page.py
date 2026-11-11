import sys
import time
import logging

from pages.base_page import BasePage
from config.locators import UpdateLocators
from config.settings import UpdateData
from selenium.webdriver.support import expected_conditions as EC

class UpdatePage(BasePage):

    def update(self, firstName= UpdateData.UPDATE_FIRST_NAME, lastName= UpdateData.UPDATE_LAST_NAME, address= UpdateData.UPDATE_ADDRESS, 
                    city= UpdateData.UPDATE_CITY, state= UpdateData.UPDATE_STATE, zipCode= UpdateData.UPDATE_ZIP_CODE, phone= UpdateData.UPDATE_PHONE):

        self.wait.until(EC.element_to_be_clickable(UpdateLocators.LINK_UPDATE_PROFILE)).click()

        self.wait.until(EC.visibility_of_element_located(UpdateLocators.INPUT_UPDATE_FIRST_NAME)).send_keys(firstName)
        self.wait.until(EC.visibility_of_element_located(UpdateLocators.INPUT_UPDATE_LAST_NAME)).send_keys(lastName)
        self.wait.until(EC.visibility_of_element_located(UpdateLocators.INPUT_UPDATE_ADDRESS)).send_keys(address)
        self.wait.until(EC.visibility_of_element_located(UpdateLocators.INPUT_UPDATE_CITY)).send_keys(city)
        self.wait.until(EC.visibility_of_element_located(UpdateLocators.INPUT_UPDATE_STATE)).send_keys(state)
        self.wait.until(EC.visibility_of_element_located(UpdateLocators.INPUT_UPDATE_ZIP_CODE)).send_keys(zipCode)
        self.wait.until(EC.visibility_of_element_located(UpdateLocators.INPUT_UPDATE_PHONE)).send_keys(phone)
        logging.info("update blanks filled")

        self.wait.until(EC.element_to_be_clickable(UpdateLocators.BUTTON_UPDATE_PROFILE)).click()
        logging.info("clicked update button")


    def get_sucess_update_title(self):
        return self.wait.until(EC.visibility_of_element_located(UpdateLocators.UPDATE_TITLE)).text

    def get_sucess_update_message(self):
        return self.wait.until(EC.visibility_of_element_located(UpdateLocators.UPDATE_MESSAGE)).text



