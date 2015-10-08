inRoom = "main" 
hasKey = 0
hasEscaped = 0 
 
while hasEscaped == 0: 
if inRoom == "west": 
print "You have arrived in the bedroom of Sebastian Michaelis. One his bed there is a candle, and a steamy… romance novel? o///o"
print "Claude: Oh, uh... Nice bedroom? O.o Only a demon like ‘HIM’ would read that bad of a book…"
  
print 
print "1) Main Room."
print “2) Pick up Candle..."
print "3) Pick up the book… -///-"
  
action = raw_input("choose #1-3: ") 
action = int(action) 
  
if action == 1: 
inRoom = "main" 
if action == 2: 
hasKey = 1 
 
if inRoom == "east": 
print "You have found an Old Library, full of bookshelves loaded with books, of all genre's."
print "Claude: Oh goodness… so many books.. :D I should take one. ;3"
  
print 
print "1) Main Room"
print "2) Pick up a Lord of The Rings novel… :P"
  
action = raw_input("choose #1-2: ") 
action = int(action) 
  

if action == 1: 
inRoom = "main"
 
if inRoom == "north": 
print "It seems like this is a kitchen.."
print "Claude: Goodness, you’d think they’d clean in here more often. o.O"
  
print 
print "1) Main Room"
print "2) Check cabinets for food... xD"
  

action = raw_input("choose #1-2: ") 
action = int(action)

if action == 1: 
inRoom = "main"
  
if inRoom == "south": 
print "There is a giant stone door, and there is a hole, fit for a candle…?"
  
print 
print "1) Main Room."
print "2) Unlock Door with Candle."
print 
  
action = raw_input("choose #1-2: ") 
action = int(action) 
  
if action == 1: 
inRoom = "main"
if action == 2: 
if hasKey == 1: 
print "You have found the lost Ciel hiding in the garden! :3"
print "You have beaten the game! You are more awesome than I thought…"
hasEscaped = 1 
else: 
print "I don’t have a Candle, I can’t open it… :/"
  
if inRoom == "main": 
print "Sebastian Michaelis: *Runs up to Claude* Claude! I need your help! I woke up this morning, and went into my master’s room to wake him up, but he wasn’t there! D: I can’t find him anywhere! Can you help me find him?"
print "Claude Faustus: Sure, I can help you."
print "Sebastian Michaelis: Yay! Thanks Claude! :3"
print "Claude Faustus: No problem, Seb’s!"
  
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
 
print "You have found Ciel Phantomhive hiding in the Garden! Congratulations, you are officially, the coolest, most beautiful, and most awesome butler in the world! ;D"
print "Ciel Phantomhive: *Runs up and hugs Claude* Thanks for finding me, Claude!"
print "Claude Faustus: No problem, Ciel. *Winks*"
print "Thank you for playing Mia and Olivia's Black Butler game! ;3"
 
