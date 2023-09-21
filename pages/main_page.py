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
        assert "basket" in self.driver.current_url.lower(), "При нажатии переход не произошел"

    # def enter_email(self):
    #     (self.driver.find_element(*self.LOGIN_LINK)).click()
    #     login_field = self.driver.find_element(*self.ENTER_LOGIN)
    #     login_field.send_keys("torb7nsk7y@icloud.com")
    #
    # def enter_password(self):
    #     (self.driver.find_element(*self.LOGIN_LINK)).click()
    #     login_field = self.driver.find_element(*self.ENTER_LOGIN)
    #     login_field.send_keys("torb7nsk7y@icloud.com")
