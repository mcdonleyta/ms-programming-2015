inRoom = "home" 
 
while inRoom != "quit": 
	if inRoom == "home": 
		print "This is your home" 
 
		print "You can: " 
		print "1) Go to your backyard" 
		print "2) Stay here" 
 
	action = raw_input("Choose #1-2: ") 
	action = int(action) 
 
if action == 1: 
	inRoom = "backyard" 
if action == 2: 
	inRoom == "home" 
 
if inRoom == "backyard": 
	print "This is your backyard, there's a cat eating a strudel." 
