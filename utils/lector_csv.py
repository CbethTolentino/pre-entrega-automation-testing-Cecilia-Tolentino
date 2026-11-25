import csv
import json
import pathlib


def read_users_csv():
    
    with open("data/users.csv",newline='',encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)

        return list(lector)


def read_productos_json():
    with open("data/products.json") as file:
        return json.load(file)