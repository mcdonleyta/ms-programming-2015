from easyGL import *
    
def draw(): 
	setColor(1,1,0)                          
	drawRect(100,400,300,200)
	
	setColor(0.46,0.34,0.34)
	drawRect(100,4000,3000,3250)
	
	setColor(1,1,0)
	drawRect(225,450,925,135)
	
	setColor(1,1,0)
	drawRect(300,500,200,400)
	
	setColor(0,0,0)
	drawRect(300,400,200,100)
	
	setColor(0.90,0.90,0.90)
	drawRect(170,270,370,570)
	
	setColor(1,1,1)
	drawRect(200,300,100,500)
	
	setColor(0.9,0.9,0.9)
	drawRect(200,400,600,800)
	
	setColor(0,0,1)
	drawRect(500,700,600,400)
	
	setColor(1,1,0)
	drawRect(200,400,500,600)
	
run(8000,6000,"Nivaas Game", draw)
