# -*- coding: utf-8 -*- #
import sys
import Image
import ImageDraw
import ImageFont
import os


def png2dot9(picfile):
	im = Image.open(picfile+'.png')
	newImg = Image.new("RGBA",(im.size[0]+4,im.size[1]+4),(0,0,0,0))
	newImg.paste(im,(2,2))
	newImg.putpixel((0,1),(0,0,0))
	newImg.putpixel((1,0),(0,0,0))
	newImg.putpixel((newImg.size[0]-2,0),(0,0,0))
	newImg.putpixel((0,newImg.size[1]-2),(0,0,0))

	fillLine=ImageDraw.Draw(newImg)
	fillLine.line(((1,newImg.size[1]-1),(newImg.size[0]-2, newImg.size[1]-1)),fill=(0,0,0))
	fillLine.line(((newImg.size[0]-1,1),(newImg.size[0]-1, newImg.size[1]-2)),fill=(0,0,0))
	newImg.save(picfile+'.9.png')
	
for filename in os.listdir(os.curdir):
	if filename.endswith(".png"): 
		png2dot9(filename[0:-4])

