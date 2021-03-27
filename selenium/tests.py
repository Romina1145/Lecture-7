import os
# The OS module in Python provides functions for interacting with the operating system.
import pathlib

import unittest

from selenium import webdriver

# Finds the Uniform Resource Identifier of a file for target a specific page


def file_uri(filename):
    return pathlib.Path(os.path.abspath(filename)).as_uri()


# Sets up web driver using Google Chrome
driver = webdriver.Chrome(
    executable_path="/Users/rominaionascu/Downloads/chromedriver")


class WebpageTests(unittest.TestCase):

    def test_title(self):
        """Make sure the title is correct"""
        driver.get(file_uri("counter.html"))
        self.assertEqual(driver.title, "Counter")

    def test_increase(self):
        """Make sure header updated to 1 after 1 click of increase button"""
        driver.get(file_uri("counter.html"))
        increase = driver.find_element_by_id("increase")
        increase.click()
        self.assertEqual(driver.find_element_by_tag_name("h1").text, "1")

    def test_multiple_increase(self):
        """Make sure header updated to 3 after 3 clicks of increase button"""
        driver.get(file_uri("counter.html"))
        increase = driver.find_element_by_id("increase")
        for i in range(3):
            increase.click()
        self.assertEqual(driver.find_element_by_tag_name("h1").text, "3")


if __name__ == "__main__":
    unittest.main()
