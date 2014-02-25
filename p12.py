import sys
import numpy as np

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


def main():

    n = 10000000
    test = generate_triangle_number(n)
    factors = count_factors(n)


    '''
    triangle_numbers = generate_list_of_triangle_numbers(n)
    print(max(triangle_numbers))
    print('Done computing triangle numbers')

    for i,num in enumerate(triangle_numbers):
        if i>1000000:
            test = count_factors(num)
            print(test, num)
            if test>500:
                print (i, num)
                break


'''


 



if __name__ == '__main__':
    #call function that we need


    sys.exit(main())
