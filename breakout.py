from easyGL import *

import random
x = 0
y = 0
incx = 1
incy = 1
screenWidth = 800
screenHeight = 600
numBlocksPerRow = 8
blockWidth = screenWidth / numBlocksPerRow
numberRows = 5
blockHeight = (screenHeight/2)/2/numberRows 

def draw():
	global x, y, incx, incy
	row = 0
	blocky = screenHeight - blockHeight
	while row < numberRows:
		block = 0
		blockx = 0
		while block < numBlocksPerRow:
			if row == 0:
				setColor(random.randint(0,1)/0.3333, 1, 0.1)
			if  row == 1:
				setColor(0.235432457324, 0.847563487563487568745, 0.12)
			if row == 2:
				setColor(0.5, 1, 0.5)
			drawRect(blockx, blocky, blockWidth, blockHeight)
			block = block + 1
			blockx = blockx + blockWidth
		row = row + 1
		blocky = blocky - blockHeight
		
	setColor(1, 0, 0)
	drawRect(x, y, 10, 10)
	
	x = x + incx
	y = y + incy
	
	if x > screenWidth:
		incx = -1
	if x < 0:
		incx = 1
	if y > screenHeight:
		incy = -1
	if y < 0:
		incy = 1
	
	
	
run (screenWidth, screenHeight, "Breakout", draw)
