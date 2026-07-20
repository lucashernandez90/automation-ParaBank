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