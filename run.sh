#!/bin/env bash
if [ $1 == "install" ]; then
    echo 'install marko_polo server'
    bash -c "./marko_server/run_server.sh install" 
    echo 'install marko_polo client'
    bash -c "./marko_client/run_client.sh install"
elif [ $1 == "start-cloud" ]; then
    echo 'start marko_polo client - server con mqtt'
    bash -c "./marko_server/run_server.sh start-cloud" 
    bash -c "./marko_client/run_client.sh start-cloud"
elif [ $1 == "start-home" ]; then
    echo 'start marko_polo client - server con socket'
    bash -c "./marko_server/run_server.sh start-home" 
    bash -c "./marko_client/run_client.sh start-home"
elif [ $1 == "stop" ]; then
    bash -c "./marko_server/run_server.sh stop"
    bash -c "./marko_client/run_client.sh stop"
fi