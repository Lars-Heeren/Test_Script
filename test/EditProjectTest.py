from selenium.webdriver.common.action_chains import ActionChains

from test.TestClass import TestClass
from selenium.webdriver.common.keys import Keys
import time


class EditProjectTests(TestClass):
    def __init__(self, driver, name="EditProject"):
        super().__init__(driver, name)

    def run(self):
        self.driver.get("http://localhost:8000/")
        self.tests["edit"] = self.editTests()
        super().run()

    def setup(self):
        pass;

    def editTests(self):
        pass;



