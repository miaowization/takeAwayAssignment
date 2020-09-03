# -*- coding: utf-8 -*-
import allure
import pytest
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.firefox.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="Firefox")
    parser.addoption("--headless", action="store", default="True")

@pytest.fixture
def driver(request):
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
        return webdriver.Chrome(executable_path='/usr/local/bin/chromedriver',
                                options=options)

    def create_firefox_driver():
        options = Options()
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--start-maximized")
        options.headless = headless
        return webdriver.Firefox(executable_path='/usr/local/bin/geckodriver',
                                 firefox_binary='/usr/local/bin/firefox',
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