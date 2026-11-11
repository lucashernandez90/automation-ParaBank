import sys
import time
import logging

from pages.base_page import BasePage
from config.settings import RegisterData
from config.locators import BillPaymentLocators
from config.settings import BillPaymentData
from selenium.webdriver.support import expected_conditions as EC

class BillPage(BasePage):

    def bill_payment(self, payeeName= RegisterData.FIRSTNAME_INPUT, address= RegisterData.ADDRESS_INPUT, city= RegisterData.CITY_INPUT, 
                    state= RegisterData.STATE_INPUT, zipCode= RegisterData.ZIP_CODE_INPUT, phone= RegisterData.PHONE_INPUT,
                    account= BillPaymentData.ACCOUNT, amount= BillPaymentData.AMOUNT):

        self.wait.until(EC.element_to_be_clickable(BillPaymentLocators.LINK_BILL_PAY)).click()
        logging.info("clicked link to bill payament")
        
        self.wait.until(EC.visibility_of_element_located(BillPaymentLocators.PAYEE_NAME)).send_keys(payeeName)
        self.wait.until(EC.visibility_of_element_located(BillPaymentLocators.PAYEE_ADDRESS)).send_keys(address)
        self.wait.until(EC.visibility_of_element_located(BillPaymentLocators.PAYEE_CITY)).send_keys(city)
        self.wait.until(EC.visibility_of_element_located(BillPaymentLocators.PAYEE_STATE)).send_keys(state)
        self.wait.until(EC.visibility_of_element_located(BillPaymentLocators.PAYEE_ZIP_CODE)).send_keys(zipCode)
        self.wait.until(EC.visibility_of_element_located(BillPaymentLocators.PAYEE_PHONE)).send_keys(phone)
        self.wait.until(EC.visibility_of_element_located(BillPaymentLocators.PAYEE_ACCOUNT)).send_keys(account)
        self.wait.until(EC.visibility_of_element_located(BillPaymentLocators.VERIFY_PAYEE_ACCOUNT)).send_keys(account)
        self.wait.until(EC.visibility_of_element_located(BillPaymentLocators.PAYEE_AMOUNT)).send_keys(amount)

        logging.info("filled blanks")

        self.wait.until(EC.element_to_be_clickable(BillPaymentLocators.BUTTON_SEND_PAYAMENT)).click()
        logging.info("button payament clicked ")

    def get_result_title(self):
        return self.wait.until(EC.visibility_of_element_located(BillPaymentLocators.RESULT_TITLE)).text

    def get_result_message(self):
        return self.wait.until(EC.visibility_of_element_located(BillPaymentLocators.RESULT_MESSAGE)).text