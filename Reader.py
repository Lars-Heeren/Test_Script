import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

CHROME_DRIVER = "\\chromedriver.exe"
CHROME_PATH = os.path.dirname(os.path.abspath(__file__)) + "\\chrome"
APPLICATION_ADDRESS_STRING = "http://localhost/"


class Reader:

    def __init__(self):

        options = Options()
        options.add_argument('user-data-dir=' + CHROME_PATH)
        print(os.path.dirname(os.path.abspath(__file__)))

        driver = webdriver.Chrome(executable_path=CHROME_PATH + CHROME_DRIVER, chrome_options=options)
        driver.get(APPLICATION_ADDRESS_STRING)

        try:
            self.test_application()
        except IndexError:
            print("test setting failed please check setup")

        input("press Enter to quit")
        driver.quit()

    def test_application(self):
        # add testing code here
        pass


Reader()
