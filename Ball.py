
from easyGL import *

import random

blockWidth = 100
blockHieght = 50

x = 0
y = 0
incx = 2
incy = 1


b1tp = 1
b2tp = 1
b3tp = 1
b4tp = 1
b5tp = 1
b6tp = 1
b7tp = 1
b8tp = 1
b9tp = 1
b10tp = 1
b11tp = 1
b12tp = 1
b13tp = 1
b14tp = 1
b15tp = 1
b16tp = 1

def draw():numBlockRow
	
	
global x,y, incx, incy, b1tp, b2tp, b3tp, b4tp, b5tp, b6tp, b7tp, b8tp, b9tp, b10tp, b11tp, b12tp, b13tp, b14tp, b15tp, numBlockRow
	
blockWidth = 800/16
blockHieght = (600/2/2/3)
blockHieght = (600/2/2/3)
blockHieght = (600/2/2/3)
blockHieght = (600/2/2/3)
blockHieght = (600/2/2/3)
blockHieght = (600/2/2/3)
blockHieght = (600/2/2/3)
blockHieght = (600/2/2/3)
blockHieght = (600/2/2/3)
blockHieght = (600/2/2/3)
blockHieght = (600/2/2/3)
blockHieght = (600/2/2/3)
blockHieght = (600/2/2/3)
blockHieght = (600/2/2/3)
blockHieght = (600/2/2/3)
blockHieght = (600/2/2/3)
	
x = x + incx
y = y + incy
	
if x > 775:
		incx = random.randint(-2, -1)
if y > 575:
	 incy = random.randint(-2, -1)		
if x < 0:
	 incx =  random.randint(1, 2)
if y < 0:
	 incy =  random.randint(1, 2)
	

	#first row
numBlockPerRow = 8
block = 0
while block < numBlockRows:
		drawRect(block*100,550,200,50)
		setColor(block/8.0,0,row/3.0)
	
		block = block + 1
	
	
	#second row	
setColor(1,0,0)
drawRect(0,495,blockWidth,blockhHight)
setColor(1,0,0)
drawRect(105,495,blockWidth,blockHeight)
setColor(1,0,0)
drawRect(210,495,blockWidth,blockHeight)
setColor(1,0,0)
drawRect(315,495,blockWidth,blockHeight)
setColor(1,0,0)
drawRect(420,495,blockWidth,blockHeight)
setColor(1,0,0)
drawRect(525,495,blockWidth,blockHeight)
setColor(1,0,0)
drawRect(630,495,blockWidth,blockHeight)
setColor(1,0,0)
drawRect(735,495,blockWidth,blockHeight)
setColor(1,0,0)
	
if x > 0 and x <  0 + blockWidth and y > 550 and y < 550 + blockHieght:
	
	if x > 100 and x <  100 + blockWidth and y > 550 and y < 550 + blockHieght:
	
		if x > 200 and x <  200 + blockWidth and y > 550 and y < 550 + blockHieght:
	
			if x > 300 and x <  300 + blockWidth and y > 550 and y < 550 + blockHieght:
	
					if x > 400 and x <  400 + blockWidth and y > 550 and y < 550 + blockHieght:
	
						if x > 500 and x <  500 + blockWidth and y > 550 and y < 550 + blockHieght:
	
							if x > 600 and x <  600 + blockWidth and y > 550 and y < 550 + blockHieght:
	
								if x > 700 and x <  700 + blockWidth and y > 550 and y < 550 + blockHieght:
	
									if x > 800 and x <  800 + blockWidth and y > 550 and y < 550 + blockHieght:
	
										if x > 900 and x <  900 + blockWidth and y > 550 and y < 550 + blockHieght:
	
											if x > 1000 and x <  1000 + blockWidth and y > 550 and y < 550 + blockHieght:
	
												if x > 1100 and x <  1100 + blockWidth and y > 550 and y < 550 + blockHieght:
	
													if x > 1200 and x <  1200 + blockWidth and y > 550 and y < 550 + blockHieght:
	
														if x > 1300 and x <  1300 + blockWith and y > 550 and y < 550 + blockHieght:
	
															if x > 1400 and x <  1400 + blockWidth and y > 550 and y < 550 + blockHieght:
	
																if x > 1500 and x <  1500 + blockWidth and y > 550 and y < 550 + blockHieght:
	
																	if x > 1600 and x <  1600 + blockWidth and y > 550 and y < 550 + blockHieght:
	
	
																		setColor(0,0,1)
																		drawRect(x,y,10,10)

run(800,600,"Bouncy Ball", draw)
