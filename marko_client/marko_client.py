#!/usr/bin/env python3

# Creado ChepeCarlos de ALSW
# Tutorial Completo en https://nocheprogramacion.com
# Canal Youtube https://youtube.com/alswnet?sub_confirmation=1
import json
from operator import index 
import paho.mqtt.client as mqtt
from decouple import config
import os

def sender(text_analized):
    ruta = config('Broker_Mqtt')
    topic = config('Topic_Mqtt')

    ruta_json = "mensaje.json"
    
    # Se lee el contenido del archivo json
    dicc_principal = open(ruta_json, "r")
    dicc_lecture = dicc_principal.read()
    dicc_principal.close()

    # Se guarda y reemplaza el contenido de Frase del archivo json 
    dicc_python = json.loads(dicc_lecture)
    dicc_python["Frase"] = text_analized
    dicc_json = json.dumps(dicc_python, indent=4)
    
    # Se reescribe el contenido del archivo json
    dicc_principal = open(ruta_json, "w")
    dicc_principal.write(dicc_json)
    dicc_principal.close()
    
    # Se envia el contenido reemplazado
    client = mqtt.Client()
    client.connect(ruta, 1883, 60)
    client.publish(topic, dicc_json)

    replay_m("ready")
    return 'nesecitas algo mas?'

def replay_m(folder):
    os.system("aplay -q `ls $PWD/voice/" + folder +"/* | shuf -n 1`" )
    return

def limpiar_acentos(text):
    acentos = { 'á': 'a', 
                'é': 'e', 
                'í': 'i', 
                'ó': 'o', 
                'ú': 'u'}
    for acen in acentos:
        if acen in text:
            text = text.replace(acen, acentos[acen])
    return text
