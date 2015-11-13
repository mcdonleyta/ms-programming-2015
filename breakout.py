from easyGL import *
import random

x = 300
y = 0
incX = 2
incY = 1
screenWidth = 800
screenHeight = 600
numBlocksPerRow = 16
blockWidth = screenWidth / numBlocksPerRow
numberRows = 5
blockHeight = (screenHeight/2)/2/numberRows

def draw():
	global numBlocksPerRow 
	
	row = 0
	blocky = screenHeight - blockHeight
	while row < numberRows:
		block = 0
		blockx = 0
		while block < numBlocksPerRow:
			if row == 0:
				setColor(0,random.randint(0,8)/8.0, random.randint(0,8)/8.0)
			if row == 1:
				setColor(random.randint(0,8)/8.0, 0, random.randint(0,8)/8.0)
			if row == 2:
				setColor(0, 0, random.randint(0,8)/8.0)
			if row == 3:
				setColor(random.randint(0,8)/8.0, random.randint(0,8)/8.0, 0)
			if row == 4:
				setColor(0, random.randint(0,8)/8.0, 0)
			drawRect(blockx, blocky, blockWidth, blockHeight)
			block = block + 1
			blockx = blockx + blockWidth
			
		row = row + 1
		blocky = blocky - blockHeight
		
	global x, y, incX, incY
	
	setColor(1, 0, 0)
	drawRect(x, y, 10, 10)
	
	x = x + incX 
	y = y + incY
	
	if x > 790:
		incX = random.randint(-2, -1)
	
	if y > 590:
		incY = random.randint(-2, -1)
		
	if x < 0:
		incX = random.randint(1, 2)
	
	if y < 0:
		incY = random.randint(1, 2)   

run(screenWidth, screenHeight, "Breakout", draw)
