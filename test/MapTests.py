from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from test.TestClass import TestClass


class MapTests(TestClass):
    def __init__(self, driver, name="Map"):
        super().__init__(driver, name)

    def run_tests(self):
        self.tests["test_map_listbutton"] = self.test_map_listbutton()
        self.tests["test_map_mapbutton"] = self.test_map_mapbutton()
        self.print_result()

    def test_map_listbutton(self):
        self.driver.get("http://localhost:8000/projecten/kaart")
        current_url = self.driver.current_url
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "listButton"))
            )
        finally:
            element.click()
            self.passit = current_url != self.driver.current_url
            self.driver.back()
        return True

    def test_map_mapbutton(self):
        self.driver.get("http://localhost:8000/projecten/lijst")
        current_url = self.driver.current_url

        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "mapButton"))
            )
        finally:
            element.click()
            self.passit = current_url != self.driver.current_url
            self.driver.back()
        return True
