from pages.homePage import HomePage,HomePageApi
from pytest import mark

@mark.smoke
def test_open(Driver):
    hp = HomePage(Driver)
    hp.navigate()
    hp.isAt()

@mark.ui
def test_open_keyboard(Driver):
    hp = HomePage(Driver)
    hp.navigate()
    hp.isAt()
    hp.virtual_keyboard_button.click()
    assert hp.virtual_keyboard.visible() == True


@mark.api
def test_api_live_search():
     hpApi = HomePageApi()
     hpApi.get_live_search('testing')
     assert hpApi.statusCode == 200