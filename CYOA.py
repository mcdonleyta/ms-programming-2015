inRoom = "main" #This is a Rp-(Black Butler) game.
hasKey = 0
hasEscaped = 0

user = raw_input("Hello, do you mind if I ask you a question. What is your name? :")

user = str(user)
print "Hello " + user + ", and welcome to Mia and Olivia's Black Butler game!"
print "I hope you have fun! :3"
print "Claude Faustus: I hope you enjoy. :)"

while hasEscaped == 0:
    if inRoom == "west":
        print "You have arrived, " + user + ", in the Bedroom of Sebastian Michaelis."
        print "Claude: Goodness, his room is so dark...why does he keep his room so dark?"
        print "There is a candle on his nightstand, and, a steamy romance novel on his bed...? o//_//o"
        print "Claude: That's a book only a demon like 'HIM' would read." 

        print "1) Head back to the Main Hall."
        print "2) Pick up the candle."
        print "3) Pick up and read the book... -//.//-" 
        
        action = raw_input("choose #1-3: ")
        action = int(action)
        
        if action == 1:
            inRoom = "main"
        if action == 2:
            hasKey = 1
        if action == 3:
			print "This... book... O///o Oh Lord Sebastian... you do have a dark sense of humor...-//.//-"
			inRoom = "main"

    if inRoom == "east":
        print "You have found you way into the kitchen, with lots of cabinets full of food and silverware."
        print "Claude: This room is so dusty, I wish they would clean here more... :/"
    
        print
        print "1) Main Room."
        print "2) Check cabinets for food."
        
        action = raw_input("choose #1-2: ")
        action = int(action)
        
        if action == 1:
            inRoom = "main"
        if action == 2:
		   print "Bread...Marmite...Cake recipes...Catnip Tequila? *Looks around and steals Tequila* ;D"

    if inRoom == "north":
        print "You have found the old library, full of books, of all genre's."
        print "Claude: This place is full of books! :D"
    
        print
        print "1) Main Room."
        print "2) Pick up a Lord of the Rings novel... ;D" 
        
        action = raw_input("choose #1-2: ")
        action = int(action)
        
        if action == 1:
            inRoom = "main"
        if action == 2:
			print "Thorin! Don't let the Dragon Sickness get to you! Smaug's tricking you! *Realizes he is talking to himself* Oh..."
    
    if inRoom == "south":
        print "Is this is the door to the garden? There is a hole, fit, for a candle.."
        print "Claude: I wonder if Ciel is behind this door. Futhermore, how did he get in there? o_o"
    
        print
        print "1) Main Room"
        print "2) Unlock Door~"
        print 
        
        action = raw_input("choose #1-3: ")
        action = int(action)
        
        if action == 1:
            inRoom = "main"
        if action == 2:
            if hasKey == 1:
                print "You have found the garden, and you have found Ciel Phantomhive!!"
                print "Ciel Phantomhive: *Hugs* Thank you for finding me Claude! :3"
                print "Claude: No problem, Ciel. *Hugs* Now, lets head back to Sebastian, he was worrying about you."
                print "Ciel: Ok! Lead the way, Claude."
                print "Claude and Ciel walk back inside, to find Sebastian drinking Catnip Tequila~"
                print "Ciel: Sebastian? What are you drinking?"
                print "Sebastian: Nothing! *Pushes drink away* I'm glad your back. I thought I lost you!"
                hasEscaped = 1
            else:
                print "The door will not open without a candle to light it...I wonder where I can find a Candle.."
    
    if inRoom == "main":
        print "Sebastian Michaelis: *Runs up to Claude ang hug him* Claude! I need you help to find Ciel, I went into his bedroom this morning to wake him up, but, he wasn't there!"
        print "You must find Ciel Phantomhive! He is lost, I tell you, lost! D:"
        print "Claude: *Pats Sebastian on the back* Don't worry, don't worry, I'll find him."
        print "Sebastian: Yay! Thanks Claude! I can always count on you. ;3"
        print "Claude: Indeed you can. ;D"
        
        print
        print "1) Move North."
        print "2) Move South."
        print "3) Move West."
        print "4) Move East."
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

print "You have found Ciel Phantomhive hiding in the Garden. Congratulations! You are the best, most beautiful, and coolest butler ever!"
print "Congratulations " + user + ", you win!"
print "Claude: *Hugs player* Thanks for playing. :3"
print "We hope you had lots of fun playing, and we hope to see you again!!"
#Typed by: Mia C. Ashby
#Helper: Olivia Ave
