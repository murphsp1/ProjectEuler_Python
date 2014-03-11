"""
This script solves problem 3 of Project Euler
"""

import sys
import math


def prime_sieve(max_val):

    """
    A very simple, classic prime_sieve function with very little in the way of optimizations
    Eventually, this needs to get refactored into a helper function module
    """
    #assume int, returns all primes up to max_val

    seive = range(max_val)
    seive[0] = None  # 0 is not prime!
    seive[1] = None  # 1 is not prime!
    for x in xrange(2, max_val):
        if seive[x]:
            print "{prime} is prime.".format(prime = x)
            # now remove multiples of prime x from the seive
            y = 2*x 
            while y < max_val:
                seive[y] = None
                y = y + x

    seive = filter(None, seive)
    return(seive)


def main():
    
    #we could simply compute all prime numbers up to root n
    #and then test each one ...
    n = 600851475143
    root_n = int(math.floor(math.sqrt(n)))
    seive = prime_sieve(root_n)

    for x in reversed(seive):
        if n%x==0:
            print(x)
            break


if __name__ == '__main__':
    #call function that we need
    sys.exit(main())


