from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    # URL

    URL = "https://www.saucedemo.com/"

    # SELECTORES DEL LOGIN

    USUARIO = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    BOTON_LOGIN = (By.ID, "login-button")
    MENSAJE_ERROR = (By.CSS_SELECTOR, "[data-test='error']")
    LOGO = (By.CLASS_NAME, "app_logo")
    TITULO_SECCION = (By.CLASS_NAME, "title")

    # init es un metodo o funcion especial que se utiliza en python cuando creamos un objeto (prepara los datos después crear un objeto cuando uno lo necesite)
    # estructura preparada para poder crear en cualquiler momento
    # conjunto de datos y variables que se van a ejecutar cuando cree el objeto
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def abrir_pagina(self):
        self.driver.get(self.URL)
        return self

    def ingresar_usuario(self, usuario):
        campo = self.wait.until(EC.visibility_of_element_located(self.USUARIO))
        campo.clear()
        campo.send_keys(usuario)
        return self

    def ingresar_password(self, password):
        campo = self.driver.find_element(*self.PASSWORD)
        campo.clear()
        campo.send_keys(password)
        return self

    def hacer_click_button(self):
        self.driver.find_element(*self.BOTON_LOGIN).click()
        return self

    def obtener_error(self):
        div_error = self.wait.until(
            EC.visibility_of_element_located(self.MENSAJE_ERROR)
        )
        return div_error.text

    def hacer_login(self, usuario, password):
        self.ingresar_usuario(usuario)
        self.ingresar_password(password)
        self.hacer_click_button()
        return self

    def logo_visible(self):
        return self.wait.until(EC.visibility_of_element_located(self.LOGO))

    def titulo_visible(self):
        return self.wait.until(EC.visibility_of_element_located(self.TITULO_SECCION))
