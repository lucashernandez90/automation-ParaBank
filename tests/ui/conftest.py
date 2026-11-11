import os
import uuid
import pytest
from config.browser import create_driver
from pages.register_page import RegisterPage

@pytest.fixture
def driver():
    driver = create_driver()
    yield driver
    driver.quit()


@pytest.fixture
def user_data():
    return {
        "username": f"qa_{uuid.uuid4().hex[:8]}",
        "password": "Senha@123",
    }


@pytest.fixture
def registered_user(driver, user_data):
    page = RegisterPage(driver)
    page.open()
    page.register(
        username=user_data["username"],
        password=user_data["password"],
        confirm=user_data["password"],
    )
    return user_data


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")
        if driver:
            os.makedirs("screenshots", exist_ok=True)
            driver.save_screenshot(f"screenshots/{item.name}.png")