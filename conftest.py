from selenium import webdriver
import pytest
import allure

@allure.step('Открываем браузер')
@pytest.fixture(params=['chrome', 'firefox'])
def driver(request):
    browser_name = request.param
    browser = None
    if browser_name == 'chrome':
        browser = webdriver.Chrome()
    elif browser_name == 'firefox':
        browser = webdriver.Firefox()
    else:
        ValueError('InvalidValue')
    browser.maximize_window()
    yield browser
    browser.quit()