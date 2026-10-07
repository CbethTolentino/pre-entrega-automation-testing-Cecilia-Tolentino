import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from utils.reutilizables import (
     PASSWORD_VALIDA,  USUARIO_VALIDO,
     hacer_login,BOTON_AGREGAR,
      CONTADOR_CARRITO,  ICONO_CARRITO,
    NOMBRE_PRODUCTO, 
    PRODUCTOS, TIMEOUT,espera_clic, 
    espera_visible
)
def test_agregar_productos_carrito_exitoso():
    
    driver=webdriver.Chrome()

    try:
           hacer_login(driver, USUARIO_VALIDO,PASSWORD_VALIDA)
           
           

           espera_visible(driver, PRODUCTOS)
           productos = driver.find_elements(*PRODUCTOS)
           primer_producto = productos[0]

           nombre_producto = primer_producto.find_element(*NOMBRE_PRODUCTO).text
          

           #Añadir un producto al carrito haciendo clic en el botón correspondiente con espera explicita incluida
         
           espera_clic(driver,BOTON_AGREGAR).click()   

          #Verificar que el contador del carrito se incremente correctamente
           assert espera_visible(driver, CONTADOR_CARRITO).text == "1"

          #Navegar al carrito de compras
           espera_clic(driver, ICONO_CARRITO).click()
           WebDriverWait(driver, TIMEOUT).until(EC.url_contains("/cart.html"))
          #Comprobar que el producto añadido aparezca correctamente en el carrito
           productos_en_carrito = driver.find_elements(*NOMBRE_PRODUCTO)

          

           assert len(productos_en_carrito) == 1 , f"El contador del carrito es {productos_en_carrito} (se esperaba 1)"

           assert productos_en_carrito[0].text == nombre_producto, "El producto no coincide"

         
    finally :
          driver.quit()
       