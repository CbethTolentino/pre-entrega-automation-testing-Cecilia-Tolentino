
import pytest
import requests
from utils.logger import logger

from utils.reader import read_usuarios_api_json

def test_obtener_usuario(base_url,header_request):
   logger.info(f"Relizando la solitud GET a {base_url} ")
    
   response = requests.get(f"{base_url}/users/2",headers=header_request)
   logger.info(f"Status code: {response.status_code}")

   assert response.status_code ==200
   logger.info("Prueba de status validada")
 

   assert "application/json" in response.headers["Content-type"]
   logger.info("Prueba de contenido del headers validada") 
  

    
   data = response.json()
   assert "data" in data
   assert isinstance(data["data"],dict)
   logger.info("Prueba que valida que el contenido sea un diccionario") 
   

    #nivel 4 : contenido

   assert data["data"]["id"] == 2
   logger.info("Prueba del contenido del id validada") 
   assert data["data"]["email"] =="janet.weaver@reqres.in"
   logger.info("Prueba del contenido del email validada") 
    #nivel 5 tiempo de respuesta

   assert response.elapsed.total_seconds() < 5 , "debe responder antes de los 5 seg"
   logger.info("Prueba del tiempo de respuesta validada") 
#crear usuario
def test_crear_usuario(base_url,header_request):
      #lee el primer producto del JSON 
   logger.info("Lectura del primer usuario del archivo json")     
   usuario =read_usuarios_api_json()[0]
   logger.info(f"Relizando la solitud POST a {base_url} ") 
   response = requests.post(f"{base_url}/users",headers=header_request,json=usuario)
      
   
         #nivel 1: status code
   assert response.status_code ==201
   logger.info("Prueba de status validada")
         #nivel 2: headers
     
   assert "application/json" in response.headers["Content-type"]
   logger.info("Prueba de contenido del headers validada")   
        #"Nivel 3 estructura, valida que el contenido sea un diccionario es isinstance"
     
   
   data = response.json()

   assert isinstance(data,dict)
   assert "email" in data
   assert "first_name" in data
   assert "last_name" in data
   assert  "id" in data
   logger.info("Prueba que valida que el contenido sea un diccionario")  
     #nivel 4 

   assert data["email"] == usuario["email"]
   assert data["first_name"] == usuario["first_name"]
   assert data["last_name"] == usuario["last_name"]
   assert data["job"] == usuario["job"]
   logger.info("Prueba que la integridad de los datos validada")  
     #nivel 5 tiempo de respuesta
     
   assert response.elapsed.total_seconds() < 10, "debe responder antes de los 10 seg"
   logger.info("Prueba del tiempo de respuesta validada") 

# Eliminar usuario
def test_delete_user(base_url,header_request):
    logger.info(f"Relizando la solitud DELETE a {base_url}")
    response = requests.delete(f"{base_url}/users/2",headers=header_request)

    assert response.status_code == 204
    logger.info("Prueba de status validada")
    assert "Content-Type" not in response.headers
    logger.info("Prueba de contenido del headers validada")
    assert len(response.content) == 0
    logger.info("Prueba de que no exista contenido validada")
    assert response.elapsed.total_seconds() < 10 , "debe responder antes de los 10 seg"
    logger.info("Prueba del tiempo de respuesta validada")