# Este es mi primer desarrollo de un agente IA muy basico, usando
# un modelo gratuito de OpenRouter.
# Author: Silvana Sanchez

import requests
import json
from dotenv import load_dotenv
import os

load_dotenv()

mensajes = [
    {
        "role": "system",
        "content": "Soy un asistente"
    }
]

while True:

    usuario = input("Tu ::  ").strip()

    if not usuario:
        continue


    if usuario.lower() in ('salir', 'exit', 'adios'):
        print("Nos vemos otro dia, adios\n")
        break

    # Agregar al historial
    mensajes.append(
        {
            "role": "user",
            "content": usuario
        }
    )

    # Primera llamada al API con razonamiento
    response = requests.post(
    url="https://openrouter.ai/api/v1/chat/completions",
    headers={
        "Authorization": "Bearer "+ os.getenv("API_KEY"),
        "Content-Type": "application/json",
    },
    data=json.dumps({
        "model": "nvidia/nemotron-3-ultra-550b-a55b:free",
        "messages": mensajes,
        "reasoning": {"enabled": True}
    })
    )

    # Obten la salida del asistente
    response = response.json()

    # Guardo un historico del asistente, por si se me acaban los tokens
    try:
        asistente = response['choices'][0]['message']['content']
       # response = response['choices'][0]['message']['content']
        mensajes.append( { "role": "assistant", "content": asistente })

    except:
        asistente = response

    print(F"Asistente ::  {asistente}")

