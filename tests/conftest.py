# -*- coding: utf-8 -*-
import allure
import pytest
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def driver(request):
    options = ChromeOptions()
    remote = True

    def create_remote_driver():
        options.add_argument('--no-sandbox')
        options.add_argument('-remote-debugging-port=9222')
        options.headless = True
        command_executor = 'http://localhost:4444/wd/hub'
        return webdriver.Remote(command_executor, desired_capabilities=options.to_capabilities())

    def create_local_driver():
        return webdriver.Chrome(
            executable_path=ChromeDriverManager().install(), options=options)

    driver_ = None
    if remote:
        driver_ = create_remote_driver()
    else:
        driver_ = create_local_driver()
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