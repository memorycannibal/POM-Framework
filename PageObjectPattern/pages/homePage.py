from pages.baseObject import BaseObject

class HomePage(BaseObject):

    def navigate(self):
        self.driver.get('http://google.com')

    def isAt(self):
        pass