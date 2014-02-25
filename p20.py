import sys

def factorial(n):
	if n > 2:
		return n*factorial(n-1)
	else:
		return 2


def main():
    
    n = 100
    f = factorial(100)
    f_int_list = [int(i) for i in str(f)]
    print(sum(f_int_list))



if __name__ == '__main__':
    #call function that we need


    sys.exit(main())

