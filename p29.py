import sys
import sets as set



def main():


    ans = []

    for a in xrange(2,101):
        for b in xrange(2,101):
            ans.append(a**b)

    test = set.Set(ans)
    print(len(test))






if __name__ == '__main__':
    #call function that we need


    sys.exit(main())