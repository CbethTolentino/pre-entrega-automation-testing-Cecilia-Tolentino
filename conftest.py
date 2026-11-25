import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.login_page import LoginPage
import pytest_html
import pathlib
import base64
from pages.login_page import LoginPage


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--incognito")
    options.add_argument("--no-sandbox")    # paraa github
    options.add_argument("--disble-gpu")   # para
    options.add_argument("--windwow-size-1920,1080")    # para tamaño ventana
    options.add_argument("--headless=new")    # para github
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
def headers():
    return {"x-api-key":""}

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport (item,call):
    outcome = yield
    report =outcome.get_result()
    if report.when =="call" and report.failed:
        driver = item.funcargs.get("driver")
        if driver is None:
            return
        carpeta = pathlib.Path("reports/screenshots")
        carpeta.mkdir(parents=True,exist_ok=True)
        archivo = carpeta / f"{item.name}.png"
        driver.save_screenshot(str(archivo)) 
        imagen = base64.b64encode(archivo.read_bytes()).decode("utf-8")
        report.extras = [
            pytest_html.extras.png(imagen, name="Screenshot")
        ]