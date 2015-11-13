from easyGL import *

x = 0
y = 550
incx = 1
incy = 1
BlockWidth = 800/8
BlockHeight = ((600/2)/2)/3
def draw(): 
	global x, y, incx, incy, BlockWidth, BlockHeight
	#Add the blocks to break
	setColor(0, 1, 0)
	drawRect(0, 600-BlockHeight, BlockWidth, BlockHeight)
	setColor(0, 1, 0)
	drawRect(100, 600-BlockHeight, BlockWidth, BlockHeight)
	setColor(0, 1, 0)
	drawRect(200, 600-BlockHeight, BlockWidth, BlockHeight)
	setColor(0, 1, 0)
	drawRect(300, 600-BlockHeight, BlockWidth, BlockHeight)
	setColor(0, 1, 0)
	drawRect(400, 600-BlockHeight, BlockWidth, BlockHeight)
	setColor(0, 1, 0)
	drawRect(500, 600-BlockHeight, BlockWidth, BlockHeight)
	setColor(0, 1, 0)
	drawRect(600, 600-BlockHeight, BlockWidth, BlockHeight)
	setColor(0, 1, 0)
	drawRect(700, 600-BlockHeight, BlockWidth, BlockHeight)
	setColor(0, 1, 0)
	drawRect(800, 600-BlockHeight, BlockWidth, BlockHeight)
	setColor(0, 0, 1)                  # this is called every          
	drawRect(x, y, 50, 50)

  
	x = x + incx
	y = y + incy

	if x > 800:
	   incx = incx * -1
	if y > 600:
	   incy = incy * -1
	if x < 0:
	   incx = incx * -1
	if y < 0:
	   incy = incy * -1
	   
run(800, 600, "Rachel's Bouncy Ball", draw)
