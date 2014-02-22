import sys

def prime_sieve(max_val):
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
    import math

 
    #Problem 10
    seive = prime_sieve(2000000)
    print(sum(seive))


if __name__ == '__main__':
    #call function that we need


    sys.exit(main())
