from easyGL import *
 
cloudX = 600
cloudY = 300
cloudW = 86
cloudH = 100
cloudMPF = 0.25
ghostX = 100
ghostY = 100
ghostW = 68
ghostH = 78
ghostMPF = 12
    
def draw():
	
  global cloudH, cloudW, cloudX, cloudY, cloudMPF
  
  global ghostX, ghostY, ghostH, ghostW, ghostMPF
  
  setColor(0, 1, 1)
  drawRect(0, 0, 1400, 800)
  setColor(0, 1, 0)
  drawRect(0, 0, 800, 100)  
  setColor(1, 1, 0)
  drawRect(100, 440, 123, 100)
  setColorA(0.99, 0.99, 0.991, 0.65)
  drawRect(ghostX, ghostY, ghostW, ghostH)#ghost
  setColor(1, 1, 1)
  drawRect(cloudX, cloudY, cloudW, cloudH) #cloud
  
  cloudX = cloudX - cloudMPF
  if cloudX < -100:
	  cloudX = 800
  ghostX = ghostX - ghostMPF
  if ghostX < -100:
	  ghostX = 800
		
  
run(800,900, "MAX DRAWING WITH ALEX FACED UP STUFF", draw)
