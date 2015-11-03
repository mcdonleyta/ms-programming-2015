from easyGL import *
import random

x = 0
y = 0
incX = 2
incY = 1

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
b17tp = 1
b18p = 1
b19tp = 1
b20tp = 1
b21tp = 1
b22tp = 1
b23tp = 1
b24tp = 1
b25tp = 1
b26tp = 1
b27tp = 1
b28tp = 1
b28tp = 1
b29tp = 1
b30tp = 1
b31tp = 1
b32tp = 1
b33tp = 1
b34tp = 1
b35tp = 1
b36tp = 1
b37tp = 1
b38tp = 1
b39tp = 1
b40tp = 1
b41tp = 1
b42tp = 1
b43tp = 1
b44tp = 1
b45tp = 1
b46tp = 1
b47tp = 1

def draw():
	global b1tp, b2tp, b3tp, b4tp, b5tp, b6tp, b7tp, b8tp, b9tp, b10tp, b11tp, b12tp, b13tp, b14tp, b15tp, b16tp, b17tp, b18tp, b19tp, b20tp, b21tp, b22tp, b23tp, b24tp, b25tp, b26tp, b27tp, b28tp, b29tp, b30tp, b31tp, b32tp, b33tp, b34tp, b35tp, b36tp, b37tp, b38tp, b39tp, b40tp, b41tp, b42tp, b43tp, b44tp, b45tp, b46tp, b47tp	
	 
	blockWidth = 800/16
	block1Height = ((600/2)/2)/3
	block2Height = ((600/2)/2)/3
	block3Height = ((600/2)/2)/3
	block4Height = ((600/2)/2)/3
	block5Height = ((600/2)/2)/3
	block6Height = ((600/2)/2)/3
	block7Height = ((600/2)/2)/3
	block8Height = ((600/2)/2)/3
	block9Height = ((600/2)/2)/3
	block10Height = ((600/2)/2)/3
	block11Height = ((600/2)/2)/3
	block12Height = ((600/2)/2)/3
	block13Height = ((600/2)/2)/3
	block14Height = ((600/2)/2)/3
	block15Height = ((600/2)/2)/3
	block16Height = ((600/2)/2)/3

	setColorA(1,0,0,b1tp)
	drawRect(0, 550, blockWidth, block1Height)

	setColorA(0,0,1,b2tp)
	drawRect(50, 550, blockWidth, block2Height)

	setColorA(1,0,0,b3tp)
	drawRect(100, 550, blockWidth, block3Height)

	setColorA(0,1,0,b4tp)
	drawRect(150, 550, blockWidth, block4Height)

	setColorA(0,0,1,b5tp)
	drawRect(200, 550, blockWidth, block5Height)

	setColorA(1,0,0,b6tp)
	drawRect(250, 550, blockWidth, block6Height)

	setColorA(0,1,0,b7tp)
	drawRect(300, 550, blockWidth, block7Height)

	setColorA(0,0,1,b8tp)
	drawRect(350, 550, blockWidth, block8Height)

	setColorA(1,0,0,b9tp)
	drawRect(400, 550, blockWidth, block9Height)

	setColorA(0,1,0,b10tp)
	drawRect(450, 550, blockWidth, block10Height)

	setColorA(0,0,1,b11tp)
	drawRect(500, 550, blockWidth, block11Height)

	setColorA(1,0,0,b12tp)
	drawRect(550, 550, blockWidth, block12Height)

	setColorA(0,1,0,b13tp)
	drawRect(600, 550, blockWidth, block13Height)

	setColorA(0,0,1,b14tp)
	drawRect(650, 550, blockWidth, block14Height)

	setColorA(1,0,0,b15tp)
	drawRect(700, 550, blockWidth, block15Height)

	setColorA(0,1,0,b16tp)
	drawRect(750, 550, blockWidth, block16Height)

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

	if x > 0 and x < 0 + blockWidth and y > 550 and y < 550 + block1Height:
		b1tp = 0
		
	if x > 50 and x < 50 + blockWidth and y > 550 and y < 550 + block1Height:
		b2tp = 0

	if x > 100 and x < 100 + blockWidth and y > 550 and y < 550 + block1Height:
		b3tp = 0

	if x > 150 and x < 150 + blockWidth and y > 550 and y < 550 + block1Height:
		b4tp = 0

	if x > 200 and x < 200 + blockWidth and y > 550 and y < 550 + block1Height:
		b5tp = 0

	if x > 250 and x < 250 + blockWidth and y > 550 and y < 550 + block1Height:
		b6tp = 0

	if x > 300 and x < 300 + blockWidth and y > 550 and y < 550 + block1Height:
		b7tp = 0
		
	if x > 350 and x < 350 + blockWidth and y > 550 and y < 550 + block1Height:
		b8tp = 0
			
	if x > 400 and x < 400 + blockWidth and y > 550 and y < 550 + block1Height:
		b9tp = 0

	if x > 450 and x < 450 + blockWidth and y > 550 and y < 550 + block1Height:
		b10tp = 0
		
	if x > 500 and x < 500 + blockWidth and y > 550 and y < 550 + block1Height:
		b11tp = 0

	if x > 550 and x < 550 + blockWidth and y > 550 and y < 550 + block1Height:
		b612tp = 0

	if x > 600 and x < 600 + blockWidth and y > 550 and y < 550 + block1Height:
		b13tp = 0	

	if x > 650 and x < 650 + blockWidth and y > 550 and y < 550 + block1Height:
		b14tp = 0
		
	if x > 700 and x < 700 + blockWidth and y > 550 and y < 550 + block1Height:
		b15tp = 0

	if x > 750 and x < 750 + blockWidth and y > 550 and y < 550 + block1Height:
		b16tp = 0
		
    
run(800, 600, "Tester", draw)
