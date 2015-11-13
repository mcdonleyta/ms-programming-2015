from easyGL import *

MPF = 3
X1 = 300
X2 = 290
X3 = 295
X4 = 310
X5 = 296.502
X6 = 312.5
X7 = 300
X8 = 297
X9 = 287

def draw():
  global X1, X2, X3, X4, X5, X6, X7, X8, X9, MPF
  setColor(0.4, 0.4, 1) #blue sky                         
  drawRect(0, 150, 800, 650)
  setColor(0,1,0) #green grass
  drawRect(0, 0, 800, 150)
  setColor(1,0.75,0) #sun
  drawRect(700, 500, 80, 80)
  setColorA(1, 1, 1, 0.7) #cloud 1
  drawRect(400, 450, 30, 30)
  setColorA(1, 1, 1, 0.7)
  drawRect(370, 420, 30, 30)
  setColorA(1, 1, 1, 0.7)
  drawRect(430, 420, 30, 30)
  setColorA(1, 1, 1, 0.7)
  drawRect(400, 420, 30, 30)
  setColorA(1, 1, 1, 0.7) #cloud 2
  drawRect(150, 350, 40, 40)
  setColorA(1, 1, 1, 0.7)
  drawRect(110, 310, 40, 40)
  setColorA(1, 1, 1, 0.7)
  drawRect(190, 310, 40, 40)
  setColorA(1, 1, 1, 0.7)
  drawRect(150, 310, 40, 40)
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
  drawRect(X1, 150, 10, 50)
  X1 = X1 + MPF
  setColor(255/256.0, 235/256.0, 122/256.0) #person head
  drawRect(X2, 200, 30, 30)
  X2 = X2 + MPF
  setColor(1, 1, 1) #person eyes
  drawRect(X3, 215, 5, 5)
  X3 = X3 + MPF
  drawRect(X4, 215, 5, 5)
  X4 = X4 + MPF
  setColor(0, 0, 0) #person pupils
  drawRect(X5, 216.7, 2, 2)
  X5 = X5 + MPF
  drawRect(X6, 216.7, 2, 2)
  X6 = X6 + MPF
  setColor(0, 0.25, 1) #person shirt
  drawRect(X7, 150, 10, 45)
  X7 = X7 + MPF
  setColor(0, 0, 0) #person mouth
  drawRect(X8, 206, 15, 2)
  X8 = X8 + MPF
  setColor(0, 0.1, 0) #person hair
  drawRect(X9, 222, 36, 8)
  X9 = X9 + MPF
  if X1 > 800:
	  MPF = MPF * -1
  if X1 < 0:
	  MPF = MPF * -1


run(800, 600, "Raaghav's Animated Graphics", draw)
