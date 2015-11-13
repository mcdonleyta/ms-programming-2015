from easyGL import *
import random

x = 0
y = 0
incX = 2
incY = 1

def draw():
	
	numBlockPerRow = 16
	block = 0
	row = 0

	
	
	while row < 3:
		while block < numBlockPerRow:
			setColor(0,1,0)
			drawRect(block * 100, 550, 100, 50)
			block = block + 1
		row = row +1
	global x, y, incX, incY

	setColor(100.0/256.0, 191.0/256.0, 222.0/256.0)
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

		
    
run(800, 600, "Tester", draw)
