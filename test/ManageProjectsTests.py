from test.TestClass import TestClass


class ManageProjectsTests(TestClass):
    def __init__(self, driver, name="ManageProjects"):
        super().__init__(driver, name)

    def run(self):
        self.tests["test_edit_project"] = self.test_edit_project()
        self.tests["test_add_project"] = self.test_add_project()
        self.tests["test_click_project"] = self.test_click_project()
        self.tests["test_delete_project"] = self.setup_test_delete_project()
        super().run()

    def test_edit_project(self):
        self.driver.get("http://localhost:8000/projecten/projecteigenaar/lijst")
        current_url = self.driver.current_url

        element = self.driver.find_elements_by_css_selector('.list li .edit-button-container #edit-button0 a')[0]
        element.click()

        return current_url != self.driver.current_url

    def setup_test_delete_project(self):
        self.driver.get("http://localhost:8000/projecten/projecteigenaar/lijst")
        li_list = self.driver.find_elements_by_css_selector('.list li')

        if len(li_list) > 0:
            return self.test_delete_project(li_list)
        else:
            return True

    def test_delete_project(self, li_list):
        self.driver.get("http://localhost:8000/projecten/projecteigenaar/lijst")

        element = self.driver.find_elements_by_css_selector('.list li .edit-button-container #delete-button0 a')[0]
        element.click()

        li_list_new = self.driver.find_elements_by_css_selector('.list li')
        return len(li_list) != len(li_list_new)

    def test_add_project(self):
        self.driver.get("http://localhost:8000/projecten/projecteigenaar/lijst")
        current_url = self.driver.current_url

        element = self.driver.find_elements_by_css_selector('div>div .add-button a')[0]
        element.click()

        return current_url != self.driver.current_url

    def test_click_project(self):
        self.driver.get("http://localhost:8000/projecten/projecteigenaar/lijst")
        current_url = self.driver.current_url

        element = self.driver.find_elements_by_css_selector('.list li a')[0]
        element.click()

        return current_url != self.driver.current_url
