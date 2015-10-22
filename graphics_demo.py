from easyGL import *

sunX = 500
sunY = 500
sunW = 100
sunH = 100 
sunMPF = 1   
sunXY = 500
def draw():
	global sunXY, sunW, sunH, sunMPF 
	setColor(0, 1, 1)
	drawRect(0, 0, 800, 600) #Sky
	
	setColor(.38, 1, 0)
	drawRect(0, 0, 800, 200)#Grass                         
	   
	setColor(0.90625, 0.87890625, 0.046875) #Sun
	drawRect(sunXY, sunW, sunH)
	
	setColorA(1, 1, 1, .65) #Cloud
	drawRect(300, 500, 100, 50)
	
	setColorA(1, 1, 1, .50) #Cloud
	drawRect(325, 550, 50, 25)
	     
	drawRect(500,600,700,800)
	
	sunXY = sunXY - sunMPF    
run(800, 600, "Kavins Kavin", draw)


