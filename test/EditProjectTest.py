from selenium.webdriver.common.action_chains import ActionChains

from test.TestClass import TestClass
from selenium.webdriver.common.keys import Keys
import time


class EditProjectTests(TestClass):
    def __init__(self, driver, name="Carrousel"):
        super().__init__(driver, name)

    def run(self):
        self.driver.get("http://localhost:8000/")
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
        expectedURL = 'http://localhost:8000/home'
        currentURL =  self.driver.current_url
        print(expectedURL)
        print(currentURL)
        return expectedURL == currentURL


    # def test_back_button(self):
    #     self.driver.get("http://localhost:8000/")
    #     button = self.driver.find_element_by_id("previous")
    #     img1 = self.driver.find_element_by_css_selector(".primary_project img")
    #     frontimg = self.driver.find_element_by_class_name("primary_project")
    #
    #     hover = ActionChains(self.driver).move_to_element(frontimg)
    #     hover.perform()
    #     click = ActionChains(self.driver).click(button)
    #     click.perform()
    #     click.perform()
    #
    #     img2 = self.driver.find_element_by_css_selector(".primary_project img")
    #
    #     return img1 != img2
