import requests


class HttpManager():

    Headers = {}
    Cookies = {}
    response = None

    def __init__(self):
        pass

    def get(self, url, inlineData = {}):
        self.response = requests.get(url, verify=False,  params=inlineData, cookies=self.Cookies, headers=self.Headers)
        self.Cookies = self.response.cookies
        return self.response
