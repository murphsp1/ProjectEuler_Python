import sys
import math

def factorial_test(n):
    num = str(n)
    f = [math.factorial(int(i)) for i in num ]
    if sum(f)==n:
        return True
    return False

def main():

    works = []
    for n in xrange(3,10000000):
        if factorial_test(n):
            works.append(n)

    print(works)






if __name__ == '__main__':
    #call function that we need


    sys.exit(main())
