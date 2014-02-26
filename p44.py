import sys

#not the fastest way to do this problem but it should work
#we will see ...

#key here is that we need to walk up the various pentagonal
#number values ...so the outer most loop should be the upper bound
#and the inner loop checks pentagonal numbers up to the outer loop value


def main():
	max = 2500
	#generate the first 1000 pentagonal numbers
	pentagonal_numbers = [n*(3*n-1)/2 for n in xrange(1,max)]
	#print(pentagonal_numbers)

	possibles = []
	gap = []
	for i in xrange(1,max):
		print(i)
		for j in xrange(0,i):
			p2 = pentagonal_numbers[i]
			p1 = pentagonal_numbers[j]
			if (p2-p1) in pentagonal_numbers:
				if (p2+p1) in pentagonal_numbers:
					print(p1,p2, abs(p2-p1))
					possibles.append((p1,p2))
					gap.append(abs(p2-p1))

	print(possibles)
	print(gap)




if __name__ == '__main__':
    #call function that we need


    sys.exit(main())
