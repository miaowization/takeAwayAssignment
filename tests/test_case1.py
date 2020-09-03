# -*- coding: utf-8 -*-
import re

import allure
from selenium.webdriver.common.by import By

from framework.ui.checkout_page import CheckoutPage
from framework.ui.home_page import HomePage
from framework.ui.menu_page import MenuPage
from framework.ui.restaurants_page import RestaurantsPage


@allure.title('Basic order')
def test_case1(driver):
    with allure.step('Open homepage and setup address'):
        driver.get('https://www.thuisbezorgd.nl/en/')
        home_page = HomePage(driver)
        home_page.address_field.click()
        home_page.address_field.clear_text()
        home_page.address_field.send_keys('8888')
        home_page.wait_until_present(home_page.post_code)
        home_page.post_code.click()
        home_page.wait_until_present(home_page.post_code_alpha)
        home_page.post_code_alpha.click()
        home_page.wait_until_url(
            "https://www.thuisbezorgd.nl/en/order-takeaway-8888-alpha?search")

    with allure.step('Choose a restaurant'):
        restr_page = RestaurantsPage(driver)
        restr_page.wait_until_text_in_element((By.XPATH, "//*[@class='topbar__title-container']/button"),'8888-alpha')
        assert restr_page.top_bar_post_code.text == '8888-alpha'
        restr_page.search_restaurants_field.set_text('Shabu Shabu Test')
        restr_page.wait_until_present(restr_page.first_restaurant)
        restr_page.first_restaurant.click()
    with allure.step('Choose a dish from the menu'):
        menu_page = MenuPage(driver)
        menu_page.first_menu_option.click()
        menu_page.order_button.click()
    with allure.step('Make a chekout'):
        checkout_page = CheckoutPage(driver)
        checkout_page.wait_until_present(checkout_page.address)
        checkout_page.address.set_text('main street 2415')
        checkout_page.post_code.clear_text()
        checkout_page.post_code.set_text('8888AA')
        checkout_page.city.set_text('Enschede')
        checkout_page.name.set_text('TestUSer')
        checkout_page.phone_number.set_text('1234567890')
        checkout_page.email.set_text('testuser@test.test')
        checkout_page.delivery_time.click()
        checkout_page.delivery_time.select_element_by_value('asap')
        checkout_page.cash_payment.click()
        payments = str.split(checkout_page.amount_selector.text, '\n')
        payment = payments[1]
        checkout_page.amount_selector.click()
        checkout_page.amount_selector.select_element_by_text(payment)
        checkout_page.order_and_pay.click()
        checkout_page.wait_until_present(checkout_page.thanks_order)
        order_number = checkout_page.order_number.text
        assert order_number != ''
