from selenium.webdriver.common.action_chains import ActionChains
from test.TestClass import TestClass


class CarrouselTests(TestClass):

    def __init__(self, driver, name="carrousel"):
        super().__init__(driver, name)
        self.result = {}

    def run_tests(self):
        self.result["test_application_next_button"] = self.test_application_next_button()
        self.result["test_application_back_button"] = self.test_application_back_button()

        self.print_result()

    def print_result(self):
        super().print_result()

    def print_failure(self):
        super().print_failure()
        print(self.result)

    def test_application_next_button(self):
        img1 = self.driver.find_element_by_css_selector(".primary_project img")

        carrousel = self.driver.find_element_by_class_name("primary_project")
        hover = ActionChains(self.driver).move_to_element(carrousel)
        hover.perform()

        button = self.driver.find_element_by_id("next")
        click = ActionChains(self.driver).click(button)
        click.perform()

        img2 = self.driver.find_element_by_css_selector(".primary_project img")

        result = img1 != img2
        self.passit = result

        return result

    def test_application_back_button(self):
        img1 = self.driver.find_element_by_css_selector(".primary_project img")

        carrousel = self.driver.find_element_by_class_name("primary_project")
        hover = ActionChains(self.driver).move_to_element(carrousel)
        hover.perform()

        button = self.driver.find_element_by_id("previous")
        click = ActionChains(self.driver).click(button)
        click.perform()

        img2 = self.driver.find_element_by_css_selector(".primary_project img")

        result = img1 != img2
        self.passit = result

        return result
