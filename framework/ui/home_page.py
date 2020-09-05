# -*- coding: utf-8 -*-
from seleniumpagefactory import PageFactory

from framework.ui.base_page import BasePage


class HomePage(BasePage):
    locators = {}

    def __init__(self,
                 driver,
                 post_code='8888',
                 post_code_second='8888-beta'):
        self.locators = {
            "address_field": ('XPATH', '//input[@id="imysearchstring"]'),
            "post_code": ('XPATH', f'//a[@data-name="{post_code}"]'),
            "post_code_second": (
                'XPATH', f'//a[contains(@data-href,"{post_code_second}")]')
            }
        super().__init__(driver)
