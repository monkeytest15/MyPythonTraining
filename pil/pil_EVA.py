# -*- coding: utf-8 -*-
from __future__ import division
import Image,os,json,re,RGB2hex
#						json_print = json_print+'{"id":'+'"'+hex(RGB2hex.rgb2hex(RGBA_list[j][0:3]))+'"'+','+'"min_x":'+min_x[j]+','+'"max_x":'+max_x[j]+','+'"min_y":'+min_y[j]+','+'"max_y":'+max_y[j]+'}]'

@profile
def traverse():
	filesPath_list= []
	files_path= []
	dir = raw_input('please input the path:')
	for root, dirs, files in os.walk(dir):
		for name in files:
			if name[-3:]=='png' and 'position' in name:
				filesPath_list.append(root)
				files_path.append(root+'/'+name)
	return filesPath_list,files_path
@profile
def ColorAnalysis(im,set_Color,Original_Color,all_Coordinate):
	count =0
	for Coordinate in all_Coordinate:
		Coordinate_Pixel = im.getpixel(Coordinate)
		if Coordinate_Pixel ==set_Color or Coordinate_Pixel ==Original_Color:
			count = count+1
	print count,len(all_Coordinate)
	if count == len(all_Coordinate):
		pixel = Original_Color
	else:
		print 'not this Layer'
	return pixel


	GetCoordinate1Pixel = im.getpixel(Coordinate1)
	GetCoordinate2Pixel = im.getpixel(Coordinate2)
	GetCoordinate3Pixel = im.getpixel(Coordinate3)
	GetCoordinate4Pixel = im.getpixel(Coordinate4)
	if GetCoordinate1Pixel ==set_Color or GetCoordinate2Pixel ==set_Color or GetCoordinate3Pixel==set_Color or GetCoordinate4Pixel ==set_Color:
		if GetCoordinate1Pixel ==Original_Color or GetCoordinate2Pixel ==Original_Color or GetCoordinate3Pixel==Original_Color or GetCoordinate4Pixel ==Original_Color:
			pic_list.append(Original_Color)
	return pic_list



if __name__ =="__main__":
	picpath_list,pic_path = traverse()
	print picpath_list,pic_path
	for path in pic_path:
		RGBA_list=[]
		color_Area = []
		json_print ='['
		pixel_array = []
		im = Image.open(path)
		pixel = im.getcolors(maxcolors=256)
		size = im.size
		for RGBA in pixel:
			if RGBA[1][3]!=0 and RGBA[1]!=(255,255,255,255):
				RGBA_list.append(RGBA[1])
				color_Area.append(RGBA[0])
		for i in range(len(RGBA_list)):
			Coordinate_array = []
			New_RGBA_list = []
			New_color_Area = []
			Coordinate_X = []
			Coordinate_Y = []
			for lenth in range(size[0]):
				for width in range(size[1]):
					if im.getpixel((lenth,width)) == RGBA_list[i]:
						Coordinate_array.append((lenth,width))
						Coordinate_X.append(lenth)
						Coordinate_Y.append(width)
			X_diff = max(Coordinate_X)+1-min(Coordinate_X)
			Y_diff = max(Coordinate_Y)+1-min(Coordinate_Y)
			print X_diff*Y_diff,color_Area[i]
			newX_Coordinate = min(Coordinate_X)
			newX_Coordinate2 = max(Coordinate_X)+1
			newY_Coordinate = min(Coordinate_Y)
			newY_Coordinate2 = max(Coordinate_Y)+1
			min_x = '%.3f'%(newX_Coordinate/size[0])
			max_x = '%.3f'%(newX_Coordinate2/size[0])
			min_y = '%.3f'%(newY_Coordinate/size[1])
			max_y = '%.3f'%(newY_Coordinate2/size[1])
			if X_diff*Y_diff == color_Area[i]:
				print '1'
				json_print = json_print+'{"id":'+'"'+hex(RGB2hex.rgb2hex(RGBA_list[i][0:3]))+'"'+','+'"min_x":'+min_x+','+'"max_x":'+max_x+','+'"min_y":'+min_y+','+'"max_y":'+max_y+'},'
				im.paste((255,255,255),(newX_Coordinate,newY_Coordinate,newX_Coordinate2,newY_Coordinate2))
			else:
				print '2'
				pixel = im.getcolors(maxcolors=256)
				for RGBA in pixel:
					if RGBA[1][3]!=0 and RGBA[1]!=(255,255,255,255):
						New_RGBA_list.append(RGBA[1])
						New_color_Area.append(RGBA[0])
				pixel_array2 = ColorAnalysis(im,(255,255,255,255),RGBA_list[i],Coordinate_array)
				json_print = json_print+'{"id":'+'"'+hex(RGB2hex.rgb2hex(pixel_array2[0:3]))+'"'+','+'"min_x":'+min_x+','+'"max_x":'+max_x+','+'"min_y":'+min_y+','+'"max_y":'+max_y+'},'
				im.paste((255,255,255),(newX_Coordinate,newY_Coordinate,newX_Coordinate2,newY_Coordinate2))
		json_print = json_print[:-1]+"]"

		file_object = open(path[:-3]+'json', 'w')
		file_object.write(json_print)
		file_object.close()



