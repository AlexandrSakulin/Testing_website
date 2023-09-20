from selenium.common.exceptions import NoSuchElementException


class BasePage:
    """
    Базовый класс для страниц веб-приложения.

    :param browser: Объект веб-драйвера.
    :param url: URL страницы, которую должен открывать этот объект.
    :param timeout: Время неявного ожидания для ожидания элементов на странице (по умолчанию 10 секунд).
    """

    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        """
        Открывает URL страницы в браузере.
        """
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        """
        Проверяет наличие элемента на странице по заданным локаторам.

        :param how: Метод локатора (например, By.XPATH, By.ID и т. д.).
        :param what: Значение локатора (например, строка с XPath, ID и т. д.).

        :return: True, если элемент присутствует на странице, False в противном случае.
        """
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True
