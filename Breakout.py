from easyGL import *
import random

screenWidth = 800
screenHeight = 600
numberBlocksPerRow = 8
blockWidth = screenWidth / numberBlocksPerRow
numberRows = 3
blockHeight = (screenHeight/2)/2/numberRows

def draw():
	
	row = 0
	blocky =  screenHeight - blockHeight
	while row < numberRows:	
		block = 0
		blockx = 0
		while block < numberBlocksPerRow:
			
			if row == 0:
				setColor(random.randint(0,8)/8.0,random.randint(0,8)/8.0,1)
				drawRect(blockx,blocky,blockWidth,blockHeight)
			if row == 1:
				setColor(random.randint(0,8)/8.0,1,0)
				drawRect(blockx,blocky,blockWidth,blockHeight)
			if row == 2:
				setColor(random.randint(0,8)/8.1,0,0)
				drawRect(blockx,blocky,blockWidth,blockHeight)
			block = block + 1
			blockx = blockx + blockWidth
		row = row + 1
		blocky = blocky - blockHeight
		
		
		
run(screenWidth,screenHeight,"Breakout",draw)
