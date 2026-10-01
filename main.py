import time
import logging
from config.browser import create_driver
from pages.register_page import RegisterPage
from pages.login_page import  LoginPage
from pages.transfer_page import TransferPage

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

driver = create_driver()

register_page = RegisterPage(driver)
login_page = LoginPage(driver)
transfer_page = TransferPage(driver)

register_page.open()

register_page.register()

login_page.login()

transfer_page.transfer()

driver.quit()