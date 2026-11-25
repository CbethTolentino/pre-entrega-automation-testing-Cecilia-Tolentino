from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductosPage:
#SELECTORES DEL INVENTORY 

 LOGO = (By.CLASS_NAME, "app_logo")
 TITULO_SECCION = (By.CLASS_NAME, "title")
 PRODUCTOS = (By.CLASS_NAME, "inventory_item")
 NOMBRE_PRODUCTO = (By.CLASS_NAME, "inventory_item_name")
 PRECIO_PRODUCTO = (By.CLASS_NAME, "inventory_item_price")
 BOTON_MENU = (By.ID, "react-burger-menu-btn")
 FILTRO_ORDEN = (By.CLASS_NAME, "product_sort_container")
 BOTON_AGREGAR = (By.CSS_SELECTOR, "button[id^='add-to-cart']")
 BOTON_QUITAR = (By.CSS_SELECTOR, "button[id^='remove']")
 def __init__(self,driver):
    self.driver = driver

 def obtener_productos(self, PRODUCTOS):
   return self.driver.find_elements(PRODUCTOS) 
 
 def obtener_nombre_primer_producto(self):
   producto = self.obtener_productos()

   return producto[0].findelement(self.NOMBRE_PRODUCTO).text

 def obtener_precio_primer_producto(self):
    producto = self.obtener_productos()
 
    return producto[0].findelement(self.PRECIO_PRODUCTO).text

 def menu_visible(self):
   menu = self.driver.findElement(self.BOTON_MENU)

   return menu.is_displayed()

 def filtro_visible(self):
    filtro = self.driver.findElement(self.FILTRO_ORDEN)
 
    return filtro.is_displayed()
 
 #Funcion que busca un producto por nombre, lo agrega al carrito y devuelve (nombre).
 def agregar_productos_por_nombre(self,nombre_buscado):
   

        productos = self.obtener_productos()

                
      
        for producto in productos:
              nombre = producto.find_element(self.NOMBRE_PRODUCTO).text
              if nombre == nombre_buscado:
                producto.find_element(self.BOTON_AGREGAR).click()
                return nombre
                # Si el for termina sin hacer return, el producto no existe
                raise AssertionError(f"No se encontró el producto '{nombre_buscado}'")

 def boton_agregar_producto(self):
      self.driver.findElement(self.BOTON_AGREGAR).click()

      return self

 def boton_quitar_producto(self):
       self.driver.findElement(self.BOTON_QUITAR).click()
 
       return self

 def contador_carrito_visible(self):
     contador =self.wait.until(EC.visibility_of_element_located(self.CONTADOR_CARRITO))                  
                         
     return len(contador)                    
              