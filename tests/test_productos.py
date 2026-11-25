
import pytest
from pages.login_page import LoginPage
from pages.productos_page import ProductosPage
from utils.reader import read_productos_json,read_users_csv,read_users_by_type

@pytest.mark.parametrize("data",read_users_by_type("user_ok"))
def test_productos(driver,data):
   login_page = LoginPage(driver)
   productos_page = ProductosPage(driver)
    

   login_page.abrir_pagina()
   login_page.hacer_login(data["usuario"],data["password"])
      
   productos = productos_page.obtener_productos()
            
   #validación de existencia de productos
            
   assert len(productos) > 0

           
   #validación de integridad de los productos
            
   
   assert productos_page.obtener_nombre_primer_producto() == "Sauce Labs Backpack"
   assert productos_page.obtener_precio_primer_producto() == "$29.99"

   #verificar menu

           
   assert productos_page.menu_visible() 

   #verificar filtro

   assert productos_page.filtro_visible()

@pytest.mark.parametrize("data",read_users_by_type("user_ok"))
def test_agregar_producto_seleccionado(driver,data):
      login_page = LoginPage(driver)
      productos_page = ProductosPage(driver)
          
      
      login_page.abrir_pagina()
      login_page.hacer_login(data["usuario"],data["password"])
            
     
      productos = productos_page.obtener_productos()
                       
     #validación de existencia de productos
                       
      assert len(productos) > 0
      #lee el primer producto del JSON 
      producto= read_productos_json()[0]  
      #Agregar producto del JSON 
      productos_page.agregar_productos_por_nombre(producto["nombre"])
      
      
      contador = productos_page.contador_carrito_visible()
      assert contador == "1", "Debe incrementarse el valor en 1"  

@pytest.mark.parametrize("data",read_users_by_type("user_ok"))
def test_eliminar_producto_seleccionado(driver,data):
      login_page = LoginPage(driver)
      productos_page = ProductosPage(driver)
               
           
      login_page.abrir_pagina()
      login_page.hacer_login(data["usuario"],data["password"])
                 
          
      productos = productos_page.obtener_productos()
                            
          #validación de existencia de productos
                            
      assert len(productos) > 0
           #lee el primer producto del JSON 
      producto= read_productos_json()[1]  
           #Agregar producto del JSON 
      productos_page.agregar_productos_por_nombre(producto["nombre"])
           
           
      contador = productos_page.contador_carrito_visible()
      assert contador == "1", "Debe incrementarse el valor en 1"

      productos_page.boton_quitar_producto()

      assert productos_page.contador_carrito_vacio(), "No debería mostrarse el contador"

                   
 