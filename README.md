# Introducción a Selenium WebDriver con Python

La idea de esta actividad es, en primera instancia, conocer la estructura más básica que podemos utilizar para automatizar pruebas con Selenium a través de Python, además de estructurar los outputs de estas pruebas para tener claros los resultados de estas.

## Desafío



---
## Consideraciones

- Para hacer el pull request, pueden iniciar sesión en GitHub con VSCode para mayor comodidad.
- Deben crear una rama con su nombre para hacer push de sus progresos.
- Notificar problemas con el repositorio a su creador.
---
## Tecnologías

- Selenium WebDriver
- Unittest
- Python
---
## Material de apoyo

- [Manual Pull Request](https://drive.google.com/file/d/1OagidqedQAEj3h_LoacEr7wqJLBv7XER/view?usp=sharing)
- [Selenium WebDriver Documentación oficial](https://www.selenium.dev/documentation/en/webdriver/)
- [Selenium en Python Documentación no oficial](https://selenium-python.readthedocs.io/)
- [Unittest](https://docs.python.org/3/library/unittest.html)
---
## Cosas basicas de Selenium

### Get

Get es un método que se utiliza para navegar a una página web. Get es un método que permite la navegación a una página

```python
driver.get("https://example.com")
```

### WebElement

WebElement es una interfaz que representa un elemento en una página web. WebElement es una interfaz que permite la
interacción con elementos en una página web.

```python
element = driver.findElement(By.ID("id"));
```

Se puede interactuar con los elementos de la siguiente manera:

```python
element.click()
element.sendKeys("Texto")
element.text
element.clear()
```
---
### Autor
[Juan Alejandro Pérez Bermúdez - Co-Lider Sonar I.S.C](https://www.linkedin.com/in/mega-barto)
