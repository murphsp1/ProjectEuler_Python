# d100 × d1000 × d10000 × d100000 × d1000000

import sys


def main():
    import math

    temp_str = [str(i) for i in xrange(200000)]
    d = "".join(temp_str)

    print(int(d[1])*int(d[100])*int(d[1000])*int(d[10000])*int(d[100000])*int(d[1000000]))

 


if __name__ == '__main__':
    #call function that we need
    sys.exit(main())