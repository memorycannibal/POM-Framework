from time import sleep
from pages.homePage import HomePage

def test_open(Driver):
    homepage = HomePage(Driver)
    homepage.navigate()
    homepage.isAt()

def test_open_keyboard(Driver):
    homepage = HomePage(Driver)
    homepage.navigate()
    homepage.isAt()
    homepage.virtual_keyboard_button.click()
    assert homepage.virtual_keyboard.visible() == True