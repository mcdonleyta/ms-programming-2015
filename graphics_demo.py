from easyGL import *

carMPF = 6
carx = 0
cary = 60
carw = 60
carh = 30

wheelMPF = 6
wheelx = 0
wheely = 50
wheelw = 10
wheelh = 10

  
    

def draw(): 
  global carx, cary, carw, carh, carMPF
  global wheelx, wheely, wheelw, wheelh, wheelMPF
  
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
  
  setColor(0, 0, 0)      #home                    
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
  drawRect(1030, 150, 30, 40)
  
  setColor(0, 0.74609375, 1)      #car                 
  drawRect(carx, cary, carw, carh)
  
  setColor(0.7, 0.7, 0.57)      #wheel
  drawRect(wheelx, wheely, wheelw, wheelh)
  
  wheelx = wheelx+wheelMPF
  carx = carx+carMPF
  


  
    
run(2000, 1000, "randome bulding", draw)
