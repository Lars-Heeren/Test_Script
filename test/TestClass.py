class TestClass:
    def __init__(self, driver, name):
        self.name = name
        self.driver = driver
        self.tests = {}

    def run(self):
        self.print_result()
        pass

    def print_result(self):
        for key in self.tests.keys():
            print(self.name.upper() + "." + key + ": " + str(self.tests[key]))