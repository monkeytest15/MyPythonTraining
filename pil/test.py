# -*- coding: utf-8 -*-
from __future__ import division
import Image,os,json,re,RGB2hex


im = Image.open('/Users/apple/Documents/pil/Apple_iPhone4_4S_t007_output_position.png')
pixel = im.getcolors(maxcolors=256)
size = im.size

RGBA_list =[]
color_Area=[]
Coordinate_X = []
Coordinate_Y = []
Layer_one = []


for RGBA in pixel:
	if RGBA[1][3]!=0:
		RGBA_list.append(RGBA[1])
		color_Area.append(RGBA[0])

print RGBA_list
print color_Area
print size



for i in range(1):
	Coordinate_array = []
	for lenth in range(size[0]):
		for width in range(size[1]):
			if im.getpixel((lenth,width)) == (97, 189, 229, 255):
				Coordinate_X.append(lenth)
				Coordinate_Y.append(width)
	X_diff = max(Coordinate_X)+1-min(Coordinate_X)
	Y_diff = max(Coordinate_Y)+1-min(Coordinate_Y)
	if X_diff*Y_diff== color_Area[i]:
		Layer_one.append(RGBA_list[i])

print max(Coordinate_X)+1
print min(Coordinate_X)
print max(Coordinate_Y)+1
print min(Coordinate_Y)

x,y = im.size
im.paste((255,255,255),(573,690,813,930))
im.save('/Users/apple/Documents/pil/Apple_iPhone4_4S_t007_output_position3.png')


#print min(Coordinate_X),max(Coordinate_X)+1
#print min(Coordinate_Y),max(Coordinate_Y)+1
#print Coordinate_array



