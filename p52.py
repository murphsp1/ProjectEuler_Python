import sys



def num_to_ordered_list(n):
	n_str = str(n)
	n_list = [i for i in n_str]
	n_list.sort()
	return(n_list)


def main():
    
    i = 0
    while True:
		i += 1
		i_list = num_to_ordered_list(i)
		for n in xrange(2,7):
			good = False
			new_i = i*n
			new_i_list = num_to_ordered_list(new_i)
			if new_i_list != i_list:
				break
			else:
				good = True
		if good:
			print('Done')
			print(i)
			break







if __name__ == '__main__':
    #call function that we need


    sys.exit(main())
