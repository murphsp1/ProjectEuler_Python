import sys
import numpy as np

'''
Working from left-to-right if no digit is exceeded by the digit to its left it is called an increasing number; for example, 134468.

Similarly if no digit is exceeded by the digit to its right it is called a decreasing number; for example, 66420.

We shall call a positive integer that is neither increasing nor decreasing a "bouncy" number; for example, 155349.

Clearly there cannot be any bouncy numbers below one-hundred, but just over half of the numbers below one-thousand (525) are bouncy. In fact, the least number for which the proportion of bouncy numbers first reaches 50% is 538.

Surprisingly, bouncy numbers become more and more common and by the time we reach 21780 the proportion of bouncy numbers is equal to 90%.

Find the least number for which the proportion of bouncy numbers is exactly 99%.
'''

import numpy as np

def is_number_bouncy(n):
	n_str = str(n)
	n_list = [int(i) for i in n_str]

	ascending = np.diff(n_list)
	ascending = np.greater_equal(ascending,0)
	ascending = np.all(ascending)

	if ascending:
		return False

	descending = np.diff(n_list)
	descending = np.less_equal(descending,0)
	descending = np.all(descending)

	if descending:
		return False

	return True




def main():

	bouncy_count = 0
	for i in xrange(1,10000000):
  		b = is_number_bouncy(i)
  		if b:
  			bouncy_count+=1
  		percent = float(bouncy_count)/float(i)
  		print percent, b, i
		if percent>=0.99:
  			print i
  			break


 



if __name__ == '__main__':
    #call function that we need


    sys.exit(main())