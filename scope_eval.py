scope = {}
scope['x'] =2
scope['y'] =3
print eval('x*y')



scope = []
exec ' x=2' in scope
print eval('x*x',scope)