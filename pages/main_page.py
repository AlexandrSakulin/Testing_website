from .base_page import BasePage
from .locators import MainPageLocators


class MainPage(BasePage, MainPageLocators):
    """Класс, представляющий главную страницу веб-приложения."""

    def should_be_login_link(self):
        """Проверяет наличие ссылки на страницу входа на главной странице."""
        assert self.is_element_present(self.LOGIN_LINK), "Ссылка на вход отсутствует"

    def should_be_register_link(self):
        """Проверяет наличие ссылки на страницу входа на главной странице."""
        assert self.is_element_present(self.REGISTRATION_LINK), "Ссылка на регистрацию отсутствует"

    def should_be_basket_link(self):
        """Проверяет наличие ссылки на корзину на главной странице."""
        assert self.is_element_present(self.BASKET_LINK), "Ссылка на корзину отсутствует"

    def go_to_login_page(self):
        """Осуществляет переход на страницу входа, кликая по соответствующей ссылке."""
        (self.driver.find_element(*self.LOGIN_LINK)).click()
        assert "login" in self.driver.current_url.lower(), "При нажатии переход не произошел"

    def go_to_registration_page(self):
        """Осуществляет переход на страницу регистрации, кликая по соответствующей ссылке."""
        (self.driver.find_element(*self.REGISTRATION_LINK)).click()
        assert "registration" in self.driver.current_url.lower(), "При нажатии переход не произошел"

    def go_to_basket_page(self):
        """Осуществляет переход на страницу регистрации, кликая по соответствующей ссылке."""
        (self.driver.find_element(*self.BASKET_LINK)).click()
        assert "cart/content" in self.driver.current_url.lower(), "При нажатии переход не произошел"

    # Проверка карточки товара
    def should_be_product_link(self):
        """Проверяет наличие ссылки на страницу карточки товара."""
        assert self.is_element_present(self.PRODUCT_LINK), "Ссылка на вход отсутствует"

    def go_to_product_page(self):
        """Осуществляет переход на страницу карточки товара."""
        (self.driver.find_element(*self.PRODUCT_LINK)).click()
        assert "product/" in self.driver.current_url.lower(), "При нажатии переход не произошел"

    def click_basket_buy(self):
        (self.driver.find_element(*self.BUTTON_BASKET_BUY)).click()
        assert "cart/content" in self.driver.current_url.lower(), "При нажатии переход не произошел"

    def screen_scroll(self):
        element = self.driver.find_element(self.PRODUCT_LINK)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def clicked_buy_product_go_to_basket(self):
        self.screen_scroll()
        self.should_be_product_link()
        self.go_to_product_page()
        self.click_basket_buy()
