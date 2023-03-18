import os

def limpiar_acentos(texto):
    text = texto.lower()
    acentos = { 'á': 'a', 
                'é': 'e', 
                'í': 'i', 
                'ó': 'o', 
                'ú': 'u'}
    for acen in acentos:
        if acen in text:
            text = text.replace(acen, acentos[acen])
    return text

def replay_m(folder):
    os.system("aplay -q `ls $PWD/voice/" + folder +"/* | shuf -n 1`" )
    return