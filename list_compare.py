def list_compare(li1,li2):
	common = [ele for ele in li1 if ele in li2]
	return common

if __name__ == "__main__":
	import random
	li1, li2 = random.sample(range(100),10), random.sample(range(100),10)
	common = list_compare(li1,li2)
	print "list 1 : " + str(li1)
	print "list 2 : " + str(li2)
	print "common elements: " + str(common) 