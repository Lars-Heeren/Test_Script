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
        self.tests["edit_Test"] = self.edit_Test()
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
        table = self.driver.find_elements_by_id("email")
        if isinstance(table, list):
            value = table[len(table) - 1].text
            if(value == "seleniumtest@gmail.com"):
                result = True
        self.navigateToEdit(table)
        return result

    def navigateToEdit(self, table):
        buttons = self.driver.find_elements_by_id("editContactButton")
        buttons[len(buttons) - 1].click()
        time.sleep(2)

    def edit_Test(self):
        time.sleep(1)
        test_data_edit = RandomStringGenerator().getRandomString(20)
        time.sleep(2)

        self.driver.find_element_by_id("firstname").clear()
        self.driver.find_element_by_id("lastname").clear()
        self.driver.find_element_by_id("email").clear()
        self.driver.find_element_by_id("address").clear()
        self.driver.find_element_by_id("zipcode").clear()
        self.driver.find_element_by_id("city").clear()
        self.driver.find_element_by_id("web_link").clear()
        time.sleep(2)
        self.driver.find_element_by_id("firstname").send_keys(test_data_edit)
        self.driver.find_element_by_id("lastname").send_keys(test_data_edit)
        self.driver.find_element_by_id("email").send_keys("seleniumtestEdit@gmail.com")
        self.driver.find_element_by_id("address").send_keys(test_data_edit)
        self.driver.find_element_by_id("zipcode").send_keys(test_data_edit)
        self.driver.find_element_by_id("city").send_keys(test_data_edit)
        self.driver.find_element_by_id("web_link").send_keys(test_data_edit)
        time.sleep(1)
        self.driver.find_element_by_css_selector("button[type='submit']").click()
        time.sleep(3)
        result = False
        table = self.driver.find_elements_by_id("email")
        if isinstance(table, list):
            value = table[len(table) - 1].text
            if (value == "seleniumtestEdit@gmail.com"):
                result = True
        self.destroy_Contact()
        return result

    def destroy_Contact(self):
        buttons = self.driver.find_elements_by_id("deleteContactButton")
        buttons[len(buttons) - 1].click()
