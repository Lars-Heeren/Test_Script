from selenium.webdriver.common.action_chains import ActionChains

from test.TestClass import TestClass
from selenium.webdriver.common.keys import Keys
import time


class EditProjectTests(TestClass):
    def __init__(self, driver, name="Carrousel"):
        super().__init__(driver, name)

    def run(self):
        self.driver.get("http://localhost:8000/")
        super().run()

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
