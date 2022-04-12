#!/bin/bash

#identifica el directorio donde estan los archivos
basedir=`readlink -e $0 | sed 's:\/[^\/]*$::g'`

echo '--> Iniciando el servidor (trinity)'
bash $basedir/server/run_server.sh &> /dev/null &

echo '--> Iniciando el cliente (trinity)'
bash $basedir/client/run_pyclient.sh &> /dev/null &

sleep 1

. /etc/os-release
case "$ID" in
neon)
    konsole -e "screen -r trinity_client" &
    konsole -e "screen -r trinity_brain" &
    ;;
*)

    ;;
esac
