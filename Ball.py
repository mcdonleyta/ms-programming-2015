from easyGL import *
x = 0
y = 0
incX = 2
incY = 1

def draw():
	global x, y, incX, incY
	setColor(1, 0, 0)
	drawRect(x, y, 10, 10)
	
	setColor(0, 1, 0) 
	drawRect(0, 0, 100, 200)

	x = x + 1 + incX
	y = y + 1 + incY	

	if x > 800:
	 incX = -1
	 
	if y > 600:
	 incY = -1
	 
	if x < 0:
	 incX = 1

	if y < 0:
	 incY = 1
	
	
	 

	blockwidth = 100
	blockheight = 200
	drawRect(0, 550, blockwidth, blockheight)
	
	 
	 
	 
	 
		 
run(800, 600, "Bouncing Ball!", draw)	
