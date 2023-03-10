#!/bin/env bash
if [ $1 == "install" ]; then
    python3 -m venv env
    . env/bin/activate
    pip install -r requirements.txt
elif [ $1 == "start" ]; then
    echo 'start marko_polo client - server'
    bash -c "./marko_client/run_client.sh start" &
    bash -c "./marko_server/run_server.sh start" &
elif [ $1 == "stop" ]; then
    bash -c "./marko_server/run_server.sh stop" &
    bash -c "./marko_client/run_client.sh stop" &
fi