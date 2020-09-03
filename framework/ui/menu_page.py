# -*- coding: utf-8 -*-
from framework.ui.base_page import BasePage


class MenuPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    locators = {
        'first_menu_option': ('XPATH', '//*[contains(@class, "add-to-basket-button")]'),
        'order_button': ('XPATH', '//*[contains(@class,"order-button")]'),
        'side_dish': ('XPATH', '//*[@class="sidedishformcontainer"]'),
        'add_value': ('XPATH', '//*[contains(@class,"sidedish-add-button")]')
        }