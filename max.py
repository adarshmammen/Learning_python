def max_without_max(li):
	sort1 = sorted(li,reverse = True)
	return sort1[0]

if __name__ == "__main__":
	import random 
	li = random.sample(range(1,100),10)
	print "the list is : " + str(li)
	real_max = max_without_max(li)
	print "Maximum : " + str(real_max)