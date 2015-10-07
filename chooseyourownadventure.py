
inRoom ="main"

if inRoom =='main': 
	print " you have killed ten zombies" 
		
	print "1) jump into bottomless"
	print "2) refil ammo and die!"
	print "3) pick a hand weapon,and ammo"

	action = raw_input ("pick a thing to do")
	action = int(action) 
	if action == 1:
		print "you loose"
	if action == 2:
		print "you should go to the basement"
	if action == 3: 	
		print  "you should go to the basement"
		inRoom ='basement'

if inRoom =='basement':		
	print "1) eat a twinkie"
	print "2) commit sucide"
	print "3) get ammo and pick up a chainsaw"
	action2 = raw_input ("pick a thing to do") 
	action2 = int(action2)
	if action2 == 1:
		print "That twinkie expired  two years ago you die"
	if action2 == 2:
		print "You die a painful death"
	if action2 == 3:
		print "see a survior what do you do"
		print " you should go upstairs " 
if inRoom == "main":
		print "1) waste him" 
		print "2) kill him and kill yourself"
		print "3) talk to it"
		action2= raw_input ("pick a thing to do") 
		if action2 == 1:
			 "You kill im you end up killing yourself"
		if action2 == 2:
			print "Hi!"		
		if action2 == 3:
			print "You save it"
