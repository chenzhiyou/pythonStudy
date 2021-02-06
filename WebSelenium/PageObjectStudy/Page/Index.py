from selenium.webdriver.common.by import By

from WebSelenium.PageObjectStudy.Page.Login import Login
from WebSelenium.PageObjectStudy.Page.Register import Register
from WebSelenium.PageObjectStudy.Page.base_page import BasePage


class Index(BasePage):

    def goto_register(self):
        self._driver.find_element(By.LINK_TEXT, "立即注册").click()
        return Register(self._driver)

    def goto_login(self):
        self._driver.find_element(By.LINK_TEXT, "企业微信").click()
        return Login(self._driver)
