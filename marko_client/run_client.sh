#!/bin/bash
basedir=`readlink -e $0 | sed 's:\/[^\/]*$::g'`

if [ 'start' == $1 ]; then
    echo '--> creando screen client'
    cd $basedir
    screen -S marko_client -dm python3 ./hotword.py
elif [ 'stop' == $1 ]; then
    echo '--> cerrando screen client'
    screen -XS marko_client quit
fi


