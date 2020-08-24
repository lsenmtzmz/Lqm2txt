# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 20:37:45 2020

@author: Enrique
"""

import datetime ,json, regex

if __name__ == "__main__":

	with open("./resources/lqm/QuickMemo+_200821_161824(4).lqm", 'rb') as iqm:
		rawData = iqm.read().decode('iso-8859-1')
		
	pattern = regex.compile(r'\{(?:[^{}]|(?R))*\}')
	dataJson = json.loads(pattern.findall(rawData)[0])

	category = rawData["Category"]["CategoryName"]
	timestamp = rawData["Memo"]["CreatedTime"]/1000 ## Unixtime
	date = datetime.datetime.fromtimestamp(timestamp).date()
	body = rawData["MemoObjectList"][0]["DescRaw"]
	
	text_file = open("./resources/txt/QuickMemo+_200821_161824(2).txt", mode="w", encoding="iso-8859-1")
	data = text_file.write(body +"\n\n" + category + " - " + str(date))
	text_file.close()
