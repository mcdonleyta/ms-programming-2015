#Absolute Value 
Number = raw_input("Enter #:" ) 
Number = int(Number) 
 
if Number > 0: 
	Number = Number * -1 
elif Number == 0: 
	Number = Number 
else:
	Number = Number * 1 
 
print "The abs of " + str(Number) 
print "is " + str(Number) 
