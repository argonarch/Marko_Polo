#!/bin/bash

#identifica el directorio donde estan los archivos
basedir=`readlink -e $0 | sed 's:\/[^\/]*$::g'`

echo '--> Cerrando Cliente python (trinity)'
kill `ps aux | grep 'SCREEN -c config/screen_conf -S trinity_client -d -m python3 ./hotword.py' | grep -v grep | awk '{print $2}'` 2> /dev/null

echo '--> Reproduciendo saludo'
trinity-randomwav bye 2> /dev/null &
