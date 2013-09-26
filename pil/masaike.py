from PIL import Image
import ImageEnhance
import ImageChops
import ImageFilter
import os
import math

im = Image.open("/Users/apple/Documents/pil/1.png")
R,G,B=0,1,2
imgwidth=im.size[0]
imgheight=im.size[1]
im.load()
Source=im.split()
r=Source[R]
g=Source[G]
b=Source[B]

def mosaic(num):
   global im
   pregray=None
   for width in range(imgwidth):
      for height in range(imgheight):
	 pixel=im.load()
	 if width%num==0 or height%num==0:
	    if width+num>imgwidth or height+num>imgheight:
	       pass
	    else:
	       pregray=[0,0,0]
	       sum=num*num
	       for i in range(num):
		  for j in range(num):
	            pregray[0]+=im.getpixel((width+i,height+j))[0]
	            pregray[1]+=im.getpixel((width+i,height+j))[1]
	            pregray[2]+=im.getpixel((width+i,height+j))[2]
	            pixel[width,height]=(pregray[0]/sum,pregray[1]/sum,pregray[2]/sum) 
	 else:
	    pixel[width,height]=(pregray[0],pregray[1],pregray[2]) 

def neoneffect():
   gray=rightgray=downgray=None
   pixel=im.load()
   for width in range(imgwidth-1):
      for height in range(imgheight-1):
	gray=im.getpixel((width,height))
	rightgray=im.getpixel((width+1,height))
	downgray=im.getpixel((width,height+1))
	r1=gray[0]-rightgray[0];r2=gray[0]-downgray[0]
	g1=gray[1]-rightgray[1];g2=gray[0]-downgray[1]
	b1=gray[0]-rightgray[2];b2=gray[0]-downgray[2]
	Red=2*math.sqrt(r1*r1+r2*r2)
	Green=2*math.sqrt(g1*g1+g2*g2)
	Blue=2*math.sqrt(b1*b1+b2*b2)
	pixel[width,height]=(int(Red),int(Green),int(Blue))

if __name__ =="__main__":
#	mosaic(2)
	neoneffect()
	im.show()