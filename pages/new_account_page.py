import logging

from pages.base_page import BasePage
from config.locators import OpenNewAccountLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


class NewAccountPage(BasePage):

    def open_account(self, account_type="CHECKING"):
        self.wait.until(EC.element_to_be_clickable(OpenNewAccountLocators.LINK_NEW_ACCOUNT)).click()
        logging.info("link new account clicked")

        # espera a lista de contas de origem terminar de carregar
        self.wait.until(
            lambda d: len(Select(d.find_element(*OpenNewAccountLocators.FROM_ACCOUNT_SELECT)).options) > 0
        )

        type_select = Select(self.wait.until(
            EC.element_to_be_clickable(OpenNewAccountLocators.ACCOUNT_TYPE_SELECT)
        ))
        type_select.select_by_visible_text(account_type)
        logging.info(f"selected {account_type} account")

        self.wait.until(EC.element_to_be_clickable(OpenNewAccountLocators.NEW_ACCOUNT_BUTTON)).click()
        logging.info("clicked on the button create account")

    def get_success_new_account_title(self):
        return self.wait.until(EC.visibility_of_element_located(OpenNewAccountLocators.SUCCESS_NEW_ACCOUNT_TITLE)).text

    def get_success_new_account_message(self):
        return self.wait.until(EC.visibility_of_element_located(OpenNewAccountLocators.SUCCESS_NEW_ACCOUNT_MESSAGE)).text

    def get_new_account_id(self):
        return self.wait.until(EC.visibility_of_element_located(OpenNewAccountLocators.NEW_ACCOUNT_ID)).text