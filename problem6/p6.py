import sys

def main():
    max = 100 + 1
    sum_of_squares = [x**2 for x in xrange(max)]
    sum_of_squares = sum(sum_of_squares)
    print sum_of_squares


    squared_sum = [x for x in xrange(max)]
    squared_sum = (sum(squared_sum))
    squared_sum = squared_sum**2
    print squared_sum

    print squared_sum - sum_of_squares


if __name__ == '__main__':
    #call function that we need


    sys.exit(main())


