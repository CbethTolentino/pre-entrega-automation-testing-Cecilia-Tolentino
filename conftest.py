import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.login_page import LoginPage
import pytest_html
import pathlib
import base64
from pages.login_page import LoginPage
import os
import re
from datetime import datetime
from dotenv import load_dotenv
from utils.logger import logger

load_dotenv()


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument("--incognito")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


@pytest.fixture
def login_in_driver(driver):
    LoginPage(driver).abrir_pagina()
    return driver


@pytest.fixture
def base_url():
    return "https://reqres.in/api"


@pytest.fixture
def header_request():
    api_key = os.getenv("REQRES_API_KEY")
    if not api_key:
        pytest.fail("Falta REQRES_API_KEY en el .env o en las variables de entorno")
    return {"x-api-key": api_key}


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        logger.error(f"Test fallido: {item.name}\n{report.longreprtext}")

        driver = item.funcargs.get("driver")
        if driver is None:
            return

        nombre = re.sub(r"[^\w\-]", "_", item.name)
        fecha = datetime.now().strftime("%Y%m%d_%H%M%S")
        carpeta = pathlib.Path("reports/screenshots")
        carpeta.mkdir(parents=True, exist_ok=True)
        archivo = carpeta / f"{fecha}_{nombre}.png"

        driver.save_screenshot(str(archivo))
        logger.info(f"Screenshot guardado en {archivo}")

        imagen = base64.b64encode(archivo.read_bytes()).decode("utf-8")
        extras = getattr(report, "extras", [])
        extras.append(pytest_html.extras.png(imagen, name="Screenshot"))
        report.extras = extras
