import unittest
import time
import os.path
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

class SelPyTest(unittest.TestCase):

    #Sets up the environment when file is executed
    def setUp(self):
        options = Options()
        
        #Comment this line out if you want to see it execute
        options.add_argument("--headless")
        
        self.driver = webdriver.Firefox(firefox_options=options)

    #Enters a search query, then presses "Search"
    def test_google_search(self):
        driver = self.driver
        driver.get("https://www.google.com")

        #Types a search query into the box
        searchBar = driver.find_element_by_name("q")
        searchBar.send_keys("python")

        #Presses "Google Search" button
        searchButton = driver.find_element_by_name("btnK")
        searchButton.click()

        assert(driver.title == "python - Google Search")

    #Enters a search query, then presses "I'm Feeling Lucky"
    def test_feeling_lucky(self):
        driver = self.driver
        driver.get("https://www.google.com")

        #Types a search query into the box
        searchBar = driver.find_element_by_name("q")
        searchBar.send_keys("python")
        
        #Presses the "I'm Feeling Lucky" button
        luckyButton = driver.find_element_by_name("btnI")
        luckyButton.click()

        assert(driver.title == "Welcome to Python.org")

    #Tests a file that is local
    def test_local_site(self):
        driver = self.driver

        #Builds the absolute path to the current location
        absolutePath = os.path.abspath(os.path.dirname(__file__))

        #Creates the full path to the file
        fullPath = absolutePath + "/web/index.html"
        
        #Opens the file with the web driver, instead of opening a web page
        driver.get("file://" + fullPath)
    
        #Click the "+" button
        plusButton = driver.find_element_by_id("controls1plus")
        plusButton.click()

        #Type "TEST" into the textbox
        addTextBox = driver.find_element_by_id("itemtoadd")
        addTextBox.send_keys("TEST")

        #Click the "Add" button
        addButton = driver.find_element_by_id("addbutton")
        addButton.click()

        #Ensure the created item starts with the entered text
        assert(driver.find_element_by_id("item1").text.startswith("TEST"))

    #Runs once, at end of execution 
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()

