import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome")
    parser.addoption("--base_url", action="store", default="https://www.cleartrip.com")

@pytest.fixture(scope='class')
def setup(request):
    browser = request.config.getoption("browser_name")
    baseURL = request.config.getoption('base_url')
    if browser.lower() == 'chrome':
        driver = webdriver.Chrome()
    elif browser.lower() == 'firefox':
        driver = webdriver.Firefox()
    else:
        driver = webdriver.Safari()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get(baseURL)
    request.cls.driver = driver
    request.cls.baseURL = baseURL
    yield
    driver.close()
