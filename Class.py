class A():
	a = 0
	def __init(self):
		a +1

	def AA(self):
		print 'this is class A method'

	def BB(self,x):
		print x+1


class B(A):
	def AA(self):
		print ' this is class B extends class A'


method = B()
method.AA()
method.BB(1)