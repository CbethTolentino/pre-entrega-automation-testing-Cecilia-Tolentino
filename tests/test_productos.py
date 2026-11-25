
from pages.login_page import LoginPage
from pages.productos_page import ProductosPage

def test_productos(driver):
   login_page = LoginPage(driver)
   productos_page = ProductosPage(driver)
    

   login_page.abrir_pagina()
   login_page.hacer_login(USUARIO_VALIDO,PASSWORD_VALIDA)
      
   productos = productos_page.obtener_productos()
            
   #validación de existencia de productos
            
   assert len(productos) > 0
            
   #validación de integridad de los productos
            
   
   assert productos_page.obtener_nombre_primer_producto == "Sauce Labs Backpack"
   assert productos_page.obtener_precio_primer_producto == "$29.99"

   #verificar menu

           
   assert productos_page.menu_visible() 

   #verificar filtro

   assert productos_page.filtro_visible()
   

def test_agregar_producto_seleccionado(driver):
      login_page = LoginPage(driver)
      productos_page = ProductosPage(driver)
               
           
      login_page.abrir_pagina()
      login_page.hacer_login(USUARIO_VALIDO,PASSWORD_VALIDA)
     
      productos = productos_page.obtener_productos()
                       
     #validación de existencia de productos
                       
      assert len(productos) > 0
     
      ProductosPage.agregar_productos_por_nombre(driver,"Sauce Labs Onesie")
      productos_page.boton_agregar_producto()
      contador = productos_page.contador_carrito_visible()
      assert contador == 1, "Debe incrementarse el valor en 1"  
def test_eliminar_producto_seleccionado(driver):
      login_page = LoginPage(driver)
      productos_page = ProductosPage(driver)
          
      
      login_page.abrir_pagina()
      login_page.hacer_login(USUARIO_VALIDO,PASSWORD_VALIDA)

      productos = productos_page.obtener_productos()
                  
         #validación de existencia de productos
                  
      assert len(productos) > 0

      ProductosPage.agregar_productos_por_nombre(driver,"Sauce Labs Onesie")
         
      productos_page.boton_quitar_producto()
      contador = productos_page.contador_carrito_visible()
      assert contador == 0 , "No debería mostrarse el contador"  
         
         
                  
     