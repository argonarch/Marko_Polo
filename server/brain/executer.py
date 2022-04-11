#!/usr/bin/env python3
import subprocess

def ejecutar(sector, tags, frase):
	if sector == 0:
		file_exec = "sectors/SPECIALS/" + tags
	else:
		separador = "+"
		print(tags)
		file_exec = "sectors/" + sector + "/" + separador.join(tags)
	print(file_exec)
	subprocess.run( ['bash', file_exec, frase], stdin=subprocess.PIPE)
	return
