import requests

from WebSelenium.ApiTestStudy.api.base_api import BaseApi


class WeWork(BaseApi):
    corpid = ""
    contact_secret = ""
    token = dict()
    token_url = ""

    # @classmethod
    # def get_token(cls, secret=contact_secret):
    #     if secret not in cls.token.keys():
    #         r = cls.get_access_token(secret)
    #         cls.token[secret] = r["access_token"]
    #         return cls.token[secret]
    #
    # @classmethod
    # def get_access_token(cls, secret):
    #     r = requests.get(cls.token_url, params={"corpid":cls.corpid, "corpsecret": secret})
    #     return r.json()

    def get_access_token(self):
        r = self.request(method="get", url=self.token_url,params={"corpid": self.corpid, "corpsecret": self.contact_secret})
        return r.json()

