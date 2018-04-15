import unittest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

class SelPyTest(unittest.TestCase):

    def setUp(self):
        options = Options()
        options.add_argument("--headless") #Comment this line out if you want to see it execute
        self.driver = webdriver.Firefox(firefox_options=options)

    def test_google_search(self):
        driver = self.driver
        driver.get("https://www.google.com")

        elem = driver.find_element_by_name("q")
        elem.send_keys("test")

        submit = driver.find_element_by_name("btnK")
        submit.click()

        assert(driver.title == "test - Google Search")

    def test_feeling_lucky(self):
        driver = self.driver
        driver.get("https://www.google.com")

        elem = driver.find_element_by_name("q")
        elem.send_keys("python")
        
        submit = driver.find_element_by_name("btnI")
        submit.click()

        assert(driver.title == "Welcome to Python.org")

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()

