# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from seleniumpagefactory import PageFactory
from selenium.webdriver.support import expected_conditions as EC


class BasePage(PageFactory):
    """This is base class representing page object"""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    def wait_until_element_present(self, locator):
        """
        This method waits for specific amount of seconds
        until the By class object is present in DOM
        """
        self.wait.until(EC.presence_of_element_located(locator))

    def wait_until_text_in_element(self, element, text):
        """
        This method waits for specific amount of seconds
        until the text in element is present
        """
        self.wait.until(EC.text_to_be_present_in_element((element._locator[0],
                                                          element._locator[1]),
                                                         text))

    def wait_until_present(self, element):
        """
        This method waits for specific amount of seconds
        until the text in webElement is present
        """
        self.wait.until(EC.presence_of_element_located((element._locator[0],
                                                        element._locator[1])))

    def wait_until_invisible(self, element):
        """
        This method waits for specific amount of seconds
        until the text in webElement is no longer visible
        """
        self.wait.until(
            EC.invisibility_of_element_located((element._locator[0],
                                                element._locator[1])))

    def wait_until_url(self, url):
        """
        This method waits for specific amount of seconds
        until the url in the browser is equal to the 'url' value
        """
        self.wait.until(EC.url_to_be(url))

    def wait_until_clickable(self, element):
        """
        This method waits for specific amount of seconds
        until the webElement is available to click
        """
        self.wait.until(
            EC.element_to_be_clickable(
                (element._locator[0], element._locator[1])))
