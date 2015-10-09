from easyGL import *
    
def draw(): 
  setColor(0, 255, 0)                          
  drawRect(0, 0, 1200, 200) #First X Second Y Third Width Fourth Height
  setColor(0, 50, 255) #RGB
  drawRect(0, 200, 1200, 1200) 
  setColor(255, 255, 0)
  drawRect(675, 600, 150, 150) #sun
  setColor(1, 1, 1) #cloud1Piece1
  drawRect(300, 600, 150, 50)
  setColor(1, 1, 1) #cloud1Piece2
  drawRect(310, 650, 125, 25)
  setColor(1, 1, 1) #cloud1Piece3
  drawRect(320, 675, 100, 25)
  setColor(1, 1, 1) #cloud2Piece1
  drawRect(850, 400, 150, 50)
  setColor(1, 1, 1) #cloud2Piece2
  drawRect(860, 450, 125, 25)
  setColor(1, 1, 1) #cloud2Piece3
  drawRect(870, 475, 100, 25)
  
run(1200, 900, "Jacks, um I guess rectangular test!!", draw)
 



