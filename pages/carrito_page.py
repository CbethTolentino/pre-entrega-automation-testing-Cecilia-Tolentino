from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CarritoPage:
    # SELECTORES DEL CARRITO
    
    BOTON_QUITAR = (By.CSS_SELECTOR, "button[id^='remove']")
    CONTADOR_CARRITO = (By.CLASS_NAME, "shopping_cart_badge")
    ITEM_CARRITO = (By.CLASS_NAME, "cart_item")
    NOMBRE_PRODUCTO = (By.CSS_SELECTOR, ".cart_item .inventory_item_name")
    PRECIO_PRODUCTO = (By.CSS_SELECTOR, ".cart_item .inventory_item_price")
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

   

    def obtener_nombre_producto_carrito(self):
        nombre_producto = self.wait.until(EC.visibility_of_element_located(self.NOMBRE_PRODUCTO))
        return nombre_producto.text

    def obtener_precio_producto_carrito(self):
        precio_producto = self.wait.until(EC.visibility_of_element_located(self.PRECIO_PRODUCTO))
        return float(precio_producto.text.replace("$", ""))

    def obtener_items_carrito(self):
         return self.driver.find_elements(*self.ITEM_CARRITO)
           
    def quitar_item_carrito(self):
        self.driver.find_element(*self.BOTON_QUITAR).click()
        return self

    def obtener_contador_carrito(self):
             return self.driver.find_elements(*self.CONTADOR_CARRITO)