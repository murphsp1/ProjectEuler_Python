#itertools makes this problem a bit easy. However,
#without itertools I am curious how you would generate
#the "alphabetical order of numbers"

import math
import sets as set

import itertools


def main():
		
	perms = itertools.permutations(range(10))

	for i,p in enumerate(perms):
		if i == 1000000-1:
			print p



if __name__ == ('__main__'):
    main()
