import sys
import numpy as np
import sets as set

#really hacked this prime_sieve function to try to get it to run
def prime_sieve(max_val):
    #assume int, returns all primes up to max_val

    #seive = range(max_val)
    seive = np.ones(max_val, dtype=np.bool)
    seive[0] = None  # 0 is not prime!
    seive[1] = None  # 1 is not prime!
    primes = []
    for x in xrange(2, max_val):
        if seive[x]:

            print "{prime} is prime.".format(prime = x)
            # now remove multiples of prime x from the seive
            y = 2*x 
            while y < max_val:
                seive[y] = False
                y = y + x

    #seive = filter(None, seive)
    return(primes)





def main():
    import math

    primes = prime_sieve(1000000000)
    print(primes)


 



if __name__ == '__main__':
    #call function that we need


    sys.exit(main())
