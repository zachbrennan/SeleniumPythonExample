import unittest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

class SelPyTest(unittest.TestCase):

    #Sets up the environment when file is executed
    def setUp(self):
        options = Options()
        
        #Comment this line out if you want to see it execute
#        options.add_argument("--headless")
        
        self.driver = webdriver.Firefox(firefox_options=options)

    #Enters a search query, then presses "Search"
    def test_google_search(self):
        driver = self.driver
        driver.get("https://www.google.com")

        searchBar = driver.find_element_by_name("q")
        searchBar.send_keys("python")

        searchButton = driver.find_element_by_name("btnK")
        searchButton.click()

        assert(driver.title == "python - Google Search")

    #Enters a search query, then presses "I'm Feeling Lucky"
    def test_feeling_lucky(self):
        driver = self.driver
        driver.get("https://www.google.com")

        searchBar = driver.find_element_by_name("q")
        searchBar.send_keys("python")
        
        luckyButton = driver.find_element_by_name("btnI")
        luckyButton.click()

        assert(driver.title == "Welcome to Python.org")

    def test_local_site(self):
        driver = self.driver
        driver.get("file://index.html")
    
        print driver.title
        
#        plusButton = driver.find_element_by_id("controls1plus")
#        plusButton.click()

#        addTextBox = driver.find_element_by_id("itemtoadd")
#        addTextBox.send_keys("TEST")

#        print driver.find_element_by_id("item1").text

    #Runs once, at end of execution 
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()

