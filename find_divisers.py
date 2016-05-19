def diviser(n):
	li = range(2,n)
	diviser_li = [ele for ele in li if n % ele == 0]
	print diviser_li

if __name__ == "__main__":
	n = raw_input("Enter a number: ")
	print "The divisers are: "
	diviser(int(n))