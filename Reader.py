from test.CarrouselTests import CarrouselTests
from test.NavigationBarTests import NavigationBarTests
from test.NewProjectsTests import NewProjectsTests
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

CHROME_DRIVER = "\\chromedriver.exe"
CHROME_PATH = os.path.dirname(os.path.abspath(__file__)) + "\\chrome"
APPLICATION_ADDRESS_STRING = " http://127.0.0.1:8000"


class Reader:
    def __init__(self):
        options = Options()
        # options.add_argument('user-data-dir=' + CHROME_PATH)
        print(os.path.dirname(os.path.abspath(__file__)))

        self.driver = webdriver.Chrome(executable_path=CHROME_PATH + CHROME_DRIVER, options=options)
        self.driver.get(APPLICATION_ADDRESS_STRING)

        try:
            self.test_application()
        except IndexError:
            print("test setting failed please check setup")
            self.driver.quit()

        input("press Enter to quit")
        self.driver.quit()

    def test_application(self):
        tests = []

        tests.append(CarrouselTests(self.driver))
        tests.append(NavigationBarTests(self.driver))
        tests.append(NewProjectsTests(self.driver))

        for test in tests:
            test.run_tests()

        # img1 = self.driver.find_element_by_css_selector(".primary_project img")

        # carrousel = self.driver.find_element_by_class_name("primary_project")
        # hover = ActionChains(self.driver).move_to_element(carrousel)
        # hover.perform()

    # button = self.driver.find_element_by_id("next")
    # click = ActionChains(self.driver).click(button)
    # click.perform()

    # img2 = self.driver.find_element_by_css_selector(".primary_project img")

    # print(img1 != img2)

    # pass


Reader()
