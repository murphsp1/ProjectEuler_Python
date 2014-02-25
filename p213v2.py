import numpy as np 

GRID_SIZE = 30


def make_jump(r,c, val, new_grid):

	if (r>0 and r<GRID_SIZE-1 and c>0 and c<GRID_SIZE-1):
		val = val/4.0
		new_grid[r+1,c] += val
		new_grid[r-1,c] += val
		new_grid[r,c+1] += val
		new_grid[r,c-1] += val

	#handle corners
	elif (r==0 and c==0):
		val = val/2.0
		new_grid[r+1,c] += val
		new_grid[r,c+1] += val

	elif (r==0 and c==GRID_SIZE-1):
		val = val/2.0
		new_grid[r+1,c] += val
		new_grid[r,c-1] += val

	elif (r==GRID_SIZE-1 and c==0):
		val = val/2.0
		new_grid[r-1,c] += val
		new_grid[r,c+1] += val		

	elif (r==GRID_SIZE-1 and c==GRID_SIZE-1):
		val = val/2.0
		new_grid[r-1,c] += val
		new_grid[r,c-1] += val		

	#handle edges
	elif (r==0 and c>0 and c<GRID_SIZE-1):
		val = val/3.0
		new_grid[r+1,c] += val
		new_grid[r,c-1]+= val
		new_grid[r,c+1]+= val

	elif (r==GRID_SIZE-1 and c>0 and c<GRID_SIZE-1):
		val = val/3.0
		new_grid[r-1,c] += val
		new_grid[r,c-1] += val
		new_grid[r,c+1] += val

	elif (r>0 and r<GRID_SIZE-1 and c==(GRID_SIZE-1)):
		val = val/3.0
		new_grid[r,c-1] += val
		new_grid[r-1,c] += val
		new_grid[r+1,c] += val

	elif (r>0 and r<GRID_SIZE-1 and c==0):
		val = val/3.0
		new_grid[r,c+1] += val
		new_grid[r-1,c] += val
		new_grid[r+1,c] += val
	else:
		print ('Case not handled!')
		print(r,c)

	return(new_grid)


def take_step(grid):

	m,n = grid.shape

	new_grid = np.zeros((GRID_SIZE, GRID_SIZE))
	for r in xrange(m):
		for c in xrange(n):
			#for each cell, need to update new_grid with relevant value
			val = grid[r,c]
			if val>0:
				new_grid = make_jump(r,c, val, new_grid)

	return(new_grid)


def simulate_flea(r,c):
	
	grid = np.zeros((GRID_SIZE, GRID_SIZE))
	grid[r,c] = 1.0

	#empty_squares=[0]*50
	for step in xrange(50):
		grid = take_step(grid)
		#print(grid)
	
	
	return(grid)


def main():
	#init grid
	num_fleas = GRID_SIZE*GRID_SIZE
	grid_game = np.zeros((GRID_SIZE, GRID_SIZE, num_fleas))

	#for each possible starting flea, 
	#need to propagate the probabilities of square occupation

	#for flea in xrange(num_fleas)
	for r in xrange(GRID_SIZE):
		for c in xrange(GRID_SIZE):
			flea = c + (r)*GRID_SIZE
			print(flea)
			grid_game[:,:,flea] = 1-simulate_flea(r,c)
	
	#for f in xrange(num_fleas):
		#print(grid_game[:,:,f])
	print np.sum(np.sum(np.prod(grid_game, 2)))




if __name__ == '__main__':
	main()