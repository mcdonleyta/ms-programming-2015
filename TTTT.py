from easyGL import *

screenWidth = 800
screenHeight = 600
blockWidth =100
blockHeight = 100

x = 0
y = 0
incx = 1
incy = 1

def draw():
	global x, y, incx, incy
	
	setColor(0, 0, 1)
	drawRect(x, y, blockWidth, blockHeight)
	
	x = x + incx
	y = y + incy

	if x > 800:
	   incy = incy * -1
	if y > 600:
	   incx = incx * -1
	
	   
run(800, 600, "Rachel's Bouncy Ball", draw)
























