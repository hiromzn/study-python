#! /usr/bin/env python3

import re

#filepath = "input.log"
filepath = "indata"

with open(filepath, "r", encoding="utf-8") as f:
	for line in f:
		logdate=""
		logfname=""
		items = re.findall(r'(^..../../..)\s+(..:..:..\....)\s+(\S+)\s+at line\s+(\d+)\. of \((.*)\)\s*$', line)
		if (len(items)):
			print(items)
			logdate=items[0][0]
			logtime=items[0][1]
			logfname=items[0][2]
			logline=items[0][3]
			logmodule=items[0][4]
		else:
			items = re.findall(r'(^..../../..)\s+(..:..:..\....)\s+at line\s+(\d+)\. of \((.*)\)\s*$', line)
			if (len(items)):
				print(items)
				logdate=items[0][0]
				logtime=items[0][1]
				logline=items[0][2]
				logmodule=items[0][3]

		if ( logdate != "" ):
			print( logdate )
			print( logtime )
			if ( logfname != "" ):
				print( logfname )
				print( logline )
			print( logmodule )
		# print(items[0][0], items[0][1])
		# print(items[0][2])
		# print(items[0][3])

