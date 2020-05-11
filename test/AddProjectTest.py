from Utilities.RandomStringGenerator import RandomStringGenerator
from test.TestClass import TestClass
from selenium.webdriver.common.keys import Keys
import time


class AddProjectTest(TestClass):
    def __init__(self, driver, name="AddProject"):
        super().__init__(driver, name)
        self.elements = []

    def run(self):
        self.driver.get("http://localhost:8000/projecten/projecteigenaar/toevoegen")
        self.tests["submit_complete"] = self.submit_complete()
        super().run()

    def submit_complete(self):

        test_data = RandomStringGenerator().getRandomString(20)

        time.sleep(3)
        self.driver.find_element_by_name("title").send_keys(test_data)
        self.driver.find_element_by_name("about").send_keys(test_data)
        self.driver.find_element_by_name("description").send_keys(test_data)
        self.driver.find_element_by_name("image_link").send_keys(test_data)
        self.driver.find_element_by_name("result_ac").send_keys(test_data)
        self.driver.find_element_by_name("startdate").send_keys("10/10/2010")
        self.driver.find_element_by_name("enddate").send_keys("15/15/2015")

        self.driver.find_element_by_id("inputAddLocation").send_keys("Berlicum")
        self.driver.find_element_by_id("locationAdd").click()
        time.sleep(2)
        deleteLocation = self.driver.find_element_by_id("deleteLocationButton")
        if isinstance(deleteLocation, list):
            deleteLocation[0].click()
        else:
            deleteLocation.click()
        time.sleep(2)
        self.driver.find_element_by_id("locationAdd").click()

        self.driver.find_element_by_id("inputAddOrganization").send_keys("Verbeek Solutions")
        self.driver.find_element_by_id("organizationAdd").click()
        time.sleep(2)
        deleteOrg = self.driver.find_element_by_id("deleteOrganizationButton")
        if isinstance(deleteOrg, list):
            deleteOrg[0].click()
        else:
            deleteOrg.click()

        time.sleep(2)
        self.driver.find_element_by_id("organizationAdd").click()

        self.driver.find_element_by_id("1").click()
        self.driver.find_element_by_css_selector("label[for='sdgnumber1']").click()
        self.driver.find_element_by_css_selector("button[type='submit']").click()
        time.sleep(3)

        result = False
        if self.driver.find_element_by_css_selector('h1').text == test_data:
            result = True

        self.clearData(test_data)
        return result

    def clearData(self, testdata):
        url = self.driver.current_url
        urlParts = url.split('/')
        id = urlParts[len(urlParts) - 1]
        self.driver.get("http://localhost:8000/projecten/projecteigenaar/lijst")
        search = self.driver.find_element_by_name("search")
        search.send_keys(testdata)
        search.send_keys(Keys.RETURN)
        time.sleep(2)
        self.driver.find_element_by_id("edit-button0").click()

