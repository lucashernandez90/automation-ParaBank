from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

class RegisterData:
    
    URL_SITE = "https://parabank.parasoft.com/parabank/index.htm" 

    FIRSTNAME_INPUT = "lucas"
    LASTNAME_INPUT = "oliveira"
    ADDRESS_INPUT = "Rua Anonima"
    CITY_INPUT = "São Paulo"
    STATE_INPUT = "São Paulo"
    ZIP_CODE_INPUT = "359"
    PHONE_INPUT = "1197677675"
    SSN_INPUT = "11"
    
    USERNAME_INPUT = "lucasoh"
    PASSWORD_INPUT = "lucas123"
    CONFIRM_INPUT = "lucas123"

class TransferData:
    AMOUNT = "2000"

class BillPaymentData:
    ACCOUNT = "14787"
    AMOUNT  = "300"

class LoanData:
    LOAN_AMMOUNT = "500"
    DOWN_PAYMENT = "100"

class UpdateData:
    UPDATE_FIRST_NAME = "Rubens"
    UPDATE_LAST_NAME = "Silva"
    UPDATE_ADDRESS = "Rua Teste"
    UPDATE_CITY = "DF"
    UPDATE_STATE = "Centro"
    UPDATE_ZIP_CODE = "345"
    UPDATE_PHONE = "11945467484"