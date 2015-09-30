nRoom = "main"
hasKey = 0
hasEscaped = 0

while hasEscaped: = 0
 if in room == "main"
	print "You are in a haunted warehouse. try to find the key and make it out alive."
	print "1. Move North"
	print "2. Move South"
	print "3. Move East"
	print "4. Move West"
	
action = raw_input ("choose #1-4")
action = int (action)

if action == 1:
	inRoom = "north"
if action == 2:
	inRoom = "south"
if action == 3:
	inRoom = "east"
if action == 4:
	inRoom = "west"

if inRoom == "west"
	print "You travel to a dusty room."
	print "There is a key on the floor"
	
	print "1.Pick up key"
	print "2. Main Room"
	
	action = raw_input("choose #1-2")
	action - int(action)
	
	if action == 1:
		inRoom = "main"
		
if action == 2:
	hasKey == 1
	
if inRoom == "north"
	print: "This room appears to have been a dining room"
	print: "1. Main Room" 

action = raw_input("choose #1")
action = (int)action

if action == 1 
	inRoom = "main"

if inRoom == "south"
	print "There is a locked door in this room"
	print "1. Unlock door"
	print "2. Main Room" 

action = raw_input("choose #1-2")
action = int(action)

if action == 1 
	if hasKey == 1:
		print "You have unlocked the door and escaped with your life. Lucky!"
	if has key == 0 
		print "You need a key to unlock the door"
	if action == 2:
		inRoom = "main"
