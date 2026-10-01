from selenium.webdriver.common.by import By

class RegisterLocators:
    REGISTER_LINK = (By.XPATH, "//a[text()='Register']")

    FIRSTNAME_INPUT = (By.XPATH, "//input[@id= 'customer.firstName']")
    LASTNAME_INPUT = (By.XPATH, "//input[@id= 'customer.lastName']")
    ADDRESS_INPUT = (By.XPATH, "//input[@id= 'customer.address.street']")
    CITY_INPUT = (By.XPATH, "//input[@id= 'customer.address.city']")
    STATE_INPUT = (By.XPATH, "//input[@id= 'customer.address.state']")
    ZIP_CODE_INPUT = (By.XPATH, "//input[@id= 'customer.address.zipCode']")
    PHONE_INPUT = (By.XPATH, "//input[@id= 'customer.phoneNumber']")
    SSN_INPUT = (By.XPATH, "//input[@id= 'customer.ssn']")
    
    USERNAME_INPUT = (By.XPATH, "//input[@id= 'customer.username']")
    PASSWORD_INPUT = (By.XPATH, "//input[@id= 'customer.password']")
    CONFIRM_INPUT = (By.XPATH, "//input[@id= 'repeatedPassword']")

    REGISTER_BUTTON = (By.XPATH, "//input[@value= 'Register']")

class LoginLocators:

    USERNAME = (By.XPATH, "//input[@name= 'username']")
    PASSWORD = (By.XPATH, "//input[@name= 'password']")

    LOGIN_BUTTON = (By.XPATH, "//input[@value= 'Log In']")

class TransferFundsLocators:

    TRANSFER_FUND_BUTTON = (By.XPATH, "//a[text()= 'Transfer Funds']")
    AMOUNT_INPUT = (By.XPATH, "//input[@id= 'amount']")
    TRANSFER_BUTTON = (By.XPATH, "//input[@value= 'Transfer']")

    

    