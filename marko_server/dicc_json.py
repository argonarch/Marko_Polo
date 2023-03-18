#!/usr/bin/env python3
import executer
import datadb

def tagcreator(frase,modo,claves):
    commands = []
    frase_listada = set(frase.split())
    #print(claves)
    if modo == 1:
        for palabra in claves:
            set_1 = set(datadb.word_sinonimo(palabra))
            #print(set_1)
            parecidos = set_1.intersection(frase_listada)
            #print (parecidos)
            if parecidos != set():
                #print(palabra)
                return(palabra)
    
    if modo == 2:
        for palabra in claves:
            set_1 = set(datadb.word_activador(palabra))
            #print(set_1)
            parecidos = set_1.intersection(frase_listada)
            #print (parecidos)
            if parecidos != set():
                #print(palabra)
                commands.append(palabra)

    if modo == 3:
        for palabra in claves:
            set_1 = set(datadb.word_sinonimo(palabra))
            #print(set_1)
            parecidos = set_1.intersection(frase_listada)
            #print (parecidos)
            if parecidos != set():
                sinonimo = ''.join(parecidos)
                return sinonimo
    return(commands)

def entrada(frase):
    # Filtro cero para frases con comandos especiales
    especial = ['SPECIAL']
    sinonimos_special = tagcreator(frase, 3, especial)
    #print(sinonimos_special)
    if sinonimos_special != list():
        print(type(sinonimos_special))
        executer.ejecutar(0, sinonimos_special, frase)
        return 0
    else:
        # Para detectar el sector (primer filtro)
        
        sectores = datadb.create_list()
        sector = tagcreator(frase, 1,sectores) # Modo 1 detecta solo la primera coincidencia

        # Para detectar los comandos en la frase (segundo filtro)

        activadores = datadb.list_activators(sector)
        set_commands = set(tagcreator(frase, 2, activadores)) # Modo 2 detecta todas las coincidencias
        
        # Para separar los comandos de la frase de los comandos habilitados por sector

        tags_list = sorted(list(set_commands), key=str.lower)
        
        # Ejecuta el comando
        executer.ejecutar(sector, tags_list, frase)
        return 0
