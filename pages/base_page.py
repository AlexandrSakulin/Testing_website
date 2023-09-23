import os
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class BasePage:
    """Базовый класс для страниц веб-приложения."""

    def __init__(self, driver):
        self.driver = driver

    def is_element_present(self, locator: tuple, timeout=10) -> bool:
        """Проверяет наличие элемента на странице по заданным локаторам."""
        try:
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def click_i(self, product_locator: tuple, cart_locator: tuple, timeout=10):
        """Добавляет товар в корзину."""
        try:
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(product_locator))

            # Нажмите на кнопку "Добавить в корзину" или выполните другие действия,
            # чтобы добавить товар в корзину
            add_to_cart_button = self.driver.find_element(*product_locator)
            add_to_cart_button.click()

            # Дождитесь появления элемента, представляющего корзину
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(cart_locator))

            # В этом месте вы можете выполнить дополнительные действия, если необходимо,
            # например, проверить сообщение об успешном добавлении в корзину
        except TimeoutException:
            print("Не удалось добавить товар в корзину.")
