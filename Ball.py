from easyGL import *

X = 0
Y = 0
incX = 1
incY = 2

def draw():
	global X, Y, incX, incY
	setColor(1, 0, 0)
	drawRect(X, Y, 10, 10)
	
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
	
run(800, 600, "Bouncy Ball", draw)
