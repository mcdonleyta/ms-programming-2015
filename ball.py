from easyGL import *

blockwidth = 100
blockheight = 50
x = 0
y = 0
incx = 4
incy = 2
block = 0
color = 1
walld = 0

def draw(): 
	
	global x,y,incx,incy, block, color, walld, blockwidth, blockheight
	
	setColor(1, 0, 0)                  
	drawRect (x, y, 100, 100)
	
	
	
	x = x + incx
	y = y + incy
	
	if x > 900:
		incx = -4
	
	if y > 780:
		incy = -2
	
	if x < -1:
		incx = 4
	
	if y < -1:
		incy = 2
	
	color = 1
	block = 0
	walld = 0
	while block < 10:
		setColor(.123, color, .234)
		drawRect (walld,830, blockwidth, blockheight)
		block = block + 1
		color = color - 0.1
		walld = walld + 100
		
	color = 1
	block = 0
	walld = 0
	while block < 10:
		setColor(1., color, .78546)
		drawRect (walld,780, blockwidth, blockheight)
		block = block + 1
		color = color - 0.1
		walld = walld + 100
		
	color = 1
	block = 0
	walld = 0
	while block < 10:
		setColor(.3456, color, 1)
		drawRect (walld,730, blockwidth, blockheight)
		block = block + 1
		color = color - 0.1
		walld = walld + 100
		
	color = 1
	block = 0
	walld = 0
	while block < 10:
		setColor(1, color,.361)
		drawRect (walld,680, blockwidth, blockheight)
		block = block + 1
		color = color - 0.1
		walld = walld + 100
		
	color = 1
	block = 0
	walld = 0
	while block < 10:
		setColor(color, color,color)
		drawRect (walld,630, blockwidth, blockheight)
		block = block + 1
		color = color - 0.1
		walld = walld + 100
	
	
	

               
	
	
	
run(1000, 1000, "chicken", draw)
