import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TiendaUTPSearch(unittest.TestCase):

    URL = "http://tienda.utp.edu.co"
    KEYWORD_1 = "Tienda UTP"
    KEYWORD_2A = "aKMñcmaslñc,ñas,"
    KEYWORD_2B = "Polo Institucional Hombre"
    KEYWORD_3 = "Resultados"
    XPATH_1 = ".//div[@class='page-content']/p"
    XPATH_2 = "//article"
    
    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_not_matches_search(self):
        driver = self.driver
        driver.get(self.URL)
        self.assertIn(self.KEYWORD_1, driver.title)
        elem = driver.find_element(By.NAME, "s")
        elem.clear()
        elem.send_keys(self.KEYWORD_2A)
        elem.send_keys(Keys.RETURN)
        wait = WebDriverWait(driver, 100)
        loading_pause = wait.until(EC.title_contains(self.KEYWORD_3))
        elem2 = driver.find_element(By.XPATH, self.XPATH_1)
        self.assertIn("nada coincide", elem2.text)
    
    def test_matched_search(self):
        driver = self.driver
        driver.get(self.URL)
        self.assertIn(self.KEYWORD_1, driver.title)
        elem = driver.find_element(By.NAME, "s")
        elem.clear()
        elem.send_keys(self.KEYWORD_2B)
        elem.send_keys(Keys.RETURN)
        wait = WebDriverWait(driver, 100)
        loading_pause = wait.until(EC.title_contains(self.KEYWORD_3))
        elem2 = driver.find_elements(By.XPATH, self.XPATH_2)
        self.assertGreater(len(elem2), 0)

    def test_analyse_results(self):
        driver = self.driver
        driver.get(self.URL)
        self.assertIn(self.KEYWORD_1, driver.title)
        elem = driver.find_element(By.NAME, "s")
        elem.clear()
        elem.send_keys(self.KEYWORD_2B)
        elem.send_keys(Keys.RETURN)
        wait = WebDriverWait(driver, 100)
        loading_pause = wait.until(EC.title_contains(self.KEYWORD_3))
        items_list = driver.find_elements(By.XPATH, self.XPATH_2)
        item = items_list[0].find_element(By.XPATH, "//article//h2")
        print(item.text)
        self.assertIn("Polo", item.text)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()