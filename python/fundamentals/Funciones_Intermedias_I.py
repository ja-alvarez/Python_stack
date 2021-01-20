import random
def randInt(min=''   , max=''   ):
    num = random.random()
    return num

print(int(randInt()*100)) 		    # should print a random integer between 0 to 100
print(int(randInt(max=50)*50)) 	    # should print a random integer between 0 to 50
print(int(randInt(min=50)*50+50)) 	    # should print a random integer between 50 to 100
print(int(randInt(min=50, max=500)*450+50))    # should print a random integer between 50 and 500