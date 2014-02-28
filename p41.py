import sys
import numpy as np
import sets as set
import math


#the function above is too slow, so we try another way

def get_num_factors(n):
    factors = []
    factors.append(1)
    # loop to square root as any higher factors can be determined from lower factors
    for j in range(2, int(math.sqrt(n))+1):
        if n % j == 0:
            factors.append(j) # factor
            factors.append(n/j) # find it's partner
    #factors.append(n)
    return len(set.Set(factors)) # sorted unique terms


def ispandigital(num):
    n_str = str(num)
    n = len(n_str)
    ref_set = set.Set(range(1,n+1))

    ints = [int(i) for i in n_str]
    if max(ints)!=n:
        return False

    if min(ints)!=1:
        return False

    if len(np.unique(ints))==n:
        return(True)

    return False

##too slow
def main2():

    max = 987654322
    n = max
    while True:
        n = n-1
        print n
        num_factors = get_num_factors(n)
        if num_factors==1:
            if ispandigital(n):
                print n
                break


 
def main():
    import itertools

    for n in range(5,10):

        perms = itertools.permutations(range(1,n))

        for p in perms:
            num = ''.join( [str(i) for i in p])
            num = int(num)
            num_factors = get_num_factors(num)
            if num_factors==1:
                if ispandigital(num):
                    print num
                    continue


    



if __name__ == '__main__':
    #call function that we need


    sys.exit(main())
