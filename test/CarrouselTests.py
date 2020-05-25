from selenium.webdriver.common.action_chains import ActionChains

from test.TestClass import TestClass


class CarrouselTests(TestClass):
    def __init__(self, driver, name="Carrousel"):
        super().__init__(driver, name)

    def run(self):
        self.tests["test_carrousel_next_button"] = self.test_next_button()
        self.tests["test_carrousel_back_button"] = self.test_back_button()
        super().run()

    def test_next_button(self):
        self.driver.get("http://localhost:8000/")
        button = self.driver.find_element_by_id("next")
        img1 = self.driver.find_element_by_css_selector(".primary_project img")
        frontimg = self.driver.find_element_by_class_name("primary_project")

        hover = ActionChains(self.driver).move_to_element(frontimg)
        hover.perform()
        click = ActionChains(self.driver).click(button)
        click.perform()
        click.perform()

        img2 = self.driver.find_element_by_css_selector(".primary_project img")

        return img1 != img2

    def test_back_button(self):
        self.driver.get("http://localhost:8000/")
        button = self.driver.find_element_by_id("previous")
        img1 = self.driver.find_element_by_css_selector(".primary_project img")
        frontimg = self.driver.find_element_by_class_name("primary_project")

        hover = ActionChains(self.driver).move_to_element(frontimg)
        hover.perform()
        click = ActionChains(self.driver).click(button)
        click.perform()
        click.perform()

        img2 = self.driver.find_element_by_css_selector(".primary_project img")

        return img1 != img2
