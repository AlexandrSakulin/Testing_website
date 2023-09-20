from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.XPATH, "//a[@href='/login']")
    REGISTRATION_LINK = (By.XPATH, "//a[@href='/registration']")
    BASKET_LINK = (By.XPATH, "//a[@href='/cart/content']")
