# -*- coding: utf-8 -*-
from seleniumpagefactory import PageFactory

from framework.ui.base_page import BasePage


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    locators = {
        "address_field": ('ID', 'imysearchstring'),
        }
