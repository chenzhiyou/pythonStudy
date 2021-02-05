from selenium import webdriver


class TestHogwarts:

    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)

    def teardown_method(self, method):
        self.driver.quit()

    def test_hogwarts(self):
        self.driver.get("https://www.baidu.com")
        self.driver.find_element_by_id('kw').send_keys("霍格沃兹测试学院")
        self.driver.find_element_by_css_selector('.s_btn').click()
        self.driver.find_element_by_link_text("霍格沃兹测试学院_腾讯课堂").click()
        handles = self.driver.window_handles
        print(handles)
        self.driver.switch_to.window(handles[-1])
        self.driver.find_element_by_partial_link_text('名企定向培养').click()
