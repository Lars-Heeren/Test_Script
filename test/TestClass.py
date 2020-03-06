import os
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains

class TestClass:

    def __init__(self, driver, name):
        self.name = name
        self.driver = driver
        self.passit = True


    def run_tests(self):
        pass

    def print_failure(self):
        print("Test Failed!!")
        pass

    def print_result(self):
        print("\n" + self.name.upper(), "test status:", self.passit)
        if not self.passit:
            self.print_failure()




