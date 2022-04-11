#!/usr/bin/env python3

import subprocess
import os

def ejecutar(sector, tags, frase):
	if sector == 0:
		file_exec = "sectors/SPECIALS/" + tags
	else:
		separador = "+"
		print(tags)
		file_exec = "sectors/" + sector + "/" + separador.join(tags)
	print(file_exec)
	if os.path.exists(file_exec):
		subprocess.run( ['bash', file_exec, frase], stdin=subprocess.PIPE)
	else:
		print("No se encuentra el archivo del comando")
	return
