import os
import time

import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common import exceptions

CHROME_DRIVER = "\\chromedriver.exe"
CHROME_PATH = "C:\\Users\\jeroe\\OneDrive\\Documenten\\Test_Script\\chrome"
options = Options()


class AutoFill:

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=CHROME_PATH + CHROME_DRIVER, options=options)
        self.login()

    def login(self):
        is_loading = True

        while is_loading:
            try:
                self.driver.get("http://localhost:8000/login")

                link = self.driver.find_element_by_css_selector('ul.login_search li a')
                link.click()
                emailInput = self.driver.find_element_by_id('email')
                emailInput.send_keys('pascal@gmail.com')

                passwordInput = self.driver.find_element_by_id('password')
                passwordInput.send_keys('weerbaarBrabant')

                submit = self.driver.find_element_by_css_selector('button')
                submit.click()
                is_loading = False
            except selenium.common.exceptions.NoSuchElementException:
                is_loading = True

