from test.TestClass import TestClass


class ProjectUpdatesTests(TestClass):
    def __init__(self, driver, name="ProjectUpdates"):
        super().__init__(driver, name)

    def run(self):
        self.tests["test_textarea_imageupload_add"] = self.test_textarea_imageupload_add()
        self.tests["test_textarea_imageupload_edit"] = self.test_textarea_imageupload_edit()
        super().run()

    def test_textarea_imageupload_add(self):
        self.driver.get("http://localhost:8000/projecten/lijst/project/weergeven/2")
        test_data = "Test update"

        # tinymce start
        self.driver.switch_to.frame(self.driver.find_element_by_css_selector("#add-update iframe"))
        self.driver.find_element_by_css_selector("#tinymce").send_keys(test_data)
        self.driver.switch_to.default_content()
        # tinymce end

        self.driver.find_element_by_id('save-update').click()

        updates = self.driver.find_elements_by_css_selector('.update-inhoud')
        for update in updates:
            if update.text == test_data:
                return True

        return False

    def test_textarea_imageupload_edit(self):
        self.driver.get("http://localhost:8000/projecten/lijst/project/weergeven/2")
        test_data = " Test update"

        self.driver.find_elements_by_id('edit-update')[0].click()

        # tinymce start
        self.driver.switch_to.frame(self.driver.find_elements_by_css_selector("iframe")[0])

        textarea = self.driver.find_element_by_css_selector("#tinymce")
        test_data_check = textarea.text + " Test update"

        textarea.send_keys(test_data)
        self.driver.switch_to.default_content()
        # tinymce end

        self.driver.find_element_by_id('save-edit-update').click()

        update_text = self.driver.find_elements_by_css_selector('.update-inhoud')[0].text
        return update_text == test_data_check
