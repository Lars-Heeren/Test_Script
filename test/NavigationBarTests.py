from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from test.TestClass import TestClass


class NavigationBarTests(TestClass):
    def __init__(self, driver, name="NavigationBar"):
        super().__init__(driver, name)

    def run(self):
        self.tests["test_navigationbar_homebutton"] = self.test_homebutton()
        self.tests["test_navigationbar_projectsbutton"] = self.test_projectsbutton()
        super().run()

    def test_homebutton(self):
        self.driver.get("http://localhost:8000/")
        current_url = self.driver.current_url
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.LINK_TEXT, "Home"))
            )
            element.click()
        except TimeoutException:
            return False
        finally:
            return current_url != self.driver.current_url

    def test_projectsbutton(self):
        self.driver.get("http://localhost:8000/")
        current_url = self.driver.current_url
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.LINK_TEXT, "Projecten"))
            )
            element.click()
        except TimeoutException:
            return False
        finally:
            return current_url != self.driver.current_url
