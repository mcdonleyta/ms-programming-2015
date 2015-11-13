from easyGL import *
import random

X = 0
Y = 0
screenWidth = 800
screenHeight = 600
numBlockPerRow = 8
numberRows = 3
blockWidth = screenWidth/numBlockPerRow
blockHeight = (screenHeight/2)/2/numberRows

incX = 1
incY = 1

def draw():
	global X, Y, incX, incY, screenWidth, screenHeight, numBlockPerRow, numberRows, blockWidth, blockHeight
	setColor(1, 0, 0)
	drawRect(X, Y, 10, 10)

	#draw blocks
	block = 0
	row = 0
	PositionY = screenHeight - blockHeight
	
	while row < numberRows:
		PositionX = 0
		block = 0
		color = 0
		while block < numBlockPerRow:
			if row == 0:
				setColor(random.randint(0, 8)/8.0, random. randint(0, 8)/8.0, color)
			if row == 1:
				setColor(random.randint(0, 8)/8.0, color, random.randint(0, 8)/8.0)
			if row == 2:
				setColor(color, random.randint(0, 8)/8.0, random.randint(0, 8)/8.0)
			drawRect(PositionX, PositionY, blockWidth, blockHeight)
			PositionX = PositionX + blockWidth
			block = block + 1
			color = color + 0.2
		PositionY = PositionY - blockHeight
		row = row + 1
	
	#Check if hit
	score = 0
	row = 0
	PositionY = screenHeight - blockHeight
	
	while row < numberRows:
		PositionX = 0
		block = 0
		while block < 8:
			if X > PositionX and X < PositionX + blockWidth and Y > PositionY and Y < PositionY + blockHeight:
				incY = -1
				score = score + 1
			block = block + 1
			PositionX = PositionX + blockWidth
		PositionY = PositionY - blockHeight
		row = row + 1

	#Moving ball
	X = X + incX
	Y = Y + incY
	
	if X > screenWidth:
		incX = -1
	if Y > screenHeight:
		incY = -1
	if X < 0:
		incX = 1
	if Y < 0:
		incY = 1
	
	
run(screenWidth, screenHeight, "Breakout", draw)
