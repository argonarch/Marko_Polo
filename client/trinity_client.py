#!/usr/bin/env python3

# Creado ChepeCarlos de ALSW
# Tutorial Completo en https://nocheprogramacion.com
# Canal Youtube https://youtube.com/alswnet?sub_confirmation=1
import json
from operator import index 
import paho.mqtt.client as mqtt


def sender(text_analized):
    ruta = "broker.emqx.io"
    topic = "sandia-con-pure-y-tostada"
    ruta_json = "config/input_prueba.json"
    
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

    return "Nesecita algo mas?"

def limpiar_acentos(texto):
    text = texto.lower()
    acentos = { 'á': 'a', 
                'é': 'e', 
                'í': 'i', 
                'ó': 'o', 
                'ú': 'u'}
    for acen in acentos:
        if acen in text:
            text = text.replace(acen, acentos[acen])
    return text
