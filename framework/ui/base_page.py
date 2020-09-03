# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from seleniumpagefactory import PageFactory
from selenium.webdriver.support import expected_conditions as EC



class BasePage(PageFactory):

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    def wait_until_element_present(self, locator):
        self.wait.until(EC.presence_of_element_located(locator))

    def wait_until_text_in_element(self, locator, text):
        self.wait.until(EC.text_to_be_present_in_element(locator, text))

    def wait_until_present(self, element):
        self.wait.until(EC.presence_of_element_located((element._locator[0],
                                                       element._locator[1])))

    def wait_until_invisible(self, element):
        self.wait.until(EC.invisibility_of_element_located((element._locator[0],
                                                       element._locator[1])))