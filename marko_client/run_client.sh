#!/bin/bash
basedir=`readlink -e $0 | sed 's:\/[^\/]*$::g'`

if [ 'start-cloud' == $1 ]; then
    echo '--> creando client con mqtt'
    cd $basedir
    source ./env/bin/activate
    screen -S marko_client -dm python3 ./hotword.py cloud
elif [ 'start-home' == $1 ]; then
    echo '--> creando client con socket'
    cd $basedir
    source ./env/bin/activate
    screen -S marko_client -dm python3 ./hotword.py home
elif [ 'stop' == $1 ]; then
    echo '--> cerrando screen client'
    screen -XS marko_client quit
elif [ "install" == $1 ]; then
    python3 -m venv env
    . env/bin/activate
    pip install -r requirements.txt
fi


