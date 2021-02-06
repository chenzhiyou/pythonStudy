from time import sleep

from selenium.webdriver.remote.webdriver import WebDriver
from selenium import webdriver


class BasePage():
    def __init__(self, driver: WebDriver = None):
        # 此处对driver进行复用，如果不存在driver，就构建一个新的
        self._base_url = "https://work.weixin.qq.com"
        if driver is None:
            self._driver = webdriver.Chrome()
            self._driver.implicitly_wait(3)
            self._driver.get(self._base_url)
        else:
            # Login与Register等页面需要用这个方法，避免重复构建driver
            self._driver = driver

    def close(self):
        sleep(20)
        self._driver.quit()
