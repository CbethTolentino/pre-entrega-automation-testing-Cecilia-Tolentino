from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from utils.reutilizables import (
     PASSWORD_VALIDA,  USUARIO_VALIDO,PRODUCTOS,NOMBRE_PRODUCTO,PRECIO_PRODUCTO,BOTON_MENU,FILTRO_ORDEN,
     agregar_productos_por_nombre,
     espera_clic, PRODUCTO2,
     CONTADOR_CARRITO,BOTON_QUITAR,TIMEOUT,

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

def test_eliminar_producto_seleccionado():
      driver=webdriver.Chrome()
      try:
           #Inicio preecondiciones
           hacer_login(driver, USUARIO_VALIDO,PASSWORD_VALIDA)
           agregar_productos_por_nombre(driver,PRODUCTO2)
           #Finaliza preconduciones

           #Acción para quitar el producto
           espera_clic(driver,BOTON_QUITAR).click()
            # Espera a que el contador desaparezca (máximo TIMEOUT segundos)
           WebDriverWait(driver, TIMEOUT).until(EC.invisibility_of_element_located(CONTADOR_CARRITO))
           #Validación del item carrito desaparezca
           assert len(driver.find_elements(*CONTADOR_CARRITO)) == 0, "No debería mostrarse el contador"
      finally:
           driver.quit()      
                  
       