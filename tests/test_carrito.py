import pytest

from pages.login_page import LoginPage
from pages.carrito_page import CarritoPage
from pages.productos_page import ProductosPage
from utils.reader import read_productos_json,read_users_csv,read_users_by_type



@pytest.mark.parametrize("data",read_users_by_type("user_ok"))
def test_agregar_productos_carrito_exitoso(driver,data):
    
    login_page = LoginPage(driver)
    productos_page =  ProductosPage(driver)
    carrito_page = CarritoPage(driver)
    
    login_page.abrir_pagina()
        
    login_page.hacer_login(data["usuario"],data["password"])
   
    #lee el primer producto del JSON 
    producto= read_productos_json()[0] 
    
    #Agregar producto del JSON 
    productos_page.agregar_productos_por_nombre(producto["nombre"])
    
    assert productos_page.contador_carrito_visible() == "1"

      #Navegar al carrito de compras
    productos_page.ir_al_carrito()
    
      #Comprobar que el producto añadido aparezca correctamente en el carrito
    assert carrito_page.obtener_nombre_producto_carrito() == producto["nombre"], "El nombre del producto no coincide"

    assert carrito_page.obtener_precio_producto_carrito() == producto["precio"], "El precio del producto no coincide"
    
    productos_en_carrito = carrito_page.obtener_items_carrito()
    assert len(productos_en_carrito) == 1 , f"El contador del carrito es {len(productos_en_carrito)} (se esperaba 1)"
    
    

          
    
@pytest.mark.parametrize("data",read_users_by_type("user_ok"))
def test_eliminar_productos_carrito_exitoso(driver,data):
    
    login_page = LoginPage(driver)
    productos_page =  ProductosPage(driver)
    carrito_page = CarritoPage(driver)
        
    login_page.abrir_pagina()
            
    login_page.hacer_login(data["usuario"],data["password"])
       
        #lee el segundo producto del JSON 
    producto= read_productos_json()[1] 
    print(producto)
        #Agregar producto del JSON 
    productos_page.agregar_productos_por_nombre(producto["nombre"])
        
    assert productos_page.contador_carrito_visible() == "1"
    
      #Navegar al carrito de compras
    productos_page.ir_al_carrito()
        
    #Comprobar que el producto añadido aparezca correctamente en el carrito
    assert carrito_page.obtener_nombre_producto_carrito() == producto["nombre"], "El nombre del producto no coincide"
    
    assert carrito_page.obtener_precio_producto_carrito() == producto["precio"], "El precio del producto no coincide"
        
    productos_en_carrito = carrito_page.obtener_items_carrito()

    assert len(productos_en_carrito) == 1 , f"El contador del carrito es {len(productos_en_carrito)} (se esperaba 1)"
    #Finaliza precondición
    carrito_page.quitar_item_carrito()
           
   

    # Verificar que no queda ningún producto ni contador
    assert len(carrito_page.obtener_items_carrito()) == 0, "El carrito debería estar vacío"
    assert len(carrito_page.obtener_contador_carrito()) == 0, "No debería mostrarse el contador"

  