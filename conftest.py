import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def browser():
    """
    Автоматически закрывает браузер после завершения теста.
    """
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture(scope="session")
def browser_session():
    """
    Автоматически закрывает браузер после завершения серии тестов.
    """
    driver = webdriver.Chrome()
    yield driver
    driver.quit()
