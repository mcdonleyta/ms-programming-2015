from easyGL import *

pigX = 0
pigY = 150
pigWidth = 50
pigHeight = 50
pigMPF = 10 # Move 1 pixel every frame

def draw():
	
  setColor(232.0/256.0, 100.0/256.0, 212.0/256.0)
  drawRect(pigX, pigY, pigWidth, pigHeight)

  
