from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.XPATH, "//a[@href='/login']")
    REGISTRATION_LINK = (By.XPATH, "//a[@href='/registration']")
    BASKET_LINK = (By.XPATH, "//a[@href='/cart/content1']")
    # ENTER_LOGIN = (By.ID, "frm-loginForm-username")
    # MY_ACCOUNT_LINK = (By.XPATH, "//a[@href='/my-account']")
