from pages.baseObject import BaseObject
from pages.baseElements import BaseElement
from selenium.webdriver.common.by import By


class HomePage(BaseObject):

    # Elements

    @property
    def virtual_keyboard_button(self):
        locator = (By.CSS_SELECTOR,'div[aria-label="Экранная клавиатура"]')
        return BaseElement(self.driver,locator)

    @property
    def virtual_keyboard(self):
        locator = (By.ID,'kbd')
        return BaseElement(self.driver,locator)
    

    # Methods

    def navigate(self):
        self.driver.get('http://google.com')
    

    def isAt(self):
        assert self.driver.title == 'Google'
        # В случае ошибки: assert self.driver.title == 'Google'
        # Как сделать показ возвращенной строки за место дублирования кода  - загадка.
    