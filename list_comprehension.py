if __name__ == "__main__":
	a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
	even = [ele for ele in a if ele%2 ==0]
	print "Original list " + str(a)
	print "Even list " + str(even)