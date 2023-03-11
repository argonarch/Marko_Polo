#!/bin/bash
basedir=`readlink -e $0 | sed 's:\/[^\/]*$::g'`

if [ 'start' == $1 ]; then    
    echo '--> creando screen server'
    cd $basedir
    screen -S marko_server -dm python3 ./marko_server.py 
elif [ 'stop' == $1 ]; then
    echo '--> cerrando screen server'
    screen -XS marko_server quit
fi




