from selenium.webdriver.common.action_chains import ActionChains

from test.TestClass import TestClass
from selenium.webdriver.common.keys import Keys
import time


class AddProjectTest(TestClass):
    def __init__(self, driver, name="EditProject"):
        super().__init__(driver, name)
        self.elemne_tname
        self.elements = {}
        self.inputs_true = {}
        self.inputs_false = {}

    def run(self):
        self.driver.get("http://localhost:8000/projects/add")
        self.setup()
        self.tests["edit"] = self.editTests()
        super().run()

    def setup(self):
        time.sleep(3)

        self.elements["title"](self.driver.find_elements_by_name("titel"))
        self.elements["about"](self.driver.find_elements_by_name("about"))
        self.elements["description"](self.driver.find_elements_by_name("description"))

    def editTests(self):
        pass




