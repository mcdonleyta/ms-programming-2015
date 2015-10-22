from easyGL import * 
   
def draw(): 
 setColorA(0, 0.52734375, 0, 1)
 drawRect(0, 0, 1500, 200)
  
 setColorA(0.1328125, 0.01953125, 0.88671875, 1) 
 drawRect(0, 200, 1500, 800)
  
 setColorA(0.90625, 0.87890625, 0.046875, 1) 
 drawRect(500, 500, 100, 100)
  
 setColorA(1, 1, 1, 0.6)
 drawRect(100, 100, 100, 300)
  
 setColorA(0, 0, 0, 1)
 drawRect(110, 300, 20, 50)
  
 setColorA(0, 0, 0, 1) 
 drawRect(150, 300, 20, 50)
  
 setColorA(0, 1, 1, 1)
 drawRect(500, 50, 800, 70)
 
 setColorA(0, 1, 1, 1)
 drawRect(400, 50, 100, 70)


run(1500, 1000,"Mia Ashby's Spectatular Scene~ :3", draw)
