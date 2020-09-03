# -*- coding: utf-8 -*-
from seleniumpagefactory import PageFactory

from framework.ui.base_page import BasePage


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    locators = {
        "address_field": ('XPATH', '//input[@id="imysearchstring"]'),
        "post_code": ('XPATH', '//a[@data-name="8888"]'),
        "post_code_alpha": ('XPATH', '//a[contains(@data-href,"8888-alpha")]')
        }
