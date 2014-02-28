import sets as set
import math
import numpy as np

#modified the inputs and outputs of this one to
#avoid changing things from int to string and back again
def ispandigital(n_str,n):
    #n = len(n_str)
    #n = 9
    ref_set = set.Set(range(1,n+1))

    ints = [int(i) for i in n_str]
    if max(ints)!=n:
        return False

    if min(ints)!=1:
        return False

    if len(np.unique(ints))==n:
        return(True)

    return False



def main():
	for n in xrange(1,10):
		l = range(1,n)
		print l
		for i in xrange(1,100000):
			test = ''.join([str(i*k) for k in l])
			if len(test)==9:
				if ispandigital(test, 9):
					print(test, i, l)


if __name__ == ('__main__'):
	main()