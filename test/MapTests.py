from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from test.TestClass import TestClass


class MapTests(TestClass):
    def __init__(self, driver, name="Map"):
        super().__init__(driver, name)

    def run(self):
        self.tests["test_map_listbutton"] = self.test_listbutton()
        self.tests["test_map_mapbutton"] = self.test_mapbutton()
        super().run()

    def test_listbutton(self):
        self.driver.get("http://localhost:8000/projecten/kaart")
        current_url = self.driver.current_url
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "listButton"))
            )
            element.click()
        except TimeoutException:
            return False
        finally:
            return current_url != self.driver.current_url

    def test_mapbutton(self):
        self.driver.get("http://localhost:8000/projecten/lijst")
        current_url = self.driver.current_url
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "mapButton"))
            )
            element.click()
        except TimeoutException:
            return False
        finally:
            self.passed = current_url != self.driver.current_url
            self.driver.back()
        return True
