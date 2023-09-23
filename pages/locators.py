from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.XPATH, "//a[@href='/login']")
    REGISTRATION_LINK = (By.XPATH, "//a[@href='/registration']")
    BASKET_LINK = (By.XPATH, "//a[@href='/cart/content']")
    PRODUCT_LINK = (By.XPATH, "//input[@title='Бейсболка клубная']")
    BUTTON_BASKET_BUY = (By.XPATH, "//input[@value='В корзину']")
