user = raw_input("what is your name?")

print "hello",user

player = raw_input("you are in a room and there are three passage ways, which one did you take?")

if player == "the second one" or player == "2" or player == "2nd" or player == "second":
    print "you another room and passage way"
elif player == "the first one" or player == "1" or player == "1st" or player == "first":
    print "you fell in a trap and died"
elif player == "the thrid one" or  player == "3" or player== "3rd" or player == "thrid":
    print "you got trapped in a room and died"

if player == "the second one" or player == "2" or player == "2nd" or player == "second":
    print "you win"
else:
    print "game over"


