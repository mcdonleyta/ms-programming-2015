from easyGL import *

carMPF = 6
carx = 20
cary = 60
carw = 30
carh = 30

carbMPF = 6
carbx = 0
carby = 60
carbw = 70
carbh = 10

wheelMPF = 6
wheelx = 5
wheely = 50
wheelw = 10
wheelh = 10

wheel2MPF = 6
wheel2x = 55
wheel2y = 50
wheel2w = 10
wheel2h = 10

windowMPF = 6
windowx = 35
windowy = 70
windoww = 15
windowh = 15

car2MPF = 6
car2x = 1860
car2y = 115
car2w = 30
car2h = 30

carb2MPF = 6
carb2x = 1840
carb2y = 115
carb2w = 70
carb2h = 10

wheel3MPF = 6
wheel3x = 1895
wheel3y = 105
wheel3w = 10
wheel3h = 10

wheel4MPF = 6
wheel4x = 1845
wheel4y = 105
wheel4w = 10
wheel4h = 10

window2MPF = 6
window2x = 1860
window2y = 125
window2w = 15
window2h = 15

planex = 200
planey = 500
planew = 200
planeh = 50

planeNx = 400
planeNy = 510
planeNw = 20
planeNh = 20

planeTx = 200
planeTy = 550
planeTw = 30
planeTh = 40

planeT2x = 230
planeT2Y = 550
planeT2w = 20
planeT2h = 20

def draw(): 
  global carx, cary, carw, carh, carMPF
  global carbx, carby, carbw, carbh, carbMPF
  global wheelx, wheely, wheelw, wheelh, wheelMPF
  global wheel2x, wheel2y, wheel2w, wheel2h, wheel2MPF
  global windowx, windowy, windoww, windowh, windowMPF
  global car2x, car2y, car2w, car2h, car2MPF
  global carb2x, carb2y, carb2w, carb2h, carb2MPF
  global wheel3x, wheel3y, wheel3w, wheel3h, wheel3MPF
  global wheel4x, wheel4y, wheel4w, wheel4h, wheel4MPF
  global window2x, window2y, window2w, window2h, window2MPF
  
  setColor(1., 0, 1)      #sun                  
  drawRect (50, 1800, 100, 100)
  
  setColor(0., 1., .2)                          
  drawRect(1, 1, 2000, 200) #grass
  
  setColor(1., .33, .2)      #desert                    
  drawRect(1, 200, 1, 1)
  
  setColor(0., 0.8125, 0.99609375)      #sky                   
  drawRect(1, 200, 2000, 800)
  
  setColor(0.88671875, 0.99609375, 0.1875)#sun                   
  drawRect(200, 700, 100, 100)
  
  setColor(1., .33, .2)      #home                    
  drawRect(1000, 200, 150, 200)
  
  setColor(.4, .4, .4)      #home                    
  drawRect(1030, 200, 30, 60)
  
  setColor(0, 0, 0)      #home                    
  drawRect(1030, 300, 30, 30)
  
  setColor(0, 0, 0)      #home                    
  drawRect(1030, 360, 30, 30)
  
  setColor(0, 0, 0)      #home                    
  drawRect(1090, 360, 30, 30)
  
  setColor(0, 0, 0)      #home                    
  drawRect(1090, 300, 30, 30)
  
  setColor(0, 0, 0)      #home                    
  drawRect(1090, 240, 30, 30)
  
  setColor(0, 0, 0)      #road                   
  drawRect(0, 50, 2000, 100)
  
  setColor(1, 1, 1)      #road                   
  drawRect(0, 40, 2000, 10)
  
  setColor(1, 1, 1)      #road                   
  drawRect(0, 150, 2000, 10)
  
  setColor(1, 1, 0)      #road                   
  drawRect(0, 95, 2000, 10)
  
  setColor(0.9, 0.9, 0.5)      #road                   
  drawRect(0, 170, 2000, 10)
  
  setColor(0, 0, 0)      #road                    
  drawRect(1030, 150, 30, 50)
  
  setColor(0, 0.74609375, 1)      #car                 
  drawRect(carx, cary, carw, carh)
  
  setColor(0, 0.74609375, 1)      #car body              
  drawRect(carbx, carby, carbw, carbh)
  
  setColor(0.7, 0.7, 0.57)      #wheel
  drawRect(wheelx, wheely, wheelw, wheelh)

  setColor(0.7, 0.7, 0.57)      #wheel2
  drawRect(wheel2x, wheel2y, wheel2w, wheel2h)
  
  setColorA(.2,.2,.2,.9) #window
  drawRect(windowx, windowy, windoww, windowh) 
  
  setColor(0, 1, 0)      #car2               
  drawRect(car2x, car2y, car2w, car2h)
  
  setColor(0, 1, 0)      #car body  2            
  drawRect(carb2x, carb2y, carb2w, carb2h)
  
  setColor(0.7, 0.7, 0.57)      #wheel 3
  drawRect(wheel3x, wheel3y, wheel3w, wheel3h)

  setColor(0.7, 0.7, 0.57)      #wheel4
  drawRect(wheel4x, wheel4y, wheel4w, wheel4h)
  
  setColorA(.2,.2,.2,.9) #window 2
  drawRect(window2x, window2y, window2w, window2h) 
  
  setColor(1,1,1)
  drawRect(planex,planey, planew, planeh)
  
  setColor(0,0,0)
  drawRect(planeNx, planeNy,planeNw, planeNh)
  
  setColor(.5,.5,.5)
  drawRect(planeTx, planeTy, planeTw, planeTh)
  
  setColor(.5,.5,.5)
  drawRect(planeT2x, planeT2Y, planeT2w, planeT2h)
  
  wheelx = wheelx+wheelMPF
  
  carx = carx+carMPF
  
  wheel2x = wheel2x+wheelMPF
  
  carbx = carbx+carbMPF
  
  windowx = windowx + windowMPF
  
  wheel3x = wheel3x - wheel3MPF
  
  car2x = car2x - car2MPF
  
  wheel4x = wheel4x - wheel4MPF
  
  carb2x = carb2x - carb2MPF
  
  window2x = window2x - window2MPF
  
  
  if carx > 1920:
	carx = 20
  if carbx > 1900:
	carbx = 0
  if wheelx > 1895:
	  wheelx = 5
  if wheel2x > 1955:
	  wheel2x = 55
  if windowx > 1935:
	  windowx = 35


  if car2x < 0:
	car2x = 1860
  if carb2x < 0:
	carb2x = 1865
  if wheel3x < 5:
	  wheel3x = 1865
  if wheel4x < 0:
	  wheel4x = 1870
  if window2x < 0:
	  window2x = 1860

  
    
run(2000, 1000, "random bulding and cars", draw)
