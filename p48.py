import sys
import sets as set



def main():


    ans = []

    sum = 0
    for a in xrange(1, 1001):
    	sum += (a**a)

    test = str(sum)
    print(test[-10:])





if __name__ == '__main__':
    #call function that we need


    sys.exit(main())