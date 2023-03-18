#!/usr/bin/env python3

import pvporcupine
from pvrecorder import PvRecorder
import speech_recognition as sr
from marko_clients import sender_home, sender_cloud
from decouple import config
import sys
from utils import *
from snowboy.snowboydecoder import HotwordDetector
import signal

modo = sys.argv[1]

def Hotword():

    keyword_path = ['lib/marcopolo_es_linux.ppn']
    access_key = config('Token_Picovoce')
    library_path = 'lib/libpv_porcupine.so'
    model_path = 'lib/porcupine_params_es.pv'
    sensitivity = [0.5]
    input_device_index = 1
    
    AZURE_SPEECH_KEY = config('Azure_Key')
    AZURE_LOCATION = config('Azure_Region')

    recognizer = sr.Recognizer()
    porcupine = None

    replay_m("ready")
    try:
        porcupine = pvporcupine.create(
            access_key=access_key,
            library_path=library_path,
            model_path=model_path,
            keyword_paths=keyword_path,
            sensitivities=sensitivity)

        recorder = PvRecorder(device_index=input_device_index, frame_length=porcupine.frame_length)
        recorder.start()
        print("{" + str(keyword_path) + str(sensitivity) + "}")
        print(f'Using device: {recorder.selected_device}')
        
        while True:
            
            pcm = recorder.read()
            result = porcupine.process(pcm)
            if result >= 0:
                print('Hotword detectado, que nesecitas?')
                with sr.Microphone() as source:
                    audio = recognizer.listen(source)
                try:
                    replay_m("working")
                    texto = recognizer.recognize_azure(audio, key=AZURE_SPEECH_KEY, location=AZURE_LOCATION, language="es-AR",show_all=True)
                    Dicc_Reducido = texto['NBest'][0]['ITN']
                    texto_sin_accento = limpiar_acentos(Dicc_Reducido)
                    if modo == 'cloud':
                        print(sender_cloud(texto_sin_accento))
                    elif modo == 'home':
                        print(sender_home(texto_sin_accento))
                except sr.UnknownValueError:
                    replay_m("repit")
                    print("No se escucho la frase")
                except sr.RequestError as e:
                    print("Error de servicio; {0}".format(e))

    except KeyboardInterrupt:
        print('Stopping ...')
    finally:
        if porcupine is not None:
            porcupine.delete()
        if recorder is not None:
            recorder.delete()

def Hotword_Free():
    recognizer = sr.Recognizer()
    replay_m("ready")
    print('Hotword detectado, que nesecitas?')
    with sr.Microphone() as source:
        audio = recognizer.listen(source)
    try:
        replay_m("working")
        texto = recognizer.recognize_google(audio, language="es_AR")
        texto_sin_accento = limpiar_acentos(texto)
        if modo == 'cloud':
            print(sender_cloud(texto_sin_accento))
        elif modo == 'home':
            print(sender_home(texto_sin_accento))
    except sr.UnknownValueError:
        replay_m("repit")
        print("No se escucho la frase")
    except sr.RequestError as e:
        print("Error de servicio; {0}".format(e))

    except KeyboardInterrupt:
        print('Stopping ...')

def signal_handler(signal, frame):
    global interrupted
    interrupted = True


def interrupt_callback():
    global interrupted
    return interrupted

if __name__ == '__main__':
    #if config('Token_Picovoce') == '' or config('Azure_Key') == '':
    interrupted = False
    signal.signal(signal.SIGINT, signal_handler)
    detector = HotwordDetector("snowboy/hotword.pmdl", sensitivity=0.47, audio_gain=1)
    detector.start(detected_callback=Hotword_Free,
        interrupt_check=interrupt_callback)
    #else:
    #    Hotword()