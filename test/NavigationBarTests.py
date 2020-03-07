from test.TestClass import TestClass
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class NavigationBarTests(TestClass):
    def __init__(self, driver, name="NavigationBar"):
        super().__init__(driver, name)

    def run_tests(self):
        self.tests["test_navigationbar_home"] = self.test_navigationbar_home()
        self.tests["test_navigationbar_projects"] = self.test_navigationbar_projects()
        self.tests["test_navigationbar_map"] = self.test_navigationbar_map()
        self.print_result()

    def test_navigationbar_home(self):
        current_url = self.driver.current_url

        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.LINK_TEXT, "Home"))
            )
        finally:
            element.click()
            self.passit = current_url != self.driver.current_url
            self.driver.back()
        return True

    def test_navigationbar_projects(self):
        current_url = self.driver.current_url

        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.LINK_TEXT, "Projecten"))
            )
        finally:
            element.click()
            self.passit = current_url != self.driver.current_url
            self.driver.back()
        return True

    def test_navigationbar_map(self):
        current_url = self.driver.current_url

        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.LINK_TEXT, "Map"))
            )
        finally:
            element.click()
            self.passit = current_url != self.driver.current_url
            self.driver.back()
        return True
