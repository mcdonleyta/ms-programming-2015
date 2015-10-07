
inRoom = "main"
hasKey = 0
hasEscaped = 0

while hasEscaped == 0:
    if inRoom == "west":
        print "You travel to a dusty room."
        print "There is a key on the floor."
    
        print
        print "1) Main Room"
        print "2) Pick up Key"
        print
        
        action = raw_input("choose #1-2: ")
        action = int(action)
        
        if action == 1:
            inRoom = "main"
        if action == 2:
            hasKey = 1

    if inRoom == "east":
        print "You find a small bedroom long abandoned."
    
        print
        print "1) Main Room"
        print
        
        action = raw_input("choose #1: ")
        action = int(action)
        
        if action == 1:
            inRoom = "main"

    if inRoom == "north":
        print "It looks like this used to be a kitchen."
    
        print
        print "1) Main Room"
        print
        
        action = raw_input("choose #1: ")
        action = int(action)
        
        if action == 1:
            inRoom = "main"
    
    if inRoom == "south":
        print "There is a locked door here."
    
    

        print
        print "1) Main Room"
        print "2) Unlock door2"
        print
        
        action = raw_input("choose #1-2: ")
        action = int(action)
        
        if action == 1:
            inRoom = "main"
        if action == 2:
            if hasKey == 1:
                print "You have found the exit!"
                print "You win!"
                hasEscaped = 1
            else:
                print "You need a key for that!"
    
    if inRoom == "main":
        print "You are in a scary warehouse."
        print "Try to escape if you can!"
        
        print
        print "1) Move North"
        print "2) Move South"
        print "3) Move West"
        print "4) Move East"
        print
        
        action = raw_input("choose #1-4: ")
        action = int(action)
        
        if action == 1:
            inRoom = "north"
        if action == 2:
            inRoom = "south"
        if action == 3:
            inRoom = "west"
        if action == 4:
            inRoom = "east"

print "You won! Hurray \(^.^)/"
