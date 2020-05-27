from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import time

from test.TestClass import TestClass

class ListTests(TestClass):
    def __init__(self, driver, name="List"):
        super().__init__(driver, name)

    def run(self):
        self.tests["test_list_searchbar"] = self.test_searchbar()
        self.tests["test_list_showcased"] = self.test_showcased()
        self.tests["test_list_created_after"] = self.test_created_after()
        self.tests["test_list_created_before"] = self.test_created_before()
        self.tests["test_list_category"] = self.test_category()
        super().run()

    def test_searchbar(self):
        self.driver.get("http://localhost:8000/projecten/lijst")
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.NAME, "search"))
            )
            element.send_keys("oirschot\n")
        except TimeoutException:
            return False
        finally:
            return "search=oirschot" in self.driver.current_url

    def test_showcased(self):
        self.driver.get("http://localhost:8000/projecten/lijst")
        action = ActionChains(self.driver)
        try:
            firstLevelMenu = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "dropdownButton"))
            )

            secondLevelMenu = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.NAME, "Showcased"))
            )

            thirdLevelMenu = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "filterSubmit"))
            )

            action.move_to_element(firstLevelMenu).click(secondLevelMenu).click(thirdLevelMenu).perform()
            
        except TimeoutException:
            return False
        finally:
            return "Showcased=on" in self.driver.current_url

    def test_created_after(self):
        self.driver.get("http://localhost:8000/projecten/lijst")
        action = ActionChains(self.driver)
        try:
            firstLevelMenu = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "dropdownButton"))
            )

            secondLevelMenu = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.NAME, "CreatedAfter"))
            )

            thirdLevelMenu = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "filterSubmit"))
            )


            action.move_to_element(firstLevelMenu).perform()
            secondLevelMenu.send_keys("18032020")
            action.click(thirdLevelMenu).perform()

            time.sleep(4)
            
        except TimeoutException:
            return False
        finally:
            return "CreatedAfter=2020-03-18" in self.driver.current_url

    def test_created_before(self):
        self.driver.get("http://localhost:8000/projecten/lijst")
        action = ActionChains(self.driver)
        try:
            firstLevelMenu = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "dropdownButton"))
            )

            secondLevelMenu = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.NAME, "CreatedBefore"))
            )

            thirdLevelMenu = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "filterSubmit"))
            )

            action.move_to_element(firstLevelMenu).perform()
            secondLevelMenu.send_keys("30062020")
            action.click(thirdLevelMenu).perform()

            time.sleep(4)
            
        except TimeoutException:
            return False
        finally:
            return "CreatedBefore=2020-06-30" in self.driver.current_url

    def test_category(self):
        self.driver.get("http://localhost:8000/projecten/lijst")
        action = ActionChains(self.driver)
        try:
            firstLevelMenu = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "dropdownButton"))
            )

            secondLevelMenu = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//select[@id='status[]']/option[text()='Gaande']"))
            )

            thirdLevelMenu = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "filterSubmit"))
            )

            action.move_to_element(firstLevelMenu).perform()
            action.click(secondLevelMenu).perform()
            action.click(thirdLevelMenu).perform()
            
        except TimeoutException:
            return False
        finally:
            return "Gaande" in self.driver.current_url