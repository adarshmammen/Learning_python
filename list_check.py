def lessThanFiveChecker(li,n):
	new_li = [ele for ele in li if ele < n]
	return new_li

if __name__ == "__main__":
	li = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
	print "The list is " + str(li)
	n = int(raw_input("Enter a number to return a list that contains only elements from the original list that are smaller than that number: "))
	new_li = lessThanFiveChecker(li,n)
	print new_li
