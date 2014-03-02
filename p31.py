#We will tackle this one with recursion but
# it is really a double recursive algorithm
# We need to recursively walk through the coins array
# and, for each coin, walk through the remaining possibilities

#I still look at the imperative version and see it 
# as "clearer," even if it is ugly. The recursive
# solution, probably because of the conditionals,
# just doesn't look that great to me.


def make_change_imperative(target):
	ways = 0
	for a in xrange(target, 0-1, -200):
		for b in xrange(a, 0-1, -100):
			for c in xrange(b, 0-1, -50):
				for d in xrange(c, 0-1, -20):
					for e in xrange(d, 0-1, -10):
						for f in xrange(e, 0-1, -5):
							for g in xrange(f, 0-1, -2):
								ways += 1
	return(ways)


def make_change_dynamic_programming(target):
	pass
	#not done yet but I know it exists


coins = [200, 100, 50, 20, 10, 5, 2, 1]
def make_change_recursive(money, coins ):
	
	if (len(coins) == 0):
		return 1

	s = 0
	for i in xrange(0, len(coins)):
		remain = money - coins[i]
		if (remain==0):
			s = s+1
		if (remain>0):
			s = s + make_change_recursive(remain,coins[i:])
	return s



def main():
	answer = make_change_recursive(200, coins)
	answer2 = make_change_imperative(200)


if __name__ == '__main__':
	main()