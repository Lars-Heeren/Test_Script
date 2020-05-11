from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from Utilities.RandomStringGenerator import RandomStringGenerator
from test.TestClass import TestClass
from selenium.webdriver.common.keys import Keys
import time


class ContactsTests(TestClass):
    def __init__(self, driver, name="ContactTest"):
        super().__init__(driver, name)
        self.elements = []

    def run(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Contacten beheren"))
        )
        element.click()

        self.tests["submit_complete_add"] = self.submit_complete_add()
        super().run()

    def submit_complete_add(self):

        test_data = RandomStringGenerator().getRandomString(20)

        time.sleep(2)
        addContact = self.driver.find_element_by_class_name("add-button-link")
        if isinstance(addContact, list):
            addContact[0].click()
        else:
            addContact.click()
        time.sleep(2)
        self.driver.find_element_by_id("firstname").send_keys(test_data)
        self.driver.find_element_by_id("lastname").send_keys(test_data)
        self.driver.find_element_by_id("email").send_keys("seleniumtest@gmail.com")
        self.driver.find_element_by_id("address").send_keys(test_data)
        self.driver.find_element_by_id("zipcode").send_keys(test_data)
        self.driver.find_element_by_id("city").send_keys(test_data)
        self.driver.find_element_by_id("web_link").send_keys(test_data)
        time.sleep(1)
        self.driver.find_element_by_css_selector("button[type='submit']").click()
        time.sleep(3)
        result = False
        table = self.driver.find_element_by_tag_name("td")
        if isinstance(table, list):
            value = table[len(table) - 7].getText()
            print(value)
            if(value == "seleniumtest@gmail.com"):
                result = True
        self.navigateToEdit(table)
        return result

    def navigateToEdit(self, table):
        if isinstance(table, list):
            table[len(table) - 2].click()
        time.sleep(2)
        url = self.driver.current_url


