import time

from pages.main_page import MainPage


def test_guest_should_see_login_link(browser):
    """Проверяет, что гость видит ссылку на страницу входа на главной странице."""
    page = MainPage(browser)
    page.should_be_login_link()


def test_guest_should_see_registration_link(browser):
    """Проверяет, что гость видит ссылку на страницу регистрации на главной странице."""
    page = MainPage(browser)
    page.should_be_register_link()


def test_guest_should_see_basket_link(browser):
    """Проверяет, что гость видит ссылку на страницу корзины на главной странице."""
    page = MainPage(browser)
    page.should_be_basket_link()


def test_guest_can_go_to_login_page(browser):
    """Проверяет, что гость может перейти на страницу входа."""
    page = MainPage(browser)
    page.go_to_login_page()


def test_guest_can_go_to_registration_page(browser):
    """Проверяет, что гость может перейти на страницу регистрации."""
    page = MainPage(browser)
    page.go_to_registration_page()


def test_guest_can_go_to_basket_page(browser):
    """Проверяет, что гость может перейти на страницу корзины."""
    page = MainPage(browser)
    page.go_to_basket_page()


# def test_enter_login_and_password(browser):
#     page = MainPage(browser)
#     page.enter_email()
#     time.sleep(5)
