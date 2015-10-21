from easyGL import *

cowX = 0
cowY = 150
cowWidth = 50
cowHeight = 50
cowMPF = 10 # Move 1 pixel every frame

cloud2X = 600
cloud2Y = 350
cloud2MPF = 0.25

cloud1X = 300
cloud1Y = 400
cloud1MPF = 0.25 

sunX = 500
sunY = 450
sunMPF = 0.05

def myColor(r, g, b):
	setColor(r/256.0, g/256.0, b/256.0)

def myColorA(r, g, b, a):
	setColorA(r/256.0, g/256.0, b/256.0, a/256.0)


def draw():
  global cowX, cowY, cowWidth, cowHeight, cowMPF
  global cloud2X, cloud2Y, cloud2MPF
  global sunX, sunY, sunMPF
  global cloud1X, cloud1Y, cloud1MPF
	 
  myColor(54.0, 199.0, 59.0)  #Grass                        
  drawRect(0, 0, 5000, 150)
  
  setColor(0.0, 250.0/256.0, 237.0/256.0) #Sky
  drawRect(0, 150, 5000, 500)
  
  setColor(242.0/256.0, 255.0/256.0,0) #Sun                         
  drawRect(sunX, sunY, 100, 100)
  
  setColorA(255.0/256.0, 255.0/256.0, 255.0/256.0, 0.8) #Cloud1
  drawRect(cloud1X, cloud1Y, 150, 50)
  
  setColorA(255.0/256.0, 255.0/256.0, 255.0/256.0, 0.8) #Cloud1
  drawRect(cloud1X + 40, cloud1Y + 50, 75, 35)
  
  setColorA(255.0/256.0, 255.0/256.0, 255.0/256.0, 0.8) #Cloud1
  drawRect(cloud1X + 20, cloud1Y + 50, 20, 20)
  
  myColorA(255.0, 255.0, 255.0, 200,)                   #Cloud1
  drawRect (cloud1X + 115, cloud1Y + 50, 20, 20)
  
  setColorA(255.0/256.0, 255.0/256.0, 255.0/256.0, 0.8) #Cloud2
  drawRect(cloud2X, cloud2Y, 150, 50)
  
  setColorA(255.0/256.0, 255.0/256.0, 255.0/256.0, 0.8) #Cloud2
  drawRect(cloud2X + 30, cloud2Y + 50, 80, 35)
  
  setColor(158.0/256.0, 76.0/256.0, 9.0/256.0) #cow body
  drawRect(cowX, cowY, cowWidth, cowHeight)
  
  setColor(158.0/256.0, 76.0/256.0, 9.0/256.0) #cow legs
  drawRect(cowX, cowY-10, cowWidth/5, cowHeight/2)
  drawRect(cowX +40, cowY-10, cowWidth/5, cowHeight/2)
  
  setColor(199.0/256.0, 199.0/256.0, 199.0/256.0)
  drawRect(cowX +15, cowY +40, cowWidth/2, cowHeight/2) #cow head
  
  setColor(0, 0, 0,)
  drawRect(cowX+20, cowY+50, cowWidth/10, cowHeight/10)
  drawRect(cowX+30, cowY+50, cowWidth/10, cowHeight/10)
  cowX = cowX + cowMPF
  
  if cowX > 1000:
	  cowMPF = cowMPF * -1
  if cowX < 0:
	  cowMPF = cowMPF + 1 
	
  cloud2X = cloud2X - cloud2MPF
  
  if cloud2X < -110:
	  cloud2X = 1000
  
  cloud1X = cloud1X - cloud1MPF
  
  if cloud1X < -130:
	  cloud1X = 1000
	  
  sunY = sunY - sunMPF	
      
run(1000, 700, "It's A Cow!", draw)
