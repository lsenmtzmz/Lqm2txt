## -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 18:17:53 2020

@author: Enrique
https://stackoverflow.com/questions/56282563/how-to-decode-bytes-object-that-contains-invalid-bytes-python3

"""
import json, datetime

def validateLqmFormat(filename):
	if filename != None:
		filename = filename.split(".")
		if filename[-1] == ("lqm" or "LQM"):
			return True
		else:
			return False
			
def readLqm(filename):
	path = "./resources/lqm/" + filename
	
	with open(path, 'rb') as iqm:
		rawData = iqm.read().decode('iso-8859-1')
		dataJson = json.loads(rawData.split("¦zycu")[0].split("ø")[1].replace("}PK","}").replace("",""))
		
	return dataJson

def dataPrep2txt(dataJson):
	if dataJson:
		try:
			category = dataJson["Category"]["CategoryName"]
			timestamp = dataJson["Memo"]["CreatedTime"]/1000 ## Unixtime
			date = datetime.datetime.fromtimestamp(timestamp).date()
			body = dataJson["MemoObjectList"][0]["DescRaw"]
		except Exception as e:
			print("No se han podido obtener todos los metadatos del json: ", e)
			return
	else:
		print("El json esta vacio")
	
	return body + "\n\n" + str(date) + " - " +category
	
def writeTxtWithStr(string,filename):
	try:
		if validateLqmFormat(filename):
			path = "./resources/txt/" + filename.split(".")[-1]
		else:
			path = "./resources/txt/" + filename
		
		fileTxt = open(path, mode="w", encoding="iso-8859-1")
		fileTxt.write(string)
		fileTxt.close()
		print("Se ha escrito el archivo txt de %s exitosamente" % filename)
	except Exception as es:
		print("La escritura del archivo %s fallo: " % filename)

			
	