import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome', \
                    help='\nChoose browser: chrome or firefox\n')
    parser.addoption('--language', action='store',default=None,\
                    help="Choose language: ru, en, ... (etc.)")

@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption('browser_name')
    user_language = request.config.getoption('language')
    browser = None
    if browser_name == 'chrome':
        print("\nstarting chrome browser for tests...\n")
        options = webdriver.ChromeOptions()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        options.add_argument("--start-maximized") 
        browser = webdriver.Chrome(options=options)
    elif browser_name =='firefox':
        print("\nstarting firefox for test...\n")   
        browser = webdriver.Firefox()
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser...\n")
    browser.quit()

    #