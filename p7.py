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

def list_to_int(numList):         # [1,2,3]
    s = map(str, numList)   # ['1','2','3']
    s = ''.join(s)          # '123'
    return int(s)

def rotate_numbers(p):
    num = str(p)
    num = [int(n) for n in num]
    circular_numbers = []
    for i in xrange(len(num)):
        t = num.pop()
        num.insert(0,t)
        circular_numbers.append(list_to_int(num))
    return circular_numbers


def check_circularity(p, primes):
    circular_numbers = rotate_numbers(p)
    for c in circular_numbers:
        if c not in primes:
            return False
    return True




def main():

    #Problem 7
    import math
    #we could simply compute all prime numbers up to root n
    #and then test each one ...
    '''
    n = 600851475143
    root_n = int(math.floor(math.sqrt(n)))
    seive = prime_sieve(root_n)
    for i, prime in enumerate(seive):
        if i == 10000:
            print prime
            break
    '''

    #Problem 10
    #seive = prime_sieve(2000000)
    #print(sum(seive))

    #Problem 35 - Circular Primes 
    #How many circular primes are there below one million?
    #Once I find a prime, I should remove it and the circular values
    #from the primes list to speed things up and prevent double counting
    primes = prime_sieve(1000000)

    count = 0
    for p in primes:
        if check_circularity(p, primes):
            count += 1
            print(p)
    return(count)




if __name__ == '__main__':
    #call function that we need


    sys.exit(main())


