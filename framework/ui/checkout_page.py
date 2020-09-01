# -*- coding: utf-8 -*-
from framework.ui.base_page import BasePage


class CheckoutPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    locators = {
        'address': ('ID', 'iaddress'),
        'post_code' : ('ID', 'ipostcode'),
        'city' : ('ID', 'itown'),
        'name' : ('ID', 'isurname'),
        'phone_number' : ('ID', 'iphonenumber'),
        'email' : ('ID', 'iemail'),
        'delivery_time' : ('ID', 'ideliverytime'),
        'amount': ('XPATH', '//*[contains(@class,"cart-row row-sum")][@style!="display:none"]/*[contains(@class,"cart-sum-price")]'),
        'payment_selector' : ('ID', 'iselectpayment'),
        'cash_payment' : ('XPATH', '//label[text()="Cash payment"]'),
        'amount_selector': ('ID', 'ipayswith'),
        'order_and_pay': ('XPATH', '//input[@value="Order and pay"]'),
        'order_number': ('CLASS_NAME', 'order-purchaseid'),
        'thanks_order': ('XPATH', '//*[text()="Thank you for your order!"]')
        }