from easyGL import *
    
def draw(): 
  #red, green, blue
  #setColor(0, 0, 1)                          
  #drawRect(10, 1, 200, 100)
  
  #sky
  setColor(148.0/256.0, 213.0/256.0, 235.0/256.0)                          
  drawRect(5, 2, 10000, 15000)
  #cloud1
  setColor(2520/256.0,2520/256.0,2520/256.0)                          
  drawRect(500, 1050, 500, 150)
  #cloud2
  setColor(250/256.0,250/256.0,250/256.0)
  drawRect(550, 1050, 500, 150)
  #Grass
  setColor(3/256.0,255/256.0,100/256.0)
  drawRect(1, 1, 10000, 250)
  #house
  setColor(247/256.0,74/256.0,106/256.0)                          
  drawRect(1000, 250, 250, 250)
  #windows
  setColor(5/256.0, 4/256.0, 0/256.0)                        
  drawRect(10, 1, 200, 100)
  #sun
  setColor(246/256.0,255/256.0,0/256.0)                          
  drawRect(1500, 900, 150, 150)
  #truck of tree
  setColor(156/256.0,93/256.0,11/256.0)
  drawRect(300, 250, 250, 400)
  #body of dog
  setColor(135/256.0,150/256.0,161/256.0)
  drawRect(500, 150, 150, 150)
  #head of dog
  setColor(135/256.0,150/256.0,161/256.0)
  drawRect(535, 300, 100, 75)
  #right ear of dog
  setColor(135/256.0,150/256.0,161/256.0)
  drawRect(575, 350, 75, 50)
  #left ear of dog
  setColor(135/256.0,150/256.0,161/256.0)
  drawRect(475, 350, 75, 50) 
  #left eye of dog
  setColor(5/256.0, 4/256.0, 0/256.0) 
  drawRect(550, 345, 10, 10)
  #right eye of dog
  setColor(5/256.0, 4/256.0, 0/256.0) 
  drawRect(610, 345, 10, 10)
  #nose of dog
  setColor(5/256.0, 4/256.0, 0/256.0) 
  drawRect(575, 325, 10, 10)
  #tonge of dog
  setColor(245/256.0, 81/256.0, 196/256.0) 
  drawRect(575, 300, 10, 10)
  #top of tree
  setColor(52/256.0,181/256.0 , 13/256.0)                          
  drawRect(175, 500, 500, 400)
  #Apple on the tree
  setColor(148/256.0,13/256.0,60/256.0)                          
  drawRect(500, 750, 50, 50)
  #Apple on the tree
  setColor(148/256.0,13/256.0,60/256.0)                          
  drawRect(300, 650, 50, 50)

run(10000, 1500, "Ansley best drawing", draw)
