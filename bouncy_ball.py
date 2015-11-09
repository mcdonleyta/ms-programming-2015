
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

#The function that does the work
def draw():
	global x, y, screenHeight, screenWidth, incx, incy
	
	
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
		
#Create our game canvas
run(screenWidth, screenHeight, "Title", draw) 
