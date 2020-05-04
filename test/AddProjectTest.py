from selenium.webdriver.common.action_chains import ActionChains

from Utilities.RandomStringGenerator import RandomStringGenerator
from test.TestClass import TestClass
from selenium.webdriver.common.keys import Keys
import time
from Utilities.DataBase import DataBase


class AddProjectTest(TestClass):
    def __init__(self, driver, name="AddProject"):
        super().__init__(driver, name)
        self.elements = []

    def run(self):
        self.driver.get("http://localhost:8000/projects/add")
        self.tests["submit_complete"] = self.submit_complete()
        super().run()

    def submit_complete(self):

        test_data = RandomStringGenerator().getRandomString(20)

        time.sleep(3)
        self.driver.find_element_by_name("title").send_keys(test_data)
        self.driver.find_element_by_name("about").send_keys(test_data)
        self.driver.find_element_by_name("description").send_keys(test_data)
        self.driver.find_element_by_name("image_link").send_keys(test_data)
        self.driver.find_element_by_name("result_ac").send_keys(test_data)
        self.driver.find_element_by_name("startdate").send_keys("10/10/2010")
        self.driver.find_element_by_name("enddate").send_keys("15/15/2015")
        self.driver.find_element_by_name("locations[]").find_elements_by_tag_name('option')[0].click()
        self.driver.find_element_by_name("organizations[]").find_elements_by_tag_name('option')[0].click()
        self.driver.find_element_by_id("1").click()
        self.driver.find_element_by_css_selector("label[for='sdgnumber1']").click()
        self.driver.find_element_by_css_selector("button[type='submit']").click()
        time.sleep(3)
        if self.driver.find_element_by_css_selector('h1').text == test_data:
            return True
        return False
