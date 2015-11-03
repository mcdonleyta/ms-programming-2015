from easyGL import*
#Olivia Ave /,(,^._.^, ~=[,,_,,]:3 /^._.^\ ^._.^ =^.^= =^W^= :3 
X=0
Y=0
incX=15
incY=3
def draw():
	
	setColor(1, 0.8, 1)
	drawRect(0, 0, 800, 600)
	
	BlockWidth=100
	BlockHieght=50
	setColor(1, 0.5, 0)
	drawRect(100, 550, BlockWidth, BlockHieght)
	
	BlockWidth=100
	BlockHieght=50
	setColor(1, 0, 0)
	drawRect(0, 550, BlockWidth, BlockHieght)
	
	BlockWidth=100
	BlockHieght=50
	setColor(1, 1, 0)
	drawRect(200, 550, BlockWidth, BlockHieght)
	
	BlockHieght=50
	setColor(0, 1, 0)
	drawRect(300, 550, BlockWidth, BlockHieght)
	
	BlockWidth=100
	BlockHieght=50
	setColor(0, 0, 1)
	drawRect(400, 550, BlockWidth, BlockHieght)
	
	BlockWidth=100
	BlockHieght=50
	setColor(0.5, 0, 1)
	drawRect(500, 550, BlockWidth, BlockHieght)
	
	BlockWidth=100
	BlockHieght=50
	setColor(0.7, 0, 1)
	drawRect(600, 550, BlockWidth, BlockHieght)
	
	BlockWidth=100
	BlockHieght=50
	setColor(1, 0, 1)
	drawRect(700, 550, BlockWidth, BlockHieght)
	
	BlockWidth=100
	BlockHieght=50
	setColor(0.7, 0, 1)
	drawRect(100, 500, BlockWidth, BlockHieght)
	
	BlockWidth=100
	BlockHieght=50
	setColor(1, 0, 1)
	drawRect(0, 500, BlockWidth, BlockHieght)
	
	BlockWidth=100
	BlockHieght=50
	setColor(0.5, 0, 1)
	drawRect(200, 500, BlockWidth, BlockHieght)
	
	BlockWidth=100
	BlockHieght=50
	setColor(0, 0, 1)
	drawRect(300, 500, BlockWidth, BlockHieght)
	
	BlockWidth=100
	BlockHieght=50
	setColor(0, 1, 0)
	drawRect(400, 500, BlockWidth, BlockHieght)
	
	BlockWidth=100
	BlockHieght=50
	setColor(1, 1, 0)
	drawRect(500, 500, BlockWidth, BlockHieght)
	
	BlockWidth=100
	BlockHieght=50
	setColor(1, 0.5, 0)
	drawRect(600, 500, BlockWidth, BlockHieght)
	
	BlockWidth=100
	BlockHieght=50
	setColor(1, 0, 0)
	drawRect(700, 500, BlockWidth, BlockHieght)
	
	BlockWidth=100
	BlockHieght=50
	setColor(0, 0, 0)
	drawRect(100, 450, BlockWidth, BlockHieght)
	
	BlockWidth=100
	BlockHieght=50
	setColor(1, 1, 1)
	drawRect(0, 450, BlockWidth, BlockHieght)
	
	BlockWidth=100
	BlockHieght=50
	setColor(1, 1, 1)
	drawRect(200, 450, BlockWidth, BlockHieght)
	
	BlockWidth=100
	BlockHieght=50
	setColor(0, 0, 0)
	drawRect(300, 450, BlockWidth, BlockHieght)
	
	BlockWidth=100
	BlockHieght=50
	setColor(1, 1, 1)
	drawRect(400, 450, BlockWidth, BlockHieght)
	
	BlockWidth=100
	BlockHieght=50
	setColor(0, 0, 0)
	drawRect(500, 450, BlockWidth, BlockHieght)
	
	BlockWidth=100
	BlockHieght=50
	setColor(1, 1, 1)
	drawRect(600, 450, BlockWidth, BlockHieght)
	
	BlockWidth=100
	BlockHieght=50
	setColor(0, 0, 0)
	drawRect(700, 450, BlockWidth, BlockHieght)
	
	global X,Y, incX, incY
	setColor(1, 0.4, 0.6)
	drawRect(X, Y, 50, 50)
	
	X=X+incX
	Y=Y+incY
	
	if X>760:
		incX=-15
	if Y>550:
		incY=-3
	if Y==0:
		incY=+3
	if X==0:
		incX=+15
	
run(800,600, "Bouncy Ball",draw)
