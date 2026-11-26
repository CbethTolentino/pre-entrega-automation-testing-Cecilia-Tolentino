import csv
import json



def read_users_csv():
    
    with open("data/users.csv",newline='',encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)

        return list(lector)

# filtra por tipo de usuario
def read_users_by_type(tipo):
    return [u for u in read_users_csv() if u["tipo_usuario"] == tipo]


def read_productos_json():
    with open("data/productos.json") as file:
        return json.load(file)


def read_usuarios_api_json():
    with open("data/users_api.json") as file:
        return json.load(file)    

def read_checkout_json():
    with open("data/checkout.json", encoding="utf-8") as file:
        return json.load(file)    