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
