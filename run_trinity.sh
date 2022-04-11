#!/bin/bash

#identifica el directorio donde estan los archivos
basedir=`readlink -e $0 | sed 's:\/[^\/]*$::g'`

echo '--> Iniciando el servidor (trinity)'
bash $basedir/server/run_server.sh &> /dev/null &

