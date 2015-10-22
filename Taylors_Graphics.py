from easyGL import *

cowX = 0
cowY = 150
cowWidth = 50
cowHeight = 50
cowMPF = 10 # Move 1 pixel every frame

cloud3X = 900
cloud3Y = 500
cloud3MPF = 0.25

cloud2X = 600
cloud2Y = 350
cloud2MPF = 0.25

cloud1X = 300
cloud1Y = 400
cloud1MPF = 0.25 

sunX = 700
sunY = 450
sunHeight = 100
sunMPF = 0.15

skyMPF = 0.09
skyColor = 250

moonTrans = 0

def myColor(r, g, b):
	setColor(r/256.0, g/256.0, b/256.0)

def myColorA(r, g, b, a):
	setColorA(r/256.0, g/256.0, b/256.0, a)


def draw():
  global cowX, cowY, cowWidth, cowHeight, cowMPF
  global cloud2X, cloud2Y, cloud2MPF
  global sunX, sunY, sunHeight, sunMPF
  global skyColor, skyMPF
  global cloud1X, cloud1Y, cloud1MPF
  global cloud3X, cloud3Y, cloud3MPF
  global moonTrans 
  
  setColor(0.0, skyColor/256.0, (skyColor-13)/256.0) #Sky
  drawRect(0, 150, 5000, 500)
  
  setColor(242.0/256.0, 255.0/256.0,0) #Sun                         
  drawRect(sunX, sunY, 100, sunHeight)
  
  myColorA(140, 163, 186, moonTrans) #Moon
  drawRect(700, 450, 100, 100)
	 
  myColor(54.0, 199.0, 59.0)  #Grass                        
  drawRect(0, 0, 5000, 150)
  
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
  
  myColorA(255.0, 255.0, 255.0, 0.8) #Cloud3
  drawRect(cloud3X, cloud3Y, 130, 45)
  
  myColorA(255.0, 255.0, 255.0, 0.8) #Cloud3
  drawRect(cloud3X + 20, cloud3Y + 45, 80, 20)                    
  
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
  
  if cowX > 1300:
	  cowMPF = cowMPF * -1
  if cowX < 0:
	  cowMPF = cowMPF + 1 
	
  cloud2X = cloud2X - cloud2MPF
  
  if cloud2X < -110:
	  cloud2X = 1300
  
  cloud1X = cloud1X - cloud1MPF
  
  if cloud1X < -160:
	  cloud1X = 1300
	  
  sunY = sunY - sunMPF
  
  skyColor = skyColor - skyMPF
  
  cloud3X = cloud3X - cloud3MPF
  
  if cloud3X < -110:
	   cloud3X = 1300
	  
  if sunY < -101:
	  moonTrans = 1
  	
      
run(1500, 1500, "It's A Brown Block (Cow)!", draw)
