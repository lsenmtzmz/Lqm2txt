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
	
	
	if args.filename:
		print("Se convertira el archivo %s en formato txt" % args.filename)
		rawData = tfm.readIqm(args.filename)
		print("Raw Data:\n", rawData)
		
	else:
		print("No hay argumento filename, se convertiran a formato txt todos los archivos con extension .iqm del directorio")