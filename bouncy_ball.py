
from easyGL import *

x = 0
y = 0
incx = 1
incy = 1
screenWidth = 800
screenHeight = 600
numBlocks = 8.0
numBlockRows = 6.0
blockWidth = screenWidth / numBlocks
blockHeight = (screenHeight/2)/numBlockRows
numblockperrow = 8
block = 0

#The function that does the work
def draw():
	global x, y, screenHeight, screenWidth, incx, incy, numblockperrow, block
	
	
	setColor(1, 0, 0)
	drawRect(x, y, 10, 10)
	
	x = x + incx
	y = y + incy
	
	## What happens when we hit the edges of the screen?
	if x > screenWidth:
		incx = -1
	if x < 0:
		incx = 1
	if y > screenHeight:
		incy = -1
	if y < 0:
		incy = 1
		
		setColor(0.23, 0.39, 0.37)
		drawRect(0, 550, blockWidth, blockHeight)
		
	while block < numblockperrow:
		setColor(0.4, 0.4, 0.456)
		drawRect(block*100, 550, 100, 50)
		block = block + 1 
	
		
#Create our game canvas
run(screenWidth, screenHeight, "CRAP TROLL GAME", draw) 
