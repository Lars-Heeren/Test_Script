from test.TestClass import TestClass


class NavigationBarTests(TestClass):
    def __init__(self, driver, name="NavigationBar"):
        super().__init__(driver, name)

    def run_tests(self):
        self.tests["test_navigationbar"] = self.test_navigationbar_buttons()
        self.print_result()

    def print_result(self):
        super().print_result()

    def print_failure(self):
        super().print_failure()
        print(self.result)

    def test_navigationbar_buttons(self):
        links = []
        #door iedere link gaan en kijken of er iets veranderd qua url
        for elem in self.driver.find_elements_by_css_selector("nav li a"):
            elem.click()
            text = elem.text
            #print(text)
            links.append(text)

        return True
