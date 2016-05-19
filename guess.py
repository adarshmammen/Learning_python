def game(ran,user):
	ran = int(ran)
	user = int(user)
	if ran == user: 
		print "you win"
		return 1
	
	a = "too low"
	b = "too high"
	if ran > user:
		print a
		return 0
	else:
		print b
		return 0	
if __name__ == "__main__":
	import random
	ran = random.randint(1,10)
	print "you get 6 tries"
	for i in range(1,6):
		user = raw_input("guess a number between 1 and 10, attempt: " + str(i)+ "\n") 
		if  game(ran,user) == 1:
			print "Good job! You guessed it in %d attempts" %(i) 
			break