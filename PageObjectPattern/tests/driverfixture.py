from selenium import webdriver
from pytest import fixture

def pytest_addoption(parser):
    parser.addoption(
        "--browser", 
        action="store",
        default="chrome",
        help="browser to run. example: --browser chrome ; --browser firefox"
    )

SUPPORTED_BROWSERS = [
    'chrome',
    'firefox'
]


@fixture(scope="function")
def Driver(request):
    browserArg =  request.config.getoption("--browser")
    if browserArg in SUPPORTED_BROWSERS:

        if browserArg == 'chrome':
            driver = webdriver.Chrome()
            yield driver
            driver.quit()

        if browserArg == 'firefox':
            driver = webdriver.Firefox()
            yield driver 
            driver.quit()   

    # elif  browserArg == None:
    #         driver = webdriver.Chrome()
    #         yield driver
    #         driver.quit()
    else: 
        raise Exception('invalid browser name')