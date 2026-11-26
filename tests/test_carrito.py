import pytest

from pages.login_page import LoginPage
from pages.carrito_page import CarritoPage
from pages.productos_page import ProductosPage
from utils.reader import read_productos_json,read_users_by_type
from utils.logger import logger


@pytest.mark.parametrize("data",read_users_by_type("user_ok"))
def test_agregar_productos_carrito_exitoso(driver,data):
   try: 
      logger.info("Inicializando prueba del carrito")
      login_page = LoginPage(driver)
      productos_page =  ProductosPage(driver)
      carrito_page = CarritoPage(driver)
      logger.info("Ingresando a la pagina web de pruebas")
      login_page.abrir_pagina()
      logger.info("Inicializando sesion con credenciales validas")    
      login_page.hacer_login(data["usuario"],data["password"])
      logger.info("Sesión iniciada correctamente")   

      logger.info("Ingresando a la pagina del inventario")  
      
      logger.info("Leyendo el primer producto del json")  
      producto= read_productos_json()[0] 
      
      logger.info("Agregando el primer producto del json")  
      productos_page.agregar_productos_por_nombre(producto["nombre"])
      
      assert productos_page.contador_carrito_visible() == "1"
      logger.info("Prueba de contador de carrito validada")  
        #Navegar al carrito de compras
      productos_page.ir_al_carrito()
      logger.info("ir a la pagina del carrito")
        #Comprobar que el producto añadido aparezca correctamente en el carrito
      assert carrito_page.obtener_nombre_producto_carrito() == producto["nombre"], "El nombre del producto no coincide"
      logger.info("Prueba del nombre del producto contra json validada")  
      assert carrito_page.obtener_precio_producto_carrito() == producto["precio"], "El precio del producto no coincide"
      logger.info("Prueba del precio del producto contra json validada")  
      productos_en_carrito = carrito_page.obtener_items_carrito()
      assert len(productos_en_carrito) == 1 , f"El contador del carrito es {len(productos_en_carrito)} (se esperaba 1)"
      logger.info("Prueba del contador del carrito validada")
   except Exception:
      logger.exception("Error durante la prueba de agregar de productos en el carrito")
      raise
    

          
    
@pytest.mark.parametrize("data",read_users_by_type("user_ok"))
def test_eliminar_productos_carrito_exitoso(driver,data):
   try: 
      logger.info("Inicializando prueba del carrito")
      login_page = LoginPage(driver)
      productos_page =  ProductosPage(driver)
      carrito_page = CarritoPage(driver)
      logger.info("Ingresando a la pagina web de pruebas")    
      login_page.abrir_pagina()
      logger.info("Inicializando sesion con credenciales validas")          
      login_page.hacer_login(data["usuario"],data["password"])
      logger.info("Sesión iniciada correctamente")   
      
      logger.info("Ingresando a la pagina del inventario")  
            
      logger.info("Leyendo el primer producto del json")    
         
      producto= read_productos_json()[1] 

      logger.info("Agregando el primer producto del json")  
        
      productos_page.agregar_productos_por_nombre(producto["nombre"])
          
      assert productos_page.contador_carrito_visible() == "1"
      logger.info("Prueba de contador de carrito validada") 
        #Navegar al carrito de compras
      productos_page.ir_al_carrito()
      logger.info("ir a la pagina del carrito")    
      #Comprobar que el producto añadido aparezca correctamente en el carrito
      assert carrito_page.obtener_nombre_producto_carrito() == producto["nombre"], "El nombre del producto no coincide"
      logger.info("Prueba del nombre del producto contra json validada")  
      assert carrito_page.obtener_precio_producto_carrito() == producto["precio"], "El precio del producto no coincide"
      logger.info("Prueba del precio del producto contra json validada")     

      logger.info("Se obtienen todos los item del carrito")
      productos_en_carrito = carrito_page.obtener_items_carrito()
         
      assert len(productos_en_carrito) == 1 , f"El contador del carrito es {len(productos_en_carrito)} (se esperaba 1)"
      logger.info("Prueba del contador del carrito validada")

      logger.info("Se quita el producto agregado del carrito")
      carrito_page.quitar_item_carrito()
            
    

      # Verificar que no queda ningún producto ni contador
      assert len(carrito_page.obtener_items_carrito()) == 0, "El carrito debería estar vacío"
      logger.info("Prueba de eliminación del producto del carrito validada")
      assert len(carrito_page.obtener_contador_carrito()) == 0, "No debería mostrarse el contador"
      logger.info("Prueba de que ya no existe el contador validada")
   except Exception:   
      logger.exception("Error durante la prueba de eliminación de productos en el carrito")
      raise