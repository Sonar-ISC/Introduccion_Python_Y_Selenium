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
elem.send_keys("aKMñcmaslñc,ñas,")
elem.send_keys(Keys.RETURN)
wait = WebDriverWait(driver, 100)
element = wait.until(EC.title_contains("Resultados"))
elem2 = driver.find_element(By.XPATH, ".//div[@class='page-content']/p")
assert "nada coincide" in elem2.text
driver.close()