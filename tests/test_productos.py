import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from utils.reutilizables import (
     PASSWORD_VALIDA,  USUARIO_VALIDO,PRODUCTOS,NOMBRE_PRODUCTO,PRECIO_PRODUCTO,BOTON_MENU,FILTRO_ORDEN,
     hacer_login
    
)
def test_productos():
    driver=webdriver.Chrome()
    try:
            hacer_login(driver, USUARIO_VALIDO,PASSWORD_VALIDA)

            

            #validación del titulo de la página
            assert driver.title =="Swag Labs"

            productos = driver.find_elements(*PRODUCTOS)
            #validación de existencia de productos
            
            assert len(productos) > 0
            
            #validación de integridad de los productos
            
            primer_producto = productos[0]

            nombre_producto = primer_producto.find_element(*NOMBRE_PRODUCTO).text
            precio_producto = primer_producto.find_element(*PRECIO_PRODUCTO).text

            assert nombre_producto == "Sauce Labs Backpack"
            assert precio_producto == "$29.99"

            #verificar menu

            menu = driver.find_element(*BOTON_MENU)
            #verifica si el menu está visible en la web
            assert menu.is_displayed()
            #verificar filtro

            filtro= driver.find_element(*FILTRO_ORDEN)

            assert filtro.is_displayed()
    finally :
          driver.quit()
       