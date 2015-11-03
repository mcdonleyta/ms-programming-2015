from easyGL import *
import random

x = 0
y = 0
incX = 2
incY = 1

def draw():
	global x, y, incX, incY
	
	setColor(1, 0, 0)
	drawRect(x, y, 100, 100)
	
	x = x + incX 
	y = y + incY
	
	if x > 700:
		incX = random.randint(-2, -1)
	
	if y > 500:
		incY = random.randint(-2, -1)
		
	if x < 0:
		incX = random.randint(1, 2)
	
	if y < 0:
		incY = random.randint(1, 2)   
	
run(800, 600, "Bouncing Ball", draw)
