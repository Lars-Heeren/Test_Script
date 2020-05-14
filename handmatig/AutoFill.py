from datetime import time


class AutoFill:

    def __init__(self, driver):
        self.driver = driver
        self.login()


    def login(self):
        self.driver.get("http://localhost:8000/login")
        link = self.driver.find_element_by_css_selector('ul.login_search li a')
        link.click()
        time.sleep(3)
        emailInput = self.driver.find_element_by_id('email')
        emailInput.send_keys('pascal@gmail.com')

        passwordInput = self.driver.find_element_by_id('password')
        passwordInput.send_keys('weerbaarBrabant')

        submit = self.driver.find_element_by_css_selector('button')
        submit.click()
        time.sleep(3)

