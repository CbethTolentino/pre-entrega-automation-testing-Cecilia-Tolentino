from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    # SELECTORES DEL CHECKOUT
    NOMBRE = (By.ID, "first-name")
    APELLIDO = (By.ID, "last-name")
    CODIGO_POSTAL = (By.ID, "postal-code")
    BOTON_CONTINUAR = (By.ID, "continue")
    BOTON_FINALIZAR = (By.ID, "finish")
    MENSAJE_ERROR = (By.CSS_SELECTOR, "[data-test='error']")
    NOMBRE_PRODUCTO_RESUMEN = (By.CSS_SELECTOR, ".cart_item .inventory_item_name")
    SUBTOTAL = (By.CLASS_NAME, "summary_subtotal_label")
    MENSAJE_CONFIRMACION = (By.CLASS_NAME, "complete-header")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def _escribir(self, localizador, texto):
        campo = self.wait.until(EC.visibility_of_element_located(localizador))
        campo.clear()
        campo.send_keys(texto)

    def completar_datos(self, nombre, apellido, codigo_postal):
        
        self._escribir(self.NOMBRE, nombre)
        self._escribir(self.APELLIDO, apellido)
        self._escribir(self.CODIGO_POSTAL, codigo_postal)
        return self

    def continuar(self):
        self.wait.until(EC.element_to_be_clickable(self.BOTON_CONTINUAR)).click()
        return self

    def obtener_error(self):
        return self.wait.until(EC.visibility_of_element_located(self.MENSAJE_ERROR)).text

    def obtener_nombre_producto_resumen(self):
        return self.wait.until(EC.visibility_of_element_located(self.NOMBRE_PRODUCTO_RESUMEN)).text

    def obtener_subtotal(self):
        return self.wait.until(EC.visibility_of_element_located(self.SUBTOTAL)).text

    def finalizar_compra(self):
        self.wait.until(EC.element_to_be_clickable(self.BOTON_FINALIZAR)).click()
        return self

    def obtener_mensaje_confirmacion(self):
        return self.wait.until(EC.visibility_of_element_located(self.MENSAJE_CONFIRMACION)).text