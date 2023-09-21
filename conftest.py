import pytest
import allure
import os
from selenium import webdriver
from configurations import MAIN_URL


@pytest.fixture
def browser(request):
    """Автоматически открывает указанный URL-адрес MAIN_URL перед началом теста и
    закрывает браузер после завершения теста"""
    driver = webdriver.Chrome()
    driver.get(MAIN_URL)
    yield driver
    driver.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        mode = "a" if os.path.exists("failures") else "w"
        try:
            with open("failures", mode) as f:
                if "browser" in item.fixturenames:
                    web_driver = item.funcargs["browser"]
                    allure.attach(
                        web_driver.get_screenshot_as_png(),
                        name="screenshot",
                        attachment_type=allure.attachment_type.PNG,
                    )
                else:
                    print("Fail to take screen-shot")
        except Exception as error:
            print("Fail to take screen-shot: {}".format(error))
