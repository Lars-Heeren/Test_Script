from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from test.TestClass import TestClass

class NewProjectsTests(TestClass):

    def __init__(self, driver, name="NewProjects"):
        super().__init__(driver, name)


    def run_tests(self):
        self.tests["test_NewProjects1_Link"] = self.test_NewProjects1_Link()
        self.tests["test_NewProjects2_Link"] = self.test_NewProjects2_Link()
        self.tests["test_NewProjects3_Link"] = self.test_NewProjects3_Link()
        self.tests["test_NewProjects4_Link"] = self.test_NewProjects4_Link()
        self.print_result()

    def print_result(self):
        super().print_result()


    def print_failure(self):
        super().print_failure()
        print(self.result)

    def test_NewProjects1_Link(self):
        result = []
        expectedurl = "http://localhost:8000/projects/display"
        # door iedere link gaan en kijken of er iets veranderd qua url
        elems = []
        elems = self.driver.find_elements_by_css_selector(".new_project_container a")

        elems[0].click()
        url = self.driver.current_url
        url = url.split("/")[0]
        result.append(url == expectedurl)
        self.driver.back()
        return result

    def test_NewProjects2_Link(self):
        result = []
        expectedurl = "http://localhost:8000/projects/display"
        # door iedere link gaan en kijken of er iets veranderd qua url
        elems = []
        elems = self.driver.find_elements_by_css_selector(".new_project_container a")

        elems[1].click()
        url = self.driver.current_url
        url = url.split("/")[0]
        result.append(url == expectedurl)
        self.driver.back()
        return result

    def test_NewProjects3_Link(self):
        result = []
        expectedurl = "http://localhost:8000/projects/display"
        # door iedere link gaan en kijken of er iets veranderd qua url
        elems = []
        elems = self.driver.find_elements_by_css_selector(".new_project_container a")

        elems[2].click()
        url = self.driver.current_url
        url = url.split("/")[0]
        result.append(url == expectedurl)
        self.driver.back()
        return result

    def test_NewProjects4_Link(self):
        result = []
        expectedurl = "http://localhost:8000/projects/display"
        # door iedere link gaan en kijken of er iets veranderd qua url
        elems = []
        elems = self.driver.find_elements_by_css_selector(".new_project_container a")

        elems[3].click()
        url = self.driver.current_url
        url = url.split("/")[0]
        result.append(url == expectedurl)
        self.driver.back()
        return result