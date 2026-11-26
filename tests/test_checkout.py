import pytest

from pages.login_page import LoginPage
from pages.productos_page import ProductosPage
from pages.carrito_page import CarritoPage
from pages.checkout_page import CheckoutPage
from utils.reader import read_productos_json, read_users_by_type, read_checkout_json
from utils.logger import logger


@pytest.mark.parametrize("data", read_users_by_type("user_ok"))
def test_checkout_exitoso(driver, data):
    login_page = LoginPage(driver)
    productos_page = ProductosPage(driver)
    carrito_page = CarritoPage(driver)
    checkout_page = CheckoutPage(driver)
    cliente = read_checkout_json()
    producto = read_productos_json()[0]

    logger.info("Iniciando prueba de checkout exitoso")
    login_page.abrir_pagina()
    login_page.hacer_login(data["usuario"], data["password"])

    logger.info("Agregando producto y yendo al checkout")
    productos_page.agregar_productos_por_nombre(producto["nombre"])
    productos_page.ir_al_carrito()
    carrito_page.ir_a_checkout()

    logger.info("Completando los datos del comprador")
    checkout_page.completar_datos(cliente["nombre"], cliente["apellido"], cliente["codigo_postal"])
    checkout_page.continuar()

    assert checkout_page.obtener_nombre_producto_resumen() == producto["nombre"], "El producto del resumen no coincide"
    assert f"${producto['precio']}" in checkout_page.obtener_subtotal(), "El subtotal no coincide"
    logger.info("Resumen de la compra validado")

    checkout_page.finalizar_compra()
    assert "Thank you for your order" in checkout_page.obtener_mensaje_confirmacion()
    assert "checkout-complete" in driver.current_url
    logger.info("Compra finalizada correctamente")


@pytest.mark.parametrize("data", read_users_by_type("user_ok"))
def test_checkout_sin_nombre(driver, data):
    login_page = LoginPage(driver)
    productos_page = ProductosPage(driver)
    carrito_page = CarritoPage(driver)
    checkout_page = CheckoutPage(driver)
    cliente = read_checkout_json()
    producto = read_productos_json()[0]

    logger.info("Iniciando prueba de checkout sin nombre")
    login_page.abrir_pagina()
    login_page.hacer_login(data["usuario"], data["password"])
    productos_page.agregar_productos_por_nombre(producto["nombre"])
    productos_page.ir_al_carrito()
    carrito_page.ir_a_checkout()

    checkout_page.completar_datos("", cliente["apellido"], cliente["codigo_postal"])
    checkout_page.continuar()

    assert "First Name is required" in checkout_page.obtener_error()
    assert "checkout-step-two" not in driver.current_url, "No debe avanzar al resumen"
    logger.info("Mensaje de error por nombre vacío validado")