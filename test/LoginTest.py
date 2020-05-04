from selenium.webdriver.common.action_chains import ActionChains
from test.TestClass import TestClass
from selenium.webdriver.common.keys import Keys
import time

EXPECTED_URL = 'http://localhost:8000/home'


class LoginTest(TestClass):
    def __init__(self, driver, name="Login"):
        super().__init__(driver, name)

    def run(self):
        self.driver.get("http://localhost:8000/login")
        self.tests["login"] = self.login()
        super().run()

    def login(self):
        link = self.driver.find_element_by_css_selector('ul.login_search li a')
        link.click()
        time.sleep(3)
        emailInput = self.driver.find_element_by_id('email')
        emailInput.send_keys('pascal@gmail.com')

        passwordInput = self.driver.find_element_by_id('password')
        passwordInput.send_keys('weerbaarBrabant')

        submit = self.driver.find_element_by_css_selector('button')
        submit.click()
        time.sleep(3)

        return EXPECTED_URL == self.driver.current_url