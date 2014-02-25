import numpy as np 

GRID_SIZE = 30


def make_jump(r,c):
	ran = np.random.uniform(0,1,1)[0]
	if (r>0 and r<GRID_SIZE-1 and c>0 and c<GRID_SIZE-1):
		if ran<0.25:
			return(r+1,c)
		elif ran<0.5:
			return(r-1,c)
		elif ran<0.75:
			return(r,c+1)
		else:
			return(r,c-1)
	#handle corners
	elif (r==0 and c==0):
		if ran<0.5:
			return(r+1,c)
		else:
			return(r,c+1)
	elif (r==0 and c==GRID_SIZE-1):
		if ran<0.5:
			return(r+1,c)
		else:
			return(r,c-1)
	elif (r==GRID_SIZE-1 and c==0):
		if ran<0.5:
			return(r-1,c)
		else:
			return(r,c+1)
	elif (r==GRID_SIZE-1 and c==GRID_SIZE-1):
		if ran<0.5:
			return(r-1,c)
		else:
			return(r,c-1)
	#handle edges
	elif (r==0 and c>0 and c<GRID_SIZE-1):
		if ran< (1.0/3.0):
			return(r+1,c)
		elif ran< (2.0/3.0):
			return(r,c-1)
		else:
			return(r,c+1)
	elif (r==GRID_SIZE-1 and c>0 and c<GRID_SIZE-1):
		if ran< (1.0/3.0):
			return(r-1,c)
		elif ran< (2.0/3.0):
			return(r,c-1)
		else:
			return(r,c+1)
	elif (r>0 and r<GRID_SIZE-1 and c==(GRID_SIZE-1)):
		if ran< (1.0/3.0):
			return(r,c-1)
		elif ran< (2.0/3.0):
			return(r-1,c)
		else:
			return(r+1,c)
	elif (r>0 and r<GRID_SIZE-1 and c==0):
		if ran< (1.0/3.0):
			return(r,c+1)
		elif ran< (2.0/3.0):
			return(r-1,c)
		else:
			return(r+1,c)
	else:
		print ('Case not handled!')
		print(r,c)


def take_step(grid):

	m,n = grid.shape

	new_grid = np.zeros((GRID_SIZE, GRID_SIZE))
	for r in xrange(m):
		for c in xrange(n):
			fleas = grid[r,c]
			for f in xrange(int(fleas)):
				new_r, new_c = make_jump(r,c)
				#print(r,c,new_r, new_c)
				new_grid[new_r,new_c] += 1
	return(new_grid)


def run_trial():
	grid = np.ones((GRID_SIZE, GRID_SIZE))

	#empty_squares=[0]*50
	for step in xrange(50):
		grid = take_step(grid)
	
	empty_squares = GRID_SIZE**2 - np.count_nonzero(grid)
	return(empty_squares)	

def main():
	#init grid

	sum = 0
	for n in xrange(1,1000):
		sum += run_trial()
		print(float(sum)/float(n))




if __name__ == '__main__':
	main()