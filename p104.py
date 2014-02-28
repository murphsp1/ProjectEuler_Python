import sys
import numpy as np
import sets as set
import math

#the function above is too slow, so we try another way

def ispandigital(n_str, n = 9):

	ref_set = set.Set(range(1,n+1))

	if len(n_str)!=9:
		return(False)

	ints = [int(i) for i in n_str]
	if max(ints)!=n:
		return False

	if min(ints)!=1:
		return False

	if len(np.unique(ints))==9:
		return(True)

	return False


def main():

	tailcut = 1000000000

	Fn_minus_2 = 1
	Fn_minus_1 = 1
	k=2

	while True:
		Fn = Fn_minus_1 + Fn_minus_2
		k += 1
		if k>100000:
			#This is much faster than turning the entire
			#Fn into a string, not surprisingly
			#Fn_str = str(Fn)
			tail = (Fn % tailcut)
			if ispandigital(str(tail)):
				#This should shift around and select
				#the first 10 digits but it threw errors
				#num_digits = math.ceil(math.log10(Fn))
				#head = math.floor(Fn/10**(num_digits-9))
				head = str(Fn/tailcut)
				if ispandigital(head[0:9]):
					print k
					break
		Fn_minus_2 = Fn_minus_1
		Fn_minus_1 = Fn



if __name__ == ('__main__'):

    main()
