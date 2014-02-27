import math

#Dumb brute force method ... could be MUCH faster
#if I implemented a prime factorization method
import sets as set
def count_factors(n):
    factor_sum = 1
    for i in xrange(2,n):
        if (n%i)==0:
            factor_sum += i
    return(factor_sum)


#Smarter way of computing factors, much smaller search
def get_factors(n):
    factors = []
    factors.append(1)
    # loop to square root as any higher factors can be determined from lower factors
    for j in range(2, int(math.sqrt(n))+1):
        if n % j == 0:
            factors.append(j) # factor
            factors.append(n/j) # find it's partner
    #factors.append(n)
    return set.Set(factors) # sorted unique terms


def main():

    b = []
    n = 10000
    total_sum = 0
    a = range(2,n)
    pairs = []
    for i in xrange(2,n):
        factors = get_factors(i)
        sum_factors = sum(factors)
        b.append(sum_factors)
        if i == sum(get_factors(sum_factors)):
            if (i not in pairs) and (i != sum_factors):
                pairs.append(i)
                pairs.append(sum_factors)
                print(i, sum_factors)

    print(sum(pairs))

if __name__ == ('__main__'):
    main()