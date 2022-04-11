#!/usr/bin/env python3

import paho.mqtt.client as mqtt
import json
import dicc_json


ruta = "192.168.0.5"
Topic = "sandia"

def input_Primary (dicc_python):
	user = str(dicc_python["Usuario"])
	password = str(dicc_python["Contrasena"])
	frase = str(dicc_python["Frase"])
	print (f"se ingreso como usuario: " + user + 
			"\nSe ingreso como contraseña: " + password +
			"\nSe ingreso como frase: " + frase)
	dicc_json.entrada(frase)
	return

def on_connect(client, userdata, flags, rc):
    print("Inicializado, esperando ordenes...")
    client.subscribe(Topic)


def on_message(client, userdata, msg):
	if msg.topic == Topic:
		input_dicc = msg.payload.decode()
		print("tu entrada fue:")
		print(input_dicc)
		input_modif = json.loads(input_dicc)
		input_Primary(input_modif)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(ruta, 1883, 60)
client.loop_forever()
