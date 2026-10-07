
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#URL 

URL = "https://www.saucedemo.com/"

#VARIABLE DE TIEMPO TOTAL QUE SE USARA COMO ESPERA EXPLICITAS

TIMEOUT = 10


#SELECTORES DEL LOGIN

USUARIO =(By.ID,"user-name")
PASSWORD =(By.ID,"password")
BOTON_LOGIN =(By.ID,"login-button")
MENSAJE_ERROR = (By.CSS_SELECTOR, "[data-test='error']")
# CREDENCIALES

USUARIO_VALIDO = "standard_user"
USUARIO_BLOQUEADO = "locked_out_user"
PASSWORD_VALIDA = "secret_sauce"

#SELECTORES DEL INVENTORY 

LOGO = (By.CLASS_NAME, "app_logo")
TITULO_SECCION = (By.CLASS_NAME, "title")
PRODUCTOS = (By.CLASS_NAME, "inventory_item")
NOMBRE_PRODUCTO = (By.CLASS_NAME, "inventory_item_name")
PRECIO_PRODUCTO = (By.CLASS_NAME, "inventory_item_price")
BOTON_MENU = (By.ID, "react-burger-menu-btn")
FILTRO_ORDEN = (By.CLASS_NAME, "product_sort_container")

#SELECTORES DEL CARRITO 
BOTON_AGREGAR = (By.CSS_SELECTOR, "button[id^='add-to-cart']")
BOTON_QUITAR = (By.CSS_SELECTOR, "button[id^='remove']")
CONTADOR_CARRITO = (By.CLASS_NAME, "shopping_cart_badge")
ICONO_CARRITO = (By.CLASS_NAME, "shopping_cart_link")

#Función de espera explicita a que el elemento localizado se vea y lo devuelve

def espera_visible(driver, localizador):
    
    espera = WebDriverWait(driver, TIMEOUT)
    return espera.until(EC.visibility_of_element_located(localizador))
 
#Función de espera explicita a que el elemento localizado se pueda clickear y lo devuelve

def espera_clic(driver, localizador):
   
    espera = WebDriverWait(driver, TIMEOUT)
    return espera.until(EC.element_to_be_clickable(localizador))
 
#Funcion reutilizable del login ,completa usuario y password y hace click en el boton de login.

def hacer_login(driver, usuario, password):
    
    driver.get(URL)
    espera_visible(driver, USUARIO).send_keys(usuario)
    driver.find_element(*PASSWORD).send_keys(password)
    espera_clic(driver, BOTON_LOGIN).click()
    assert "/inventory.html" in driver.current_url
    assert espera_visible(driver, LOGO).text == "Swag Labs"
    assert espera_visible(driver, TITULO_SECCION).text == "Products"
 


