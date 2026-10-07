# Pre-entrega Automation Testing – saucedemo.com

## Propósito
Automatizar con Selenium WebDriver y Pytest los flujos básicos de
[saucedemo.com](https://www.saucedemo.com): login, verificación del catálogo
y carrito de compras para el curso "Automation Testing" del Gobierno de la Ciudad de Buenos Aires

## Tecnologias Utilizadas

-Python
-Selenium
-Pytest
-Git
-Github

## Instalación

Para instalar las dependencias:
```python
pip install pytest
```
```python
pip install pytest-html
```
```python
pip install selenium
```

## Ejecución de pruebas

```python 
pytest 
```
## Carpeta `utils/`

Contiene `reutilizables.py`, el archivo con todo lo que se repite en más de un test. Así los tests quedan cortos y, si la página cambia, se corrige en un solo lugar.

### Qué incluye

**Configuración**
- `URL`: dirección de la página de saucedemo.
- `TIMEOUT`: segundos máximos que Selenium espera por un elemento (10).

**Credenciales**
- `USUARIO_VALIDO`, `USUARIO_BLOQUEADO` y `PASSWORD_VALIDA`: los datos de login usados en las pruebas.

**Localizadores**
Cada elemento de la página se guarda como una tupla `(By.X, "valor")`, agrupada por sección:
- Login: campos de usuario y password, botón de login y mensaje de error.
- Inventario: logo, título, productos, nombre, precio, menú y filtro de orden.
- Carrito: botones de agregar y quitar, contador e ícono del carrito.

Para los botones de agregar y quitar se usa un selector por prefijo (`id^='add-to-cart'`), porque el id cambia según el producto.

**Funciones**
- `espera_visible(driver, localizador)`: espera explícita hasta que el elemento sea visible y lo devuelve.
- `espera_clic(driver, localizador)`: espera explícita hasta que el elemento se pueda clickear y lo devuelve.
- `hacer_login(driver, usuario, password)`: abre la página, completa el formulario, hace clic en Login y verifica que se llegó al inventario.


## Casos de prueba

-Login exitoso
-Login con usuario bloqueado
-Login con password incorrecta
-Login con password vacio
-Login con usuario vacio
-Login con usuario invalido
-Agregar productos al carrito
-Verificar producto al carrito

## Autora

Cecilia Tolentino