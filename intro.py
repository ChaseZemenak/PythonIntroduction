print("Welcome to my Python Novice Program for Functions")

#name variable
_name = "My name is David Chase Zemenak"

#age variable
_age = 26

#isHardWorking variable
_isHardWorking = True


#print your name
def printName():
    print(_name)

#print your age
def printAge():
    print(_age)

#print true/false if you are a hard working software developer
def printHardWorkingStatus():
    print(_isHardWorking)
	if _isHardWorking == True:
	    print("Yes I am a hard working software developer")
	elif _isHardWorking != True:
	    print("No I am not a hard working software developer")
	
printName()
printAge()
printHardWorkingStatus()