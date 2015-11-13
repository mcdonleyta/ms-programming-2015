from easyGL import *
import random

screenwidth = 1000
screenheight = 800
numberblocksperrow = 10
numbofrows = 3
blockwidth = screenwidth/numberblocksperrow
blockheight = screenheight/4/numbofrows
walld = 0 



def draw():
	r = 1
	g = 1
	b = 1
	r2 = 0.3
	g2 = 0.3
	b2 = 0.3
	rows = 0
	blocky = screenheight-blockheight
	while rows < numbofrows:
		block = 0
		walld = 0
		while block < numberblocksperrow:
			if rows == 0:
				setColor(r,g,b)
			if rows == 1:
				setColor(random.randint (0,8)/8.1, random.randint (0,8)/8.3, random.randint (0,8)/8.2,)
			if rows == 2:
				setColor(r2,g2,b2) 
			drawRect(walld,blocky, blockwidth, blockheight)
			block = block + 1
			walld = walld + blockwidth
			r = r - 0.02
			g = g - 0.08
			b = b - 0.1
			r2 = r2 + 0.01
			g2 = g2 + 0.02
			b2 = b2 + 0.03
		rows = rows + 1
		blocky = blocky - blockheight
		
		
		
	

	
run(screenwidth, screenheight, "Breakout", draw)
