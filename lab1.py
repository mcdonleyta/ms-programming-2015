from easyGL import *
import random


screenWidth = 800
screenHeight = 600
numBlocksPerRow = 8
blockWidth = screenWidth / numBlocksPerRow
blockHeight = (screenHeight/2)/2/3

def draw():
	
	blocky = screenHeight - blockHeight
	block = 0
	blockx = 0
	while block < numBlocksPerRow:
		setColor(random.randint(0,8)/8.0, 0, 1)
		drawRect(blockx, blocky, blockWidth, blockHeight)
		block = block + 1
		blockx = blockx + blockWidth
		
run(screenWidth, screenHeight, "Breakout", draw)
