from selenium.webdriver.common.by import By

from WebSelenium.PageObjectStudy.Page.Register import Register
from WebSelenium.PageObjectStudy.Page.base_page import BasePage


class Login(BasePage):

    def scan_qrcode(self):
        pass

    def goto_registry(self):
        self._driver.find_element(By.LINK_TEXT, "立即注册").click()
        return Register(self._driver)
