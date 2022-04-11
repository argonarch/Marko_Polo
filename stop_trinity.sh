#!/bin/bash

#identifica el directorio donde estan los archivos
basedir=`readlink -e $0 | sed 's:\/[^\/]*$::g'`

echo '--> Deteniendo el servidor (trinity)'
bash $basedir/server/stop_server.sh &> /dev/null &
