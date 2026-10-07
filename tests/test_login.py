import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from utils.reutilizables import (URL,
     PASSWORD_VALIDA,  USUARIO_VALIDO,
      USUARIO,PASSWORD,BOTON_LOGIN,LOGO,
     TIMEOUT,espera_clic, TITULO_SECCION,
    espera_visible
)
def test_login_exitoso():
    driver = webdriver.Chrome()

    driver.implicitly_wait(TIMEOUT)
    
    try:
        driver.get(URL)
# definición de elementos
        usuario =driver.find_element(*USUARIO)
        password =driver.find_element(*PASSWORD)
        boton_login =driver.find_element(*BOTON_LOGIN)

#acciones de dichos elementos
        usuario.send_keys(*USUARIO_VALIDO)
        password.send_keys(*PASSWORD_VALIDA)
        espera_clic(driver,boton_login)
        boton_login.click()

 #validaciones
        assert "/inventory.html" in driver.current_url , "No se redirigió al inventario"

   
        assert   espera_visible(driver,LOGO).text  == "Swag Labs",  "Título inesperado"

      
        assert  espera_visible(driver,TITULO_SECCION).text == "Products" , "Se espera el titulo Products"

    finally :

       driver.quit()