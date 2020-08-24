# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 18:17:53 2020

@author: Enrique
"""

import transform as tfm
import argparse

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='Converter IQM to TXT')
	parser.add_argument('--file', type=str, required=False, dest='filename', help="Poner el nombre del archivo que desea convertir")
	args = parser.parse_args()
	
	if args.filename == None:
		print("No hay argumento filename, se convertiran a formato txt todos los archivos con extension .iqm del directorio ./resources/lqm/")
	else:
		if tfm.validateLqmFormat(args.filename):
			print("Se convertira el archivo %s en formato txt" % args.filename)
			dataJson = tfm.readLqm(args.filename)
			fullNote = tfm.dataPrep2txt(dataJson)
			tfm.writeTxtWithStr(fullNote,args.filename)
		else:
			print("El formato del archivo %s no es lqm.Intente de nuevo" % args.filename)
			