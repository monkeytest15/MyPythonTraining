#coding: utf-8


import unittest, my_math

class testXXX(unittest.TestCase):

	def testxxx(self):
		total =my_math.add(1,2)
		self.assertEqual(total,3)

if __name__ == '__main__':
	unittest.main()