from easyGL import *
    
def draw(): 
  setColor(.8, .8, 1) # Red, Green, Blue                         
  drawRect(50, 10, 100, 100)
  setColor(.6, .6, 1) # Red, Green, Blue                         
  drawRect(150, 110, 100, 100)
  setColor(.4, .4, 1) # Red, Green, Blue                         
  drawRect(250, 210, 100, 100)
  setColor(.6, .6, 1) # Red, Green, Blue                         
  drawRect(350, 110, 100, 100)
  setColor(.8, .8, 1) # Red, Green, Blue                         
  drawRect(450, 10, 100, 100)
  setColor(.8, .8, 1) # Red, Green, Blue                         
  drawRect(250, 110, 100, 100)
  setColor(.4, .4, 1) # Red, Green, Blue                         
  drawRect(150, 10, 100, 100)
  setColor(.6, .6, 1) # Red, Green, Blue                         
  drawRect(250, 10, 100, 100)
  setColor(.4, .4, 1) # Red, Green, Blue                         
  drawRect(350, 10, 100, 100)
run(800, 600, "Rachel's Awesome Example", draw)
