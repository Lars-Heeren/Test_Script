from Utilities.RandomStringGenerator import RandomStringGenerator
from handmatig.AutoFill import AutoFill


class AddProjectAutofill(AutoFill):

    def __init__(self):
        super().__init__()
        self.autoFill()

    def autoFill(self):
        print('test')
        self.driver.get("http://localhost:8000/projecten/toevoegen")

        test_data = RandomStringGenerator().getRandomString(20)

        self.driver.find_element_by_name("title").send_keys(test_data)
        self.driver.find_element_by_name("about").send_keys(test_data)

        #tinymce start
        self.driver.switch_to.frame(self.driver.find_element_by_css_selector("iframe"))
        self.driver.find_element_by_css_selector("#tinymce").send_keys(test_data)
        self.driver.switch_to.default_content()
        #tinymce end

        self.driver.find_element_by_name("result_ac").send_keys(test_data)
        self.driver.find_element_by_name("startdate").send_keys("10/10/2010")
        self.driver.find_element_by_name("enddate").send_keys("15/15/2015")

        self.driver.find_element_by_name("prac_vals[]").find_elements_by_tag_name("option")[0].click()

        self.driver.find_element_by_id("display-label-box").click()
        self.driver.find_element_by_id("inputAddLocation").send_keys("Berlicum")
        self.driver.find_element_by_id("locationAdd").click()

        self.driver.find_element_by_id("display-label-box-organisations").click()
        self.driver.find_element_by_id("inputAddOrganization").send_keys(test_data)
        self.driver.find_element_by_id("organizationAdd").click()

        self.driver.find_element_by_id("1").click()
        self.driver.find_element_by_css_selector("label[for='sdgnumber1']").click()


        input("press any key to continue...")


AddProjectAutofill()