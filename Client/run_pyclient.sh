#!/bin/bash

#identifica el directorio donde estan los archivos
basedir=`readlink -e $0 | sed 's:\/[^\/]*$::g'`

echo '  > Cliente python para Trinity'

echo '--> Iniciando el client python (trinity)'
screen -c ./screen_conf -S trinity_client -d -m ./hotword.py
