import pytest
from pages.login_page import LoginPage
from pages.productos_page import ProductosPage
from utils.reader import read_productos_json, read_users_by_type
from utils.logger import logger


@pytest.mark.parametrize("data", read_users_by_type("user_ok"))
def test_productos(driver, data):
    try:
        logger.info("Inicializando la prueba de Inventario")
        login_page = LoginPage(driver)
        productos_page = ProductosPage(driver)

        logger.info("Ingresando a la pagina web")
        login_page.abrir_pagina()
        logger.info("Ingresando credenciales para iniciar sesión")
        login_page.hacer_login(data["usuario"], data["password"])
        logger.info("Sesión iniciada correctamente")
        productos = productos_page.obtener_productos()
        logger.info("Productos de la pagina web capturados")
        # validación de existencia de productos

        assert len(productos) > 0
        logger.info("Prueba de cantidad de productos validada")

        # validación de integridad de los productos

        assert productos_page.obtener_nombre_primer_producto() == "Sauce Labs Backpack"
        assert productos_page.obtener_precio_primer_producto() == "$29.99"
        logger.info("Prueba de integridad de la información de los productos validada")
        # verificar menu

        assert productos_page.menu_visible()
        logger.info("Prueba de visibilidad del menu en la pagina validada")
        # verificar filtro

        assert productos_page.filtro_visible()
        logger.info("Prueba de visibilidad del filtro en la pagina validada")
    except Exception:
        logger.exception("Error durante la prueba de Inventario")
        raise


@pytest.mark.parametrize("data", read_users_by_type("user_ok"))
def test_agregar_producto_seleccionado(driver, data):
    try:
        logger.info("Inicializando la prueba de Inventario")
        login_page = LoginPage(driver)
        productos_page = ProductosPage(driver)

        logger.info("Ingresando a la pagina web")
        login_page.abrir_pagina()

        logger.info("Ingresando credenciales para iniciar sesión")

        login_page.hacer_login(data["usuario"], data["password"])
        logger.info("Sesión iniciada correctamente")

        productos = productos_page.obtener_productos()
        logger.info("Productos de la pagina web capturados")
        # validación de existencia de productos

        assert len(productos) > 0
        logger.info("Prueba de cantidad de productos validada")
        # lee el primer producto del JSON
        producto = read_productos_json()[0]
        # Agregar producto del JSON
        logger.info("Se agrega productos al inventario por nombre")
        productos_page.agregar_productos_por_nombre(producto["nombre"])

        contador = productos_page.contador_carrito_visible()
        assert contador == "1", "Debe incrementarse el valor en 1"
        logger.info("Prueba del producto agregado validada")
    except Exception:
        logger.exception("Error durante la prueba de Agregar producto seleccionado")
        raise


@pytest.mark.parametrize("data", read_users_by_type("user_ok"))
def test_eliminar_producto_seleccionado(driver, data):
    try:
        logger.info("Inicializando la prueba de Inventario")
        login_page = LoginPage(driver)
        productos_page = ProductosPage(driver)

        logger.info("Ingresando a la pagina web")
        login_page.abrir_pagina()
        logger.info("Ingresando credenciales para iniciar sesión")
        login_page.hacer_login(data["usuario"], data["password"])
        logger.info("Sesión iniciada correctamente")

        productos = productos_page.obtener_productos()
        logger.info("Productos de la pagina web capturados")
        # validación de existencia de productos

        assert len(productos) > 0
        logger.info("Prueba de cantidad de productos validada")
        # lee el primer producto del JSON
        producto = read_productos_json()[1]
        # Agregar producto del JSON
        logger.info("Se agrega productos al inventario por nombre")
        productos_page.agregar_productos_por_nombre(producto["nombre"])

        contador = productos_page.contador_carrito_visible()
        assert contador == "1", "Debe incrementarse el valor en 1"
        logger.info("Prueba del producto agregado validada")
        productos_page.boton_quitar_producto()
        logger.info("Eliminación del producto")
        assert (
            productos_page.contador_carrito_vacio()
        ), "No debería mostrarse el contador"
        logger.info("Prueba del producto eliminado validada")
    except Exception:
        logger.exception("Error durante la prueba de Eliminar producto seleccionado")
        raise
