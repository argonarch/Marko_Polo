#!/bin/bash
basedir=`readlink -e $0 | sed 's:\/[^\/]*$::g'`

if [ 'start-cloud' == $1 ]; then
    echo '--> creando client con mqtt'
    cd $basedir
    screen -S marko_client -dm python3 ./hotword.py cloud
elif [ 'start-home' == $1 ]; then
    echo '--> creando client con socket'
    cd $basedir
    screen -S marko_client -dm python3 ./hotword.py home
elif [ 'stop' == $1 ]; then
    echo '--> cerrando screen client'
    screen -XS marko_client quit
fi


