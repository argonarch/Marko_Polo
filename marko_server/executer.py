#!/usr/bin/env python3

import subprocess
import datadb


def ejecutar(sector, tags, frase):
	if sector == 0:
		comando = datadb.comando_special(tags)
		bash(comando,frase)
		return
	else:
		tags_string = "'" + "','".join(map(str, tags)) + "'"
		print(tags_string)
		comando = datadb.encontar_comando(sector,f"{tags_string}")
		print(comando)
		if isinstance(comando,str) :
			print("Ejecutando comando")
			bash(comando,frase)
		else:
			print("No se encuentra el archivo del comando")
		return

def bash(comando,frase):
	with open('bin/command.sh', 'w') as f:
		f.write(comando)
	subprocess.run( ['bash','bin/command.sh', frase], stdin=subprocess.PIPE)