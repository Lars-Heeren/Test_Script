import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from test.CarrouselTests import CarrouselTests
from test.MapTests import MapTests
from test.NavigationBarTests import NavigationBarTests
from test.NewProjectsTests import NewProjectsTests

CHROME_DRIVER = "\\chromedriver.exe"
CHROME_PATH = os.path.dirname(os.path.abspath(__file__)) + "\\chrome"
APPLICATION_ADDRESS_STRING = " http://127.0.0.1:8000"


class Reader:
    def __init__(self):
        options = Options()
        self.driver = webdriver.Chrome(executable_path=CHROME_PATH + CHROME_DRIVER, options=options)
        self.driver.get(APPLICATION_ADDRESS_STRING)
        self.run_tests()
        self.driver.quit()

    def run_tests(self):
        tests = []

        tests.append(NavigationBarTests(self.driver))
        tests.append(CarrouselTests(self.driver))
        tests.append(NewProjectsTests(self.driver))
        tests.append(MapTests(self.driver))

        for test in tests:
            test.run()


Reader()
