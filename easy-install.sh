#!/bin/bash

cd $HOME

sudo apt install python3-pip git python3-pyaudio libatlas-base-dev screen

git clone https://github.com/argonarch/Marko_Polo.git

pip install paho-mqtt SpeechRecognition pvporcupine pvrecorder

