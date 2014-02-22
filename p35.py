import sys
from collections import deque

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

def list_to_int(numList):  # [1,2,3]
    #s = map(str, numList)   # ['1','2','3']
    s = [str(i) for i in numList]
    s = ''.join(s)          # '123'
    return int(s)

def rotate_numbers(p):

    num = str(p)
    num = [int(n) for n in num]
    len_num = len(num)
    circular_numbers = [4] * len_num

    if (2 in num) | (4 in num) | (6 in num) | (8 in num) | (0 in num):
        pass
    else:
        num = deque(num)
        for i in xrange(len_num):
            ##return l[n:] + l[:n]
            ##t = num.pop()
            ##num.insert(0,t)
            ##num = num[1:] + num[:1]
            num.rotate(1)
            circular_numbers[i] = list_to_int(list(num))
    return circular_numbers

def check_circularity(p, primes):
    circular_numbers = rotate_numbers(p)
    for c in circular_numbers:
        if c not in primes:
            return False
    return True

def main():
    #Problem 35 - Circular Primes 
    #How many circular primes are there below one million?
    #This is really slow ...

    primes = prime_sieve(1000000)

    count = 0
    for p in primes:
        if p < 12:
            count+=1
            print(p)
        else: 
            if check_circularity(p, primes):
                count += 1
                print(p)
    print(count)





if __name__ == '__main__':
    #call function that we need


    sys.exit(main())
