from easyGL import *

x = 0
y = 550
incx = 1
incy = 1
def draw(): 
	global x, y, incx, incy
	setColor(0, 0, 1)                  # this is called every                
	drawRect(x, y, 50, 50)
  
	x = x + incx
	y = y + incy

	if x > 800:
	   incx = incx * -1
	if y > 600:
	   incy = incy * -1
	if x < 0:
	   incx = incx * -1
	if y < 0:
	   incy = incy * -1
	   
run(800, 600, "Rachel's Bouncy Ball", draw)
