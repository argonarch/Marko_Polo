#!/bin/bash
basedir=`readlink -e $0 | sed 's:\/[^\/]*$::g'`

if [ $1 == "start" ]; then
    echo $basedir
    echo '--> creando screen client'
    screen -S marko_client -dm python3 ./hotword.py
elif [ $1 == "stop" ]; then
    echo '--> cerrando screen client'
    screen -XS marko_client quit
fi


