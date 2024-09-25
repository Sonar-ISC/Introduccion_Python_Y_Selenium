import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TiendaUTPSearch(unittest.TestCase):

    URL = "http://tienda.utp.edu.co"
    KW_TITLE_PAGE = "Tienda UTP"
    KW_RANDOM_STRING = "aKMñcmaslñc,ñas,"
    KW_SEARCH_POLO = "Polo Institucional Hombre"
    KW_RESULTS_TITLE = "Resultados"
    KW_RESULTS_LIST = [
        "Polo Institucional bordada Verde Militar Hombre",
        "Polo Institucional bordada Negra Hombre",
        "Polo Institucional bordada Ocre Hombre",
        "Polo Institucional bordada Crema Hombre",
        "Polo institucional crema hombre",
        "Polo institucional ocre hombre “Soy Egresado”",
        "Polo institucional camel hombre",
        "Camiseta polo verde con azul hombre"
    ]
    
    CSS_SEL_1 = "section.no-results p"
    CSS_SEL_2 = "article"
    CSS_SEL_3 = "article.product h2"
    
    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_not_matches_search(self):
        driver = self.driver
        driver.get(self.URL)
        self.assertIn(self.KW_TITLE_PAGE, driver.title)
        
        elem = driver.find_element(By.NAME, "s")
        elem.clear()
        elem.send_keys(self.KW_RANDOM_STRING)
        elem.send_keys(Keys.RETURN)
        
        wait = WebDriverWait(driver, 100)
        loading_pause = wait.until(EC.title_contains(self.KW_RESULTS_TITLE))
        elem2 = driver.find_element(By.CSS_SELECTOR, self.CSS_SEL_1)
        self.assertIn("nada coincide", elem2.text)
    
    def test_matched_search(self):
        driver = self.driver
        driver.get(self.URL)
        self.assertIn(self.KW_TITLE_PAGE, driver.title)
        
        elem = driver.find_element(By.NAME, "s")
        elem.clear()
        elem.send_keys(self.KW_SEARCH_POLO)
        elem.send_keys(Keys.RETURN)
        
        wait = WebDriverWait(driver, 100)
        loading_pause = wait.until(EC.title_contains(self.KW_RESULTS_TITLE))
        elem2 = driver.find_elements(By.CSS_SELECTOR, self.CSS_SEL_2)
        self.assertGreater(len(elem2), 0)

    def test_analyse_results(self):
        driver = self.driver
        driver.get(self.URL)
        self.assertIn(self.KW_TITLE_PAGE, driver.title)
        
        elem = driver.find_element(By.NAME, "s")
        elem.clear()
        elem.send_keys(self.KW_SEARCH_POLO)
        elem.send_keys(Keys.RETURN)
        
        wait = WebDriverWait(driver, 100)
        loading_pause = wait.until(EC.title_contains(self.KW_RESULTS_TITLE))
        title_items = driver.find_elements(By.CSS_SELECTOR, self.CSS_SEL_3)
        
        list_titles = []
        for title_it in title_items:
            list_titles.append(title_it.text)
            
        self.assertSetEqual(set(list_titles), set(self.KW_RESULTS_LIST))
            

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()