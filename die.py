'''This program gives an output that simulates a 6 sided die 
Additionally it also finds the Expected value of the random variable E(X)'''
import random as rn
def random_gen()	:
	'''Simulate the random throw'''
	li = [1,2,3,4,5,6]
	return rn.choice(li)

if __name__ == "__main__":
	'''user level communication and function calls'''
	n = raw_input("how many times would you like to roll the die?")
	i=0
	li = []
	while i != int(n):
		li.append(random_gen())
		print li[i]
		i = i+1
	avg = sum(li)/int(n)
	print "Average of %s rolls is %d" %(n,avg)