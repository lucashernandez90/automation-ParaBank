import time
import logging
from config.browser import create_driver
from pages.register_page import RegisterPage
from pages.login_page import  LoginPage
from pages.transfer_page import TransferPage
from pages.new_account_page import NewAccountPage
from pages.bill_page import BillPage
from pages.request_page import RequestPage

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

driver = create_driver()

register_page = RegisterPage(driver)
login_page = LoginPage(driver)
transfer_page = TransferPage(driver)
new_account_page = NewAccountPage(driver)
bill_page = BillPage(driver)
request_page = RequestPage(driver)

register_page.open()

register_page.register()

if register_page.username_already_exists():
    logging.info("Usuário já existe, fazendo login...")
    login_page.login()
else:
    logging.info("Cadastro realizado com sucesso")

transfer_page.transfer()

new_account_page.open_account()

bill_page.bill_payment()

request_page.request_loan()

driver.quit()