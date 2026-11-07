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
    USERNAME_ERROR = (By.ID, "customer.username.errors")

class LoginLocators:

    USERNAME = (By.XPATH, "//input[@name= 'username']")
    PASSWORD = (By.XPATH, "//input[@name= 'password']")

    LOGIN_BUTTON = (By.XPATH, "//input[@value= 'Log In']")

class TransferFundsLocators:

    TRANSFER_FUND_BUTTON = (By.XPATH, "//a[text()= 'Transfer Funds']")
    AMOUNT_INPUT = (By.XPATH, "//input[@id= 'amount']")
    TRANSFER_BUTTON = (By.XPATH, "//input[@value= 'Transfer']")

class OpenNewAccountLocators:

    LINK_NEW_ACCOUNT = (By.XPATH, "//a[text()= 'Open New Account']")
    TYPE_ACCOUNT = (By.XPATH, "//select[@id= 'type']")
    OPTION_CHECKING = (By.XPATH, "//option[@value = '0']")
    OPTION_SAVINGS = (By.XPATH, "//option[@value = '1']")
    SELECT_ACCOUNT = (By.XPATH, "//select[@id= 'fromAccountId']")
    NEW_ACCOUNT_BUTTON = (By.XPATH, "//input[@value= 'Open New Account']")

class BillPaymentLocators:

    LINK_BILL_PAY = (By.XPATH, "//a[text()= 'Bill Pay']")
    PAYEE_NAME = (By.XPATH, "//input[@name= 'payee.name']")
    PAYEE_ADDRESS = (By.XPATH, "//input[@name= 'payee.address.street']")
    PAYEE_CITY = (By.XPATH, "//input[@name= 'payee.address.city']")
    PAYEE_STATE = (By.XPATH, "//input[@name= 'payee.address.state']")
    PAYEE_ZIP_CODE = (By.XPATH, "//input[@name= 'payee.address.zipCode']")
    PAYEE_PHONE = (By.XPATH, "//input[@name= 'payee.phoneNumber']")
    PAYEE_ACCOUNT = (By.XPATH, "//input[@name= 'payee.accountNumber']")    
    VERIFY_PAYEE_ACCOUNT = (By.XPATH, "//input[@name= 'verifyAccount']")
    PAYEE_AMOUNT = (By.XPATH, "//input[@name= 'amount']")
    PAYEE_FROM_ACCOUNT = (By.XPATH, "//input[@name= 'fromAccountId']")
    BUTTON_SEND_PAYAMENT = (By.XPATH, "//input[@value= 'Send Payment']")

class RequestLoanLocators:

    LINK_REQUEST_LOAN = (By.XPATH, "//a[text()= 'Request Loan']")
    INPUT_LOAN_AMOUNT = (By.XPATH, "//input[@id= 'amount']")
    INPUT_DOWN_PAYMENT = (By.XPATH, "//input[@id= 'downPayment']")
    BUTTON_APPLY_LOAN = (By.XPATH, "//input[@value= 'Apply Now']")

class UpdateLocators:

    LINK_UPDATE_PROFILE = (By.XPATH, "//a[text()= 'Update Contact Info']")
    INPUT_UPDATE_FIRST_NAME = (By.XPATH, "//input[@id= 'customer.firstName']")
    INPUT_UPDATE_LAST_NAME = (By.XPATH, "//input[@id= 'customer.lastName']")
    INPUT_UPDATE_ADDRESS = (By.XPATH, "//input[@id= 'customer.address.street']")
    INPUT_UPDATE_CITY = (By.XPATH, "//input[@id= 'customer.address.city']")
    INPUT_UPDATE_STATE = (By.XPATH, "//input[@id= 'customer.address.state']")
    INPUT_UPDATE_ZIP_CODE = (By.XPATH, "//input[@id= 'customer.address.zipCode']")
    INPUT_UPDATE_PHONE = (By.XPATH, "//input[@id= 'customer.phoneNumber']")
    BUTTON_UPDATE_PROFILE = (By.XPATH, "//input[@value= 'Update Profile']")
    