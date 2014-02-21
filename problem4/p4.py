
import sys

def check_number_symmetry(n):
    #assume int
    n_str = str(n)
    len_str = len(n_str)
    str_rev = n_str[::-1]
    if (len_str%2)==0: #even
        mid = len_str/2+1
        if n_str[0:mid]==str_rev[0:mid]:
            return True
    else:
        mid = len_str/2
        if n_str[0:mid]==str_rev[0:mid]:
            return True

def main():
    palindromes = []
    for x in xrange(1,1000):
        for y in xrange(1,1000):
            prod = x*y
            if check_number_symmetry(prod):
                palindromes.append(prod)

    print(palindromes)
    print(max(palindromes))


if __name__ == '__main__':
    #call function that we need


    sys.exit(main())


