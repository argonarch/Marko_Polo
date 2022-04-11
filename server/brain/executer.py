#!/usr/bin/env python3
import subprocess

def ejecutar(sector, tags, frase):
	if sector == 0:
		file_exec = "sectors/SPECIALS/" + tags
	else:
		separador = "+"
		file_exec = "sectors/" + sector + "/" + separador.join(tags) + " " + frase
	print(file_exec)
	subprocess.run( ['sh', file_exec], stdin=subprocess.PIPE)
	return
