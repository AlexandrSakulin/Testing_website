import os

from selenium.common.exceptions import NoSuchElementException


class BasePage:
    """Базовый класс для страниц веб-приложения."""

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.driver.implicitly_wait(timeout)
        self.screenshots_dir = "screenshots"

        if not os.path.exists(self.screenshots_dir):
            os.makedirs(self.screenshots_dir)

    def is_element_present(self, locator):
        """Проверяет наличие элемента на странице по заданным локаторам."""
        try:
            self.driver.find_element(*locator)
        except NoSuchElementException:
            return False
        return True
