import math
import sets as set

#Smarter way of computing factors, much smaller search
def get_proper_divisors(n):
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
	max = 28123

	sum_of_abundant_numbers = []

	abundant = []
	for i in xrange(1,max+1):
		proper_divisors = get_proper_divisors(i)
		if sum(proper_divisors)>i:
			abundant.append(i)

	for a in abundant:
		for b in abundant:
			if a+b<=max:
				sum_of_abundant_numbers.append(a+b)


	abundant_sum = set.Set(sum_of_abundant_numbers)
	all_ints = set.Set(range(1,max+1))
	deficient_sum = all_ints - abundant_sum
	print(sum(deficient_sum))


if __name__ == ('__main__'):
    main()