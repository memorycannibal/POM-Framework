from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

class BaseElement():
    elementType = None

    def __init__(self,driver,locator):
        self.webelement = WebDriverWait(driver,5).until(lambda driver : driver.find_element(*locator))
        return None

    def send_keys(self,val):
        self.webelement.send_keys(val)

    def click(self):
        self.webelement.click()

    def visible(self):
        return self.webelement.is_displayed()


    