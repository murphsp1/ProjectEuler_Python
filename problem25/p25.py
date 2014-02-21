import sys

'''
F1 = 1
F2 = 1
F3 = 2
'''

def main():
	a = 1
	b = 1
	count = 2
	while True:
		count = count + 1
		next = a+b
		a = b
		b = next
		print(count, next)
		if len(str(next))>=1000:
			break



if __name__ == "__main__":
	sys.exit(main())
