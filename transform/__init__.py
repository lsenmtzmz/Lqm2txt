## -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 18:17:53 2020

@author: Enrique
https://stackoverflow.com/questions/56282563/how-to-decode-bytes-object-that-contains-invalid-bytes-python3

"""
import json



def readLqm(filename):
	path = "./resources/iqm/" + filename
	
	with open(path, 'rb') as iqm:
		rawData = iqm.read().decode('iso-8859-1')
		rawData = json.loads(rawData.split("¦zycu")[0].split("ø")[1].replace("}PK","}").replace("",""))
		
	return rawData