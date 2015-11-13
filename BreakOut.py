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
	blocky = 0
	blocky = screenHeight-blockHeight
	while row < numberRows:
		block = 0
		blockx = 0
		while block < numberBlocksPerRow:
			if row == 0:
				setColor((row+block)/11.0, 0.3, 0.2)
			if row ==1:
				setColor((row+block)/14.0, 0.9, 0.1)
			if row == 2:
				setColor((row+block)/19.0, 0.6, 0.9)
			drawRect(blockx, blocky, blockWidth, blockHeight)
			block = block + 1
			blockx = blockx + blockWidth
		row = row + 1
		blocky = blocky -blockHeight
	
run(screenWidth, screenHeight, "Breakout", draw)
