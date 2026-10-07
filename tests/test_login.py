import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from utils.reutilizables import (URL,
     PASSWORD_VALIDA,  USUARIO_VALIDO,
      USUARIO,PASSWORD,BOTON_LOGIN,LOGO,USUARIO_BLOQUEADO,
     TIMEOUT,espera_clic, TITULO_SECCION,MENSAJE_ERROR,
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

def test_login_usuario_bloqueado():

    driver = webdriver.Chrome()

    driver.implicitly_wait(TIMEOUT)
    
    try:
        driver.get(URL)
# definición de elementos
        usuario =driver.find_element(*USUARIO)
        password =driver.find_element(*PASSWORD)
        boton_login =driver.find_element(*BOTON_LOGIN)

#acciones de dichos elementos
        usuario.send_keys(*USUARIO_BLOQUEADO)
        password.send_keys(*PASSWORD_VALIDA)
        espera_clic(driver,boton_login)
        boton_login.click()

 #validaciones
        mensaje=espera_visible(driver,MENSAJE_ERROR).text
        assert "locked out" in mensaje, "El usuario no se encuentra bloqueado"
        assert "/inventory.html" not in driver.current_url
    finally :
 
       driver.quit()


def test_login_password_incorrecta(): 

    driver = webdriver.Chrome()

    driver.implicitly_wait(TIMEOUT)

    try:
        driver.get(URL)
        # definición de elementos
        usuario =driver.find_element(*USUARIO)
        password =driver.find_element(*PASSWORD)
        boton_login =driver.find_element(*BOTON_LOGIN)

#acciones de dichos elementos
        usuario.send_keys(*USUARIO_BLOQUEADO)
        password.send_keys("alfabravo1212")
        espera_clic(driver,boton_login)
        boton_login.click()

        mensaje=espera_visible(driver,MENSAJE_ERROR).text
        assert "Epic sadface: Username and password do not match any user in this service" in mensaje, "Debe mostrar un mensaje de error por usuario o contraseña incorrecta" 
        assert "/inventory.html" not in driver.current_url
    finally :
             
        driver.quit()   

def test_login_password_vacio(): 

    driver = webdriver.Chrome()

    driver.implicitly_wait(TIMEOUT)

    try:
        driver.get(URL)
        # definición de elementos
        usuario =driver.find_element(*USUARIO)
        password =driver.find_element(*PASSWORD)
        boton_login =driver.find_element(*BOTON_LOGIN)

#acciones de dichos elementos
        usuario.send_keys(*USUARIO_BLOQUEADO)
        password.send_keys("")
        espera_clic(driver,boton_login)
        boton_login.click()

        mensaje=espera_visible(driver,MENSAJE_ERROR).text
        assert "Epic sadface: Password is required" in mensaje, "Debe requerir al usuario ingresar una contraseña" 
        assert "/inventory.html" not in driver.current_url
    finally :
         
        driver.quit()                                              

def test_login_usuario_vacio(): 

    driver = webdriver.Chrome()

    driver.implicitly_wait(TIMEOUT)

    try:
        driver.get(URL)
        # definición de elementos
        usuario =driver.find_element(*USUARIO)
        password =driver.find_element(*PASSWORD)
        boton_login =driver.find_element(*BOTON_LOGIN)

#acciones de dichos elementos
        usuario.send_keys("")
        password.send_keys(*PASSWORD_VALIDA)
        espera_clic(driver,boton_login)
        boton_login.click()

        mensaje=espera_visible(driver,MENSAJE_ERROR).text
        assert "Epic sadface: Username is required" in mensaje, "Debe requerir ingresar un usuario" 
        assert "/inventory.html" not in driver.current_url
    finally :
         
        driver.quit()                                              
    
def test_login_usuario_invalido(): 

    driver = webdriver.Chrome()

    driver.implicitly_wait(TIMEOUT)

    try:
        driver.get(URL)
        # definición de elementos
        usuario =driver.find_element(*USUARIO)
        password =driver.find_element(*PASSWORD)
        boton_login =driver.find_element(*BOTON_LOGIN)

#acciones de dichos elementos
        usuario.send_keys("ratelf_123")
        password.send_keys(*PASSWORD_VALIDA)
        espera_clic(driver,boton_login)
        boton_login.click()

        mensaje=espera_visible(driver,MENSAJE_ERROR).text
        assert "Epic sadface: Username and password do not match any user in this service" in mensaje, "Debe mostrar un mensaje de error por usuario o contraseña incorrecta" 
        assert "/inventory.html" not in driver.current_url
    finally :
         
        driver.quit()                                              
    
                