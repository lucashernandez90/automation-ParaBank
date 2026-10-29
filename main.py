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

if register_page.username_already_exists():
    logging.info("Usuário já existe, fazendo login...")
    login_page.login()
else:
    logging.info("Cadastro realizado com sucesso")

transfer_page.transfer()

driver.quit()