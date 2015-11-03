from easyGL import *

X = 0
Y = 0
incX = 1
incY = 2

def draw():
	global X, Y, incX, incY
	setColor(1, 0, 0)
	drawRect(X, Y, 10, 10)

	block = 0
	PositionX = 0
	PositionY = 550
	
	#draw blocks
	while block < 8:
		setColor(PositionX/800.0, 0.1, 0.9)
		drawRect(PositionX, PositionY, 100, 50)
		PositionX = PositionX + 100
		block = block + 1
	PositionY = PositionY - 50
	PositionX = 0
	while block >= 8 and block <= 16:
		setColor(0.7, PositionX/800.0, 1)
		drawRect(PositionX, PositionY, 100, 50)
		PositionX = PositionX + 100
		block = block + 1
	PositionY = PositionY - 50
	PositionX = 0
	while block > 16 and block <= 25:
		setColor(0.3, 1, PositionX/800.0)
		drawRect(PositionX, PositionY, 100, 50)
		PositionX = PositionX + 100
		block = block + 1
	
	#Check if hit
	score = 0
	PositionY = 550

	PositionX = 0
	block = 0
	while block < 8:
		if X > PositionX and X < PositionX + 100 and Y > PositionY and Y < PositionY + 50:
			incY = -1
			score = score + 1
		block = block + 1
		PositionX = PositionX + 100
	PositionY = PositionY - 50
	PositionX = 0
	block = 0
	while block < 8:
		if X > PositionX and X < PositionX + 100 and Y > PositionY and Y < PositionY + 50:
			incY = -1
			score = score + 1
		block = block + 1
		PositionX = PositionX + 100
	PositionY = PositionY - 50
	PositionX = 0
	block = 0
	while block < 8:
		if X > PositionX and X < PositionX + 100 and Y > PositionY and Y < PositionY + 50:
			incY = -1
			score = score + 1
		block = block + 1
		PositionX = PositionX + 100
	
	

	#Moving ball
	X = X + incX
	Y = Y + incY
	
	if X > 800:
		incX = -1
	if Y > 600:
		incY = -1
	if X < 0:
		incX = 1
	if Y < 0:
		incY = 1
	
	
run(800, 600, "Breakout", draw)
