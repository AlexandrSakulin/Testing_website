from .base_page import BasePage
from .locators import MainPageLocators


class MainPage(BasePage):
    """
    Класс, представляющий главную страницу веб-приложения.

    """

    def should_be_login_link(self):
        """
        Проверяет наличие ссылки на страницу входа на главной странице.

        """
        assert self.is_element_present(
            *MainPageLocators.LOGIN_LINK
        ), "Login link is not presented"

    def should_be_register_link(self):
        """
        Проверяет наличие ссылки на страницу входа на главной странице.

        """
        assert self.is_element_present(
            *MainPageLocators.REGISTRATION_LINK
        ), "Registration link is not presented"

    def should_be_basket_link(self):
        """
        Проверяет наличие ссылки на корзину на главной странице.

        """
        assert self.is_element_present(
            *MainPageLocators.BASKET_LINK
        ), "Basket link is not presented"

    def go_to_login_page(self):
        """
        Осуществляет переход на страницу входа, кликая по соответствующей ссылке.
        """
        link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        link.click()
        return MainPage(browser=self.browser, url=self.browser.current_url)

    def go_to_registration_page(self):
        """
        Осуществляет переход на страницу регистрации, кликая по соответствующей ссылке.
        """
        link = self.browser.find_element(*MainPageLocators.REGISTRATION_LINK)
        link.click()
        return MainPage(browser=self.browser, url=self.browser.current_url)

    def go_to_basket_page(self):
        """
        Осуществляет переход на страницу регистрации, кликая по соответствующей ссылке.
        """
        link = self.browser.find_element(*MainPageLocators.BASKET_LINK)
        link.click()
        return MainPage(browser=self.browser, url=self.browser.current_url)
