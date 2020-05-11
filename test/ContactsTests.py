from Utilities.RandomStringGenerator import RandomStringGenerator
from test.TestClass import TestClass
from selenium.webdriver.common.keys import Keys
import time


class ContactsTests(TestClass):
    def __init__(self, driver, name="AddProject"):
        super().__init__(driver, name)
        self.elements = []

    def run(self):
        self.driver.get("http://127.0.0.1:8000/contacten")
        self.tests["submit_complete_add"] = self.submit_complete_add()
        super().run()

    def submit_complete_add(self):

        test_data = RandomStringGenerator().getRandomString(20)

        time.sleep(3)
        self.driver.find_element_by_class_name("add-button-link")[0].click()
        self.driver.find_element_by_id("firstname").send_keys(test_data)
        self.driver.find_element_by_id("lastname").send_keys(test_data)
        self.driver.find_element_by_id("email").send_keys("seleniumtest@gmail.com")
        self.driver.find_element_by_id("address").send_keys(test_data)
        self.driver.find_element_by_id("zipcode").send_keys(test_data)
        self.driver.find_element_by_id("city").send_keys(test_data)
        self.driver.find_element_by_id("web_link").send_keys(test_data)
        time.sleep(1)
        self.driver.find_element_by_css_selector("button[type='submit']").click()
        time.sleep(2)
        deleteLocation = self.driver.find_element_by_class_name("add-button-link")
        if isinstance(deleteLocation, list):
            deleteLocation[0].click()
        else:
            deleteLocation.click()
        time.sleep(2)

        result = False
        if self.driver.find_element_by_css_selector('h1').text == test_data:
            result = True

        self.clearData(test_data)
        return result

    def clearData(self, testdata):
        url = self.driver.current_url
        urlParts = url.split('/')
        id = urlParts[len(urlParts) - 1]
        self.driver.get("http://localhost:8000/projecten/productowner/lijst")
        search = self.driver.find_element_by_name("search")
        search.send_keys(testdata)
        search.send_keys(Keys.RETURN)
        time.sleep(2)
        self.driver.find_element_by_id("edit-button0").click()

