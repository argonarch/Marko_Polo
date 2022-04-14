#!/bin/bash

#identifica el directorio donde estan los archivos
basedir=`readlink -e $0 | sed 's:\/[^\/]*$::g'`

echo '--> Estableciendo nuevo PATH'
PATH=$PATH:$basedir/bin

echo '--> Iniciando el servidor Brain (trinity)'
cd $basedir/brain
screen -c ../config/screen_conf -S trinity_brain -d -m python3 trinity.py

