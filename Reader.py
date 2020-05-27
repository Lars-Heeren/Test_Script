import os
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common import exceptions

from Utilities.RandomStringGenerator import RandomStringGenerator
from test.CarrouselTests import CarrouselTests
from test.MapTests import MapTests
from test.NavigationBarTests import NavigationBarTests
from test.NewProjectsTests import NewProjectsTests
from test.EditProjectTest import EditProjectTests
from test.ManageProjectsTests import ManageProjectsTests
from test.ListTests import ListTests
from test.LoginTest import LoginTest
from test.AddProjectTest import AddProjectTest
from test.ContactsTests import ContactsTests

CHROME_DRIVER = "\\chromedriver.exe"
CHROME_PATH = os.path.dirname(os.path.abspath(__file__)) + "\\chrome"
APPLICATION_ADDRESS_STRING = " http://127.0.0.1:8000"


class Reader:
    def __init__(self):
        options = Options()
        self.driver = webdriver.Chrome(executable_path=CHROME_PATH + CHROME_DRIVER, options=options)
        # self.driver.get(APPLICATION_ADDRESS_STRING)

        timesTry = 0

        while timesTry <= 5:
            try:
                self.run_tests()
                break;
            except exceptions.JavascriptException:
                timesTry += 1
                print(timesTry)
        self.driver.quit()

    def run_tests(self):
        tests = []

        tests.append(LoginTest(self.driver))
        tests.append(AddProjectTest(self.driver))
        tests.append(EditProjectTests(self.driver))
        tests.append(ContactsTests(self.driver))
        tests.append(NavigationBarTests(self.driver))
        tests.append(CarrouselTests(self.driver))
        tests.append(NewProjectsTests(self.driver))
        tests.append(MapTests(self.driver))
        tests.append(ListTests(self.driver))
        tests.append(ManageProjectsTests(self.driver))

        for test in tests:
            test.run()


Reader()
