# -*- coding: utf-8 -*-
import allure
import pytest
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.firefox.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from tests import get_test_data


def pytest_addoption(parser):
    """This method adds options for pytest runner"""
    parser.addoption("--browser", action="store", default="Firefox")
    parser.addoption("--headless", action="store", default="True")


@pytest.fixture
def driver(request):
    """This method creates webdriver object to use in tests.
    webdriver can represent ChromeDriver of Geckodriver (for Firefox)
    and can either be an ordinary browser or a headless browser.
    Those options can be set in cmd when running pytest
    Example:
    pytest tests --headless True --browser 'Firefox'
    pytest tests --headless False --browser 'Chrome'
    """
    if request.config.getoption('--headless') == 'True':
        headless = True
    else:
        headless = False
    browser = request.config.getoption('--browser')

    def create_chrome_driver():
        options = ChromeOptions()
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--start-maximized")
        options.headless = headless
        return webdriver.Chrome(executable_path=ChromeDriverManager().install(),
                                options=options)

    def create_firefox_driver():
        options = Options()
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--start-maximized")
        options.headless = headless
        return webdriver.Firefox(executable_path=GeckoDriverManager().install(),
                                 options=options)

    driver_ = None
    if browser == 'Chrome':
        driver_ = create_chrome_driver()
    elif browser == 'Firefox':
        driver_ = create_firefox_driver()
    driver_.set_script_timeout(10)
    driver_.set_page_load_timeout(30)

    def tear_down():
        call_result = getattr(request.node, 'rep_call', None)
        if call_result and call_result.failed:
            allure.attach(driver_.get_screenshot_as_png(),
                          attachment_type=allure.attachment_type.PNG)
        driver_.quit()

    request.addfinalizer(tear_down)
    yield driver_


def pytest_generate_tests(metafunc):
    """This method links testcase in folder tests
    to the test data in folder resources and creates data fixture"""
    def parametrize(test_data):
        for key, value in test_data.items():
            param_keys = [k.strip() for k in key.split(',')]
            diff = set(param_keys) - set(metafunc.fixturenames)
            if diff:
                raise AssertionError(f'{diff} fixtures were set in JSON data, '
                                     'but not found in test')
            parameters = value if isinstance(value, list) else [value]
            metafunc.parametrize(key, parameters)
    data = get_test_data(metafunc.definition)
    if data:
        parametrize(data)
