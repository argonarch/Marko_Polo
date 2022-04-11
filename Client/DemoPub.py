# Creado ChepeCarlos de ALSW
# Tutorial Completo en https://nocheprogramacion.com
# Canal Youtube https://youtube.com/alswnet?sub_confirmation=1

import paho.mqtt.client as mqtt
dicc_principal = open("input_prueba.json", "r")
dicc_lecture = dicc_principal.read()
dicc_principal.close()
client = mqtt.Client()
client.connect("broker.emqx.io", 1883, 60)
client.publish("sandia-con-pure-y-tostada", dicc_lecture)
