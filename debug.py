# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 20:37:45 2020

@author: Enrique
"""

import transform as tfm
import argparse, ast,json

if __name__ == "__main__":

	with open("./resources/iqm/QuickMemo+_200821_161824(2).lqm", 'rb') as iqm:
		rawData = iqm.read().decode('iso-8859-1')
	rawData = rawData.split("¦zycu")[0].split("ø")[1].replace("}PK","}").replace("","")
	rawData = json.loads(rawData)