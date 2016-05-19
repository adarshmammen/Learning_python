def checker(n):
	returner = "lol"
	if n%2 ==0:
		returner = "even"
		if n%4 ==0:
			returner = "multiple of 4"
	else:
		returner = "odd"
	return returner

def checker2(num):
	if int(num[1])/int(num[0]) %2 ==0:
		print "divides evenly"
	else:
		print "something strange"


if __name__ == "__main__":
	n = 0
	output = checker(int(raw_input("Enter a number\n")))
	print output 
	# another test
	num = raw_input("Enter 2 numbers, first <single space> second:  ")
	num =  num.split()
	checker2(num)
