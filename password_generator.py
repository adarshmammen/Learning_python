weak_list = list("qwertyuiopasdfghjklzxcvbnm")
strong_list = weak_list + list("`-=[];',./~!@#$%^&*()_+}{|:<>?")

import random

def pass_gen(n,strength = True):
	return random.sample(strong_list,n) if strength == True else random.sample(weak_list,n)

if __name__ == "__main__":
	n = raw_input("Enter length of your password: (Optional enter <Length Strength> - True or False): ").split()
	print ''.join(pass_gen(int(n[0]))) if len(n) == 1  else ''.join(pass_gen(int(n[0]),n[1]))