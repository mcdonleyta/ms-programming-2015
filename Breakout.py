from easyGL import *
import random

screenWidth = 800
screenHeight = 600
numberBlocksPerRow = 8
blockWidth = screenWidth / numberBlocksPerRow
NumberRows = 3
blockHeight = (screenHeight/2) /2/NumberRows

def draw():
	global numberBlocksPerRow
	
	r = 1
	g = 1
	b = 1
	row = 0
	blocky = screenHeight - blockHeight
	while row < NumberRows:
		block = 0
		blockx = 0
		while block < numberBlocksPerRow:
			if row == 0:
				setColor(r, g, b)
			if row == 1:
				setColor(random.randint(0,4)/8.0, random.randint(0,2)/8.0, 0.2)
			if row == 2:
				setColor(0.2,1,0.5)
				
			drawRect(blockx, blocky, blockWidth, blockHeight)
			block = block + 1
			blockx = blockx + blockWidth
			r = r - 0.06
			g = g - 0.12
			b = b - 0.07

		row = row + 1	
		blocky = blocky - blockHeight
		r = r + 0.5
		g = g + 0.6
		b = b + 0.12
		
		
run(screenWidth,screenHeight, "Breakout", draw)
