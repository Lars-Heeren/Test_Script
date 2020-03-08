from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from test.TestClass import TestClass


class NewProjectsTests(TestClass):
    # Deze tests moeten nog uitgebreider, met dat je werkelijk ook op de pagina terecht komt
    def __init__(self, driver, name="NewProjects"):
        super().__init__(driver, name)

    def run(self):
        self.tests["test_newprojects1_link"] = self.test_newprojects1_link()
        self.tests["test_newprojects2_link"] = self.test_newprojects2_link()
        self.tests["test_newprojects3_link"] = self.test_newprojects3_link()
        self.tests["test_newprojects4_link"] = self.test_newprojects4_link()
        super().run()

    def test_newprojects1_link(self):
        self.driver.get("http://localhost:8000/")
        current_url = self.driver.current_url
        element = self.driver.find_elements_by_css_selector(".new_project_container a")[0]
        element.click()
        return current_url != self.driver.current_url

    def test_newprojects2_link(self):
        self.driver.get("http://localhost:8000/")
        current_url = self.driver.current_url
        element = self.driver.find_elements_by_css_selector(".new_project_container a")[1]
        element.click()
        return current_url != self.driver.current_url

    def test_newprojects3_link(self):
        self.driver.get("http://localhost:8000/")
        current_url = self.driver.current_url
        element = self.driver.find_elements_by_css_selector(".new_project_container a")[2]
        element.click()
        return current_url != self.driver.current_url

    def test_newprojects4_link(self):
        self.driver.get("http://localhost:8000/")
        current_url = self.driver.current_url
        element = self.driver.find_elements_by_css_selector(".new_project_container a")[3]
        element.click()
        return current_url != self.driver.current_url
