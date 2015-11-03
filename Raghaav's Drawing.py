from easyGL import *

blockMPF = 1
blockX = 0
blockY = 50
blockW = 20
blockH = 50  

flyingHeadX = 290 
flyingHeadY = 200
flyingHeadW = 30
flyingHeadH = 30
flyingHeadMPF = 2

def draw():
  global blockX, blockY, blockW, blockH, blockMPF
  global flyingHeadX, flyingHeadY, flyingHeadW, flyingHeadH, flyingHeadMPF
  drawRect(blockX, blockY, blockW, blockH)
  blockX = blockX - blockMPF
  setColor(0.4, 0.4, 1) #blue sky                         
  drawRect(0, 150, 800, 650)
  setColor(0,1,0) #green grass
  drawRect(0, 0, 800, 150)
  setColor(1,0.75,0) #sun
  drawRect(700, 500, 80, 80)
  setColorA(1, 1, 1, 1) #cloud 1
  drawRect(400, 450, 30, 30)
  drawRect(370, 420, 30, 30)
  drawRect(430, 420, 30, 30)
  drawRect(400, 420, 30, 30)
  setColorA(1, 1, 1, 1) #cloud 2
  drawRect(150, 350, 40, 40)
  drawRect(110, 310, 40, 45)
  drawRect(190, 310, 40, 35)
  drawRect(150, 310, 43, 40)
  setColor(87/256.0, 77/256.0, 39/256.0) #house
  drawRect(400, 150, 150, 150)
  setColor(232/256.0, 80/256.0, 63/256.0) #house roof
  drawRect(385, 300, 180, 30)
  drawRect(410, 330, 130, 25)
  setColor(181/256.0, 237/256.0, 255/256.0) #window
  drawRect(410, 190, 50, 50)
  setColor(0, 0, 0) #window bars
  drawRect(432, 190, 5, 52)
  drawRect(410, 215, 52, 5)
  setColor(150/256.0, 128/256.0, 62/256.0) #door
  drawRect(485, 150, 50, 100)
  setColor(255/256.0, 235/256.0, 122/256.0) #person body
  drawRect(300, 150, 10, 50)
  setColor(255/256.0, 235/256.0, 122/256.0) #person head
  drawRect(flyingHeadX, flyingHeadY, flyingHeadW, flyingHeadH)
  setColor(1, 1, 1) #person eyes
  drawRect(flyingHeadX + 5, flyingHeadY + 15, 5, 5)
  drawRect(310, 215, 5, 5)
  setColor(0, 0, 0) #person pupils
  drawRect(296.502, 216.7, 2, 2)
  drawRect(312.5, 216.7, 2, 2)
  setColor(0, 0.25, 1) #person shirt
  drawRect(300, 150, 10, 45)
  setColor(0, 0, 0) #person mouth
  drawRect(297, 206, 15, 2)
  setColor(0, 0.1, 0) #person hair
  drawRect(287, 222, 36, 8)
  
  flyingHeadY = flyingHeadY + flyingHeadMPF

run(800, 600, "Raaghav's Demo Graphics", draw)
