from urllib import urlopen
from reportlab.graphics.shapes import *
from reportlab.graphics.charts.lineplots import LinePlot
from reportlab.graphics.charts.textlabels import Label
from reportlab.graphics import renderPDF


name_infile = file('/Users/apple/Desktop/python/gfxinfo.txt', 'r')

char = []
drawing = Drawing(400,200)
data = []
times = []

for line in name_infile.readlines():
	try:
		char.append(line)
	except IndexError,e:
		print 'out of range'

for i in range(len(char)):
	if 'Draw' in char[i][1:5]:
		Begin_number = i
	if 'View' in char[i][0:4]:
		End_number = i

for i in range(Begin_number+1,End_number-1):
	data.append([float(n) for n in char[i].split()])

print data

for i in range(len(data)):
	times.append(i)

print times


Draw = [row[0] for row in data]
Process = [row[1] for row in data]
Execute = [row[2] for row in data]
lp = LinePlot()
lp.x = 50
lp.y = 50
lp.height = 125
lp.width = 300
lp.data = [zip(times, Draw),zip(times,Process),zip(times, Execute)]
lp.lines[0].strokeColor = colors.blue
lp.lines[1].strokeColor = colors.red
lp.lines[2].strokeColor = colors.green

drawing.add(lp)
drawing.add(String(250,150, 'ngxinfo',fontSize=14,fillColor=colors.red))

renderPDF.drawToFile(drawing, 'ngxinfo.pdf','ngxinfo')

