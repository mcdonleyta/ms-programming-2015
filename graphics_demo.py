from easyGL import *
    
def draw(): 
  setColor(54.0/256.0, 199.0/256.0, 59.0/256.0)  #Grass                        
  drawRect(0, 0, 5000, 150)
  
  setColor(0.0, 250.0/256.0, 237.0/256.0) #Sky
  drawRect(0, 150, 5000, 500)
  
  setColor(242.0/256.0, 255.0/256.0,0) #Sun                         
  drawRect(500, 450, 100, 100)
  
  setColor(255.0/256.0, 255.0/256.0, 255.0/256.0) #Cloud1
  drawRect(300, 400, 150, 50)
  
  setColor(255.0/256.0, 255.0/256.0, 255.0/256.0) #Cloud1
  drawRect(350, 450, 75, 50)
  
  setColor(255.0/256.0, 255.0/256.0, 255.0/256.0) #Cloud1
  drawRect(325, 430, 50, 50)
  
  setColor(255.0/256.0, 255.0/256.0, 255.0/256.0) #Cloud1
  drawRect(390, 420, 50, 50)
  
  setColor(255.0/256.0, 255.0/256.0, 255.0/256.0) #Cloud2
  drawRect(600, 350, 150, 50)
  
  setColor(255.0/256.0, 255.0/256.0, 255.0/256.0) #Cloud2
  drawRect(630, 380, 80, 50)

      
run(1000, 1000, "Taylor Changed Mr. McDonley's Awesome Example", draw)
