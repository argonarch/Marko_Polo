#!/usr/bin/env python3
import executer
import database

def tagcreator(frase,modo,claves):
    commands = []
    frase_listada = set(frase.split())
    #print(claves)
    if modo == 1:
        for palabra in claves:
            set_1 = set(database.word_sinonimo(palabra))
            #print(set_1)
            parecidos = set_1.intersection(frase_listada)
            #print (parecidos)
            if parecidos != set():
                #print(palabra)
                return(palabra)
    
    if modo == 2:
        for palabra in claves:
            set_1 = set(database.word_activador(palabra))
            #print(set_1)
            parecidos = set_1.intersection(frase_listada)
            #print (parecidos)
            if parecidos != set():
                #print(palabra)
                commands.append(palabra)
            
    return(commands)

def entrada(frase):
    # Filtro cero para frases con comandos especiales
    especial = ['SPECIAL']
    command_special = tagcreator(frase, 1, especial)
    if command_special != list():
        print(command_special)
        #executer.ejecutar(0, frase, 0)
        return
    else:
        # Para detectar el sector (primer filtro)
        
        sectores = database.create_list()
        sector = tagcreator(frase, 1,sectores) # Modo 1 detecta solo la primera coincidencia

        # Para detectar los comandos en la frase (segundo filtro)

        activadores = database.list_activators(sector)
        set_commands = set(tagcreator(frase, 2, activadores)) # Modo 2 detecta todas las coincidencias
        
        # Para separar los comandos de la frase de los comandos habilitados por sector

        tags_list = sorted(list(set_commands), key=str.lower)

        print(sector)
        #print(set_commands)
        print(tags_list)

        # Ejecuta el comando
        executer.ejecutar(sector, tags_list, frase)
        return
