

class Person:

	def setName(self,name):
		self.name = name

	def getName(self):
		return self.name


	def greed(self):
		print "hello,world! I`m %s" % self.name



foo = Person()
foo.setName('monkey')
foo.greed()