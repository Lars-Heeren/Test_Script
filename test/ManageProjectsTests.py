from selenium.webdriver.common.action_chains import ActionChains

from test.TestClass import TestClass


class ManageProjectsTest(TestClass):
    def __init__(self, driver, name="ManageProjects"):
        super().__init__(driver, name)

    def run(self):
        self.driver.get("http://localhost:8000/projecten/productowner/lijst")
        super().run()

    def
