from random import shuffle
import random

list1 = []
def CreateList():
	for i in range(100):
		list1.append(i)



CreateList()

#print list1

shuffle(list1)

print list1