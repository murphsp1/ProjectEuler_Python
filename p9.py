import sys


def main():
    possible_solutions = []
    for a in xrange(1,1000):
        for b in xrange(a,1000):
            left_side = 2000*(a+b)-2*a*b
            if left_side==1000**2:
                possible_solutions.append([a,b])
    print(possible_solutions)
    even_closer = []

    for ab in possible_solutions:
        for c in xrange(3,1000):
            a = ab[0]
            b = ab[1]
            if a+b+c==1000:
                even_closer.append([a,b,c])
    print(even_closer)
    for abc in even_closer:
        a = abc[0]
        b = abc[1]
        c = abc[2]
        if (a**2 + b**2) == c**2:
            print(a,b,c)
            print(a*b*c)
            break



if __name__ == '__main__':
    #call function that we need


    sys.exit(main())


