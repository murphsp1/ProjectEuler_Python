import sys
import numpy as np
import math
import sets as set

'''
def generate_triangle_number(n):
    output = 0
    for i in xrange(n):
        output += i
    return(output)
'''

def generate_triangle_number(n):
    #sum from 1:n
    return (sum(range(n)))

def generate_list_of_triangle_numbers(n):
    #returns a list of triangle numbers up to n
    nums = np.zeros(n)
    nums[1]=1
    for i in xrange(2,n):
        nums[i] = i+nums[i-1]

    return(nums)

def count_factors(n):
    count = 0
    for i in xrange(1,n):
        if (n%i)==0:
            count += 1
    return(count)


#Smarter way of computing factors, much smaller search
def get_num_of_factors(n):
    factors = []
    factors.append(1)
    # loop to square root as any higher factors can be determined from lower factors
    for j in range(2, int(math.sqrt(n))+1):
        if n % j == 0:
            factors.append(j) # factor
            factors.append(n/j) # find it's partner
    factors.append(n)
    return len(set.Set(factors)) # sorted unique terms


def main():

    prev=0 
    i = 0
    triangle_number = 0

    while True:
        i += 1
        triangle_number += i
        num_factors = get_num_of_factors(triangle_number)
        if num_factors>=500:
            print triangle_number
            break





if __name__ == '__main__':
    #call function that we need
    sys.exit(main())
