def diviser(n):
	li = range(2,n)
	diviser_li = [ele for ele in li if n % ele == 0]
	if diviser_li == True:
		print "The divisers are: " + str(diviser_li)
	if diviser_li == []:
		print str(n) + " is a prime number"
	else:
		print str(n) + " is not prime"

if __name__ == "__main__":
	n = raw_input("Enter a number: ")
	diviser(int(n))
