from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class Carrito_Page:

#SELECTORES DEL CARRITO 
 BOTON_AGREGAR = (By.CSS_SELECTOR, "button[id^='add-to-cart']")
 BOTON_QUITAR = (By.CSS_SELECTOR, "button[id^='remove']")
 CONTADOR_CARRITO = (By.CLASS_NAME, "shopping_cart_badge")
 ICONO_CARRITO = (By.CLASS_NAME, "shopping_cart_link")
 ITEM_CARRITO = (By.CLASS_NAME, "cart_item")
NOMBRE_PRODUCTO = (By.CLASS_NAME, "inventory_item_name")

def __init__(self,driver):
    self.driver = driver
    self.wait = WebDriverWait(driver,10)

def boton_icono_carrito(self):
      self.driver.findElement(self.ICONO_CARRITO).click()

      return self

def obtener_nombre_producto_carrito(self):
        nombre_producto = self.wait.until(EC.visibility_of_element_located(self._CART_ITEM_NAME))
        return nombre_producto.text


