from selenium.webdriver.common.by import By
import time
from pages.main_page import MainPage
from configurations import LINK_SITE


def test_guest_should_see_login_link(browser_session):
    """
    Проверяет, что гость видит ссылку на страницу входа на главной странице.

    """
    link = LINK_SITE
    page = MainPage(browser_session, link)
    page.open()
    page.should_be_login_link()


def test_guest_should_see_registration_link(browser_session):
    """
    Проверяет, что гость видит ссылку на страницу регистрации на главной странице.

    """
    link = LINK_SITE
    page = MainPage(browser_session, link)
    page.open()
    page.should_be_register_link()


def test_guest_should_see_basket_link(browser_session):
    """
    Проверяет, что гость видит ссылку на страницу корзины на главной странице.

    """
    link = LINK_SITE
    page = MainPage(browser_session, link)
    page.open()
    page.should_be_basket_link()


def test_guest_can_go_to_login_page(browser):
    """
    Проверяет, что гость может перейти на страницу входа.

    """
    link = LINK_SITE
    page = MainPage(browser, link)
    page.open()
    login_page = page.go_to_login_page()
    login_page.should_be_login_link()
    time.sleep(3)


def test_guest_can_go_to_registration_page(browser):
    """
    Проверяет, что гость может перейти на страницу регистрации.

    """
    link = LINK_SITE
    page = MainPage(browser, link)
    page.open()
    login_page = page.go_to_registration_page()
    login_page.should_be_login_link()
    time.sleep(3)


def test_guest_can_go_to_basket_page(browser):
    """
    Проверяет, что гость может перейти на страницу корзины.

    """
    link = LINK_SITE
    page = MainPage(browser, link)
    page.open()
    login_page = page.go_to_basket_page()
    login_page.should_be_login_link()
    time.sleep(3)
