from easyGL import *
    
def draw(): 
  setColor(0, 255, 0)  #GRASS                        
  drawRect(0, 0, 1200, 200) 
  setColor(0, 50, 255) #SKY
  drawRect(0, 200, 1200, 1200) 
  setColor(255, 55, 0) #SUN
  drawRect(675, 600, 150, 150) 
  
  setColorA(1, 1, 1, 0.7) #cloud1Piece1
  drawRect(300, 600, 150, 50)
  setColorA(1, 1, 1, 0.7) #cloud1Piece2
  drawRect(310, 650, 125, 25)
  setColorA(1, 1, 1, 0.7) #cloud1Piece3
  drawRect(320, 675, 100, 25)
  
  setColorA(1, 1, 1, 0.7) #cloud2Piece1
  drawRect(850, 400, 150, 50)
  setColorA(1, 1, 1, 0.7) #cloud2Piece2
  drawRect(860, 450, 125, 25)
  setColorA(1, 1, 1, 0.7) #cloud2Piece3
  drawRect(870, 475, 100, 25)
  
  setColor(1, 1, 1) #Fence1Piece1
  drawRect(0, 200, 25, 125)
  setColor(1, 1, 1) #Fence1Piece2
  drawRect(500, 200, 25, 130)
  setColor(1, 1, 1) #Fence1Piece3
  drawRect(0, 300, 500, 30)
  setColor(1, 1, 1) #Fence1Piece3
  drawRect(0, 225, 500, 30)
  
  setColor(1, 1, 1) #Fence2Piece1
  drawRect(650, 200, 25, 125)
  setColor(1, 1, 1) #Fence2Piece2
  drawRect(1175, 200, 25, 130)
  setColor(1, 1, 1) #Fence2Piece3
  drawRect(650, 300, 550, 30)
  setColor(1, 1, 1) #Fence2Piece3
  drawRect(650, 225, 550, 30)
  
  setColor(0.54, 0.26, 0.07)
  drawRect(200, 200, 50, 300) #tree1piece1
  setColor(0, 0.39, 0)
  drawRect(120, 500, 200, 50) #tree1piece2
  setColor(0, 0.39, 0)
  drawRect(150, 550, 150, 35) #tree1piece3
  setColor(0, 0.39, 0)
  drawRect(180, 580, 100, 35) #tree1piece4
  
  setColor(0.54, 0.26, 0.07)
  drawRect(800, 200, 50, 300) #tree1piece1
  setColor(0, 0.39, 0)
  drawRect(720, 500, 200, 50) #tree1piece2
  setColor(0, 0.39, 0)
  drawRect(750, 550, 150, 35) #tree1piece3
  setColor(0, 0.39, 0)
  drawRect(780, 580, 100, 35) #tree1piece4
  
  
run(1200, 900, "Jacks I guess rectangular test!!", draw)
 



