def uniq(li):
	set_li = set(li)
	return set_li

if __name__ == "__main__":
	import random
	li = random.sample(range(100),20)*10 # same set repeated 10 times
	print str(uniq(li))

	# set functions
	print (uniq(li) - uniq(li))
	print (uniq(li) & uniq(li))
	print (uniq(li) | uniq(li))
	print (uniq(li) ^ uniq(li))