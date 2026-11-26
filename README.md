# Proyecto Final - Automation Testing

## Propósito

Framework de automatización de pruebas en Python para el curso "Automation Testing"
(Gobierno de la Ciudad de Buenos Aires). Incluye pruebas de UI sobre
[saucedemo.com](https://www.saucedemo.com) y pruebas de API sobre [ReqRes](https://reqres.in).

## Tecnologias Utilizadas

- Python 3.13
- Pytest y pytest-html (ejecución y reportes)
- Selenium WebDriver (UI) con Page Object Model
- Requests (API)
- python-dotenv (variables de entorno)
- Git, GitHub y GitHub Actions

## Estructura del proyecto

```
.github/workflows/test.yml   # pipeline de CI
data/                        # datos de prueba (users.csv, productos.json, users_api.json)
pages/                       # Page Objects: login, productos y carrito
tests/                       # test_login, test_productos, test_carrito, test_api, test_checkout
utils/                       # reader (CSV/JSON) y logger
conftest.py                  # fixtures y screenshots en fallos
pytest.ini                   # configuración de pytest y reporte HTML
requirements.txt
```
## Instalación
```powershell
git clone https://github.com/<usuario>/proyecto-final-automation-testing-cecilia-tolentino.git
cd proyecto-final-automation-testing-cecilia-tolentino
pip install -r requirements.txt
```

Creá un archivo `.env` en la raíz (copiá `.env.example`) con tu API key de ReqRes:

```
REQRES_API_KEY=tu_api_key
```

## Ejecución

```powershell
pytest                          # todas las pruebas
pytest tests/test_api.py        # solo API
pytest tests/test_login.py      # solo login
pytest tests/test_carrito.py    # solo carrito
pytest tests/test_checkout.py   # solo checkout
pytest tests/test_productos.py  # solo productos

```

## Ejecución de pruebas

```python 
pytest 
```
## Carpeta `utils/`

Contiene las utilidades que comparten todos los tests.

### `logger.py`

Configura el sistema de logging del proyecto. Al ejecutar las pruebas crea la carpeta `logs/` (si no existe) y genera un archivo nuevo por ejecución, con la fecha y hora en el nombre (`log_<ddmmaaaa_hhmmss>.log`). Cada línea registra la hora, el nivel (`INFO`, `ERROR`), el nombre del logger y el mensaje. Los tests importan `logger` y lo usan para dejar registrados los pasos clave, y el hook de `conftest.py` registra los tests fallidos junto con su traceback.

### `reader.py`

Lee los datos de prueba desde la carpeta `data/`, para que los tests no tengan datos escritos en el código:

- `read_users_csv()`: devuelve todos los usuarios de `users.csv` como lista de diccionarios.
- `read_users_by_type(tipo)`: devuelve solo los usuarios de un tipo (por ejemplo `user_ok` o `user_block`).
- `read_productos_json()`: devuelve la lista de productos de `productos.json`.
- `read_usuarios_api_json()`: devuelve los usuarios de `users_api.json`, usados en los tests de API.
- `read_checkout_json()`: devuelve los datos del comprador de `checkout.json`.

## Manejo de datos de prueba
- En la carpeta `data` se incluyen archivos como:
- `users.csv` -> datos de usuarios validos o invalidos
- `productos.json`-> datos de productos para validación
- `checkout.json` -> datos de usuarios para el checkout
- `users_api.json`-> datos de usuario para las pruebas de api

## Casos de prueba

**UI (saucedemo)**
- Login exitoso, usuario bloqueado, usuario vacío, contraseña vacía, contraseña incorrecta y usuario inexistente (parametrizado desde `users.csv`)
- Verificación del inventario (productos, menú y filtro)
- Agregar y eliminar producto desde el inventario
- Agregar producto y verificarlo en el carrito
- Eliminar producto desde el carrito

**API (ReqRes)**
- GET de un usuario, GET de un usuario inexistente (404), POST de un usuario y DELETE de un usuario

## Reportes, logs y capturas

- **Reporte HTML:** `reportes/reporte.html`. Muestra cada test con su estado (Passed/Failed), su duración y, en los fallidos, el traceback y la captura de pantalla. Abrilo en el navegador.
- **Capturas:** `reports/screenshots/<fecha>_<test>.png`, una por cada test de UI que falla.
- **Logs:** `logs/log_<fecha>.log`, con los pasos de cada prueba para depurar.

## Integración continua

El workflow de GitHub Actions corre las pruebas en cada push a `main` y guarda el reporte como artefacto. La API key se configura como secret `REQRES_API_KEY` del repositorio.

## Autora

Cecilia Tolentino