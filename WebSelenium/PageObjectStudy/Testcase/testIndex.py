from WebSelenium.PageObjectStudy.Page.Index import Index


class TestIndex:

    def setup(self):
        self.index = Index()

    def test_register(self):
        self.index.goto_register().register("霍格沃兹测试学院")

    def test_login(self):
        register_page = self.index.goto_login().goto_registry().register("测吧")
        assert "请选择" in "|" .join(register_page.get_error_message())

    def teardown(self):
        self.index.close()
