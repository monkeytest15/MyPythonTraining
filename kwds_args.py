def story(**kwds):
	return 'Once upon a time. there was a ' \
	'%(job)s called %(name)s.' %kwds


def power(x,y, *others):
	if others:
		print ' Received redundant parameters:', others
	return pow(x,y)

def interval(start,stop=None,step =1):
	'Imitates range() for step >0'
	if stop is None:
		start, stop = 0, start
	result = []
	i = start
	while i <stop:
		result.append(i)
		i += step
	return result

print story(job = 'king', name ='Gumby')
print interval.__doc__
print story(name='Sir Robin',job = 'brave knight')

print power(2,3)
print power(y=3,x=2)
print power(3,3,'hello,world')
print interval(10)
print interval(1.5)
