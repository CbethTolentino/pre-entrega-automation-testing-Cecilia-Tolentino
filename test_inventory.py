import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_inventory():
    driver=webdriver.Chrome()
    try:
        # Login
            driver.get("https://www.saucedemo.com/")
        # definición de elementos
            usuario =driver.find_element(By.ID,"user-name")
            password =driver.find_element(By.ID,"password")
            boton_login =driver.find_element(By.ID,"login-button")
        
        #acciones de dichos elementos
            usuario.send_keys("standard_user")
            password.send_keys("secret_sauce")
            boton_login.click()

             #Validaciones

             #validación del titulo de la página
            assert driver.title =="Swag Labs"

            productos = driver.find_elements(By.CLASS_NAME,"inventory_item")
            #validación de existencia de productos
            
            assert len(productos) > 0
            
            #validación de integridad de los productos
            
            primer_producto = productos[0]

            nombre_producto = primer_producto.find_element(By.CLASS_NAME,"inventory_item_name").text
            precio_producto = primer_producto.find_element(By.CLASS_NAME,"inventory_item_price").text

            assert nombre_producto == "Sauce Labs Backpack"
            assert precio_producto == "$29.99"

            #verificar menu

            menu = driver.find_element(By.ID,"react-burger-menu-btn")
            #verifica si el menu está visible en la web
            assert menu.is_displayed()
            #verificar filtro

            filtro= driver.find_element(By.CLASS_NAME,"product_sort_container")

            assert filtro.is_displayed()
    finally :
          driver.quit()
       