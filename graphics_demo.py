from easyGL import *
  
blockX = 500
blockY = 400
blockW = 50
blockH = 70
blockMPF = 1  
  
  
    
def draw():
  global blockX, blockY, blockW, blockH, blockMPF
  
  setColor(0.06640625, 0.94921875, 0.96484375) #Sky
  drawRect(0, 0, 900, 900)	
  setColor(0, 1, 0) #Grass
  drawRect(0, 0, 900, 50)
  setColor(0.89453125, 0.99609375, 0)
  drawRect(100, 500, 50, 50)
  setColor(0.99609375, 0.99609375, 0.99609375)
  drawRect(blockX, blockY, blockW, blockH)
  blockX = blockX - blockMPF
  if blockX < -100:
	  blockX = 800
  
 

    
run(800, 600, "Mr McDonley's Awesome Example", draw)
