import uuid, random, time
import  json, unittest
a = []
f = file('/Users/apple/Desktop/python/python_study/test.txt','r')

for outfile in f.readlines():
	outfile =  outfile.strip('\n')
	a.append(outfile)
	print a



