#!/bin/bash
basedir=`readlink -e $0 | sed 's:\/[^\/]*$::g'`

if [ 'start-cloud' == $1 ]; then    
    echo '--> creando screen server'
    cd $basedir
    screen -S marko_server -dm python3 ./marko_server_mqtt.py 
elif [ 'start-home' == $1 ]; then    
    echo '--> creando screen server'
    cd $basedir
    screen -S marko_server -dm python3 ./marko_server_socket.py 
elif [ 'stop' == $1 ]; then
    echo '--> cerrando screen server'
    screen -XS marko_server quit
fi




