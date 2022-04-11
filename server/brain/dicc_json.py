#!/usr/bin/env python3
import json
import executer

def tagcreator(file_json,frase,modo):
    commands = []
    frase_listada = set(frase.split())
    dicc_principal = open("dictionaries/"+file_json, "r")
    dicc_lecture = dicc_principal.read()
    dicc_principal.close()
    dicc_python = json.loads(dicc_lecture)
    claves = list(dicc_python.keys())
    for palabra in claves:
        set_1 = set(dicc_python.get(palabra))
        parecidos = set_1.intersection(frase_listada)
        #print (pom)
        if parecidos != set() and modo == 1:
            #print(palabra)
            return(palabra)
        elif parecidos != set() and modo == 2:
            commands.append(palabra)
    return(commands)

def detect_commands(sector, set_commands):
    dicc_principal = open("dictionaries/sectors.json", "r")
    dicc_lecture = dicc_principal.read()
    dicc_principal.close()
    dicc_python = json.loads(dicc_lecture)
    set_sector = set(dicc_python[sector])
    parecidos = set_commands.intersection(set_sector)
    #print(parecidos)
    return(parecidos)

def entrada(frase):
    # Filtro cero para frases con comandos especiales
    command_special = tagcreator("commands_specials.json", frase, 1)
    if command_special != list():
        print(command_special)
        executer.ejecutar(0, frase, 0)
        return
    else:
        # Para detectar el sector (primer filtro)
        sector = tagcreator("detect_sector.json", frase, 1) # Modo 1 detecta solo la primera coincidencia

        # Para detectar los comandos en la frase (segundo filtro)
        set_commands = set(tagcreator("commands.json", frase, 2)) # Modo 2 detecta todas las coincidencias
        
        # Para separar los comandos de la frase de los comandos habilitados por sector
        tags = detect_commands(sector, set_commands)
        tags_list = sorted(list(tags), key=str.lower)
        print(sector)
        print(set_commands)
        print(tags_list)
        executer.ejecutar(sector, tags_list, frase)
        return