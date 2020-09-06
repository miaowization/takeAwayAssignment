# -*- coding: utf-8 -*-
from os import environ

import allure

from configs.autotests_config import BASE_URL
from framework.ui.checkout_page import CheckoutPage
from framework.ui.home_page import HomePage
from framework.ui.menu_page import MenuPage
from framework.ui.restaurants_page import RestaurantsPage


@allure.title('Basic order')
def test_case1(driver, data):
    with allure.step('Open homepage and setup address'):
        driver.get(BASE_URL)
        home_page = HomePage(driver,
                             post_code=data['post_code'],
                             post_code_second=data['post_code_second'])
        home_page.address_field.click()
        home_page.address_field.clear_text()
        home_page.address_field.send_keys(data['post_code'])
        home_page.wait_until_present(home_page.post_code)
        home_page.post_code.click()
        home_page.wait_until_present(home_page.post_code_second)
        home_page.post_code_second.click()
        home_page.wait_until_url(f"{BASE_URL}/order-takeaway-{data['post_code_second']}?search")

    with allure.step('Choose a restaurant'):
        restr_page = RestaurantsPage(driver)
        restr_page.wait_until_text_in_element(restr_page.top_bar,
                                              data['post_code_second'])
        assert restr_page.top_bar_post_code.text == data['post_code_second']
        restr_page.search_restaurants_field.set_text(data['restaurant_name'])
        restr_page.wait_until_present(restr_page.first_restaurant)
        restr_page.first_restaurant.click()
    with allure.step('Choose a dish from the menu'):
        menu_page = MenuPage(driver)
        menu_page.first_menu_option.click()
        # when a dish has a side dish there can be problems
        # clicking it sometimes,
        # I didn't find a workaround with this.
        try:
            if menu_page.side_dish.is_displayed():
                menu_page.add_value.is_displayed()
                menu_page.add_value.click()
        except:
            pass
        menu_page.order_button.click()
    with allure.step('Make a checkout'):
        checkout_page = CheckoutPage(driver)
        checkout_page.wait_until_present(checkout_page.address)
        checkout_page.address.set_text(data['address_checkout'])
        checkout_page.post_code.clear_text()
        checkout_page.post_code.set_text(data['post_code_checkout'])
        checkout_page.city.set_text(data['city_checkout'])
        checkout_page.name.set_text(data['name_checkout'])
        checkout_page.phone_number.set_text(data['phone_checkout'])
        checkout_page.email.set_text(data['email_checkout'])
        checkout_page.delivery_time.click()
        checkout_page.delivery_time.select_element_by_value(
            data['delivery_time'])
        checkout_page.cash_payment.click()
        payments = str.split(checkout_page.amount_selector.text, '\n')
        payment = payments[1]
        checkout_page.amount_selector.click()
        checkout_page.amount_selector.select_element_by_text(payment)
        checkout_page.order_and_pay.click()
        checkout_page.wait_until_present(checkout_page.thanks_order)
        order_number = checkout_page.order_number.text
        assert order_number != ''
