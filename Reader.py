import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

CHROME_DRIVER = "\\chromedriver.exe"
CHROME_PATH = os.path.dirname(os.path.abspath(__file__)) + "\\chrome"
APPLICATION_ADDRESS_STRING = "http://localhost/phpweek2/index.html"


class Reader:

    def __init__(self):

        options = Options()
        options.add_argument('user-data-dir=' + CHROME_PATH)
        print(os.path.dirname(os.path.abspath(__file__)))

        self.driver = webdriver.Chrome(executable_path=CHROME_PATH + CHROME_DRIVER, options=options)
        self.driver.get(APPLICATION_ADDRESS_STRING)

        try:
            self.test_application()
        except IndexError:
            print("test setting failed please check setup")

        input("press Enter to quit")
        self.driver.quit()

    def test_application(self):
        self.driver.find_element_by_name("firstname").send_keys("Dennis")
        self.driver.find_element_by_name("lastname").send_keys("sjaak")
        self.driver.find_element_by_name("bijbel").send_keys("holy godddddddddd")
        self.driver.find_element_by_css_selector("input[type='submit']").click()
        pass


Reader()
