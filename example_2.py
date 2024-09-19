from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.get("http://tienda.utp.edu.co")
assert "Tienda UTP" in driver.title
elem = driver.find_element(By.NAME, "s")
elem.clear()
elem.send_keys("ingenierías")
elem.send_keys(Keys.RETURN)
wait = WebDriverWait(driver, 100)
element = wait.until(EC.title_contains("Resultados"))
elem2 = driver.find_elements(By.XPATH, ".//article")
assert len(elem2) > 0, "No existen resultados para esta busqueda"
driver.close()