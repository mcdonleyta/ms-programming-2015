from easyGL import *

screenWidth = 800
screenHeight = 600
numberBlocksPerRow = 8
blockWidth = screenWidth / numberBlocksRow
numberRows = 3
blockHeight = (screenHeight/2)/2/numberRows

def draw():
	setColor(0, 0, 1)
	drawRect(0, screenHeight-blockHeight, blockWidth, blockHeight)
	
run(screenWidth, screenHeight, "Breakout", draw)
