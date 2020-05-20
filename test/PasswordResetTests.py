from test.TestClass import TestClass
from selenium.webdriver.common.keys import Keys
import time

EXPECTED_URL = 'http://projectagile.nl/home'


class PasswordResetTests(TestClass):
    def __init__(self, driver, name="Login"):
        super().__init__(driver, name)

    def run(self):
        self.driver.get("http://projectagile.nl/login")
        self.tests["passwordResetFailure"] = self.passwordResetsFailure()
        self.tests["passwordResetSucces"] = self.passwordResetsSucces()
        super().run()

    def passwordResetsFailure(self):
        time.sleep(2)
        link = self.driver.find_element_by_class_name('btn-link')
        link.click()
        time.sleep(3)
        emailInput = self.driver.find_element_by_id('email')
        emailInput.send_keys('TestBrabant999@gmail.com')

        submit = self.driver.find_element_by_css_selector('button')
        submit.click()
        time.sleep(3)

        try:
            alert = self.driver.find_element_by_class_name('invalid-feedback')
            if alert == None:
                return False
            return True
        except:
            return False

    def passwordResetsSucces(self):
        emailInput = self.driver.find_element_by_id('email')
        emailInput.clear()
        emailInput.send_keys('bbfire@gmail.com')

        submit = self.driver.find_element_by_css_selector('button')
        submit.click()
        time.sleep(8)

        try:
            alert = self.driver.find_element_by_class_name('alert-success')
            if alert == None:
                return False
            return True
        except:
            return False

