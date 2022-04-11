#!/bin/bash

cd ~

git clone https://github.com/argonarch/trinity.git

pip install paho-mqtt

sudo apt install python3-pyaudio libatlas-base-dev screen
