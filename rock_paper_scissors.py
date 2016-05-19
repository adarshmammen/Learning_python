import random
options = ['r','p','s']

def meet_your_maker():
	return str(random.choice(options))

if __name__ == "__main__":
	while(1):
		you = raw_input("rock paper or scissors? (enter r, p or s): ")
		comp = meet_your_maker()
		print "Computer picked : "+ comp
		if you == comp:
			print "Its a tie!"
		elif ((comp == 'r' and you == 's') or (comp == 'p' and you == 'r') or (comp == 's' and you == 'p')):
			print "You lose"
		elif you != 'r' or 'p' or 's':
			print "invalid option idiot"
		else:
			print "You WIN!"
		choice = raw_input ("Play again? y/n: ")
		if choice == 'n':
			break