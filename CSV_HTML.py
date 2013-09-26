import sys

def main():
	maxwidth = 100
	print_start()
	count = 0
	while True:
		try:
			line = input()
			if count = 0:
				color = "lightgreen"
			elif count%2:
				color = "while"
			else:
				color = "lightyellow"
			print_line(line,color,maxwidth)
			count + =1
		except EOFError:
			break
	print_end()

def print_start():
	print("<table border= '1'>")

def print_end():
	print("<table>")


def print_line(line,color,maxwidth):
	print ("<tr bgcolor = '{0}'".format(color))
	fields = extract_fields(line)
	for field in fields:
		if not field:
			print("<td></td>")
		else:
			number = field.replace(",","")
			try:
				x = float(number)
				print("<td align = 'right'>")