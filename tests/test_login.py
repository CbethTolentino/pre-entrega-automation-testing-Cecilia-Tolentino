from pages.login_page import LoginPage
import pytest
from utils.reader import read_users_csv
from utils.logger import logger

@pytest.mark.parametrize("data",read_users_csv())

def test_validacion_del_login(driver,data):
 try: 
    logger.info("Iniciando prueba de login")
    login_page = LoginPage(driver)

    login_page.abrir_pagina()
    logger.info("Página abierta correctamente")
    login_page.hacer_login(data["usuario"],data["password"])
    logger.info("Ingreso de credenciales")
    if data["tipo_usuario"] == "user_ok":
    
    #validaciones
     assert "/inventory.html" in driver.current_url , "No se redirigió al inventario"
     assert   login_page.logo_visible().text  == "Swag Labs",  "Título inesperado"
     assert  login_page.titulo_visible().text == "Products" , "Se espera el titulo Products"
     logger.info("Login exitoso")
    elif  data["tipo_usuario"] == "user_block":
     mensaje= login_page.obtener_error()
     assert "locked out" in mensaje, "El usuario no se encuentra bloqueado"
     assert "/inventory.html" not in driver.current_url , "No debe aparecer el inventario"
     logger.info("Login con usuario bloqueado valido")
    elif  data["tipo_usuario"] == "user_empty":
         mensaje= login_page.obtener_error()
         assert "Epic sadface: Username is required" in mensaje, "Debe requerir ingresar un usuario"
         assert "/inventory.html" not in driver.current_url , "No debe aparecer el inventario"
         logger.info("Mensaje de error usuario vacio valido")
    elif  data["tipo_usuario"] == "password_empty":
         mensaje= login_page.obtener_error()
         assert "Epic sadface: Password is required" in mensaje, "Debe requerir al usuario ingresar una contraseña" 
         assert "/inventory.html" not in driver.current_url , "No debe aparecer el inventario"
         logger.info("Mensaje de error contraseña vacia valida")
    elif data["tipo_usuario"] in ("user_wrong", "password_wrong"):
        mensaje = login_page.obtener_error()
        assert "Epic sadface: Username and password do not match any user in this service" in mensaje, \
            "Debe mostrar un mensaje de error por usuario o contraseña incorrecta"
        assert "/inventory.html" not in driver.current_url, "No debe aparecer el inventario"
        logger.info("Mensaje de error contraseña y usuario incorrecto valida")
    else:
        pytest.fail(f"tipo_usuario desconocido en el CSV: '{data["tipo_usuario"]}'")
        
 except Exception:
           logger.exception("Error durante la prueba de login")
           raise                      
    
