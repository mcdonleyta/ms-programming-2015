from easyGL import *
x = 0
y = 0
incx = 2
incy = 1


def draw():
	BlockWidth = 100
	BlockHeight = 50
	global x,y, incx, incy
	setColor(1, 0, 0)
	drawRect(x, y, 30, 30)
	x = x + incx
	y = y + incy
	if x > 800:
		incx = -1
	if y > 600:
		incy = -1
	if x < 0:
		incx = 1
	if y < 0:
		incy = 1 
	setColor(1, 1, 0)
	drawRect(0, 600-BlockHeight, BlockWidth, BlockHeight)
	drawRect(105, 600-BlockHeight, BlockWidth, BlockHeight)
	drawRect(210, 600-BlockHeight, BlockWidth, BlockHeight)
	drawRect(315, 600-BlockHeight, BlockWidth, BlockHeight)
	drawRect(420, 600-BlockHeight, BlockWidth, BlockHeight)
	drawRect(525, 600-BlockHeight, BlockWidth, BlockHeight)
	drawRect(630, 600-BlockHeight, BlockWidth, BlockHeight)
	drawRect(735, 600-BlockHeight, BlockWidth, BlockHeight)
	drawRect(0, 540-BlockHeight, BlockWidth, BlockHeight)
	drawRect(105, 540-BlockHeight, BlockWidth, BlockHeight)
	drawRect(210, 540-BlockHeight, BlockWidth, BlockHeight)
	drawRect(315, 540-BlockHeight, BlockWidth, BlockHeight)
	drawRect(420, 540-BlockHeight, BlockWidth, BlockHeight)
	drawRect(525, 540-BlockHeight, BlockWidth, BlockHeight)
	drawRect(630, 540-BlockHeight, BlockWidth, BlockHeight)
	drawRect(735, 540-BlockHeight, BlockWidth, BlockHeight)
	drawRect(0, 480-BlockHeight, BlockWidth, BlockHeight)
	drawRect(105, 480-BlockHeight, BlockWidth, BlockHeight)
	drawRect(210, 480-BlockHeight, BlockWidth, BlockHeight)
	drawRect(315, 480-BlockHeight, BlockWidth, BlockHeight)
	drawRect(420, 480-BlockHeight, BlockWidth, BlockHeight)
	drawRect(525, 480-BlockHeight, BlockWidth, BlockHeight)
	drawRect(630, 480-BlockHeight, BlockWidth, BlockHeight)
	drawRect(735, 480-BlockHeight, BlockWidth, BlockHeight)

	
		
run(800,600, "Breakout Like Game", draw)
 
