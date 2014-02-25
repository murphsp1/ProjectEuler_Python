import sys

def collatz_sequence(n):
    count = 0
    while True:
        if n>1:
            if n%2==0:
                n = n/2
                count += 1
            else:
                n = 3*n+1
                count += 1
        else:
            break
    return(count)



def main():


 
    #Problem 10
    seq_length = 0
    winning_number= 0
    for i in xrange(999999):
        new_length = collatz_sequence(i)
        if new_length > seq_length:
            winning_number=i
            seq_length = new_length
            print(i, seq_length)


if __name__ == '__main__':
    #call function that we need


    sys.exit(main())
