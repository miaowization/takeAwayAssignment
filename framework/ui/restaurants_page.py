# -*- coding: utf-8 -*-
from framework.ui.base_page import BasePage


class RestaurantsPage(BasePage):
    locators = {
        'top_bar_post_code': (
        'XPATH', '//*[@class="topbar__title-container"]/button'),
        'search_restaurants_field': ('ID', 'irestaurantsearchstring-middle'),
        'first_restaurant': ('XPATH', '//*[not(contains(@class, "restaurant-hide"))][contains(@class, "restaurant__open")]')
        }

    def __init__(self, driver):
        super().__init__(driver)
