from pages.httpManager import HttpManager

class BaseObject(object):
    driver = None

    def __init__(self,driver):
        self.driver = driver
       
class BaseOApi(object):
    api = None

    def __init__(self):
        self.api = HttpManager()
        