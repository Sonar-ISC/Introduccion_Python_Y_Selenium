#Provided by https://selenium-python.readthedocs.io/getting-started.html
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Firefox() #Definición del webdriver a utilizar (Firefox, Chrome, etc.)
driver.get("http://www.python.org") #El get indica cual va a ser la página a levantar
assert "Python" in driver.title #Assert #1
elem = driver.find_element(By.NAME, "q") # Localización de elementos del DOM
elem.clear() # Interacción con el elemento
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source # Assert #2
driver.close() #Cerrar la pestaña
