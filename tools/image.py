# -*- coding: utf-8 -*- #
import sys, getopt
import Image
import ImageDraw
import ImageFont
import os


def png2dot9(picfile, isCrop, pos):
	if isCrop:
		im = Image.open(picfile+'.o.png')
	else:
		im = Image.open(picfile+'.png')
	newImg = Image.new("RGBA",(im.size[0]+4,im.size[1]+4),(0,0,0,0))
	newImg.paste(im,(2,2))
	
	if pos == 1:
		newImg.putpixel((0,1),(0,0,0))
		newImg.putpixel((1,0),(0,0,0))
		newImg.putpixel((newImg.size[0]-2,0),(0,0,0))
		newImg.putpixel((0,newImg.size[1]-2),(0,0,0))
	elif pos == 2:
		newImg.putpixel((newImg.size[0]/2,0),(0,0,0))
		newImg.putpixel((0,newImg.size[1]/2),(0,0,0))

	fillLine=ImageDraw.Draw(newImg)
	fillLine.line(((1,newImg.size[1]-1),(newImg.size[0]-2, newImg.size[1]-1)),fill=(0,0,0))
	fillLine.line(((newImg.size[0]-1,1),(newImg.size[0]-1, newImg.size[1]-2)),fill=(0,0,0))
	newImg.save(picfile+'.9.png')

def cropImage(picfile, gw, gh):
	im = Image.open(picfile+'.png')
	w = gw
	h = gh
	if gw == 0 or gh == 0:
		print 'size=',im.size
		w = input("input new width:\n")
		h = input("input new height:\n")
	print w,h
	newImg = Image.new("RGBA",(w, h),(0,0,0,0))
	imW = im.size[0]
	imH = im.size[1]
	tL = im.crop((0, 0, w/2, h/2))
	tR = im.crop((imW-w/2, 0, imW, h/2))
	bL = im.crop((0, imH-h/2, w/2, imH))
	bR = im.crop((imW-w/2, imH-h/2, imW, imH))
	
	newImg.paste(tL,(0,0))
	newImg.paste(tR,(w/2,0))
	newImg.paste(bL,(0,h/2))
	newImg.paste(bR,(w/2,h/2))
	newImg.save(picfile+'.o.png')
	
def start():
	opts, args=getopt.getopt(sys.argv[1:], "cw:h:",['dot_pos='])
	whetherCrop = False
	cropWidth = 0
	cropHeight = 0
	dotPos = 1
	print opts
	for op, value in opts:
		if op == '-c':
			whetherCrop = True
		elif op == '-w':
			cropWidth = int(value)
		elif op == '-h':
			cropHeight = int(value)
		elif op == '--dot_pos':
			dotPos = int(value)
			
	for filename in os.listdir(os.curdir):
		if filename.endswith(".png"):
			if whetherCrop:
				cropImage(filename[0:-4], cropWidth, cropHeight)
			png2dot9(filename[0:-4], whetherCrop, dotPos)
#--dot_pos image, 1=two side, 2=center
#--c wheter crop
#-w global crop width
#-h global crop height
#======example===============
# image.py -c -w 30 -h 30 --dot_pos 2

if __name__ == '__main__':
	start()