#!/usr/bin/env python3

# Creado ChepeCarlos de ALSW
# Tutorial Completo en https://nocheprogramacion.com
# Canal Youtube https://youtube.com/alswnet?sub_confirmation=1

from decouple import config
from utils import replay_m

def sender_cloud(text_analized):
    import json
    import paho.mqtt.client as mqtt
    
    ruta = config('Broker_Mqtt')
    topic = config('Topic_Mqtt')

    mensaje = {
        "Usuario": "Pepe",
        "Contrasena": "Paris",
        "Frase": ""
    }

    mensaje["Frase"] = text_analized

    dicc_json = json.dumps(mensaje)

    client = mqtt.Client()
    client.connect(ruta, 1883, 60)
    client.publish(topic, dicc_json)

    replay_m("more")
    return 'nesecitas algo mas?'

def sender_home(text_analized):
    import socket

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 10000)
    sock.connect(server_address)

    #enviado frase
    print('Enviando: %s'%text_analized)
    sock.send(text_analized.encode('utf-8'))
    
    # Look for the response
    data = sock.recv(1024).decode('utf-8')
    print('%s'%data)

    print('Cerrando socket')
    sock.close()
    replay_m("more")
    return 'nesecitas algo mas?'


