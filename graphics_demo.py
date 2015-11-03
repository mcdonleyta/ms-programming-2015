from easyGL import *

bodyX = 450
bodyY = 100
bodyw = 200
bodyh = 100
bodympf = 1 
def draw(): 
 
  global bodyX, bodyY, bodyw, bodyh, bodympf
  setColor(0.5, 0.8, 1)                          
  drawRect(0, 0, 20000, 20000) #Sky
  
  setColor(0.6, 1, 0.4)                          
  drawRect(0, 0, 20000, 80)#Grass
  
  setColor(1, 0.9, 0)                          
  drawRect(300, 350, 150, 150) #Sun
   
  setColor(255.0/256.0, 171.0/256.0, 240.0/256.0)  #Head                       
  drawRect(bodyX - 100, bodyY + 50, bodyw - 100, bodyh)
  
  setColor(255.0/256.0, 171.0/256.0, 240.0/256.0 ) #Body                          
  drawRect(bodyX, bodyY, bodyw, bodyh)
  
  setColor(255.0/256.0, 171.0/256.0, 240.0/256.0 ) #leg1                         
  drawRect(bodyX, bodyY-70, bodyw-150, bodyh)
  
  setColor(255.0/256.0, 171.0/256.0, 240.0/256.0 )   #leg2                       
  drawRect(bodyX+200, bodyY-70, bodyh-150, bodyh)
  
  setColor(255.0/256.0, 171.0/256.0, 240.0/256.0 ) #ear horizontal part 1                        
  drawRect(bodyX-100, bodyY+150, bodyw-180, bodyh-92)
  
  setColor(255.0/256.0, 171.0/256.0, 240.0/256.0 ) #ear vertical part 1                         
  drawRect(bodyX-95, bodyY+150, bodyw-190, bodyh-85)
  
  setColor(255.0/256.0, 171.0/256.0, 240.0/256.0 ) #ear horizontel part 2                         
  drawRect(bodyX-20, bodyY+150, bodyw-180, bodyh-92)
  
  setColor(255.0/256.0, 171.0/256.0, 240.0/256.0 ) #ear vertical part 2                         
  drawRect(bodyX-15, bodyY+150, bodyw-190, bodyh-85)
  
  setColor(143.0/256.0, 84.0/256.0, 3.0/256.0 ) #Hoof                        
  drawRect(bodyX, bodyY-70, bodyw-150, bodyh-80)
  
  setColor(143.0/256.0, 84.0/256.0, 3.0/256.0 ) #Hoof                         
  drawRect(bodyX+150, bodyY-70, bodyw-150, bodyh-80)
  
  setColor(1, 1, 1)                          
  drawRect(bodyX-40, bodyY+130,bodyw- 180, bodyh-80)#eye white 1
  
  setColor(0, 0, 0)                          
  drawRect(bodyX-30, bodyY+130, bodyw-180, bodyh-80)#eye black 1 
  
  setColor(1, 1, 1)                          
  drawRect(bodyX-75, bodyY+130, bodyw-180, bodyh-80)#eye white 2
  
  setColor(0, 0, 0)                          
  drawRect(bodyX-85, bodyY+130, bodyw-180, bodyh-80)#eye black 2
  
  setColor(1, 0.1, 0.4)                          
  drawRect(bodyX-70, bodyY+100, bodyw-160, bodyh-80)#nose
  
  setColor(0, 0, 0)                          
  drawRect(bodyX-70, bodyY+110, bodyw-190, bodyh-90)#nose black part 1
  
  setColor(0, 0, 0)                          
  drawRect(bodyX-40, bodyY+110, bodyw-190, bodyh-90)#nose black part 2
  
  bodyX = bodyX - bodympf
  
run(800, 600, "Olivia's pig", draw)
