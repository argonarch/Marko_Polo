#!/bin/bash

cd $HOME

git clone https://github.com/argonarch/trinity.git

pip install paho-mqtt SpeechRecognition

sudo apt install python3-pyaudio libatlas-base-dev screen
