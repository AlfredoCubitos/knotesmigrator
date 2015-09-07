#!/usr/bin/python

import os
import re
import json
import codecs
import sys

user = os.getlogin()
path =  "/home/"+user+"/.kde4/share/apps/knotes/"
filename = "notes.ics"
outp = ""

liste = ["DTSTAMP","CREATED","UID","LAST-MODIFIED","DESCRIPTION","SUMMARY"]

if len(sys.argv) >1:
	outp = sys.argv[1]

fn = path + filename

jsonData = []

def noteFiles(data,filename):
	datei = open(filename+".txt","w")
	#datei.write(data["DESCRIPTION"])
	text = data.split("\\n")
	if len(text) > 0:
		for line in text:
			datei.write(line+"\n")

def getData(fn):
	
	obj = dict()
	key = None
	val = None
	tags = False
	filename = None
	
	for line in fn:
		
		tag = re.split(":",line)
		
		if tag[0] == "END":
			
			if obj:
				if outp == "json":
					jsonData.append(obj)
				noteFiles(obj["DESCRIPTION"].encode('utf-8'), filename)
			key = None
			val = None
			obj = {}

		
		if tag[0] in liste:
		
			if len(tag) > 2:
				key = tag.pop(0);
				obj[key] = ":".join(tag)
				line = ""
			elif len(tag) == 2:
				obj[tag[0]] = tag[1]
				key = tag[0]
				val = tag[1]
			
			
			if key == "SUMMARY":
				filename = val.rstrip()
			
		if key and len(line) > 0:
			obj[key] += line
		
			
	if outp == "json":
		jsData = json.dumps(jsonData)
		jsonFile = codecs.open("notes.js","w","utf8")
		jsonFile.write(str(jsData))
		jsonFile.close()



		


if os.path.isfile(fn):
	f = codecs.open(fn,'r','utf-8')
	getData(f)
else:
	print "no file"
	

