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

	#the 10,000 range is a guesstimate
	products = []
	for i in xrange(1,2000):
		for j in xrange(1,2000):
			ij = i*j
			num = ''.join([str(i), str(j), str(ij)])
			if ispandigital(num):
				products.append(ij)
				print(i,j,ij)

	products_set = set.Set(products)
	print(products_set)
	print(sum(products_set))


if __name__ == ('__main__'):

    main()

