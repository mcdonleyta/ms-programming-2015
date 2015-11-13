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
	blocky =  screenHeight -blockHeight
	while row < numberRows:
		block = 0
		blockx = 0
		while block < numberBlocksPerRow:
			
			if row == 0:
				setColor (0, 1, block/8.0)
			if row == 1:
				setColor(0, 0, block/5.0)
			if row == 2:
				setColor(random.randint(0,8)/8.0, 0, 1)
			
			drawRect(blockx, blocky, blockWidth, blockHeight)
			block = block + 1
			blockx = blockx + blockWidth
		row = row + 1
		blocky = blocky - blockHeight

run(screenWidth, screenHeight, "Rachel's Breakout", draw)
