from WebSelenium.ApiTestStudy.api.wework import WeWork


class TestWeWork(WeWork):
    def test_get_access_token(self):
        r = self.get_access_token()
        assert r["errcode"] == 0
