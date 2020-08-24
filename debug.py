# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 20:37:45 2020

@author: Enrique
"""

import datetime ,json

if __name__ == "__main__":

	with open("./resources/lqm/QuickMemo+_200821_161824(2).lqm", 'rb') as iqm:
		rawData = iqm.read().decode('iso-8859-1')
	rawData = rawData.split("¦zycu")[0].split("ø")[1].replace("}PK","}").replace("","")
	rawData = json.loads(rawData)
	
	category = rawData["Category"]["CategoryName"]
	timestamp = rawData["Memo"]["CreatedTime"]/1000 ## Unixtime
	date = datetime.datetime.fromtimestamp(timestamp).date()
	body = rawData["MemoObjectList"][0]["DescRaw"]
	
	text_file = open("./resources/txt/QuickMemo+_200821_161824(2).txt", mode="w", encoding="iso-8859-1")
	data = text_file.write(body +"\n\n" + category + " - " + str(date))
	text_file.close()
