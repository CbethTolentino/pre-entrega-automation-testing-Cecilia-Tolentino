import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from utils.reutilizables import (
     PASSWORD_VALIDA,  USUARIO_VALIDO,
     hacer_login,BOTON_AGREGAR,
      CONTADOR_CARRITO,  ICONO_CARRITO,
    NOMBRE_PRODUCTO, agregar_productos_por_nombre,
    PRODUCTOS, TIMEOUT,espera_clic, PRODUCTO,
    espera_visible,BOTON_QUITAR,PRODUCTOS,
    ITEM_CARRITO
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

def test_eliminar_productos_carrito_exitoso():
    
    driver=webdriver.Chrome()

    try:
           #Inicio precondición
           hacer_login(driver, USUARIO_VALIDO,PASSWORD_VALIDA)
           
           

           agregar_productos_por_nombre(driver,PRODUCTO)

          #Verificar que el contador del carrito se incremente correctamente
           assert espera_visible(driver, CONTADOR_CARRITO).text == "1"

          #Navegar al carrito de compras
           espera_clic(driver, ICONO_CARRITO).click()
           WebDriverWait(driver, TIMEOUT).until(EC.url_contains("/cart.html"))
          #Comprobar que el producto añadido aparezca correctamente en el carrito
           productos_en_carrito = driver.find_elements(*NOMBRE_PRODUCTO)

          

           assert len(productos_en_carrito) == 1 , f"El contador del carrito es {productos_en_carrito} (se esperaba 1)"

           assert productos_en_carrito[0].text == PRODUCTO, "El producto no coincide"
          #Finaliza precondición
           espera_clic(driver,BOTON_QUITAR).click()
           
         # Esperar a que el producto desaparezca del carrito
           WebDriverWait(driver, TIMEOUT).until(EC.invisibility_of_element_located(ITEM_CARRITO))

         # Verificar que no queda ningún producto ni contador
           assert len(driver.find_elements(*ITEM_CARRITO)) == 0, "El carrito debería estar vacío"
           assert len(driver.find_elements(*CONTADOR_CARRITO)) == 0, "No debería mostrarse el contador"

    finally :
          driver.quit()       