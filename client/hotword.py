#!/usr/bin/env python3
import os
import pvporcupine
from pvrecorder import PvRecorder
import speech_recognition as sr
import trinity_client

def Hotword():
    keyword_path = ['keywords/marcopolo_es_linux.ppn']
    access_key = 'poner aqui llave de picovoice'
    library_path = 'lib/libpv_porcupine.so'
    model_path = 'lib/porcupine_params_es.pv'
    sensitivity = [0.5]
    input_device_index = 1

    r = sr.Recognizer()
    porcupine = None
    recorder = None
    os.system("bash voice/trinity-randomwav ready")
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
                    audio = r.listen(source)
                try:
                    os.system("bash voice/trinity-randomwav working")
                    texto = r.recognize_google(audio, language="es_AR")
                    texto_lower = trinity_client.limpiar_acentos(texto)
                    print(trinity_client.sender(texto_lower))
                except sr.UnknownValueError:
                    os.system("bash voice/trinity-randomwav repit")
                    print("No se escucho la frase")
                except sr.RequestError as e:
                    print("Error de servicio; {0}".format(e))

    except pvporcupine.PorcupineInvalidArgumentError as e:
        print("One or more arguments provided to Porcupine is invalid")
        raise e
    except pvporcupine.PorcupineActivationError as e:
        print("AccessKey activation error")
        raise e
    except pvporcupine.PorcupineActivationLimitError as e:
        print(f"AccessKey '{access_key}' has reached it's temporary device limit")
        raise e
    except pvporcupine.PorcupineActivationRefusedError as e:
        print(f"AccessKey '{access_key}' refused")
        raise e
    except pvporcupine.PorcupineActivationThrottledError as e:
        print(f"AccessKey '{access_key}' has been throttled")
        raise e
    except pvporcupine.PorcupineError as e:
        print(f"Failed to initialize Porcupine")
        raise e
    except KeyboardInterrupt:
        print('Stopping ...')
    finally:
        if porcupine is not None:
            porcupine.delete()

        if recorder is not None:
            recorder.delete()


Hotword()
