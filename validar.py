# Script que valida si un portal web esta disponible, si el login de acceso es correcto
# y si el acceso es denegado, se sale, de lo contrario se ejecuta el modulo de captura
# se toma una captura de pantalla del escritorio completo + navegador una vez que el acceso
# al portal web es exitoso.

#######################################
##   Autor: Silvana Sanchez           #
#######################################

import requests
from dotenv import load_dotenv
import os
from Modulos import Captura

# Cargamos todas las variables de ambientes definidas en el archivo de texto local .env
load_dotenv()

# Variable que valida si el portal web esta disponible

response = requests.get('https://example.com/login.php')

# Se obtiene el estado del portal web, si esta arriba es codigo 200, si esta abajo o da time out es codigo 404
resultado = response.status_code

if resultado != 200:
    print("Error, portal caido, revisar\n")
    exit()


# Si el portal esta arriba, se procede a hacer el login con las credenciales definidas como parametros de entorno en el archivo .env,
url = 'https://example.com/login.php'
values = {'username': os.getenv("USUARIO"),
         'password': os.getenv("PASSWORD") }

r = requests.post(url, data=values)

# El resultado del acceso lo enviamos a un archivo TXT nuevo en vez de mostrar la salida de la pagina web en pantalla
f = open("salida.txt", "w")
print (r.content, file=f)
f.close()

# leemos el archivo creado previamente para obtener un estatus del acceso al portal web
def check():
    with open('salida.txt') as c:
        datafile = c.readlines()
    for line in datafile:
        if 'Denegado' in line:
            return True
        else:
            return False  

    
# mostramos si el acceso fue denegado o no
if check():
    print('Acceso Denegado, revisar credenciales\n')
    exit()
    
    
if __name__ == "__main__":
    # Se ejecuta el modulo de prueba
    print("Modulo de prueba ejecutado correctamente\n")
    Captura.login_and_screenshot_selenium("https://example.com/login.php", os.getenv("USUARIO"), os.getenv("PASSWORD"))




