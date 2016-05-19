def is_palindrome(s):
	return True if s == s[::-1] else False

if __name__ == "__main__":
	s = raw_input("Enter a string : ")
	check = is_palindrome(s)
	print  s + " is a palindrome" if check == True else s + " is not a palindrome"