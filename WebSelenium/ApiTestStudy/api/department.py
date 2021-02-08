import requests

from WebSelenium.ApiTestStudy.api.wework import WeWork


class Department(WeWork):
    list_url = ""

    def list(self, id):
        self.json_data = requests.get(self.list_url, params={"access_token": WeWork.get_token(),
                                                             "id": id}).json()
        return self.json_data
